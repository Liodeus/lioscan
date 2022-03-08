#!/usr/bin/env python3

from functions.detect import *
from functions.crawl import *
from functions.js import *
from functions.active import *
from functions.install import *

from os import getcwd, makedirs
from datetime import datetime
import validators
import argparse


if __name__ == '__main__':
	banner()
	parser = argparse.ArgumentParser()
	parser.add_argument("-u", "--url", help="URL to scan", type=str)
	parser.add_argument("-o", "--out", help="Output directory", type=str)
	parser.add_argument("-a", "--apikey", help="Acunetix API key", type=str)
	parser.add_argument('-i', '--install', help='Install all tools', default=False, action="store_true")
	args = parser.parse_args()
	url = args.url

	# Install tools
	if args.install:
		install_all()
		exit()

	# Validate URL
	if url:
		if validators.url(url):
			url = '/'.join(url.split('/')[:3])

			# if there is no data in files abort part of the scan
			# read all files in the directory and remove the one without content

			# crawl - before uro, grep *.pdf

			# Make something with new_path.out 

			# 403 bypass
				# dontgo403 -u <URL>

			# Find backup file
				# bfac --url <URL>

			# Find parameters
				# gf redirect domain.txt //for potential open redirect/SSRF parameters
				# gf xss domain.txt //for potential xss vulnerable parameters
				# gf potential domain.txt //for xss + ssrf + open redirect parameters
				# cat *| parth

			# nuclei scan

			# make install script

			now = datetime.now()
			domain = url.split('/')[2]
			dir_name =  now.strftime("%b_%d_%Y_%H_%M_%S_") + domain
			path = getcwd()

			if args.out:
				path = args.out

			path_arg = f"{path}/{dir_name}"

			try:
				makedirs(path_arg, exist_ok=False)
				make_directory(path_arg)
			except FileExistsError:
				print("Directory already exists")
				exit()

			# Detect
			# detect_techno(url, path_arg)
			# detect_waf(url, path_arg)
			# cve_nrich(domain, path_arg)
			# port_scan_tcp(domain, path_arg)
			# make_screenshot(url, path_arg)

			# # Crawl
			# launch_spider(url, domain, path_arg)
			# launch_gauplus(domain, path_arg)
			# merge_files(domain, path_arg)

			# # Parsing
			# parse_data_merge_gospider_gauplus(domain, path_arg)
			# remove_unused_files_gospider_gauplus(domain, path_arg)

			# # JS
			# launch_js(url, domain, path_arg)
			# remove_unused_files_js(domain, path_arg)

			# Active scan
			if args.acunetixApi:
				acunetix(args.acunetixApi, domain, path_arg)
			# nuclei()
		else:
			print("Need a valid URL")
			exit()
