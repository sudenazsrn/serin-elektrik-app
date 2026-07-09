import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Serin Elektrik", layout="centered")
st.title("⚡ Serin Elektrik Takip")

# Veri tabanı yerine bir CSV dosyası gibi çalıştıralım
if "veri" not in st.session_state:
    st.session_state.veri = pd.DataFrame(columns=["Proje", "Malzeme", "Miktar", "Birim", "Tarih"])

# 1. Proje ve Malzeme
proje = st.text_input("Proje Adı:")
malzeme = st.text_input("Malzeme:")
c1, c2 = st.columns(2)
miktar = c1.number_input("Miktar:", min_value=0.0)
birim = c2.selectbox("Birim:", ["Adet", "Metre", "Kg", "Boy"])

# 2. Kaydet
if st.button("Kaydet"):
    yeni_satir = {"Proje": proje, "Malzeme": malzeme, "Miktar": miktar, "Birim": birim, "Tarih": datetime.now().strftime("%d-%m-%Y %H:%M")}
    st.session_state.veri = pd.concat([st.session_state.veri, pd.DataFrame([yeni_satir])], ignore_index=True)
    st.success("✅ Kaydedildi!")

# 3. Tabloyu Göster
st.table(st.session_state.veri)

# Baban için İndirme Tuşu
csv = st.session_state.veri.to_csv(index=False).encode('utf-8')
st.download_button("📥 Verileri İndir (Excel'e at)", csv, "veriler.csv", "text/csv")
