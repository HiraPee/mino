# mino de asobo

# 遊び方

```
pip install boto3
```

```
git clone https://github.com/HiraPee/mino/
```

```
docker compose up -d
```

or

```
docker-compose up -d
```

コンテナ作成後ローカルディレクトリに minio_data フォルダが作成されています
minio_data 直下にディレクトリを作成するとその名前のバケットが作成されます

http://localhost:9001/ で docker-compose.yml に設定した user とパスワードを入力後バケット内に画像を置きます

ローカルのディレクトリで

```
python list_objects_sample.py
```

するとアップロードした画像の情報が得られます
やったね
