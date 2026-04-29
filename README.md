# Signal Cleaner

Signal Cleaner is a Python and Streamlit app that generates noisy sensor data and applies a smoothing filter to clean the signal.

## Why I Built This

Real-world sensor data is rarely perfect. Sensors can produce noisy readings because of electrical interference, vibration, measurement error, or environmental conditions.

This project demonstrates how a simple moving average filter, simple weighted fitler, and exponential moving average filter can reduce noise and make a signal easier to interpret.

## Features

- Generate synthetic noisy sensor data
- Control the noise level
- Adjust smoothing strength
- Compare noisy and filtered signals
- Preview the generated data

## Tech Stack

- Python
- Streamlit
- NumPy
- Pandas
- Matplotlib

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py