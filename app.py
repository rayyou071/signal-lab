import streamlit as st

from processing.generate import create_signal
from processing.filter import moving_average_filter, simple_weighted_filter, exponential_moving_filter
from processing.plot import plot_data

st.set_page_config (

    page_title = "Signal Cleaner", layout="wide"
)

st.title("SignalLab")

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

windows_size = st.sidebar.slider("Smoothing Window Size (Moving Average Filter)", 3, 100, 10)
alpha_value = st.sidebar.slider("EMA Alpha", 0.05, 1.0, 0.2)

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

    if st.sidebar.button("Apply Exponential Moving Average"):

        st.session_state.filtered_data = exponential_moving_filter(st.session_state.generated_data, alpha_value)
        st.session_state.active_filter = "Exponential Moving Average"

if st.session_state.filtered_data is not None:
    st.write(f"Current filter: {st.session_state.active_filter}")

    fig = plot_data(st.session_state.filtered_data)
    st.pyplot(fig)

sensor_type = st.sidebar.selectbox("Sensor Type", ["Current Sensor", "Temp Sensor", "Vibration Sensor"])
st.write(f"Simulating data from a {sensor_type}.")

if st.session_state.generated_data is not None and st.session_state.filtered_data is not None:

    unfiltered_data = st.session_state.generated_data["noisy_signal"].std()
    filtered_noise = st.session_state.filtered_data["filtered_signal"].std()

    noise_reduction_percent = ((unfiltered_data - filtered_noise) / unfiltered_data) * 100

    st.metric("Noise Reduction", f"{noise_reduction_percent:.1f}%")

    if st.session_state.active_filter == "Moving Average":
        if noise_reduction_percent > 40:
            st.success("Signal quality improved significantly.")
        elif noise_reduction_percent > 15:
            st.info("Signal quality improved moderately.")
        else:
            st.warning("Filtering had limited effect. Try adjusting the smoothing settings.")

    elif st.session_state.active_filter == "Simple Weighted":
        
        if noise_reduction_percent > 40:
            st.success("Signal quality improved significantly.")
        elif noise_reduction_percent > 15:
            st.info("Signal quality improved moderately.")
        else:
            st.warning("Filtering had limited effect. Try using the Moving Average Filter.")

    
    elif st.session_state.active_filter == "Exponential Moving Average":
        
        if noise_reduction_percent > 40:
            st.success("Signal quality improved significantly.")
        elif noise_reduction_percent > 15:
            st.info("Signal quality improved moderately.")
        else:
            st.warning("Filtering had limited effect. Try adjusting EMA Alpha settings.")



