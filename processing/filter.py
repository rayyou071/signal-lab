

def moving_average_filter(data, window_size):
    
    filtered_data = data.copy()

    filtered_data["filtered_signal"]  = (filtered_data["noisy_signal"].rolling(window = window_size, center = True)).mean()

    filtered_data["filtered_signal"] = filtered_data["filtered_signal"].fillna(filtered_data["noisy_signal"])


    return filtered_data



def simple_weighted_filter(data):

    filtered_data = data.copy()

    filtered_data["filtered_signal"] = 0.7 * filtered_data["noisy_signal"] + 0.3 * (filtered_data["noisy_signal"].shift(1))

    filtered_data["filtered_signal"] = filtered_data["filtered_signal"].fillna(filtered_data["noisy_signal"])

    return filtered_data

