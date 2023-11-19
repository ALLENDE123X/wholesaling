import streamlit as st
import time
import pandas as pd
from app.generateLead import generatePropertyLeads, generateBuyerLeads
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

# Load CSV file from the repo
csv_file_path_properties = "/Users/allisonwang/Documents/Hackathon/wholesaling/ActualPropertyOwnerList.csv"
properties = pd.read_csv(csv_file_path_properties)

csv_file_path_buyers = "/Users/allisonwang/Documents/Hackathon/wholesaling/ActualBuyerList.csv"
buyers = pd.read_csv(csv_file_path_buyers)

def simulate_backend_processing(progress_bar, display_text):
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

        # Add filtering UI
        global properties  # Ensure 'properties' is treated as a global variable
        properties = filter_dataframe(properties)
        st.write(properties)

        st.subheader("Voicemail Message for Property Owners:")
        premade_text = "Hey there <name>, we saw that you matched for a listing at <address>.\nGive us a call when you can, thank you!"
        st.text(premade_text)
        progress_bar_properties = st.progress(0)
        display_text_properties = st.empty()
        st.slider('Batch Size', min_value=1, max_value=100)
        button_properties = st.button("Start Calling")

        # Simulate backend processing on button click
        if button_properties:
            generatePropertyLeads()
            simulate_backend_processing(progress_bar_properties, display_text_properties)

    # Buyers Tab
    elif selected_tab == "Buyers":
        st.header("Buyers List")

        # Add filtering UI
        global buyers  # Ensure 'buyers' is treated as a global variable
        buyers = filter_dataframe(buyers)
        st.write(buyers)

        st.subheader("Voicemail Message for Buyers:")
        premade_text = "Hey there <name>, we saw that you matched for a listing at <address>.\nGive us a call when you can, thank you!"
        st.text(premade_text)
        progress_bar_buyers = st.progress(0)
        display_text_buyers = st.empty()
        st.slider('Batch Size', min_value=1, max_value=100)
        button_buyers = st.button("Start Calling")

        # Simulate different backend processing on button click
        if button_buyers:
            generateBuyerLeads()
            simulate_backend_processing(progress_bar_buyers, display_text_buyers)

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Values for {column}",
                    df[column].unique(),
                    default=list(df[column].unique()),
                )
                df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                _min = float(df[column].min())
                _max = float(df[column].max())
                step = (_max - _min) / 100
                user_num_input = right.slider(
                    f"Values for {column}",
                    min_value=_min,
                    max_value=_max,
                    value=(_min, _max),
                    step=step,
                )
                df = df[df[column].between(*user_num_input)]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Values for {column}",
                    value=(
                        df[column].min(),
                        df[column].max(),
                    ),
                )
                if len(user_date_input) == 2:
                    user_date_input = tuple(map(pd.to_datetime, user_date_input))
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring or regex in {column}",
                )
                if user_text_input:
                    df = df[df[column].astype(str).str.contains(user_text_input)]

    return df

if __name__ == "__main__":
    main()
