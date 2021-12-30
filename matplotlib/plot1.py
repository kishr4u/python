import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.set_xlabel("Values")
ax.set_ylabel("Squares")
ax.plot(input_values,squares,linewidth=3)
plt.show()

