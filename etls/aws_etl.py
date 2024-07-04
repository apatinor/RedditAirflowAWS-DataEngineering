import s3fs

from utils.constants import AWS_ACCESS_KEY, AWS_ACCESS_KEY_ID


def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False,
                               key=AWS_ACCESS_KEY_ID,
                               secret=AWS_ACCESS_KEY)
        return s3
    except Exception as e:
        print(e)


def create_bucket_if_not_exists(s3: s3fs.S3FileSystem, bucket: str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print('Created bucket {}'.format(bucket))
        else:
            print('Bucket {} already exists'.format(bucket))
    except Exception as e:
        print(e)


def upload_to_s3(s3: s3fs.S3FileSystem, file_path: str, bucket: str, s3_file_name: str):
    try:
        s3.put(file_path, bucket+'/raw/'+s3_file_name)
        print('Uploaded {} to {}'.format(file_path, bucket+'/raw/'+s3_file_name))
    except FileNotFoundError:
        print('File not found')
