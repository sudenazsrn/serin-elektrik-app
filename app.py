import streamlit as st
import pandas as pd
from datetime import datetime
import gspread
from google.oauth2.service_account import Credentials

# --- GOOGLE SHEETS AYARLARI ---
# Streamlit'in secrets (gizli) kısmına ekleyeceğimiz JSON anahtarı için kurulum
creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"])
client = gspread.authorize(creds)
sheet = client.open_by_key("1_I_q0qgwqRRqSLDY60meNuSicaKLp1cjn1j3VKbx4EM").sheet1

st.set_page_config(page_title="Serin Elektrik", layout="centered")
st.title("⚡ Serin Elektrik Takip")

# 1. Proje Seçimi
proje_secim = st.radio("İşlem:", ["Var olan projeye git", "Yeni proje aç"])
if proje_secim == "Var olan projeye git":
    secilen_proje = st.selectbox("Proje Seç:", ["Seis Yapı", "Konut Projesi"])
else:
    secilen_proje = st.text_input("Yeni Proje Adı:")

# 2. Malzeme Girişi
malzeme = st.text_input("Malzeme Adı:")
c1, c2 = st.columns(2)
miktar = c1.number_input("Miktar:", min_value=0.0)
birim = c2.selectbox("Birim:", ["Adet", "Metre", "Kg", "Boy"])

# 3. Kaydet ve Google Sheets'e Gönder
if st.button("Kaydet"):
    tarih = datetime.now().strftime("%d-%m-%Y %H:%M")
    # Veriyi Google Sheets'e ekle
    sheet.append_row([secilen_proje, malzeme, miktar, birim, tarih])
    st.success(f"✅ {malzeme} verisi Google Tabloya başarıyla gönderildi!")
