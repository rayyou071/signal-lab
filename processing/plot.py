import matplotlib.pyplot as plt

def plot_data(data):

    graph, ax = plt.subplots(figsize = (10,5))

    ax.plot(data["time"], data["noisy_signal"], label = "Noisy Signal", alpha = 0.3)
    ax.plot(data["time"], data["filtered_signal"], label = "Filtered Signal", linewidth = 2.1)

    ax.set_title("Noisy Signal vs Filtered Signal")
    ax.set_ylabel("Signal Value")
    ax.set_xlabel("Time")
    ax.legend()
    ax.grid(True)

    return graph   
    