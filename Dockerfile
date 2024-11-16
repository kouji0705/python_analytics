# ContinuumIOのAnacondaイメージを使用
FROM continuumio/anaconda3:latest

# 作業ディレクトリを設定
WORKDIR /workspace

# Jupyter Labをインストール
RUN conda install -y jupyterlab

# 必要なPythonライブラリをインストール（必要に応じて追加）
RUN conda install -y numpy pandas matplotlib seaborn scikit-learn

# Jupyter Labを起動するためのデフォルトコマンド
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]