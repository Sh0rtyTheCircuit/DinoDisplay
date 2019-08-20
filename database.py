import os
from random import randrange
import string
import getpass
import time
import array as arr

dinos_print = [] 
dino_list = []

#open a file for read only
with open('dinos.txt','r') as file:
	data = file.read()

#Adds each word (AKA Dino) from the dinos.txt file to a new list
for word in data.split():
	dino_list.append(word)
file.close()

### Chooses a random dino from the dinos.txt file. Add it to a list and print it ###
def add_dino():
	rand_dino = randrange(0,len(dino_list))
	dinos_print.append(rand_dino)
	if (len(dinos_print) < 30):
		for x in range (len(dinos_print)):
			print(x)
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
