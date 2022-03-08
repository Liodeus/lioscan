from subprocess import PIPE, Popen
import urllib3


# Disable warnings
urllib3.disable_warnings()

# Folders creation
FOLDER_TECHNOLOGIE = "/TECHNOLOGIE/"
FOLDER_CRAWL = "/CRAWL/"
FOLDER_JS = "/JS/"

# Path off the tools
WEB_ANALYZE_TECHNO_PATH = "/home/liodeus/technologies.json"
LINKFINDER_PATH = "/home/liodeus/Documents/bugbounty/js/LinkFinder/linkfinder.py"
SECRETFINDER_PATH = "/home/liodeus/Documents/bugbounty/js/secretfinder/SecretFinder.py"

# Browser used
BROWSER = "brave"