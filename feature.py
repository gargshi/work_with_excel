import pandas
import os


def create_config_file(fn):
	f=open(os.getcwd()+"\\"+fn,"w")
	f.close()


def config_file_create_if_not_exists():
	fi="config.txt"
	print(os.getcwd()+"\\"+fi,os.path.exists(os.getcwd()+"\\"+fi))
	if os.path.exists(os.getcwd()+"\\"+fi):
		print("config file present")
	else:
		print("config file not present")
		create_config_file(fi)

	ffn=os.getcwd()+"\\"+fi
	f=open(ffn, 'r')
	con=f.read().split("\n")
	con=[i for i in con if len(i) != 0]
	con=[i.split("<->") for i in con]
	con=dict(con)
	f.close()
	print(con)





def add_to_file(fn,name,marks):
	print("Adding record")
	config_file_create_if_not_exists()