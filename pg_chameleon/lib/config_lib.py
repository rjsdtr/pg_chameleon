import yaml
import sys
import os
class global_config:
	"""class to manage the mysql connection"""
	def __init__(self,config_file='config/config.yaml'):
		if not os.path.isfile(config_file):
			print "**FATAL - configuration file missing **\ncopy config/config-example.yaml to config/config.yaml and set your connection settings."
			sys.exit()
		conffile=open(config_file, 'rb')
		confdic=yaml.load(conffile.read())
		conffile.close()
		self.mysql_conn=confdic["mysql_conn"]
		self.my_database=confdic["my_database"]
		self.pg_database=confdic["pg_database"]
		self.my_server_id=confdic["my_server_id"]
		self.replica_batch_size=confdic["replica_batch_size"]
		
		
