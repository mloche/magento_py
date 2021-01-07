#  magento_py 

Version : 1.0  

Developed by : Michel LOCHE   

Release date : 2021 jan 10th  

#  UTILITY    

This script writen in Python3 will take care of installing all the packages required,  
 create the database and install Magento software in its community edition.  



# REQUISITES 

To work the script requires a few tools listed bellow. You can use the bash script requisites.sh   
in the modules folder to install them.  

Or you can install manualy the following packages and modules :   
 - Python3 package
 - python3-pip package 
 - sudo package
 - git package
 - python modules PyYAML and PyMySQL


#  USAGE  


Usage is pretty straight forward, user will need to type 

>./setup.py PATH
>./setup.py config_files/config.yaml                       ***for exemple***




PATH is the path to the YAML config file, can be either relative or absolute path. The script will 
raise an error is argument is not given or invalid.  
Each step of the setup will be ended by a notification message "STEP ....." to indicate that the
step has ended successfully.  

# LOGGING 
Logs will be saved in the folder/file specified in the yaml configuration file.  


# notes :  
>if databse is on remote server, allow connection to the database from the serveur where the script will be executed
Config files are in config_files/  
 - cert.cnf for the auto certification informations, can be personalized with Organization informations
 - config.yaml for all the conf params, going from database access to magento install options.


Securing mariadb installation should be done by user if required at the end of the setup.



