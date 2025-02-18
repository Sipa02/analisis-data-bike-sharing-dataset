# -*- coding: utf-8 -*-
"""dashboard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uM6kh2FMKkIedED1hPqyQJ_fvDe9CWIu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load dataset
day_df = pd.read_csv('https://raw.githubusercontent.com/Sipa02/analisis-data-bike-sharing-dataset/main/data/day.csv')
hour_df = pd.read_csv('https://raw.githubusercontent.com/Sipa02/analisis-data-bike-sharing-dataset/main/data/hour.csv')

# Streamlit Title
st.title('Bike Sharing Dashboard')
st.write('Pilih kategori untuk melihat jumlah penyewa sepeda')

# Pilihan kategori
kategori = st.selectbox("Pilih Kategori", ["Hari", "Jam", "Musim", "Cuaca"])

# Membuat visualisasi sesuai kategori yang dipilih
fig, ax = plt.subplots(figsize=(8, 5))

if kategori == "Musim":
    season_rentals = day_df.groupby('season')['cnt'].sum()
    ax.bar(season_rentals.index, season_rentals.values, color='skyblue')
    ax.set_xlabel("Musim")
    ax.set_ylabel("Jumlah Penyewa")
    ax.set_title("Jumlah Penyewa Sepeda Berdasarkan Musim")
    ax.set_xticks([1, 2, 3, 4])
    ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])

elif kategori == "Cuaca":
    weather_labels = {
        1: "Clear, Few clouds, Partly cloudy",
        2: "Mist + Cloudy, Broken clouds, Few clouds",
        3: "Light Snow, Light Rain + Thunderstorm",
        4: "Heavy Rain + Thunderstorm, Snow + Fog"
    }
    
    # Pastikan indeksnya bertipe integer
    weather_rentals = day_df.groupby('weathersit')['cnt'].sum()
    weather_rentals.index = weather_rentals.index.astype(int)  # Konversi ke integer
    
    # Filter indeks yang ada dalam dictionary untuk mencegah error
    valid_indices = [i for i in weather_rentals.index if i in weather_labels]

    ax.bar(valid_indices, weather_rentals.loc[valid_indices].values, color='skyblue')
    ax.set_xlabel("Cuaca")
    ax.set_ylabel("Jumlah Penyewa")
    ax.set_title("Jumlah Penyewa Sepeda Berdasarkan Cuaca")
    ax.set_xticks(valid_indices)
    ax.set_xticklabels([weather_labels[i] for i in valid_indices], rotation=20, ha='right')


elif kategori == "Hari":
    day_rentals = day_df.groupby('weekday')['cnt'].sum()
    ax.bar(day_rentals.index, day_rentals.values, color='skyblue')
    ax.set_xlabel("Hari")
    ax.set_ylabel("Jumlah Penyewa")
    ax.set_title("Jumlah Penyewa Sepeda Berdasarkan Hari")
    ax.set_xticks(range(7))
    ax.set_xticklabels(['Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'])

elif kategori == "Jam":
    hour_rentals = hour_df.groupby('hr')['cnt'].sum()
    ax.bar(hour_rentals.index, hour_rentals.values, color='skyblue')
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Penyewa")
    ax.set_title("Jumlah Penyewa Sepeda Berdasarkan Jam")
    ax.set_xticks(range(0, 24, 2))  # Menampilkan setiap 2 jam untuk keterbacaan

# Menampilkan plot di Streamlit
st.pyplot(fig)
