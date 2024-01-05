import matplotlib.pyplot as plt
import numpy as np
import csv


elec_time = []
elec_use = []
with open('boston_elec.csv', 'r', newline='') as csvfile:
    elec_reader = csv.reader(csvfile, delimiter=' ',
    quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in elec_reader:
        line_read = row[0]
        line_list = row[0].split(',')
        elec_time.append(float(line_list[0]))
        elec_use.append(float(line_list[1]))
        #print(', '.join(row))
print(len(elec_time))
print(len(elec_use))
#print(elec_time[2])


plt.style.use("seaborn-dark")



x = elec_time
#4 + np.random.normal(0,2,24)
y = elec_use
#4 + np.random.normal(0,2,len(x))

fig, ax = plt.subplots()

ax.scatter(x, y)

#ax.set(xlim = (0,8), ylim = (0,8))

plt.show()
