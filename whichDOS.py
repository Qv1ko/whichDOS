#!/usr/bin/python3
#Coding: UTF-8

# Author: Víctor García (aka v1xo)

import re, sys, subprocess

if len(sys.argv) != 2:
	print("\n\n[!] ERROR - Write syntax correctly -> python3 " + sys.argv[0] + " <ip-address>\n")
	sys.exit(1)

def get_ttl(ip_address):

	proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
	(out,err) = proc.communicate()
	out = out.split()
	out = out[12].decode('utf-8')
	ttl_value = re.findall(r"\d{1,3}", out)[0]

	return ttl_value

def get_os(ttl):

	ttl = int(ttl)
	if ttl >= 54 and ttl <= 74:
		# Linux, FreeBSD and MacOS default TTL -> 64
		return "Linux / FreeBSD / MacOS"
	elif ttl >= 118 and ttl <= 138:
		# Windows default TTL -> 128
		return "Windows"
	elif ttl >= 245 and ttl <= 255:
		# Solaris, OpenBSD default TTL -> 255
		return "Solaris / OpenBSD"
	else:
		return "Default TTL not found"

if __name__ == '__main__':

	ip_address = sys.argv[1]
	ttl = get_ttl(ip_address)
	os_name = get_os(ttl)

	print("\n%s (ttl -> %s): %s\n" % (ip_address, ttl, os_name))
