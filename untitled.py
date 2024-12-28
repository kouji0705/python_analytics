# ライブラリをインポート
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# データフレームを作成
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
})

# 棒グラフを作成
plt.figure(figsize=(8, 5))
sns.barplot(x='Category', y='Values', data=data)
plt.title('Sample Bar Plot')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()