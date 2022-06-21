import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm 
import statistics

from functions.classes.graph_class import Graph

def barplot(results):

    x_axis = sorted(results)
    print(f"ordered!{x_axis}")

    # Calculating mean and standard deviation
    mean = statistics.mean(x_axis)
    sd = statistics.stdev(x_axis)
    
    plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
    plt.savefig("NormalDistribution.png")