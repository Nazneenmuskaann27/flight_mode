import streamlit as st
import pandas as pd
import pickle
# Load the dataset
df = pd.read_csv('flight_management_final.csv')  # Replace with the actual file name
with open('flight_management_dataset.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
# Streamlit app
st.title('Flight Booking Information App')
def set_background_image(image_url):
    # Apply custom CSS to set the background image
    page_bg_img = '''
    <style>
    .stApp {
        background-position: top;
        background-image: url(%s);
        background-size: cover;
    }

    @media (max-width: 768px) {
        /* Adjust background size for mobile devices /
        .stApp {
            background-position: top;
            background-size: contain;
            background-repeat: no-repeat;
        }
    }
    </style>
    ''' % image_url
    st.markdown(page_bg_img, unsafe_allow_html=True)


def main():
    # Set the background image URL
    background_image_url = "https://c4.wallpaperflare.com/wallpaper/860/284/941/airbus-airplane-aviation-airport-airbus-evening-light-sky-wallpaper-preview.jpg"

    # Set the background image
    set_background_image(background_image_url)

    custom_css = """
       <style>
       body {
           background-color: #4699d4;
           color: #ffffff;
           font-family: Arial, sans-serif;
       }
       select {
           background-color: #000000 !important; / Black background for select box /
           color: #ffffff !important; / White text within select box /
       }
       label {
           color: #ffffff !important; / White color for select box label */
       }
       </style>
       """
    st.markdown(custom_css, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

# Add input fields for user to provide input data
name = st.selectbox('Select Name:', df['Name'].unique())
destination = st.selectbox('Destination:', df['Destination'].unique())
flight_type = st.selectbox('Flight Type:', df['FlightType'].unique())
age = st.select_slider('Select Age:', options=list(range(df['Age'].min(), df['Age'].max() + 1)))
fare = st.select_slider('Select Fare:', options=list(range(df['Fare'].min(), df['Fare'].max() + 1)))
customer_rating = st.number_input('Customer Rating:', min_value=df['CustomerRating'].min(), max_value=df['CustomerRating'].max())
travel_class = st.selectbox('Travel Class:', df['TravelClass'].unique())
flight_status = st.selectbox('Flight Status:', df['FlightStatus'].unique())
num_passengers = st.number_input('Number of Passengers:', min_value=df['NumPassengers'].min(), max_value=df['NumPassengers'].max())

# Button to trigger prediction
if st.button('Predict Booking Mode'):
    # Combine user inputs into a DataFrame
    user_input = pd.DataFrame({
        'Name': [name],
        'Destination': [destination],
        'FlightType': [flight_type],
        'Age': [age],
        'Fare': [fare],
        'CustomerRating': [customer_rating],
        'TravelClass': [travel_class],
        'FlightStatus': [flight_status],
        'NumPassengers': [num_passengers],
    })



    # Make a prediction based on the user input
    booking_mode_prediction = 'No Online Booking' if df['BookingMode'].iloc[0] == 0 else 'Online Booking'

    # Display prediction
    st.subheader('Booking Mode Prediction:')
    st.write(f'The predicted Booking Mode is: {booking_mode_prediction}')


