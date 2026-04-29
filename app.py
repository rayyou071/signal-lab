import streamlit as st

from processing.generate import create_signal
from processing.filter import moving_average_filter, simple_weighted_filter
from processing.plot import plot_data

st.set_page_config (

    page_title = "Signal Cleaner", layout="wide"
)

st.title("Signal Cleaner")

st.subheader("Create noisy sensor data and clean it using a moving average filter or a simple weighted filter.")

st.sidebar.header("Signal Generation Settings")

length = st.sidebar.slider("Length", 5, 30, 10)
points = st.sidebar.slider("Points", 100, 1000, 500)
noise_level = st.sidebar.slider("Noise", 0.0, 2.0, 0.5)

if "generated_data" not in st.session_state:
    st.session_state.generated_data = None

if "filtered_data" not in st.session_state:
    st.session_state.filtered_data = None

if "active_filter" not in st.session_state:
    st.session_state.active_filter = None

if st.sidebar.button("Generate New Signal"):
    st.session_state.generated_data = create_signal(length, points, noise_level)
    st.session_state.filtered_data = None
    st.session_state.active_filter = None

st.sidebar.header("Filter Settings")

windows_size = st.sidebar.slider("Smoothing Window Size (Moving Average Filter)", 3, 50, 10)

st.subheader("Signal Plot")


if st.session_state.generated_data is not None:

    if st.sidebar.button("Apply Moving Average Filter"):
        st.session_state.filtered_data = moving_average_filter(
            st.session_state.generated_data,
            windows_size
        )
        st.session_state.active_filter = "Moving Average"

    if st.sidebar.button("Apply Simple Weighted Filter"):
        st.session_state.filtered_data = simple_weighted_filter(
            st.session_state.generated_data
        )
        st.session_state.active_filter = "Simple Weighted"

if st.session_state.filtered_data is not None:
    st.write(f"Current filter: {st.session_state.active_filter}")

    fig = plot_data(st.session_state.filtered_data)
    st.pyplot(fig)






    



