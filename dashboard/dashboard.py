# dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Bike Sharing Analysis Dashboard")

# Muat Data
day_df = pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

# Feature Engineering: Menggabungkan Data Cuaca dari hour_df ke day_df
daily_weather = hour_df.groupby('dteday')[['temp', 'hum']].mean().reset_index()
daily_weather.rename(columns={'temp': 'avg_temp', 'hum': 'avg_hum'}, inplace=True)
merged_df = pd.merge(day_df, daily_weather, on='dteday', how='left')

# Visualisasi 1: Pengaruh Musim
st.header("Pengaruh Musim Terhadap Jumlah Penyewaan Sepeda")
season_rental = merged_df.groupby('season')['cnt'].mean().reset_index()
fig_season, ax_season = plt.subplots(figsize=(8, 5))
sns.barplot(x='season', y='cnt', data=season_rental, ax=ax_season)
ax_season.set_xlabel("Musim")
ax_season.set_ylabel("Rata-rata Jumlah Penyewaan")
st.pyplot(fig_season)

# Visualisasi 2: Pengaruh Hari Kerja
st.header("Pengaruh Hari Kerja Terhadap Jumlah Penyewaan Sepeda")
workingday_rental = merged_df.groupby('workingday')['cnt'].mean().reset_index()
fig_workingday, ax_workingday = plt.subplots(figsize=(8, 5))
sns.barplot(x='workingday', y='cnt', data=workingday_rental, ax=ax_workingday)
ax_workingday.set_xlabel("Hari Kerja (0: Bukan, 1: Iya)")
ax_workingday.set_ylabel("Rata-rata Jumlah Penyewaan")
st.pyplot(fig_workingday)

# Visualisasi 3: Pengaruh Temperatur
st.header("Pengaruh Temperatur Terhadap Jumlah Penyewaan Sepeda")
fig_temp, ax_temp = plt.subplots(figsize=(8, 5))
sns.scatterplot(x='avg_temp', y='cnt', data=merged_df, ax=ax_temp)
ax_temp.set_xlabel("Rata-rata Temperatur Harian")
ax_temp.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig_temp)

# Visualisasi 4: Pengaruh Kelembaban
st.header("Pengaruh Kelembaban Terhadap Jumlah Penyewaan Sepeda")
fig_hum, ax_hum = plt.subplots(figsize=(8, 5))
sns.scatterplot(x='avg_hum', y='cnt', data=merged_df, ax=ax_hum)
ax_hum.set_xlabel("Rata-rata Kelembaban Harian")
ax_hum.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig_hum)

st.write("Sumber data: day.csv dan hour.csv")
