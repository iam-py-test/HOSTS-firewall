"""the main python file for HOSTS-firewall"""
import os
import subprocess
try:
  hostsf = open("/etc/hosts","r")
except:
  print("Error:")
