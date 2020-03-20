import matplotlib.pyplot as plt
import pandas as pd

geometry_filepath = "nx96_ny96_nl24_ne8_ntheta26"

summary_filename = "/".join([geometry_filepath, "profiling_summary.csv"])

df = pd.read_csv(summary_filename)
print(df.values)
plt.close('all')

df_bufferPacking = df[df.version.eq("bufferPacking")]
df_orig = df[df.version.eq("orig")]

plt.figure()

ax = plt.gca()

bufferPackingError = df_bufferPacking.values[:,5]*3
origError = df_orig.values[:,5]*3

ax1 = df_bufferPacking.plot.scatter(x=1, y=4, yerr=bufferPackingError, c="red", label='bufferPacking', ax=ax, marker='x', linewidth=1, s=50)
ax2 = df_orig.plot.scatter(x=1, y=4, yerr=origError, c="blue", label='orig', ax=ax, marker='x', linewidth=1, s=50)

h1, l1 = ax1.get_legend_handles_labels()

plt.legend(h1, l1, loc=0)
plt.xlabel('Number of processes')
plt.ylabel('Total time for 3000 timesteps (minutes)')
plt.ylim(0,5)

output_filename = "/".join([geometry_filepath, "profiling_summary.pdf"])
plt.savefig(output_filename)

### --------------


all_trials_filename = "/".join([geometry_filepath, "profiling_all_trials.csv"])

df = pd.read_csv(all_trials_filename)
print(df.values)
plt.close('all')

df_bufferPacking = df[df.version.eq("bufferPacking")]
df_orig = df[df.version.eq("orig")]

plt.figure()

ax = plt.gca()

ax1 = df_bufferPacking.plot.scatter(x=1, y=3, c="red", label='bufferPacking', ax=ax, marker='x', linewidth=1, s=50)
ax2 = df_orig.plot.scatter(x=1, y=3, c="blue", label='orig', ax=ax, marker='x', linewidth=1, s=50)

h1, l1 = ax1.get_legend_handles_labels()

plt.legend(h1, l1, loc=0)
plt.xlabel('Number of processes')
plt.ylabel('Total time for 3000 timesteps (minutes)')
plt.ylim(0,5)

output_full_filename = "/".join([geometry_filepath, "profiling_all_trials.pdf"])
plt.savefig(output_full_filename)

