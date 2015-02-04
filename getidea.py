## An Eric Sato Program
## Random Idea Generator
## Gets a random suggestion from a pre-populated text file in the same directory
## If file does not exist, a blank file is created and you are asked to add items

## Version 1.0
## start -> get idea

import os
import os.path
from random import randrange


file_name = 'mainlist.txt'
path = './' + file_name

def file_exists():
	if os.path.isfile(path) and os.access(path, os.R_OK):
			return True
	else:
    		return False

def create_file():
	fname = file_name
	with open(fname, 'w') as fout:
    		fout.write('')    		

## -- Populate list with items from txt file (line by line)
def import_from_file():
	with open(file_name) as f:
    		import_list = f.readlines()	
    		import_list = [line.strip() for line in open('mainlist.txt')]
	return import_list

def fetch_idea():
	idea_choice = randrange(0, len(idea_list), 1)
	os.system('clear')
	print "This is your idea and you must do it!"
	print ">>>> " + idea_list[idea_choice] + " <<<<"	

def start():
	## -- Define list variable
	
	if file_exists() == True:
		fetch_idea()
	else:
		create_file()
		print "No idea file existed."
		print "A file has been created for you."
		print "Please open it and add one idea per line."
		
idea_list = import_from_file()

start()






