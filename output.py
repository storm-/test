#this is just some code for an example 
#when working with github

# Assumes that the package 'weather-util' has been installed.
#   sudo apt-get install weather-util
#   weather -iKBOS

import subprocess

weather=subprocess.check_output(["weather", "-iKBOS"])

print "Current weather for Boston:\n\n%s" % weather
