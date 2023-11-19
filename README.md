# Wholesale Lead Generator

## Overview
The Wholesale Lead Generator is a cutting-edge solution designed to help wholesalers optimize their lead generation process by seamlessly connecting them with prospective properties and buyers. This platform leverages live online data and employs automation to streamline the calling process, making it efficient and hassle-free.

## Features
1. Lead Generation Automation
The heart of the platform is the automated lead generation system. It incorporates audio data from Eleven Labs and utilizes the Twilio API for batch calling. The system is designed to automatically reach out to a list of specified phone numbers, playing pre-recorded voicemail messages. This eliminates the need for manual outreach, allowing wholesalers to focus on more strategic aspects of their business.

2. Streamlit Dashboard
The user interface is powered by Streamlit, providing a user-friendly and interactive dashboard. The dashboard is organized into tabs for "Properties" and "Buyers," allowing wholesalers to manage and track different aspects of their business easily.

3. Real-time Progress Tracking
The platform provides real-time progress tracking through dynamic progress bars and display text. When initiating the processing for either properties or buyers, users can visualize the progress of the backend tasks, ensuring transparency and awareness.

4. Efficient Batch Calling
The Twilio integration enables efficient batch calling with machine detection capabilities. Wholesalers can initiate calling campaigns with pre-defined voicemail messages, maximizing the reach to potential leads.

## Installation and Usage
To use the Wholesale Lead Generator , follow these steps:

## Clone the Repository:

bash
Copy code
git clone https://github.com/ALLENDE123X/wholesaling.git

Set the Twilio account SID and authentication token as environment variables:
export TWILIO_ACCOUNT_SID=AC36760b958e539f23fb69a01b89db7caf
export TWILIO_AUTH_TOKEN=2dcfdb7e0bf76a0214c880480e54fa5b

Run the Streamlit App:
streamlit run streamlit.py
Navigate the Dashboard:

Access the Streamlit app in your web browser and navigate through the "Properties" and "Buyers" tabs.
Click the "Start Processing" button to initiate the backend processing and lead generation.
Credits
Audio Data: Eleven Labs
Batch Calling System: Twilio
Support and Feedback
For any issues or feedback, please contact our support team. We appreciate your valuable input to enhance and improve the Wholesale Lead Geneartor. Thank you for choosing our platform to streamline your wholesaling process!