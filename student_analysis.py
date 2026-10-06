import pandas as pd

df = pd.read_csv("student_performance.csv")

print(df)
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)

print("\nStudent Average:")
print(df[["Name", "Average"]])
top_student = df.loc[df["Average"].idxmax()]

print("\nTop Performing Student:")
print(top_student)

import matplotlib.pyplot as plt

plt.bar(df["Name"], df["Average"])
plt.title("Student Average Performance")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.show()