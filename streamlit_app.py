import streamlit as st
import numpy as np

# Set page configuration
st.set_page_config(
    page_title = 'Rosie Boo',
    page_icon = '?',
    layout = 'wide',
    )

st.title("🎈 My new app")
st.write(
    "Hi Baby. Lets play a game of connections"
)

options = ["North", "East", "South", "West"]
options2 = ["Wenny", "Rosie", "Madeline", "Divya"]
selection = st.pills("Directions", options, selection_mode="multi", label_visibility="hidden")
selection2 = st.pills("Names", options2, selection_mode="multi", label_visibility="collapsed")

if st.button("Submit"):
    st.markdown(f"Your selected options: {selection, selection2}.")

st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
