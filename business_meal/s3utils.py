from storages.backends.s3boto3 import S3Boto3Storage


def StaticS3BotoStorage():
    return S3Boto3Storage(location="business_meal/static")


def MediaS3BotoStorage():
    return S3Boto3Storage(location="business_meal/media")
