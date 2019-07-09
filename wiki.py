#!/usr/bin/python3
import wikipedia
import sys

def search(arg):
	pad = wikipedia.summary(arg)
	print (pad)
	
search(sys.argv[1])


