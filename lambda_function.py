import csv
import boto3
import io

def lambda_handler(event, context):
    """
    Reads a CSV file from an S3 bucket and prints its contents.
    """
    # Initialize S3 client
    s3_client = boto3.client('s3')

    # Bucket and file details
    bucket_name = 'sarasocialmediabucket'
    file_key = 'Final-Project/raw/Fatalities Isr-Pse Conflict 2000-2023.csv'

    try:
        # Get the object from S3
        s3_object = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        
        # Read the content of the file
        file_content = s3_object['Body'].read().decode('utf-8')
        
        # Use a CSV reader to process the content
        csv_reader = csv.reader(io.StringIO(file_content))
        
        # Print each row of the CSV
        for row in csv_reader:
            print(row)
            
        return {
            'statusCode': 200,
            'body': 'Successfully read and processed the file.'
        }
    except Exception as e:
        print(f"Error reading file from S3: {e}")
        return {
            'statusCode': 500,
            'body': f'Error reading file from S3: {e}'
        }