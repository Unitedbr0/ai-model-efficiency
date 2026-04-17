import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print("Dataset:\n", df)

plt.figure()
plt.bar(df['model'], df['accuracy'])
plt.title("Model Accuracy")
plt.xlabel("Model")
plt.ylabel("Accuracy")
plt.show()

df['efficiency'] = df['accuracy'] / df['latency']

plt.figure()
plt.bar(df['model'], df['efficiency'])
plt.title("Model Efficiency (Accuracy / Latency)")
plt.xlabel("Model")
plt.ylabel("Efficiency")
plt.show()
