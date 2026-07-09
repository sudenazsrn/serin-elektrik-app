import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Serin Elektrik", layout="centered")

# Veri hafızası
if 'tum_kayitlar' not in st.session_state:
    st.session_state.tum_kayitlar = pd.DataFrame(columns=["Proje", "Malzeme", "Miktar", "Birim", "Tarih"])

st.title("⚡ Serin Elektrik Takip")

# 1. Proje Seçimi veya Yeni
proje_listesi = st.session_state.tum_kayitlar["Proje"].unique().tolist()
secim = st.radio("İşlem:", ["Var olan projeye git", "Yeni proje aç"])

if secim == "Var olan projeye git":
    secilen_proje = st.selectbox("Proje Seç:", proje_listesi) if proje_listesi else st.error("Henüz proje yok!")
else:
    secilen_proje = st.text_input("Yeni Proje Adı:")

if secilen_proje:
    st.subheader(f"📁 Proje: {secilen_proje}")
    
    # Malzeme Girişi
    with st.expander("➕ Yeni Malzeme Ekle"):
        malzeme = st.text_input("Malzeme:")
        c1, c2 = st.columns(2)
        miktar = c1.number_input("Miktar:", min_value=0.0)
        birim = c2.selectbox("Birim:", ["Adet", "Metre", "Kg", "Boy"])
        
        if st.button("Kaydet"):
            yeni = {"Proje": secilen_proje, "Malzeme": malzeme, "Miktar": miktar, "Birim": birim, "Tarih": datetime.now().strftime("%H:%M")}
            st.session_state.tum_kayitlar = pd.concat([st.session_state.tum_kayitlar, pd.DataFrame([yeni])], ignore_index=True)
            st.rerun()

    # Sadece o projeye ait malzemeleri göster
    proje_verisi = st.session_state.tum_kayitlar[st.session_state.tum_kayitlar["Proje"] == secilen_proje]
    st.table(proje_verisi[["Malzeme", "Miktar", "Birim", "Tarih"]])
