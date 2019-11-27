import seaborn as sns
import matplotlib.pyplot as plt
sns.set()

tips = sns.load_dataset('tips')
sns.relplot(x="total_bill", y="tip", col="time", hue="smoker", style="smoker", size="size",data=tips)

plt.savefig("seab")

dots = sns.load_dataset("dots")
sns.relplot(x="time", y="firing_rate", col="align",
            hue="choice", size="coherence", style="choice",
            facet_kws=dict(sharex=False),
            kind="line", legend="full", data=dots)
plt.savefig('linear')