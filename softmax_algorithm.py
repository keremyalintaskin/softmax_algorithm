# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gl0B-TY4RgNSVUMY_ho8sx_1MVf5idUK
"""

import numpy as np
import pandas as pd
import folium

def softmax(x):
    exp_x = np.exp(x - np.max(x))
    return exp_x / exp_x.sum()

mahalleler = ["Yayla", "İstasyon", "Karahıdır"]
veriler = {
    "Nüfus Yoğunluğu": [5000, 7000, 4500],
    "Mevcut Ulaşım Altyapısı": [3, 5, 2],
    "Maliyet Analizi": [100000, 150000, 90000],
    "Çevresel Etki": [2, 4, 3],
    "Sosyal Fayda": [8, 6, 9]
}

df = pd.DataFrame(veriler, index=mahalleler)

Nveri = df.copy()
Nveri["Maliyet Analizi"] = 1 / Nveri["Maliyet Analizi"]
Nveri["Çevresel Etki"] = 1 / Nveri["Çevresel Etki"]

agırlıklar = {
    "Nüfus Yoğunluğu": 0.3,
    "Mevcut Ulaşım Altyapısı": 0.2,
    "Maliyet Analizi": 0.2,
    "Çevresel Etki": 0.1,
    "Sosyal Fayda": 0.2
}

df["Toplam Skor"] = sum(normalized_data[k] * w for k, w in agırlıklar.items())
df["Softmax Puanı"] = softmax(df["Toplam Skor"].values)

enUygun = df["Softmax Puanı"].idxmax()

df["Fayda-Maliyet Oranı"] = df["Sosyal Fayda"] / df["Maliyet Analizi"]

enFaydalı = df["Fayda-Maliyet Oranı"].idxmax()

center_location = [41.7333, 27.2167]
map_kirklareli = folium.Map(location=center_location, zoom_start=13)

for mahalle, coord in zip(mahalleler, [(41.74, 27.22), (41.73, 27.21), (41.72, 27.20)]):
    folium.Marker(coord, tooltip=mahalle).add_to(map_kirklareli)

print(df)
print(f"\nEn uygun güzergah: {en_uygun}")
print(f"En faydalı güzergah (Maliyet-Fayda analizi ile): {en_faydalı}")

map_kirklareli.save("kirklareli_harita.html")