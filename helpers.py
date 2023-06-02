import boto3
from io import BytesIO

s3_client = boto3.client('s3')


def resize_image(image, size):
    # Resize the image while preserving the aspect ratio
    image.thumbnail(size)
    return image


def upload_image_to_s3(image, key, bucket_name):
    # Convert the image to WebP format with lossless compression
    image_data = BytesIO()
    image.save(image_data, format='webp', lossless=True)
    image_data.seek(0)

    # Upload the image to S3 using the pre-created client object
    s3_client.upload_fileobj(image_data, bucket_name, key)
    image_data.close()


def is_file_exists(bucket_name, key):
    # Check if the file already exists in the bucket
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    objs = list(bucket.objects.filter(Prefix=key))
    return len(objs) > 0


def format_file_size(file_size):
    if file_size >= 1024 * 1024:
        # Convert to MB
        file_size = f'{file_size / (1024 * 1024):.2f} MB'
    else:
        # Convert to KB
        file_size = f'{file_size / 1024:.2f} KB'

    return file_size


def get_file_size(bucket_name, key):
    # Get the file size from S3
    s3 = boto3.client('s3')
    response = s3.head_object(Bucket=bucket_name, Key=key)
    file_size = response['ContentLength']

    # Format the file size
    formatted_size = format_file_size(file_size)

    return formatted_size
