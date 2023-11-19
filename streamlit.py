import streamlit as st
import time

def simulate_backend_processing(progress_bar, display_text):
    progress_bar.progress(0)
    for i in range(1, 101):
        time.sleep(0.1)  # Simulating some backend processing time
        progress_bar.progress(i)
    display_text.text("Processing complete!")

def main():
    st.title("Streamlit App with Tabs")

    # Create tabs
    tabs = ["Properties", "Buyers"]
    selected_tab = st.sidebar.selectbox("Select Tab", tabs)

    # Properties Tab
    if selected_tab == "Properties":
        st.header("Properties Tab")
        progress_bar_properties = st.progress(0)
        display_text_properties = st.empty()
        button_properties = st.button("Start Processing")

        # Simulate backend processing on button click
        if button_properties:
            simulate_backend_processing(progress_bar_properties, display_text_properties)

    # Buyers Tab
    elif selected_tab == "Buyers":
        st.header("Buyers Tab")
        progress_bar_buyers = st.progress(0)
        display_text_buyers = st.empty()
        button_buyers = st.button("Start Processing")

        # Simulate different backend processing on button click
        if button_buyers:
            simulate_backend_processing(progress_bar_buyers, display_text_buyers)

if __name__ == "__main__":
    main()