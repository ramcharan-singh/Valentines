import streamlit as st
import numpy as np
import time

# Variables
st.session_state.fragment_runs = 0

# JavaScript code to scroll to the top of the page
js = '''
<script>
    var body = window.parent.document.querySelector(".main");
    console.log(body);
    body.scrollTop = 0;
</script>
'''

# Function to handle button click events (go forward)
def click_button():
    st.session_state.fragment_runs += 1
    temp = st.empty()
    with temp:
        st.components.v1.html(js)
        time.sleep(.5) # To make sure the script can execute before being deleted
    temp.empty()

# Function to check answers
def answer_check(selected,answer,message, link):
    size = len(selected)
    if size == 1:
        st.write(f"You have selected {size} item. Please select {4 - size} more.")
    elif size < 4:
        st.write(f"You have selected {size} items. Please select {4 - size} more.")
    elif size == 5:
        st.write(f"You have selected {size} items. Please remove {size - 4} item.")
    elif size > 5:
        st.write(f"You have selected {size} items. Please remove {size - 4} items.")
    elif size == 4:
        if selected == answer:
            st.write(message)
            st.markdown("![Alt Text]({temp})".format(temp=link))
            st.button("Next", on_click=click_button)
        else:
            st.write("Nope, try again")
    else:
        st.write("error")

####################### Top of the page ###########################
# Set page configuration
st.set_page_config(
    page_title = 'Rosie Boo',
    page_icon = '?',
    layout = 'wide',
    )

# Title
st.title("🎈 My new app")
st.write(
    "Hi Baby. Lets play a game of connections :smile:."
)

# Instructions
st.write("""
This game of connections is abit different from usual.
You will need to find the group of four items that share something in common amongst all the random items.
There is only 1 group per level. 
There are 5 levels ranging from easy to hard. 
"""
)

st.write(
    "Thats all! Let's begin."
)

# Main Body
@st.fragment
def my_fragment():
    # State 1: Friends
    if st.session_state.fragment_runs == 0:
        st.write(
            "Level 1: Easy"
        )

        easy = [["Jolene", "Daewoo", "Amanda", "Denise"], 
                ["Rachel", "Wenny", "Diane", "Chloe"], 
                ["Divya", "Lynn", "Celeste", "Madeline"], 
                ["Esther", "Maurice", "Rosie", "Jennifer"]]
        
        easy_answer = set(["Divya", "Madeline", "Rosie", "Wenny"])

        easy1 = st.pills("easy1", easy[0], selection_mode="multi", label_visibility="collapsed")
        easy2 = st.pills("easy2", easy[1], selection_mode="multi", label_visibility="collapsed")
        easy3 = st.pills("easy3", easy[2], selection_mode="multi", label_visibility="collapsed")
        easy4 = st.pills("easy4", easy[3], selection_mode="multi", label_visibility="collapsed")

        if st.button("Submit"):
            easy_selected = set(easy1 + easy2 + easy3 + easy4)
            easy_message = "Nice! Your clique from JC 	:woman-tipping-hand: 	:woman-tipping-hand: 	:woman-tipping-hand: 	:woman-tipping-hand:"
            easy_link = "https://media1.tenor.com/m/SBqTSsfp5uMAAAAC/mochi-mochimochi.gif"
            answer_check(easy_selected, easy_answer, easy_message, easy_link)
    # State 2: Places
    elif st.session_state.fragment_runs == 1:
        st.write(
            "Level 2: Medium"
        )

        medium = [["Entrance", "Bali", "Tramp Park", "Gym"], 
                ["Dempsey", "Vietnam", "Bouldering", "Swee Choon"], 
                ["Hai Di Lao", "Nani's House", "Ark Bloc", "Australia"], 
                ["Kimchi Dining", "Japan", "Tampines", "Bangkok"]]
        
        medium_answer = set(["Bangkok", "Kimchi Dining", "Swee Choon", "Entrance"])

        medium1 = st.pills("medium1", medium[0], selection_mode="multi", label_visibility="collapsed")
        medium2 = st.pills("medium2", medium[1], selection_mode="multi", label_visibility="collapsed")
        medium3 = st.pills("medium3", medium[2], selection_mode="multi", label_visibility="collapsed")
        medium4 = st.pills("medium4", medium[3], selection_mode="multi", label_visibility="collapsed")

        if st.button("Submit"):
            medium_selected = set(medium1 + medium2 + medium3 + medium4)
            medium_message = "Yay! These are places we have been to together. So so fun :blush:"
            medium_link = "https://media1.tenor.com/m/G2tnkBFGsZkAAAAC/peach-and-goma-goma-and-peach.gif"
            answer_check(medium_selected, medium_answer, medium_message, medium_link)
    # State 3
    elif st.session_state.fragment_runs == 1:
        st.write(
            "Level 3: Hard"
        )

        medium = [["Entrance", "Bali", "Tramp Park", "Gym"], 
                ["Dempsey", "Vietnam", "Bouldering", "Swee Choon"], 
                ["Hai Di Lao", "Nani's House", "Ark Bloc", "Australia"], 
                ["Kimchi Dining", "Japan", "Tampines", "Bangkok"]]
        
        medium_answer = set(["Bangkok", "Kimchi Dining", "Swee Choon", "Entrance"])

        medium1 = st.pills("medium1", medium[0], selection_mode="multi", label_visibility="collapsed")
        medium2 = st.pills("medium2", medium[1], selection_mode="multi", label_visibility="collapsed")
        medium3 = st.pills("medium3", medium[2], selection_mode="multi", label_visibility="collapsed")
        medium4 = st.pills("medium4", medium[3], selection_mode="multi", label_visibility="collapsed")

        if st.button("Submit"):
            medium_selected = set(medium1 + medium2 + medium3 + medium4)
            medium_message = "Yay! These are places we have been to together. So so fun :blush:"
            medium_link = "https://media1.tenor.com/m/G2tnkBFGsZkAAAAC/peach-and-goma-goma-and-peach.gif"
            answer_check(medium_selected, medium_answer, medium_message, medium_link)

my_fragment()

# "![Alt Text]({link})"