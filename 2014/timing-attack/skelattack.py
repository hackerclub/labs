#!/usr/bin/env python

import time
import urllib
import urllib2

def timerequest(url, data=None): 

	# start a primitive timer
	start = time.time()

        # data is assumed to be a python dictionary
        payload = urllib.urlencode(data)

	# make our http request, if data is provided we will send 
	# a POST request, otherwise a GET request is sent
	urllib2.urlopen(url, payload)

	end = time.time()

	return end - start

def main():

	url = "http://ada.evergreen.edu"
	data = None
	intervals = []
	
	for i in range(0, 5):
		if (data):
			method = "HTTP/1.1 POST"	
		else:
			method = "HTTP/1.1 GET"
		print "[!] sending", method, url,
		if (data):
			print " with paramters", data
		else:
			print
		interval = timerequest(url, data)	
		intervals.append(interval)
		print "[+] returned in", interval, "seconds"	
		
	avg = reduce(lambda x, y: x + y, intervals) / len(intervals)
	print "[+] average response time was", avg, "seconds"

main()
