import boto3
import pandas

def readfroms3(accesskeyid,accesskey,region,bucketname,bucketkey):
    # Creating the low level functional client
    client = boto3.client(
        's3',
        aws_access_key_id = accesskeyid,
        aws_secret_access_key = accesskey,
        region_name = region
    )

    # Creating the high level object oriented interface
    resource = boto3.resource(
        's3',
        aws_access_key_id = accesskeyid,
        aws_secret_access_key = accesskey,
        region_name = region
    )


    # Fetch the list of existing buckets
    clientResponse = client.list_buckets()
    
    # Print the bucket names one by one
    print('Printing bucket names...')
    for bucket in clientResponse['Buckets']:
        print(f'Bucket Name: {bucket["Name"]}')



    # Create the S3 object
    obj = client.get_object(
        Bucket = bucketname,
        Key = bucketkey
    )

    # Read data from the S3 object
    data = pandas.read_csv(obj['Body'],keep_default_na=False, na_values=None,encoding='latin-1')

    # Print the data frame
    #print('Printing the data frame...')
    #print(data)
    return data


