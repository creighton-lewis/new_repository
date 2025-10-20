import os 
import sys 
import subprocess 
import requests

url = "https://raw.githubusercontent.com/trickest/cve/refs/heads/main/2001/CVE-2001-0004.md"
text = requests.get(url, timeout=10).text
print(text)
