import os
import subprocess

URL = "https://github.com/CSSEGISandData/COVID-19.git"
CLONE_DIR = r"C:\Users\offco\Documents\Dev_Projects\JHUCovidDatasetAnP\COVID-19"

if os.path.exists(CLONE_DIR): subprocess.call("fetch.sh", shell=True)
else: subprocess.call("clone.sh", shell=True)