import boto3

s3 = boto3.resource("s3")

account_id = 216320350078
name_directory = "bucket-campeonato-brasileiro"
bucket_name = "{}-{}".format(name_directory, account_id)
path_relative_csv = 'archive/campeonato-brasileiro-full.csv'
archive_name = "campeonato-brasileiro.csv"

bucket = s3.Bucket(bucket_name)

if bucket.creation_date:
   print("The Bucket: {}, exists.".format(bucket_name))
   #delete_bucket =s3.delete_bucket(Bucket = bucket_name)
else:
    bucket_dl = s3.create_bucket(Bucket = bucket_name)
    print("The Bucket: {}, has been created.".format(bucket_name))

bucket.upload_file(path_relative_csv, "{}{}".format(\
    "raw-data/",\
    archive_name))
bucket.upload_file("job_spark_campeonato.py", "s3://bucket-campeonato-brasileiro-216320350078/emr-code/pyspark/job_spark_campeonato.py")

