import matplotlib.pyplot as plt

def plot_data(data1, data2):

    fig1, ax1 = plt.subplots(figsize = (10,5))

    ax1.plot(data1["time"], data1["noisy_signal"], label = "Noisy Signal", alpha = 0.6)

    ax1.set_xlabel("Time")

    ax1.set_title("Noisy Signal")

    ax1.set_ylabel("Signal Value")

    ax1.legend()
    ax1.grid(True)


    fig2, ax2 = plt.subplots(figsize = (10,5))

    ax2.plot(data2["time"], data2["filtered_signal"], label = "Filtered Signal", linewidth=2)

    ax2.set_xlabel("Time")

    ax2.set_title("Filtered Signal")

    ax2.set_ylabel("Signal Value")

    ax2.legend()
    ax2.grid(True)

    return fig1, fig2

