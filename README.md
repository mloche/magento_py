# magento_py
Developed for Python 3
pip module deeded :
PyYAML
Python3 installed
mariadb

requires python3 -m pip install module
python3 -c 'import module'

#Usage
script PATH
PATH is the path to the YAML config file, can be either relative or absolute path. Script will 
raise an error is argument is not given.


#packages

libmariadbclient-dev


#notes :
#if databse is on remote server, allow connection to the database from the serveur where the 
#script will be executed
Config files are in config_files/
	- cert.cnf for the auto certification informations, can be personalized with Organization
	 informations

	- config.yaml for all the conf params

Secure mariadb installation to be done by user if required


List of script functions and required arguments :
connect_database(db_serv,db_admin,db_pass,db_name)  #connects to db and returns a connector object
database_query(conn,query)  #connects with conn and applies query, returns query results
install_package(pgk_name)   #install package 
command_use(cmd)   #applies command
insert_begining_conf_files(file,added_text)   #will insert added_text at the begining of file
replace_line_file(file,string,new_string)     #will replace string by new_string in file
import_yaml_file(file)                      #import the file and return python objet with file datas
data_base()   #function configuring the database
temp()


