# CP3 : Command-line captive portal connection

CP3 is a python script that provides connection to Quantic Telecom's Captive Portal without needing any graphic interface.
It can be helpful espcially for raspberry pi users that connect through SSH to their pi or any other type of command-line interfaces.

> The script is supported on both ```Windows``` and ```Linux``` distributions.

## Prerequisites

In order to work this script needs some python3 compatible modules :
```py
import requests
import argparse
import time
import os
import ping3
import sys
from selenium import webdriver
```
Those can be downloaded by running this command in the python console :
```
pip install requests argparse time os ping3 sys selenium
```
You will also need ```PhantomJS``` to execute the js script which will allow us to connect to the captive portal.
To download the executable , go to this page : https://phantomjs.org/download.html and download the proper executable according to your exploitation system.
> Note : PhantomJS doesn't support Raspbian OS, you will need to get an adapted version of the software on this repository :
> ```sh 
> git clone https://github.com/piksel/phantomjs-raspberrypi
> ```

Remember the path to the executable, you will need to write it in the variable ```PhantomJS_path``` at the top of the script, for example : 
```py
PhantomJS_path = "C:\\Users\\John\\Documents\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe"
```
