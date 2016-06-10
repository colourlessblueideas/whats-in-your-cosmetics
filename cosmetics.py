"""
Data source: http://www.healthdata.gov/dataset/chemicals-cosmetics
"""

import json
import operator
import matplotlib.pyplot as plt
import numpy as np

datafile = open("chemicals.json")
data = json.load(datafile)

#Count the number of times each chemical appears
chemcounts = {}

for item in data["data"]:
	if chemcounts.has_key(item[14]):
		chemcounts[item[14]] += 1
	else:
		chemcounts[item[14]] = 1

#Sort by frequency
sortedcounts = sorted(chemcounts.items(), key=operator.itemgetter(1), reverse=True)

#Plot 10 most frequently occurring chemicals
figure = plt.figure()
width = .35
ind = np.arange(10)
xs = [i[0] for i in sortedcounts[:10]]
ys = [i[1] for i in sortedcounts[:10]]
plt.bar(ind, ys, width=width)
plt.xticks(ind + width / 2, xs, rotation=90)

for i in range(len(xs)):
	print str(xs[i]) + ": " + str(ys[i])

plt.show()

"""
Top 10 potentially harmful chemicals found in cosmetics according to the California Safe Cosmetics Program (CSCP) in the California Department of Public Health.
http://www.healthdata.gov/dataset/chemicals-cosmetics

Titanium dioxide: 63864
Retinol/retinyl esters, when in daily dosages in excess of 10,000 IU, or 3,000 retinol equivalents: 2153
Butylated hydroxyanisole: 1832
Cocamide diethanolamine: 1391
Retinyl palmitate: 1042
"Trade Secret": 727
Vitamin A palmitate: 715
Mica: 512
Silica, crystalline (airborne particles of respirable size): 482
Carbon black: 474

"Worst" product categories, according to number of instances of harmful chemicals reported:

Makeup Products (non-permanent): 49459
Nail Products: 9408
Skin Care Products: 5977
Sun-Related Products: 4449
Bath Products: 2324
Hair Coloring Products: 1616
Hair Care Products (non-coloring): 1302
Tattoos and Permanent Makeup: 714
Personal Care Products: 640
Fragrances: 460

"Worst" companies, according to number of instances of harmful chemicals reported:
NYX: 3227
bareMinerals: 2412
Sally Hansen: 1774
Sephora: 1771
Victoria's Secret Beauty: 1721
CoverGirl: 1645
NARS: 1537
No7: 1472
CLARINS PARIS: 1401
Rimmel - London: 1362

"""