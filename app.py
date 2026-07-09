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
        "Proje": [secilen_proje],
        "Malzeme": [malzeme],
        "Miktar": [miktar],
        "Tarih": [datetime.now().strftime("%d-%m-%Y %H:%M")]
    }
    
    # Veriyi bir tabloya dönüştür
    df_yeni = pd.DataFrame(yeni_veri)
    
    # Ekrana başarı mesajı ver
    st.success(f"{malzeme} sisteme kaydedildi!")
    st.table(df_yeni)
    
    # NOT: Google Sheets'e doğrudan yazmak için bir "Service Account" gerekir.
    # Şimdilik baban uygulamayı kullansın, verileri ekranında görsün.
    # Ben sana verileri tek tuşla Google Sheet'ine "yapıştırabileceğin" 
    # en basit yöntemi 1 dakikada anlatayım mı?
