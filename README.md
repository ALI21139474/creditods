# creditods
# credit Operational Data Store - Credit Risk management System
# This is a short project deomonstrating different aws components interacting with each other.

The goal of this project is to create a workflow which will read files from AWS S3 bucket and the files will act as input to the AWS RDS staging table (after a simple formatting). After Database load selective columns will be used to show dashboard using AWS quciksite.
>Install AWS CLI , follow the official AWS instuction here : https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
>Install python 
>Download and istall MySQL in the local system as Query Editor : https://dev.mysql.com/downloads/mysql/
>Install Python on CLI if not available already
>Run script jbp_seq_trigger_creditidsapp.sh to trigger the workflow (As part of future scope this script can be setup as a job )



