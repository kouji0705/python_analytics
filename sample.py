# 必要なライブラリのインポート
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# サンプルデータの作成
data = {
    '名前': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    '年齢': [24, 27, 22, 32, 29],
    '得点': [85, 90, 88, 92, 95]
}

# データフレームの作成
df = pd.DataFrame(data)

# データの表示
print(df)

# 年齢と得点の散布図を作成
plt.figure(figsize=(10, 6))
sns.scatterplot(x='年齢', y='得点', data=df)
plt.title('年齢と得点の散布図')
plt.xlabel('年齢')
plt.ylabel('得点')
plt.show()