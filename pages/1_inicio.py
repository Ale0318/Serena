import streamlit as st

st.set_page_config(
    page_title="Serena",
    page_icon="Logo.png",
    layout="wide"
)

# ===== ESTILOS =====

st.markdown("""
<style>

.stApp {
    background-color: #2B0A57;
    color: white;
}

h1 {
    color: #F6E6B4;
    text-align:center;
    font-size:60px !important;
}

p {
    color:white;
    font-size:20px;
}

[data-testid="stSidebar"] {
    background-color: #220046;
}

div.stButton > button {
    width: 100%;
    border-radius: 25px;
    border: none;
    background-color: #FF5E8A;
    color: white;
    font-size: 24px;
    font-weight: bold;
    padding: 20px;
    min-height: 110px;
    transition: 0.3s;
    box-shadow: 0px 0px 20px rgba(255, 94, 138, 0.35);
}

div.stButton > button:hover {
    background-color: #ff7ca2;
    transform: scale(1.03);
}

</style>
""", unsafe_allow_html=True)

# ===== CONTENIDO =====

# ===== TÍTULO =====

st.title("¿Cómo te sientes hoy?")

st.markdown("""
<div style="
text-align:center;
font-size:24px;
margin-bottom:30px;
">
Estoy aquí contigo.
</div>
""", unsafe_allow_html=True)

# ===== LAYOUT PRINCIPAL =====

col1, col2 = st.columns([1,1])

# ===== IMAGEN =====

with col1:

    st.image("imagen1.png", width=450)

# ===== BOTONES =====

with col2:

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    fila1_col1, fila1_col2 = st.columns(2)
    fila2_col1, fila2_col2 = st.columns(2)

    with fila1_col1:
        if st.button("😣 Ansiedad"):
            st.success("Respira conmigo. Esto pasará.")

    with fila1_col2:
        if st.button("😵 Abrumada"):
            st.warning("Vamos paso a paso.")

    with fila2_col1:
        if st.button("😞 Tristeza"):
            st.info("No tienes que cargar todo sola.")

    with fila2_col2:
        if st.button("😤 Estrés"):
            st.success("Tu cuerpo necesita calma, no presión.")
