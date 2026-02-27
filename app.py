import streamlit as st
import time

# DESIGN VIP AZUL BEBÊ & PRETO
st.set_page_config(page_title="UNBAN VIP FF", page_icon="💎")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    div.stButton > button {
        background-color: #89CFF0 !important;
        color: #000000 !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        height: 50px !important;
        width: 100% !important;
        border: none !important;
    }
    input { background-color: #1a1a1a !important; color: #89CFF0 !important; border: 1px solid #89CFF0 !important; }
    </style>
    """, unsafe_allow_box=True)

st.title("💎 UNBAN VIP: BLUE EDITION")
st.write("---")

id_player = st.text_input("SISTEMA: DIGITE O ID PARA DESBANIR", placeholder="Ex: 12345678")

if st.button("🚀 ATIVAR DESBANIMENTO IMEDIATO"):
    if id_player:
        bar = st.progress(0)
        msg = st.empty()
        msg.write("🛰️ Localizando ID...")
        time.sleep(1)
        bar.progress(50)
        msg.write("🔓 Liberando Lobby...")
        time.sleep(1)
        bar.progress(100)
        st.snow()
        st.success(f"✅ ID {id_player} DESBANIDO!")
    else:
        st.error("DIGITE UM ID!")
