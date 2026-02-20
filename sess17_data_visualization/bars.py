# python file to demonstrate visualising students scores on a line

# import the required module
import matplotlib.pyplot as plt
import numpy as np

x_pt = np.array(["Adam", "Richard", "William", "Emy", "Linda"])
y_pt = np.array([86, 90, 79, 89, 80])

plt.bar(x_pt, y_pt, color='red')
plt.xlabel("Students")
plt.ylabel("Scores")
plt.title("Students' Scores Line Graph")
plt.show()
