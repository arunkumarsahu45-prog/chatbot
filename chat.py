import streamlit as st
from deep_translator import GoogleTranslator

# Streamlit app
st.title("🌐 English to Odia Translator")

st.write("Type any English text below and get the Odia translation instantly.")

# Input text
english_text = st.text_area("Enter English text:")

# Translate button
if st.button("Translate"):
    if english_text.strip() != "":
        try:
            # Perform translation
            translation = GoogleTranslator(
                source="en",
                target="or"
            ).translate(english_text)

            st.success("✅ Translation:")
            st.text_area("Odia Translation:", translation, height=150)

        except Exception as e:
            st.error(f"Translation failed: {e}")

    else:
        st.warning("Please enter some text to translate.")
