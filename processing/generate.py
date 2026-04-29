import numpy as np
import pandas as pd

def create_signal (length, points, noise_level):
   
   
    time = np.linspace(0, length, points)

    clean_signal = np.sin(time) + 0.5 * np.sin(3*time)

    noise = np.random.normal(0, noise_level, points)

    noisy_signal = clean_signal + noise


    data = pd.DataFrame ( { 

        "time": time, "clean_signal": clean_signal, "noisy_signal": noisy_signal

    })

    return data

