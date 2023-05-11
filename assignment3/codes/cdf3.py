import matplotlib.pyplot as plt
import numpy as np

# Define the PMF of a fair six-sided die
pmf_die = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]

def calculate_cdf(pmf):
    # Calculate the CDF based on the PMF
    cdf = [pmf[0]]
    for i in range(1, len(pmf)):
        cdf.append(cdf[i-1] + pmf[i])
    return cdf

def plot_cdf(cdf):
    # Plot the CDF
    x = np.arange(len(cdf))
    plt.plot(x, cdf, marker='o')
    plt.xlabel('Product XY')
    plt.ylabel('CDF')
    plt.title('CDF of the Product XY')
    plt.grid(True)
    plt.xticks(x)
    plt.show()

# Calculate and plot the CDF for the product XY
pmf_xy = [0] * 36  # Initialize the PMF for product XY
for i in range(6):
    for j in range(6):
        pmf_xy[i*j] += pmf_die[i] * pmf_die[j]
cdf_xy = calculate_cdf(pmf_xy)
plot_cdf(cdf_xy)

