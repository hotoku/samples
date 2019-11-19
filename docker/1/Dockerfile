FROM python:3.7.4

# ローカルのhogeがコンテナのカレントディレクトリにコピーされる
COPY hoge . 

# WORKDIRで新しいディレクトリが作成され、実行ディレクトリがそこになる
# コンテナにログインした時のディレクトリが、指定されたディレクトリになる
RUN pwd
WORKDIR /root/fuga
RUN pwd
