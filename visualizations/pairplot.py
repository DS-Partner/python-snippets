import seaborn as sns

penguins = sns.load_dataset("penguins")

sns.pairplot(penguins, hue="species")
