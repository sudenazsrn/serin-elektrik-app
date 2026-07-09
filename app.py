import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Serin Elektrik", layout="centered")
st.title("⚡ Serin Elektrik Takip")

# Projeler
projeler = ["Seis Yapı", "Konut Projesi", "Diğer"]
secilen_proje = st.selectbox("Proje Seç:", projeler)

malzeme = st.text_input("Malzeme Adı")
miktar = st.number_input("Miktar", min_value=0)

if st.button("Kaydet"):
    yeni_veri = {
        "Proje": secilen_proje,
        "Malzeme": malzeme,
        "Miktar": miktar,
        "Tarih": datetime.now().strftime("%d-%m-%Y %H:%M")
    }
    st.success(f"{malzeme} sisteme kaydedildi!")
    st.write("Eklenen Veri:", yeni_veri)
