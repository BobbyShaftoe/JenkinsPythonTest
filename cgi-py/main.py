#!/usr/bin/env python

import cgi
import cgitb
import os

cgitb.enable(display=0, logdir="/var/log")
#cgitb.enable()

form = cgi.FieldStorage()

print ("Content-type: text/html")
print ("\r\n")

print("<p>name:", form["name"].value)


#if "name" not in form:
####    print("<H1>Error</H1>")
#    print("Please fill in the name and addr fields.")
#    return
#print("<p>name:", form["name"].value)

