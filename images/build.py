import seaborn as sns
import matplotlib.pyplot as plt
import pioupiou as pp
sns.set_theme(style="whitegrid")

tips = sns.load_dataset("tips")
g = sns.jointplot(x="total_bill", y="tip", data=tips,
                  kind="reg", truncate=False,
                  xlim=(0, 60), ylim=(0, 12),
                  color="b", height=7)

plt.show()