import matplotlib.pyplot as plt

x = [i for i in range(len(price_quote))]
y = list(reversed(price_quote))

plt.plot(x, y)
plt.xlabel('Time (day)')
plt.ylabel('USD')
plt.show()
