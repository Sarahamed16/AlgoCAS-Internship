import boto3

aws_access_key_id = 'ASIAXBZV5QBYRNBUG22A'
aws_secret_access_key = '8NH+XupsKSM+NZ8tHgblKSsuGu5k+r/dfjbXWmdL'
aws_session_token = 'IQoJb3JpZ2luX2VjEB8aCXVzLWVhc3QtMSJGMEQCIE5OFIAbxC5kRjkpevFSN3P6AU38aB2702nNa5ZbDm24AiATL4H+1qJ1NMzSgtueBSoHQzMvrULkOyQeMBVcV8w62CrzAgh4EAAaDDQ4NDkwNzUxNjAxNyIM27sRssNk056+xDQIKtAC/Jq+N8VhxsZ2kFBtDxRYph/S6DlEgasC6249ruW6m8PJx8s1GgvNX91ebd0Rym1VJzZF6BUBzpxNgJXpVS0LGjJPOpK819A/yFCoegcyrVg4T4fg/5XeexMabAeP3K7c34FrYUcoASPJu9/xpPL3bXu8RO0xmzCARIvmcC4fJGMSvcZ6hZ55oeHIDmb+gH8TF04DpxrRfLr0hqXyvSeKgk73ukd6pfOu/Aak/G7KoiIqFPpP+tHa1ofiCEE3es6JleFmH/E5easTvZxuswjfDb930qvC+mPb22XOVTwUl1Nf3CtOczNiynO7lY2/3PzBlj865KSJpq12uf3M0aKSL41rKNNvaiQ70+Z0i4zoPsry7jKWv3LcMGVPRv+ZBqXEw9M0NazMck7GTMy99GJ4bNvZObanRNlrjMEt64js7QBEeJTzGJ+lxx/+ElrDtJ44MPWGt8UGOqgB14nSlpp+KKjeq/L3YhpUPKpvbWe/dZYFWMBvYxewjvCcTJNGMoKAXCwHgr335FjNkfclY19qHGW0PVKVtlEKGMKGUZzycGpBcIkEuM2R+1L/ayRUUgVeCGyjvekiIH0qQWlwxUrWQhqq4r6Gnt+i4S4sITY1a7+uVkxi21O7AnAZxCO3QseVi/Fh+3TwavEM9IBOe9FZtjAdJ6wTn7gRc2+vyxHJWUSy'

# Create an S3 client with temporary credentials
s3_client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
    region_name='us-east-1' 
)

# Define upload details
bucket_name = 'sarasocialmediabucket'       
local_file_path = 'P:\Career\Data Engineering\ALGOcas\Tasks\Week 9\Task 1\Fatalities Isr-Pse Conflict 2000-2023.csv'
s3_key = 'Final-Project/Fatalities Isr-Pse Conflict 2000-2023.csv'          

# Upload to S3
try:
    s3_client.upload_file(local_file_path, bucket_name, s3_key)
    print(f"File uploaded to s3://{bucket_name}/{s3_key}")
except Exception as e:
    print(f"Upload failed: {e}")