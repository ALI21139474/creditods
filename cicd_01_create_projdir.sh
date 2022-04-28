echo "Execution Started"
if [ -d "/creditODS_TEST" ]; then
	echo "project directory exist"
else 
	sudo mkdir /creditODS_TEST
	sudo mkdir /creditODS_TEST/script
	sudo mkdir /creditODS_TEST/log
        sudo mkdir /creditODS_TEST/reject
        sudo mkdir /creditODS_TEST/report
	sudo mkdir /creditODS_TEST/target
	sudo mkdir /creditODS_TEST/temp
	sudo mkdir /creditODS_TEST/landing
        sudo chmod 775 *
fi

