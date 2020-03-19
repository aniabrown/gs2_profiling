import matplotlib.pyplot as plt
import pandas as pd

geometry_filepath = "nx96_ny96_nl24_ne8_ntheta26"
#geometry_filepath = "nx192_ny64_nl27_ne12_ntheta32"

summary_filename = "/".join([geometry_filepath, "profiling_summary.csv"])

df = pd.read_csv(summary_filename)
print(df.values)
plt.close('all')

df_bufferPacking = df[df.version.eq("bufferPacking")]
df_orig = df[df.version.eq("orig")]

plt.figure()
plt.xlabel('Number of processes')
plt.ylabel('Total time for 3000 timesteps')

ax = plt.gca()

ax1 = df_bufferPacking.plot.scatter(x=1, y=4, c="red", label='bufferPacking', ax=ax)
ax2 = df_orig.plot.scatter(x=1, y=4, c="blue", label='orig', ax=ax)

h1, l1 = ax1.get_legend_handles_labels()

plt.legend(h1, l1)

output_filename = "/".join([geometry_filepath, "profiling_summary.pdf"])
plt.savefig(output_filename)
