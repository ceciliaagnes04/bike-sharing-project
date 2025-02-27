# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Muat Data
day_df = pd.read_csv("day.csv")

# 2. Cleaning Data (Penting untuk konsistensi dengan notebook)
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
day_df['season'] = day_df['season'].astype('category')
day_df['weathersit'] = day_df['weathersit'].astype('category')
day_df['season'] = day_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})

# 3. Visualisasi Menggunakan Streamlit

st.title("Bike Sharing Analysis Dashboard")

# Plot 1: Pengaruh Musim
st.subheader("Pengaruh Musim Terhadap Jumlah Sepeda yang Disewa")
fig_season, ax_season = plt.subplots(figsize=(10, 6))
sns.barplot(x='season', y='cnt', data=day_df, ci=None, ax=ax_season)
ax_season.set_xlabel("Musim")
ax_season.set_ylabel("Jumlah Sepeda yang Disewa (Rata-rata)")
st.pyplot(fig_season)  # Menampilkan plot di Streamlit

# Plot 2: Pengaruh Hari Kerja
st.subheader("Pengaruh Hari Kerja Terhadap Jumlah Sepeda yang Disewa")
fig_workingday, ax_workingday = plt.subplots(figsize=(8, 5))
sns.barplot(x='workingday', y='cnt', data=day_df, ci=None, ax=ax_workingday)
ax_workingday.set_xlabel("Hari Kerja (0: Bukan, 1: Iya)")
ax_workingday.set_ylabel("Jumlah Sepeda yang Disewa (Rata-rata)")
st.pyplot(fig_workingday)

# Plot 3: Pengaruh Kondisi Cuaca
st.subheader("Pengaruh Kondisi Cuaca Terhadap Jumlah Sepeda yang Disewa")
fig_weathersit, ax_weathersit = plt.subplots(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=day_df, ci=None, ax=ax_weathersit)
ax_weathersit.set_xlabel("Kondisi Cuaca")
ax_weathersit.set_ylabel("Jumlah Sepeda yang Disewa (Rata-rata)")
ax_weathersit.set_xticklabels(['Clear/Partly Cloudy', 'Mist/Cloudy', 'Light Rain/Snow', 'Heavy Rain/Snow/Fog'], rotation=45, ha='right')
st.pyplot(fig_weathersit)

st.write("Sumber data: day.csv")