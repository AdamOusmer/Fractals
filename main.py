""" Program for generation of fractals base on z(n+1) = zn ^ 2 + c"""

""" Imports """

import numpy as np
from matplotlib import pyplot as ppl
from tqdm import tqdm
import datetime
from tkinter import simpledialog as sd


""" Constant Declaration """

sizePoints = 00.1
sizeImage = 500 # number of pixels on one side of the picture
nbIteration = 60


""" Ask for inputs and creating the number """

a = sd.askfloat("Real Value", "Please enter here the real value.")
b = sd.askfloat("Imaginary Value", "Please enter here the imaginary value.")

c = a + (b * 1j)


""" Creating Grid """

x = []
y = []
temporaryTable = np.linspace(-2, 2, sizeImage)

print("Generating grid...")
for i in tqdm(temporaryTable):
    for k in temporaryTable:
        x.append(i)
        y.append(k)


""" Calculation for the colors """

print("Generating values...")

nbIterationsMade = []

for i in tqdm(range(len(x))):
    k = 0
    z = 0 + 0j

    while np.absolute(z)<3 and k < nbIteration:

        k += 1
        z = z**2 + c

    nbIterationsMade.append(k)


""" Creating picture with matplotlib.pyplot"""

print("Generating picture...")

ppl.scatter(x, y, sizePoints, c=nbIterationsMade, cmap="inferno")

ppl.xlim(-2, 2)
ppl.ylim(-2, 2)
ppl.grid(False)

ppl.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
ppl.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
for pos in ['right', 'top', 'bottom', 'left']:
    ppl.gca().spines[pos].set_visible(False)

ppl.show()
