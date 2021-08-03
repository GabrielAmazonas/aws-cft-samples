import boto3


def upload_code(s3_client, file_name, bucket_name):
    s3_client.upload_file(file_name, bucket_name, 'etl.py')


def main():

    s3_client = boto3.client(
        's3',
        region_name='us-east-1',
        aws_access_key_id='',
        aws_secret_access_key='',
    )
    
    # Update the glue-etl-bucket- string appending the aws account id to it, as per GlueJobResource.yaml
    upload_code(s3_client, 'etl.py', 'glue-etl-bucket-')


if __name__ == '__main__':
    main()