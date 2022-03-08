from functions.config import *


def make_directory(path):
	cmd(f"mkdir {path}{FOLDER_TECHNOLOGIE}")
	cmd(f"mkdir {path}{FOLDER_CRAWL}")
	cmd(f"mkdir {path}{FOLDER_JS}")


def start_print(tool_name):
	print("**************************************************************")
	print(f"\t\t\tSTART {tool_name}")
	print("**************************************************************")


def end_print(tool_name):
	print("**************************************************************")
	print(f"\t\t\tEND {tool_name}")
	print("**************************************************************")


def banner():
	banner = '''
 _      _                                 
| |    (_)                                
| |     _   ___   ___   ___   __ _  _ __  
| |    | | / _ \ / __| / __| / _` || '_ \ 
| |____| || (_) |\__ \| (__ | (_| || | | |
\_____/|_| \___/ |___/ \___| \__,_||_| |_|
	
	'''
	print(banner)


# Thanks HaxUnit
def cmd(cmd):
    cmd = " ".join(cmd.split())
    subprocess_cmd = Popen(
        cmd,
        shell=True,
        stdout=PIPE
    )
    subprocess_return = subprocess_cmd.stdout.read().decode("utf-8").strip()
    if subprocess_return:
        print(subprocess_return)
    return subprocess_return
