import matplotlib.pyplot as plt
import pandas as pd

geometry_filepath = "nx192_ny64_nl27_ne12_ntheta32"

all_trials_filename = "/".join([geometry_filepath, "profiling_all_trials.csv"])
summary_filename = "/".join([geometry_filepath, "profiling_summary.csv"])

### -----

plt.close('all')

df = pd.read_csv(all_trials_filename)
print(df.values)

df_fieldsLocal = df[df.version.eq("fieldsLocal")]
df_fieldsImplicit = df[df.version.eq("fieldsImplicit")]
df_fieldsLocalBufferPacking = df[df.version.eq("fieldsLocalBufferPacking")]

fig = plt.figure()

ax = plt.gca()

ax1 = df_fieldsLocal.plot.scatter(x=0, y=3, c="red", label='fieldsLocal', ax=ax, marker='+', linewidth=1, s=20)
ax2 = df_fieldsImplicit.plot.scatter(x=0, y=3, c="blue", label='fieldsImplicit', ax=ax, marker='+', linewidth=1, s=20)
ax3 = df_fieldsLocalBufferPacking.plot.scatter(x=0, y=3, c="purple", label='fieldsLocalBufferPacking', ax=ax, marker='+', linewidth=1, s=20)
h1, l1 = ax1.get_legend_handles_labels()

df = pd.read_csv(summary_filename)
df_fieldsLocal = df[df.version.eq("fieldsLocal")]
df_fieldsImplicit = df[df.version.eq("fieldsImplicit")]
df_fieldsLocalBufferPacking = df[df.version.eq("fieldsLocalBufferPacking")]

ax1 = df_fieldsLocal.plot.scatter(x=0, y=4, c="red", label='fieldsLocal', ax=ax, marker='x', linewidth=1, s=100)
ax2 = df_fieldsImplicit.plot.scatter(x=0, y=4, c="blue", label='fieldsImplicit', ax=ax, marker='x', linewidth=1, s=100)
ax3 = df_fieldsLocalBufferPacking.plot.scatter(x=0, y=4, c="purple", label='fieldsLocalBufferPacking', ax=ax, marker='x', linewidth=1, s=100)

lgd = plt.legend(h1, l1, loc=(1.04, 0.9))
plt.xlabel('Number of processes')
plt.ylabel('Total time for 3000 timesteps (minutes)')
plt.ylim(0,11)
#plt.xlim(1296,1296)
plt.margins(x=0.3)
plt.xticks(rotation=10)

fig.set_size_inches(5.5,5)
output_full_filename = "/".join([geometry_filepath, "profiling_all_trials.pdf"])
plt.savefig(output_full_filename, bbox_extra_artists=(lgd,), bbox_inches='tight')

### -----

df = pd.read_csv(all_trials_filename)
print(df.values)
plt.close('all')

df_fieldsLocal = df[df.version.eq("fieldsLocal")]
df_fieldsImplicit = df[df.version.eq("fieldsImplicit")]
df_fieldsLocalBufferPacking = df[df.version.eq("fieldsLocalBufferPacking")]

fig = plt.figure()

ax = plt.gca()

ax1 = df_fieldsLocal.plot.scatter(x=0, y=4, c="red", label='fieldsLocal', ax=ax, marker='+', linewidth=1, s=20)
ax2 = df_fieldsImplicit.plot.scatter(x=0, y=4, c="blue", label='fieldsImplicit', ax=ax, marker='+', linewidth=1, s=20)
ax3 = df_fieldsLocalBufferPacking.plot.scatter(x=0, y=4, c="purple", label='fieldsLocalBufferPacking', ax=ax, marker='+', linewidth=1, s=20)
h1, l1 = ax1.get_legend_handles_labels()

df = pd.read_csv(summary_filename)
df_fieldsLocal = df[df.version.eq("fieldsLocal")]
df_fieldsImplicit = df[df.version.eq("fieldsImplicit")]
df_fieldsLocalBufferPacking = df[df.version.eq("fieldsLocalBufferPacking")]

ax1 = df_fieldsLocal.plot.scatter(x=0, y=6, c="red", label='fieldsLocal', ax=ax, marker='x', linewidth=1, s=100)
ax2 = df_fieldsImplicit.plot.scatter(x=0, y=6, c="blue", label='fieldsImplicit', ax=ax, marker='x', linewidth=1, s=100)
ax3 = df_fieldsLocalBufferPacking.plot.scatter(x=0, y=6, c="purple", label='fieldsLocalBufferPacking', ax=ax, marker='x', linewidth=1, s=100)

lgd = plt.legend(h1, l1, loc=(1.04,0.9))
plt.xlabel('Number of processes')
plt.ylabel('Initialization time (minutes)')
#plt.ylim(0,11)
#plt.xlim(1296,1296)
plt.margins(x=0.3)
plt.xticks(rotation=10)

output_full_filename = "/".join([geometry_filepath, "profiling_init_all_trials.pdf"])
fig.set_size_inches(5.5,5)
plt.savefig(output_full_filename, bbox_extra_artists=(lgd,), bbox_inches='tight')
