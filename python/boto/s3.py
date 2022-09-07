import boto3
from boto3.session import Session

profile_name = "sciseed"
bucket_name = "sagemaker-ap-northeast-1-711091934628"

session = Session(profile_name=profile_name) # ~/.aws/credentialsのプロファイル名
s3 = session.resource("s3")

bucket = s3.Bucket(bucket_name)
objs = bucket.objects.all()

for obj in objs.filter(Prefix="data/"):
    print(obj.key)
