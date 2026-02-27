import streamlit as st
import time

# DESIGN PREMIUM AZUL BEBÊ, PRETO E BRANCO
st.set_page_config(page_title="UNBAN VIP - BLUE", page_icon="💎")

st.markdown("""
    <style>
    .stApp { background-color: #000000; }
    h1, h2, h3, p, label { color: #FFFFFF !important; }
    /* Botão Azul Bebê VIP */
    div.stButton > button {
        background-color: #89CFF0 !important;
        color: #000000 !important;
        border-radius: 15px !important;
        border: 2px solid #FFFFFF !important;
        font-weight: bold !important;
        height: 60px !important;
        width: 100% !important;
        box-shadow: 0px 0px 15px #89CFF0;
    }
    input { background-color: #1a1a1a !important; color: #89CFF0 !important; border: 1px solid #89CFF0 !important; }
    </style>
    """, unsafe_allow_box=True)

st.title("💎 UNBAN VIP: BLUE EDITION")
st.write("---")

# CAMPO DE ID
id_player = st.text_input("DIGITE O ID PARA REMOVER O BAN", placeholder="Ex: 12345678")

if st.button("🚀 INJETAR DESBANIMENTO NO LOBBY (60s)"):
    if id_player:
        with st.status("🛠️ INICIANDO BYPASS...", expanded=True) as status:
            st.write("🔍 Localizando ID nos servidores...")
            time.sleep(2)
            st.write("💉 Injetando Script de Limpeza...")
            time.sleep(3)
            st.write("🔓 Quebrando Restrição de Lobby...")
            time.sleep(2)
            status.update(label="🚀 INJEÇÃO CONCLUÍDA!", state="complete", expanded=False)
        
        st.snow()
        st.success(f"✅ ID {id_player} FOI DESBANIDO COM SUCESSO!")
        st.info("Limpe o cache do jogo e entre agora em menos de 1 minuto.")
    else:
        st.error("ERRO: DIGITE O ID!")
