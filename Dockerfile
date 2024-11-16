# ベースイメージとしてPythonを使用
FROM python:3.9-slim

# 必要なツールをインストール
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# pipを最新バージョンにアップグレード
RUN pip install --upgrade pip

# データ分析用ライブラリをインストール
RUN pip install \
    numpy \
    pandas \
    matplotlib \
    seaborn \
    scikit-learn \
    jupyterlab

# 作業ディレクトリを設定
WORKDIR /workspace

# コンテナ起動時のデフォルトコマンドを設定
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]