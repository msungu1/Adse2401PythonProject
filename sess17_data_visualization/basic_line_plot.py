# python file to demonstrate visualising students scores on a line

# import the required module
import matplotlib.pyplot as plt
import numpy as np

x_pt = np.array(["adam", "Richard", "William", "Emy", "Linda"])
y_pt = np.array([86, 90, 79, 89, 80])
plt.plot(x_pt, y_pt, marker='x', color='red')
plt.show()
