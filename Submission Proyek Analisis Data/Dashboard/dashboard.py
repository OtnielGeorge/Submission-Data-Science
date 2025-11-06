import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def load_and_clean_data(file_path):
    """Memuat dan membersihkan dataset kualitas udara."""
    df = pd.read_csv(file_path)
    df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])
    df = df.set_index('datetime')
    df = df.drop(columns=['No', 'year', 'month', 'day', 'hour', 'station'])


    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    df[numeric_cols] = df[numeric_cols].interpolate(method='linear')


    mode_wd = df['wd'].mode()[0]
    df['wd'] = df['wd'].fillna(mode_wd)

    return df


FILE_PATH = "PRSA_Data_Aotizhongxin_20130301-20170228.csv"
df_cleaned = load_and_clean_data(FILE_PATH)


st.set_page_config(
    page_title="Dashboard EDA Kualitas Udara Aotizhongxin",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏙️ Dashboard EDA Kualitas Udara & Implikasi Bisnis")
st.markdown("Dashboard ini menyajikan hasil eksplorasi data (EDA) untuk mengidentifikasi **tren polusi PM2.5 & O3** serta **korelasi cuaca**.")


st.sidebar.header("Opsi Filter Data")


selected_year = st.sidebar.selectbox(
    "Filter Data Berdasarkan Tahun:",
    ['Semua Tahun'] + list(df_cleaned.index.year.unique().astype(str))
)


if selected_year != 'Semua Tahun':
    df_filtered = df_cleaned[df_cleaned.index.year == int(selected_year)]
else:
    df_filtered = df_cleaned



st.header("1. Tren PM2.5: Kapan Polusi Memuncak?")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Pola Musiman: PM2.5 Bulanan")

    monthly_avg_pm25 = df_cleaned['PM2.5'].resample('M').mean()
    seasonal_avg_pm25 = monthly_avg_pm25.groupby(monthly_avg_pm25.index.month).mean()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=seasonal_avg_pm25.index, y=seasonal_avg_pm25.values, palette="flare", ax=ax)
    ax.set_title('PM2.5 Rata-rata per Bulan (2013-2017)')
    ax.set_xlabel('Bulan (1=Jan, 12=Des)')
    ax.set_ylabel('Konsentrasi PM2.5 (µg/m³)')
    ax.grid(axis='y', linestyle='--')
    st.pyplot(fig)

    st.info("💡 **Insight:** PM2.5 paling tinggi saat **Musim Dingin (Des-Mar)**. Waktunya *stock-up* produk.")

with col2:
    st.subheader(f"Pola Harian: PM2.5 Jam-an ({selected_year})")

    hourly_avg_pm25 = df_filtered['PM2.5'].groupby(df_filtered.index.hour).mean()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(x=hourly_avg_pm25.index, y=hourly_avg_pm25.values, marker='o', color='darkblue', ax=ax)
    ax.set_title(f'PM2.5 Rata-rata per Jam')
    ax.set_xlabel('Jam dalam Sehari')
    ax.set_ylabel('Konsentrasi PM2.5 (µg/m³)')
    ax.set_xticks(np.arange(0, 24, 2))
    ax.grid(axis='both', linestyle='--')
    st.pyplot(fig)

    st.info("💡 **Insight:** Puncak PM2.5 terjadi saat jam sibuk (**09:00** dan **21:00**).")

st.markdown("---")



st.header("2. Korelasi Cuaca & Polutan Lain (O3)")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Korelasi PM2.5 vs Faktor Cuaca")
    correlation_vars = ['PM2.5', 'TEMP', 'DEWP', 'PRES', 'WSPM']
    corr_matrix = df_cleaned[correlation_vars].corr()

    fig, ax = plt.subplots(figsize=(7, 5))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, linecolor='black', ax=ax)
    ax.set_title('Heatmap Korelasi (2013-2017)')
    st.pyplot(fig)

    st.info("💡 **Insight:** Angin rendah (WSPM Negatif) dan Udara Lembap (DEWP Positif) adalah faktor risiko polusi tinggi.")

with col4:
    st.subheader(f"Tren Harian Ozon (O3) ({selected_year})")

    hourly_avg_o3 = df_filtered['O3'].groupby(df_filtered.index.hour).mean()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(x=hourly_avg_o3.index, y=hourly_avg_o3.values, marker='o', color='orange', ax=ax)
    ax.set_title(f'Ozon (O3) Rata-rata per Jam')
    ax.set_xlabel('Jam dalam Sehari')
    ax.set_ylabel('Konsentrasi O3 (µg/m³)')
    ax.set_xticks(np.arange(0, 24, 2))
    ax.grid(axis='both', linestyle='--')
    st.pyplot(fig)

    st.info("💡 **Insight:** Ozon memuncak saat **siang hari (14:00 - 16:00)** karena sinar matahari. Perlu peringatan untuk aktivitas *outdoor*.")

st.markdown("---")



st.subheader("Ringkasan Statistik PM2.5")
st.dataframe(df_cleaned['PM2.5'].describe().to_frame().T.round(2))

st.caption("Data Kualitas Udara dari Stasiun Aotizhongxin, 2013-2017.")