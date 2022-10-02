import boto3
s3 = boto3.client("s3",
                  endpoint_url="http://127.0.0.1:9000",
                  aws_access_key_id='root',
                  aws_secret_access_key='password')
file = s3.download_file('test',"qiita.png", "./qiita.png")
