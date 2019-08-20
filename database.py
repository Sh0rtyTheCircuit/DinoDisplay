import os
from random import randrange
import string
import getpass
import time
import array as arr

dinos_print = [] 
dino_list = []
file_name = 'dinos.txt'

#open a file for read only
with open(file_name,'r') as file:
	data = file.read()

#Adds each word (AKA Dino) from the dinos.txt file to a new list
for word in data.split():
	dino_list.append(word)
file.close()

### Chooses a random dino from the dinos.txt file. Add it to a list and print it ###
def add_dino():
	global dinos_print
	rand_dino = randrange(0,len(dino_list))
	print "Dino number: %d" % rand_dino
	dinos_print.append(dino_list[rand_dino])
	if (len(dinos_print) < 30):
		for x in range (len(dinos_print)):
			print(dinos_print[x])
			print ("\n")
	else:
		dinos_print = " "
		print ("cleared")

def main():
	print ("Dino Database\n")
	while True:
		add_dino()
		time.sleep (30)

main()
