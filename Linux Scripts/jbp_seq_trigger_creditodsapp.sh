#!/bin/sh

echo  "Executing Credit ODS process"
echo  "Execution Started @ " `TZ="CET" date`

#Job #1 - For Account

echo  "*****   Job #1 : scr_001_01_readfrom_s3_mysql_account.py   *****"
echo  "*****   Job Functionality: Triggering Python job that reads account data from Amazon s3 datalake and load into Amazon RDS DB- MySql table creditODS.STG_ACCOUNT"

echo "*****   Process Started @ " `TZ="CET" date` "   *****"

sudo python3 /creditODS/script/scr_001_01_readfrom_s3_mysql_account.py

if [ $? -eq 0 ]; then
	echo "*****   Job Executed successfully   *****"
	echo "*****   Process Ended @ " `TZ="CET" date` "   *****"
else 
	echo "*****   Job Aborted   *****"
	echo "***** Process Aborted @ " `TZ="CET" date` "   *****"
fi


echo "****************************************************************"
echo ""
echo ""
echo ""

#Job #2 - For Customer

echo  "*****   Job #2 : scr_001_02_readfrom_s3_mysql_customer.py    *****"
echo  "*****   Job Functionality: Triggering Python job that reads customer data from Amazon s3 datalake and load into Amazon RDS DB- MySql table creditODS.STG_CUSTOMER"

echo "*****   Process Started @ " `TZ="CET" date` "   *****"

sudo python3 /creditODS/script/scr_001_02_readfrom_s3_mysql_customer.py

if [ $? -eq 0 ]; then
        echo "*****   Job Executed successfully   *****"
        echo "*****   Process Ended @ " `TZ="CET" date` "   *****"
else
        echo "*****   Job Aborted   *****"
        echo "***** Process Aborted @ " `TZ="CET" date` "   *****"
fi


echo "****************************************************************"
echo ""
echo ""
echo ""


#Job #3 - For Product

echo  "*****   Job #3 : scr_001_03_readfrom_s3_mysql_product.py   *****"
echo  "*****   Job Functionality: Triggering Python job that reads product data from Amazon s3 datalake and load into Amazon RDS DB- MySql table creditODS.STG_PRODUCT"

echo "*****   Process Started @ " `TZ="CET" date` "   *****"

sudo python3 /creditODS/script/scr_001_03_readfrom_s3_mysql_product.py

if [ $? -eq 0 ]; then
        echo "*****   Job Executed successfully   *****"
        echo "*****   Process Ended @ " `TZ="CET" date` "   *****"
else
        echo "*****   Job Aborted   *****"
        echo "***** Process Aborted @ " `TZ="CET" date` "   *****"
fi


echo "****************************************************************"
echo ""
echo ""
echo ""


#Job #4 - For Credit Bureau

echo  "*****   Job #4 : scr_001_04_readfrom_s3_mysql_creditbureau.py   *****"
echo  "*****   Job Functionality: Triggering Python job that reads credit bureau data from Amazon s3 datalake and load into Amazon RDS DB- MySql table creditODS.STG_BUREAU_DEBT_SUMMARY"

echo "*****   Process Started @ " `TZ="CET" date` "   *****"

sudo python3 /creditODS/script/scr_001_04_readfrom_s3_mysql_creditbureau.py

if [ $? -eq 0 ]; then
        echo "*****   Job Executed successfully   *****"
        echo "*****   Process Ended @ " `TZ="CET" date` "   *****"
else
        echo "*****   Job Aborted   *****"
        echo "***** Process Aborted @ " `TZ="CET" date` "   *****"
fi


echo "****************************************************************"
echo ""
echo ""
echo ""

