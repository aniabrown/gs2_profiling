import matplotlib.pyplot as plt
import pandas as pd

summary_filename = 'profiling_summary.csv'
df = pd.read_csv(summary_filename)
print(df.values)
plt.close('all')

plt.figure()
df.plot.scatter(x=1, y=4)
plt.savefig("profiling_summary.pdf")
