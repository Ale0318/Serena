import streamlit as st

st.title("¿Cómo te sientes hoy?")

emocion = st.radio(
    "Selecciona una emoción:",
    ["Ansiedad", "Estrés", "Tristeza", "Abrumado"]
)

if emocion == "Ansiedad":
    st.warning("Estoy aquí contigo.")

elif emocion == "Estrés":
    st.info("Respira profundo.")

elif emocion == "Tristeza":
    st.info("Tus emociones son válidas.")

elif emocion == "Abrumado":
    st.warning("Vamos paso a paso.")
