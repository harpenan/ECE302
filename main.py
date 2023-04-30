import random
import matplotlib.pyplot as plt
import numpy as np
import math as m

#######################################
# Task 1
random_numbers = []
mu = 0  # zero-mean
sigma = 1  # unit-variance

for i in range(5000):
    random_variable = random.gauss(mu, sigma)
    random_numbers.append(random_variable)

fig1 = plt.figure("Task 1.1")
plt.hist(random_numbers, bins=70)
plt.title('Gaussian Random Variables')
plt.xlabel('"X" value')
plt.ylabel('Occurrences')
# plt.show()

x = []
for i in range(1, 5001):
    x.append(i)


def find_sample_mean(array):
    return np.cumsum(array)


y = np.divide(find_sample_mean(random_numbers), x)
fig2 = plt.figure("Task 1.2")
plt.plot(x, y)
plt.title('Gaussian Sample Mean')
plt.xlabel('Number of Samples')
plt.ylabel('Mean value')
# plt.show()

#######################################

#######################################
# Task 2
uniform_variable_50 = np.random.uniform(-1, 1, 50)
uniform_variable_100 = np.random.uniform(-1, 1, 100)
uniform_variable_1000 = np.random.uniform(-1, 1, 1000)
uniform_variable_5000 = np.random.uniform(-1, 1, 5000)


def find_cn(array):
    c_n = []
    for i in array:
        c_n.append(m.tan(m.pi * i))
    return c_n


fig3 = plt.figure("Task 2.1")
plt.hist(find_cn(uniform_variable_50), bins=20)
plt.title('Cn with 50 Samples')
plt.xlabel('Cn value')
plt.ylabel('Occurrences')
fig4 = plt.figure("Task 2.2")
plt.hist(find_cn(uniform_variable_100), bins=20)
plt.title('Cn with 100 Samples')
plt.xlabel('Cn value')
plt.ylabel('Occurrences')
fig5 = plt.figure("Task2.3")
plt.hist(find_cn(uniform_variable_1000), bins=40)
plt.title('Cn with 1000 Samples')
plt.xlabel('Cn value')
plt.ylabel('Occurrences')
fig6 = plt.figure("Task 2.4")
plt.hist(find_cn(uniform_variable_5000), bins=70)
plt.title('Cn with 5000 Samples')
plt.xlabel('Cn value')
plt.ylabel('Occurrences')
# plt.show()

y_value = np.divide((find_sample_mean(find_cn(uniform_variable_5000))), x)
fig7 = plt.figure("Task 2.5")
plt.plot(x, y_value)
plt.title('Cauchy Sample Mean')
plt.xlabel('Number of Samples')
plt.ylabel('Mean Value')
# plt.show()

#######################################

#######################################
# Task 3
random_numbers_x = []
random_numbers_y = []

for i in range(5000):
    random_variable_x = random.gauss(mu, sigma)
    random_numbers_x.append(random_variable_x)

for i in range(5000):
    random_variable_y = random.gauss(mu, sigma)
    random_numbers_y.append(random_variable_y)

random_numbers_x1 = []
random_numbers_y1 = []

for i in range(1000):
    random_variable_x1 = random.gauss(mu, sigma)
    random_numbers_x1.append(random_variable_x1)

for i in range(1000):
    random_variable_y1 = random.gauss(mu, sigma)
    random_numbers_y1.append(random_variable_y1)

random_numbers_x2 = []
random_numbers_y2 = []

for i in range(100):
    random_variable_x2 = random.gauss(mu, sigma)
    random_numbers_x2.append(random_variable_x2)

for i in range(100):
    random_variable_y2 = random.gauss(mu, sigma)
    random_numbers_y2.append(random_variable_y2)

random_numbers_x3 = []
random_numbers_y3 = []

for i in range(50):
    random_variable_x3 = random.gauss(mu, sigma)
    random_numbers_x3.append(random_variable_x3)

for i in range(50):
    random_variable_y3 = random.gauss(mu, sigma)
    random_numbers_y3.append(random_variable_y3)

z_5000 = np.divide(random_numbers_x, random_numbers_y)
z_1000 = np.divide(random_numbers_x1, random_numbers_y1)
z_100 = np.divide(random_numbers_x2, random_numbers_y2)
z_50 = np.divide(random_numbers_x3, random_numbers_y3)

fig8 = plt.figure('Task 3.1')
plt.hist(z_50, bins=40)
plt.title('Zn with 50 Samples')
plt.xlabel('Zn Value')
plt.ylabel('Occurrences')
fig9 = plt.figure('Task 3.2')
plt.hist(z_100, bins=40)
plt.title('Zn with 100 Samples')
plt.xlabel('Zn Value')
plt.ylabel('Occurrences')
fig10 = plt.figure('Task 3.3')
plt.hist(z_1000, bins=40)
plt.title('Zn with 1000 Samples')
plt.xlabel('Zn Value')
plt.ylabel('Occurrences')
fig11 = plt.figure('Task 3.4')
plt.hist(z_5000, bins=70)
plt.title('Zn with 5000 Samples')
plt.xlabel('Zn value')
plt.ylabel('Occurrences')
# plt.show()

y_value1 = np.divide(find_sample_mean(z_5000), x)
fig12 = plt.figure('Task 3.5')
plt.plot(x, y_value1)
plt.title('Zn Gaussian Sample Mean')
plt.xlabel('Number of Samples')
plt.ylabel('Mean Value')
plt.show()

#######################################
