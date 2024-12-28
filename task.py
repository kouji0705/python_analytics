import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import NearestNeighbors

# サンプルデータ (機械名称, メーカー, 大分類, 小分類, 重量, 出力など)
data = {
    'machine_name': ['M1', 'M2', 'M3', 'M4'],
    'maker': ['A社', 'B社', 'A社', 'C社'],
    'category_main': ['産業用', '産業用', '家庭用', '産業用'],
    'category_sub': ['ロボット', 'プレス機', 'ミキサー', 'ロボット'],
    'weight': [1000, 2000, 10, 1200],
    'power': [500, 800, 50, 450],
}

df = pd.DataFrame(data)

# 数値カラムとカテゴリカラムの指定
num_cols = ['weight', 'power']
cat_cols = ['maker', 'category_main', 'category_sub']

# 数値スケーリング用のパイプライン
num_pipeline = Pipeline([
    ('scaler', StandardScaler())
])

# カテゴリ → ワンホットエンコーディング
cat_pipeline = Pipeline([
    ('ohe', OneHotEncoder(handle_unknown='ignore'))
])

# 列ごとに適用する変換を定義
preprocessor = ColumnTransformer(transformers=[
    ('num', num_pipeline, num_cols),
    ('cat', cat_pipeline, cat_cols)
])

# 前処理をまとめたパイプライン
pipe = Pipeline([
    ('preprocessor', preprocessor)
])

# データをベクトル化
X = pipe.fit_transform(df)

print("ベクトル化後の形状:", X.shape)
print("ベクトル:")
print(X.toarray())

# 距離計算＋最近傍探索をする
# 例: ユークリッド距離で最近傍を探す
nn = NearestNeighbors(n_neighbors=3, metric='euclidean')
nn.fit(X)

# M1(=row0) に近い機器を探す
distances, indices = nn.kneighbors(X[0], n_neighbors=3)
print("M1に近い上位2件:")
for dist, idx in zip(distances[0][1:], indices[0][1:]):
    print(f" - 機器: {df['machine_name'].iloc[idx]}, 距離: {dist}")