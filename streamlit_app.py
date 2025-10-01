import streamlit as st

st.title("🎈 Meine neue App")
st.write(
    "Lade ein Bild hoch, um es direkt in der App anzusehen. Für Hilfe und Inspiration geht es zu "
    "[docs.streamlit.io](https://docs.streamlit.io/)."
)

uploaded_file = st.file_uploader(
    "Bild auswählen",
    type=["png", "jpg", "jpeg", "gif", "bmp", "webp"],
    help="Unterstützte Formate: PNG, JPG, JPEG, GIF, BMP und WEBP.",
)

if uploaded_file is not None:
    st.success(f"Datei '{uploaded_file.name}' erfolgreich hochgeladen!")
    st.image(uploaded_file, caption=uploaded_file.name, use_container_width=True)
else:
    st.info("Bitte wähle ein Bild aus, das angezeigt werden soll.")
