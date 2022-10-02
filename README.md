# mino de asobo


# 遊び方

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

コンテナ作成後ローカルディレクトリにminio_dataフォルダが作成されています
minio_data直下にディレクトリを作成するとその名前のバケットが作成されます

http://localhost:9001/ でdocker-compose.ymlに設定したuserとパスワードを入力後バケット内に画像を置きます

ローカルのディレクトリで
```
python list_objects_sample.py 
```
するとアップロードした画像の情報が得られます
やったね
