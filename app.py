import streamlit as st

from processing.generate import create_signal
from processing.filter import moving_average_filter, simple_weighted_filter
from processing.plot import plot_data

st.set_page_config (

    page_title = "Signal Cleaner", layout="wide"
)

st.title("Signal Clenaer")

st.header("Create noisy sensor data and clean it using a moving average filter or a simple weighted filter.")

st.sidebar.header("Signal Generation Settings")

length = st.sidebar.slider("Length", 5, 30, 10)
points = st.sidebar.slider("Points", 100, 1000, 500)
noise_level = st.sidebar.slider("Noise", 0.0, 2.0, 0.5)

st.sidebar.header("filter Settings")

windows_size = st.sidebar.slider("Smoothing Window Size", 3, 50, 10)

generated_data = create_signal(length, points, noise_level)

st.subheader("Signal Plot")

st.subheader("Noisy Data")


if st.button("Apply Moving Average Filter"):

    filtered_data = moving_average_filter(generated_data, windows_size)

    noisy_data_plot, filtered_data_plot = plot_data(generated_data, filtered_data)

    st.pyplot(noisy_data_plot)
    st.pyplot(filtered_data_plot)
    



