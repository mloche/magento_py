#!/bin/python3
# -*-  coding: UTF-8

import pymysql as mariadb
import sys

#########################
# DATABASE USAGE MODULE #
#########################


### Connecting to database returns connector ### 
def _connect(db_serv,db_admin,db_pass,db_name,db_port=3306):
	if isinstance(db_serv, str) and isinstance(db_admin,str) and isinstance(db_pass,str) and isinstance(db_name,str) and isinstance(db_port,int):
		try:
			conn = mariadb.connect(host=db_serv,user=db_admin,password=db_pass,database=db_name,port=db_port)
		except mariadb.Error as error:
			print("error connecting to mariadb platform: {} with _connect".format(error))
	else:
		sys.exit("Error invalid values given, for CONNECTING TO A DATABASE. Quit")
	return(conn)

### Query database, requires connector and query, returns query result ###
def _query(conn,query):
	if  isinstance(query,str) and isinstance(conn, mariadb.connections.Connection):
		try:
			cursor = conn.cursor()
			cursor.execute(query)
			data_query = cursor.fetchone()
		except:
			print("could not query {} with {}".format(conn,query))
	else:
		print("Error, invalid values given to QUERY A DATABASE")
	return(data_query)

### Connects to the database using the db_info list and the query list, execute querys ###
def _query_list(db_info,query):
#control purpose	print("received {} and {}".format(db_info,query))
	if isinstance(db_info, dict) and isinstance(query,(str, list)):
		try:	
			db_conn=_connect(db_info["ip_address"],db_info["db_admin"],db_info["db_password"],db_info["db_name"],db_info['db_port'])
			value =0
			max=len(query)
			for value in range(0,max):
				query_result=_query(db_conn,query[value])
#control				print(query_result)
		except:
			print("could not query {} to database {}".format(query,db_info))
#control		print("Releasing the database")
		db_conn.close()

	else:
		print("Invalid values given for QUERY LIST, DB_INFOS must be a list and QUERY a string or list of strings")


def _check_db(db_info):
	if isinstance(db_info,dict):
		try:
#			db_info["db_name"]="datatest"
			db_conn=_connect(db_info["ip_address"],db_info["db_admin"],db_info["db_password"],db_info["db_name"],db_info['db_port'])
			test_query=_query(db_conn,"show tables from {} ;".format(db_info["db_name"]))
#control			print("test_query",test_query)
			if test_query == None :
#control				print("database is empty")
				return(False)

			else:
				sys.exit("Database is not empty")
		except:
			sys.exit("Database is not empty")



