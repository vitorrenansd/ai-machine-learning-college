import matplotlib.pyplot as plt
from data_importer import DataImporter as dt_imp

price_quote = dt_imp.pull_data_from(dt_imp, '/assets/bcdata.sgs.10813.csv')

x = [i for i in range(len(price_quote))]
y = list(reversed(price_quote))

plt.plot(x, y)
plt.xlabel('Time (day)')
plt.ylabel('USD')
plt.show()
