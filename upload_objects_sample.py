import boto3
from botocore.exceptions import ClientError

endpoint_url = 'http://localhost:9000/'
access_key_id = 'root'
secret_access_key = 'password'
filename = 'qiita.png'



s3 = boto3.resource(
        service_name='s3',
        endpoint_url=endpoint_url,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key)

try:
        # バケットを作成する
        bucket = s3.create_bucket(Bucket='uploadtest')
except ClientError as e:
  if e.response['Error']['Code'] in ('BucketAlreadyExists', 'BucketAlreadyOwnedByYou'):
    bucket = s3.Bucket('uploadtest')
  else:
    raise


bucket.upload_file(f'{filename}', filename)
