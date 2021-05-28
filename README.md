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
To download the executable , go to this page :
> https://phantomjs.org/download.html.

And download the proper executable according to your exploitation system.
