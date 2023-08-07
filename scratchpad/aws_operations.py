import concurrent.futures
import logging
import os
import boto3

# logger config
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# AWS bucket location
BUCKET_SOURCE_DATA_NAME = "..."
PREFIX = '...'
SUFIX = '...'


def get_all_files_as_objects_from_s3_bucket(bucket_source_data_name: str, disk_path: str, aws_access_key_id,
                                            aws_secret_access_key) -> None:
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
    )
    s3_resource = session.resource('s3')
    my_bucket = s3_resource.Bucket(bucket_source_data_name)
    s3_object_list = []  # list of objects to be downloaded from bucket

    def _get_all_files_as_objects_from_s3_bucket(
            bucket_name: str,
            s3_objects_list: list[object]
    ) -> None:
        """
        function to get list of all files in given bucket. Function appends s3 objects to empty list.
        bucket_name: name of bucket
        :param s3_objects_list: empty list
        :return: None
        """

        for s3_object in bucket_name.objects.filter(Prefix=PREFIX):
            s3_objects_list.append(s3_object)
            # print(s3_object)

    _get_all_files_as_objects_from_s3_bucket(my_bucket, s3_object_list)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        [executor.submit(
            my_bucket.download_file(s3_object.key, f'{disk_path}//' + os.path.split(s3_object.key)[-1])
        ) for s3_object in s3_object_list[1:]]


def upload_files_to_s3(bucket_target_data_name: str, output: str, sufix: str, aws_access_key_id, aws_secret_access_key,
                       region_name) -> None:
    """function to upload data to s3"""
    logger.info(f"s3 upload started")
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=region_name
                      )
    for item in os.listdir(output):
        logger.info(f'started upload of {item}')
        with open(f'{output}/{item}', 'rb') as f:
            s3.upload_fileobj(f, bucket_target_data_name, f'{sufix}/{item}')
    logger.info(f"s3 upload ends")
