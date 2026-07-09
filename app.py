import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

st.set_page_config(page_title="Serin Elektrik", layout="centered")
st.title("⚡ Serin Elektrik Takip")

# Google Sheets Bağlantısı
conn = st.connection("gsheets", type=GSheetsConnection)

# 1. Proje Seçimi
proje_secim = st.radio("İşlem:", ["Var olan projeye git", "Yeni proje aç"])
if proje_secim == "Var olan projeye git":
    # Google Sheet'ten proje listesini çek
    df = conn.read(spreadsheet="1_I_q0qgwqRRqSLDY60meNuSicaKLp1cjn1j3VKbx4EM", usecols=[0])
    secilen_proje = st.selectbox("Proje Seç:", df["Proje"].unique())
else:
    secilen_proje = st.text_input("Yeni Proje Adı:")

# 2. Malzeme Girişi
malzeme = st.text_input("Malzeme Adı:")
c1, c2 = st.columns(2)
miktar = c1.number_input("Miktar:", min_value=0.0)
birim = c2.selectbox("Birim:", ["Adet", "Metre", "Kg", "Boy"])

# 3. Kaydet
if st.button("Kaydet"):
    yeni_satir = pd.DataFrame([[secilen_proje, malzeme, miktar, birim, datetime.now().strftime("%d-%m-%Y %H:%M")]], 
                               columns=["Proje", "Malzeme", "Miktar", "Birim", "Tarih"])
    conn.append(spreadsheet="1_I_q0qgwqRRqSLDY60meNuSicaKLp1cjn1j3VKbx4EM", data=yeni_satir)
    st.success("✅ Veri Google Tabloya gönderildi!")
