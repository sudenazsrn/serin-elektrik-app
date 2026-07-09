import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Serin Elektrik", layout="centered")
st.title("⚡ Serin Elektrik Takip")

# Projeler listesi
projeler = ["Seis Yapı", "Konut Projesi", "Diğer"]

# 1. Proje Seçimi veya Yeni Proje Ekleme
secim_turu = st.radio("İşlem Türü:", ["Kayıtlı Proje Seç", "Yeni Proje Ekle"])

if secim_turu == "Kayıtlı Proje Seç":
    secilen_proje = st.selectbox("Proje Seç:", projeler)
else:
    secilen_proje = st.text_input("Yeni Proje Adını Yaz:")

# 2. Malzeme ve Miktar
malzeme = st.text_input("Malzeme Adı")
miktar = st.number_input("Miktar", min_value=0)

if st.button("Kaydet"):
    if secilen_proje and malzeme:
        st.success(f"✅ {secilen_proje} için {malzeme} kaydedildi!")
        # Burada tabloyu gösteriyoruz
        df = pd.DataFrame({
            "Proje": [secilen_proje],
            "Malzeme": [malzeme],
            "Miktar": [miktar],
            "Tarih": [datetime.now().strftime("%d-%m-%Y %H:%M")]
        })
        st.table(df)
    else:
        st.error("Lütfen tüm alanları doldur!")
