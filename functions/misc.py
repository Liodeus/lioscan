from functions.config import *
import requests
import os


def make_directory(path):
	"""
		Create directories
	"""
	cmd(f"mkdir {path}{FOLDER_TECHNOLOGIE}")
	cmd(f"mkdir {path}{FOLDER_CRAWL}")
	cmd(f"mkdir {path}{FOLDER_JS}")


def url_respond(url):
	"""
		Return True if url response code is 200
	"""
	return requests.get(url, verify=False).status_code == 200


def check_install():
	"""
		Check if files in config.py are there
	"""
	check1 = os.path.exists(LINKFINDER_PATH)
	check2 = os.path.exists(SECRETFINDER_PATH)

	if check1 == False or check2 == False:
		return False
	return True


def start_print(tool_name):
	"""
		Global print start
	"""
	print("**************************************************************")
	print(f"\t\t\tSTART {tool_name}")
	print("**************************************************************\n")


def end_print(tool_name):
	"""
		Global print end
	"""
	print("**************************************************************")
	print(f"\t\t\tEND {tool_name}")
	print("**************************************************************")


def banner():
	"""
		Print the banner
	"""
	banner = '''
 _      _                                 
| |    (_)                                
| |     _   ___   ___   ___   __ _  _ __  
| |    | | / _ \ / __| / __| / _` || '_ \ 
| |____| || (_) |\__ \| (__ | (_| || | | |
\_____/|_| \___/ |___/ \___| \__,_||_| |_|
	
	'''
	print(banner)


def cmd_screen(cmd_arg):
	"""
		Run any command given and print it directly on the screen
	"""
	cmd_arg = " ".join(cmd_arg.split())
	subprocess_cmd = Popen(cmd_arg, shell=True, stdout=PIPE)

	while subprocess_cmd.poll() is None:
		nextline = subprocess_cmd.stdout.readline()
		if nextline == '':
			continue
		print(nextline.decode("utf-8").strip())


# Thanks HaxUnit
def cmd(cmd_arg):
	"""
		Run any command given retrun a result
	"""
	cmd_arg = " ".join(cmd_arg.split())
	subprocess_cmd = Popen(
		cmd_arg,
		shell=True,
		stdout=PIPE
	)
	subprocess_return = subprocess_cmd.stdout.read().decode("utf-8").strip()
	if subprocess_return:
		print(subprocess_return)
	return subprocess_return