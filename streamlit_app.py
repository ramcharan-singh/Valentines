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
            st.write("Nope, try again!")
    else:
        st.write("error")

####################### Top of the page ###########################
# Set page configuration
st.set_page_config(
    page_title = 'Ram & Rosie',
    page_icon = '?',
    layout = 'wide',
    )

# Main Body
@st.fragment
def my_fragment():
    # State 1: Friends
    if st.session_state.fragment_runs == 0:
        # Title
        st.title("Ram & Rosie :cat: :bear:")
        st.write("Hi Baby. Lets play a game of connections :smile:.")
        st.write("""
        This game of connections is abit different from usual.
        You will need to find the group of four items that share something in common amongst all the random items.
        There is only 1 group per level. 
        There are 5 levels that increases in difficulty with each level. 
        """
        )
        st.write("Thats all! Let's begin.")
        st.write("Level 1: Easy")

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
        # Title
        st.title("Ram & Rosie :cat: :bear:")
        st.write("Level 2: Medium")

        medium = [["Entrance", "Bali", "Tramp Park", "Gym"], 
                ["Dempsey", "Vietnam", "Bouldering", "Swee Choon"], 
                ["Hotpot", "Nani's House", "Ark Bloc", "Australia"], 
                ["Kimchi Dining", "Japan", "Tampines", "Bangkok"]]
        
        medium_answer = set(["Bangkok", "Kimchi Dining", "Swee Choon", "Entrance"])

        medium1 = st.pills("medium1", medium[0], selection_mode="multi", label_visibility="collapsed")
        medium2 = st.pills("medium2", medium[1], selection_mode="multi", label_visibility="collapsed")
        medium3 = st.pills("medium3", medium[2], selection_mode="multi", label_visibility="collapsed")
        medium4 = st.pills("medium4", medium[3], selection_mode="multi", label_visibility="collapsed")

        if st.button("Submit"):
            medium_selected = set(medium1 + medium2 + medium3 + medium4)
            medium_message = "Yay! These are the places we have been to together. So so fun :blush:"
            medium_link = "https://media1.tenor.com/m/G2tnkBFGsZkAAAAC/peach-and-goma-goma-and-peach.gif"
            answer_check(medium_selected, medium_answer, medium_message, medium_link)
    # State 3: Places I wanna go with Rosie
    elif st.session_state.fragment_runs == 2:
        # Title
        st.title("Ram & Rosie :cat: :bear:")
        st.write("Level 3: Hard")
        st.write("Hint: Where do you think I would want to go with you in the near future?")

        hard = [["Ram's House", "Bali", "Tramp Park", "Gym"], 
                ["Dempsey", "Vietnam", "Bouldering", "America"], 
                ["Hotpot", "Nani's House", "Ark Bloc", "Australia"], 
                ["NTU", "Japan", "Tampines", "Prawning"]]
        
        hard_answer = set(["Vietnam", "Gym", "Nani's House", "Hotpot"])

        hard1 = st.pills("hard1", hard[0], selection_mode="multi", label_visibility="collapsed")
        hard2 = st.pills("hard2", hard[1], selection_mode="multi", label_visibility="collapsed")
        hard3 = st.pills("hard3", hard[2], selection_mode="multi", label_visibility="collapsed")
        hard4 = st.pills("hard4", hard[3], selection_mode="multi", label_visibility="collapsed")

        if st.button("Submit"):
            hard_selected = set(hard1 + hard2 + hard3 + hard4)
            hard_message = "Ding Ding Ding! I want to go these places with you in the near future but the rest are also good well except America :sweat_smile:"
            hard_link = "https://media1.tenor.com/m/OfeJ1KC93AEAAAAC/goma-frisky-peach-and-goma.gif"
            answer_check(hard_selected, hard_answer, hard_message, hard_link)
    # State 4: Relek Cat
    elif st.session_state.fragment_runs == 3:
        # Title
        st.title("Ram & Rosie :cat: :bear:")
        st.write("Level 4: Damn")
        st.write("Hint: Structured nonsense I occasionally do")

        damn = [["how about it", "follow me", "out and about", "where is it"], 
                ["is it here", "oh my god", "what the", "who's asking"], 
                ["time to chow", "maybe i guess", "in every way", "lets makan"], 
                ["woah woah", "very nice", "everyday", "only friday"]]
        
        damn_answer = set(["out and about", "in every way", "everyday", "time to chow"])

        damn1 = st.pills("damn1", damn[0], selection_mode="multi", label_visibility="collapsed")
        damn2 = st.pills("damn2", damn[1], selection_mode="multi", label_visibility="collapsed")
        damn3 = st.pills("damn3", damn[2], selection_mode="multi", label_visibility="collapsed")
        damn4 = st.pills("damn4", damn[3], selection_mode="multi", label_visibility="collapsed")

        if st.button("Submit"):
            damn_selected = set(damn1 + damn2 + damn3 + damn4)
            damn_message = "Relek cat is both happy and relek :sunglasses:"
            damn_link = "https://media.tenor.com/KTx1WW-lmfUAAAAi/peach-and-goma-peach-goma.gif"
            answer_check(damn_selected, damn_answer, damn_message, damn_link)
    # State 5: Valentines
    elif st.session_state.fragment_runs == 4:
        # Title
        st.title("Ram & Rosie :cat: :bear:")
        st.write("Level 5: Happy")

        happy = [["Christmas", "Jewel Changi", "Dusk", "9.30am - 11.30am"], 
                ["Dawn", "1pm - 3pm", "6.30pm - 8.30pm", "Songkran"], 
                ["4pm - 6pm", "Sunset Way", "CNY", "Brunch"], 
                ["Mount Faber Peak", "Midnight", "My House", "Valentines"]]
        
        happy_answer = set(["Dusk", "Mount Faber Peak", "6.30pm - 8.30pm", "Valentines"])

        happy1 = st.pills("happy1", happy[0], selection_mode="multi", label_visibility="collapsed")
        happy2 = st.pills("happy2", happy[1], selection_mode="multi", label_visibility="collapsed")
        happy3 = st.pills("happy3", happy[2], selection_mode="multi", label_visibility="collapsed")
        happy4 = st.pills("happy4", happy[3], selection_mode="multi", label_visibility="collapsed")

        if st.button("Submit"):
            happy_selected = set(happy1 + happy2 + happy3 + happy4)
            happy_message = ""
            happy_link = "https://media.tenor.com/ivKWdfdbV3EAAAAi/goma-goma-cat.gif"
            answer_check(happy_selected, happy_answer, happy_message, happy_link)
    # State 6: Final
    elif st.session_state.fragment_runs == 5:
        st.write("Hope you had fun Baby :grin:")
        st.write("Valentines will be at")
        st.write("Dusk @ Mount Faber Peak")
        st.write("6.30pm - 8.30pm")
        st.markdown("![Alt Text]({temp})".format(temp="https://media.tenor.com/WKCutj8Z3IIAAAAj/peach-goma.gif"))
        st.write("You are and will always be my Valentines")

my_fragment()