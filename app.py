import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Serin Elektrik", layout="centered")
st.title("⚡ Serin Elektrik Takip")

# Oturum yönetimi (Verilerin silinmemesi için)
if 'kayitlar' not in st.session_state:
    st.session_state.kayitlar = pd.DataFrame(columns=["Proje", "Malzeme", "Miktar", "Birim", "Tarih"])

# 1. Proje Seçimi
secim_turu = st.radio("İşlem:", ["Kayıtlı Proje", "Yeni Proje"])
if secim_turu == "Kayıtlı Proje":
    secilen_proje = st.selectbox("Proje:", ["Seis Yapı", "Konut Projesi"])
else:
    secilen_proje = st.text_input("Proje Adı:")

# 2. Malzeme, Miktar ve BİRİM
malzeme = st.text_input("Malzeme Adı:")
col1, col2 = st.columns(2)
with col1:
    miktar = st.number_input("Miktar:", min_value=0.0)
with col2:
    birim = st.selectbox("Birim:", ["Adet", "Metre", "Kg", "Boy"])

# 3. Kayıt Etme
if st.button("Kaydet"):
    yeni_satir = {"Proje": secilen_proje, "Malzeme": malzeme, "Miktar": miktar, "Birim": birim, "Tarih": datetime.now().strftime("%H:%M")}
    st.session_state.kayitlar = pd.concat([st.session_state.kayitlar, pd.DataFrame([yeni_satir])], ignore_index=True)
    st.success(f"✅ {malzeme} eklendi!")

# 4. Tabloyu sürekli göster
st.subheader("Eklenen Malzemeler")
st.table(st.session_state.kayitlar)
