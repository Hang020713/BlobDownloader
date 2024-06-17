import os
import locale
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from urllib.parse import urlparse

import subprocess

#Get current directory
path = os.path.realpath(__file__+ "/..") + "/"
print(path)

#Read all links in list.txt
link_list = []
list_file = open(path + 'list.txt', 'r')
while True:
    line = list_file.readline()
    
    #EOF
    if not line:
        break
    
    print(line)
    link_list.append(line)
list_file.close()
print("There are total", len(link_list), "links")

#Start Looping the link
for i in range(len(link_list)):
    print("Now getting link", i, ",", link_list[i])
    #driver.get(link_list[i])
    #time.sleep(3)

    '''
    #Get Link
    JS_get_network_requests = "var performance = window.performance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; for(let i = 0; i < network.length; i++) { if(network[i].initiatorType == 'xmlhttprequest') { if(network[i].name.includes('m3u8') && !network[i].name.includes('chunklist')) { return network[i].name; } } }"
    network_requests = driver.execute_script(JS_get_network_requests)
    '''

    #Start download
    #command = 'yt-dlp ' + '\'' + network_requests + '\' -o \'' + path + str((i+1)) + '.mp4\''
    command = 'yt-dlp "' + link_list[i] + '" -o "' + path + str((i+1)) + '.mp4"'
    process = subprocess.Popen(command, shell=True).wait()
    print("Finish")