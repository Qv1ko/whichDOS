#!/usr/bin/python3
#Coding: UTF-8

# Author: Víctor García (Qv1ko)

import re, sys, subprocess

if len(sys.argv) != 2:
	print("\n\n[!] ERROR - Write syntax correctly -> python3 " + sys.argv[0] + " <ip-address>\n")
	sys.exit(1)

def get_ttl(ip_address):

	command = ["ping", "-c", "1"] if sys.platform != "win32" else ["ping", "-n", "1"]
	proc = subprocess.Popen(command + [ip_address], stdout=subprocess.PIPE)
	(out,err) = proc.communicate()
	ttl_value = re.findall(r"ttl[=:]?\s*(\d{1,3})", out.decode('utf-8'), re.IGNORECASE)

	if not ttl_value:
		print("\n\n[!] ERROR - No response from host\n")
		sys.exit(1)

	return ttl_value[0]

def get_os(ttl):

	ttl = int(ttl)
	if ttl >= 54 and ttl <= 74:
		# Linux, FreeBSD and MacOS default TTL -> 64
		return "Linux / FreeBSD / MacOS"
	elif ttl >= 118 and ttl <= 138:
		# Windows default TTL -> 128
		return "Microsoft Windows"
	elif ttl >= 245 and ttl <= 255:
		# Solaris, OpenBSD default TTL -> 255
		return "OpenBSD / Solaris"
	else:
		return "Default TTL not found"

if __name__ == '__main__':

	ip_address = sys.argv[1]
	ttl = get_ttl(ip_address)
	os_name = get_os(ttl)

	print("\n%s (ttl -> %s): %s\n" % (ip_address, ttl, os_name))
