import streamlit as st
import numpy as np

# Set page configuration
st.set_page_config(
    page_title = 'Rosie Boo',
    page_icon = '?',
    layout = 'wide',
    )

# Title
st.title("🎈 My new app")
st.write(
    "Hi Baby. Lets play a game of connections"
)

# Instructions
st.write("""
This game of connections is abit different from usual.
You will need to find the group of four items that share something in common amongst all the random items.
There is only 1 group per level. 
There are 5 levels, and a bonus level, in this game ranging from easy to hard. 
"""
)

st.write(
    "Thats all! Let's begin."
)

st.write(
    "Level 1: Easy"
)

"""
"""

easy = [["Jolene", "Daewoo", "Amanda", "Denise"], ["Rachel", "Wenny", "Diane", "Chloe"], 
        [" Divya  ", "  Lynn  ", " Celeste ", "Madeline"], ["Rosie", "Maurice", "Esther", "Jennifer"]]

easy1 = st.pills("easy1", easy[0], selection_mode="multi", label_visibility="collapsed")
easy2 = st.pills("easy2", easy[1], selection_mode="multi", label_visibility="collapsed")
easy3 = st.pills("easy3", easy[2], selection_mode="multi", label_visibility="collapsed")
easy4 = st.pills("easy4", easy[3], selection_mode="multi", label_visibility="collapsed")

# options = ["North", "East", "South", "West"]
# options2 = ["Wenny", "Rosie", "Madeline", "Divya"]
# selection = st.pills("Directions", options, selection_mode="multi", label_visibility="hidden")
# selection2 = st.pills("Names", options2, selection_mode="multi", label_visibility="collapsed")

if st.button("Submit"):
    st.markdown(f"Your selected options: {easy1, easy2, easy3, easy4}.")

st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
