import numpy as np
import matplotlib.pyplot as plt
import random
class Plot:
    def GraphPlot():
        x_axis=np.random.randint(10,40,10)
        y_axis=np.random.randint(20,50,10)
        print("X axis values ",x_axis)
        print("Y axis values ",y_axis)
        plt.plot(x_axis,marker="o",mfc="violet",mec="yellow",color="red",linestyle="-.",label="first line")
        plt.plot(y_axis,marker="o",mfc="black",mec="black",color="green",linestyle="dashed",label="second line")
        plt.grid(color="green")
        plt.xlabel('Market Cap')
        plt.ylabel('Share prices')
        plt.title("Stock Market")
        plt.legend()
        plt.legend()
        plt.show()
Plot.GraphPlot()
