import pandas as pd
import boto3
from io import StringIO

# initialise the session with AWS
s3 = boto3.client('s3')

def read_file_from_s3(bucket_name, file_key):
    response = s3.get_object(Bucket=bucket_name, Key=file_key)

    csv_content = response['Body'].read().decode('utf-8')

    data = StringIO(csv_content)
    df = pd.read_csv(data)
    print(df)
    return df

def write_file_from_s3(df, bucket_name, file_key):
    # convert the dataframe to csv format
    csv_buffer= StringIO()
    df.to_csv(csv_buffer, index=False)
    s3.put_object(Bucket=bucket_name, Key=file_key, Body=csv_buffer.getvalue())

df = read_file_from_s3("data-folder-local-to-s3", "source_files/flight_data.csv")
write_file_from_s3(df,"data-folder-local-to-s3", "source_files/flight_data_target.csv")

"""
boto3: Allows Python code to interact with AWS services like S3, EC2, DynamoDB, etc.

io, StringIO: It helps you read/write CSV data without saving to disk.

csv_buffer: is a file-like object that you can write the CSV into.
            Later, it’s passed as the body of the S3 object upload
            
response['Body']: A stream of the file contents.


"""