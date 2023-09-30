import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('AXISBANK.csv')

print("Dataset Information:")
print(data.info())

print("\nFirst Few Rows of the Dataset:")
print(data.head())

print("\nSummary Statistics:")
print(data.describe())

plt.figure(figsize=(10, 6))
plt.title("Example Data Visualization")
plt.scatter(data['Feature1'], data['Feature2'], c=data['Target'], cmap='viridis')
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.colorbar(label="Target")
plt.show()