import streamlit as st
import time
import pandas as pd
from app.generateLead import generateleads

# Load CSV file from the repo
csv_file_path = "/Users/allisonwang/Documents/Hackathon/wholesaling/ActualPropertyOwnerList.csv"  # Update with the actual path
properties = pd.read_csv(csv_file_path)

csv_file_path2 = "/Users/allisonwang/Documents/Hackathon/wholesaling/ActualBuyerList.csv"  # Update with the actual path
buyers = pd.read_csv(csv_file_path2)

def simulate_backend_processing(progress_bar, display_text):
    generateleads()
    progress_bar.progress(0)
    for i in range(1, 101):
        time.sleep(0.1)  # Simulating some backend processing time
        progress_bar.progress(i)
    display_text.text("Processing complete!")

def main():
    st.title("Wholesale Lead Generator")

    # Create tabs
    tabs = ["Properties", "Buyers"]
    selected_tab = st.sidebar.radio("Select Tab", tabs)

    # Properties Tab
    if selected_tab == "Properties":
        st.header("Properties List")
<<<<<<< HEAD
        st.subheader("Voicemail Template:")
        premade_text = "Hey there <owner name>, we found a buyer for a property at <street address>.\nGive us a call when you can, thank you!"
=======
        st.write(properties)

        st.subheader("Voicemail Message for Property Owners:")
        premade_text = "Hey there <name>, we saw that you matched for a listing at <address>.\nGive us a call when you can, thank you!"
>>>>>>> 65df91ccdb3aad602f51e688cf414414de8bd037
        st.text(premade_text)
        progress_bar_properties = st.progress(0)
        display_text_properties = st.empty()
        button_properties = st.button("Start Calling")

        # Simulate backend processing on button click
        if button_properties:
            simulate_backend_processing(progress_bar_properties, display_text_properties)

    # Buyers Tab
    elif selected_tab == "Buyers":
        st.header("Buyers List")
<<<<<<< HEAD
        st.subheader("Voicemail Template:")
        premade_text = "Hey there <real estate company name>, we saw that you matched for a listing at <street address>.\nGive us a call when you can, thank you!"
=======
        st.write(buyers)

        st.subheader("Voicemail Message for Buyers:")
        premade_text = "Hey there <name>, we saw that you matched for a listing at <address>.\nGive us a call when you can, thank you!"
>>>>>>> 65df91ccdb3aad602f51e688cf414414de8bd037
        st.text(premade_text)
        progress_bar_buyers = st.progress(0)
        display_text_buyers = st.empty()
        button_buyers = st.button("Start Calling")

        # Simulate different backend processing on button click
        if button_buyers:
            simulate_backend_processing(progress_bar_buyers, display_text_buyers)

if __name__ == "__main__":
    main()
