import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/students.csv")

avg_by_major = df.groupby("major")["score"].mean()
print(avg_by_major)

avg_by_major.plot(kind="bar")
plt.title("Average Score by Major")
plt.xlabel("Major")
plt.ylabel("Average Score")
plt.tight_layout()
plt.savefig("average_score.png")
plt.show()