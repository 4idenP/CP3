# CP3 : Command-line captive portal connection

CP3 is a python script that provides connection to Quantic Telecom's Captive Portal without needing any graphic interface.
It can be helpful espcially for raspberry pi users that connect through SSH to their pi or any other type of command-line interfaces.

> The script is supported on both ```Windows``` and ```Linux``` distributions.

## Prerequisites

In order to work this script needs some python3 compatible modules :
```
import requests
import argparse
import time
import os
import ping3
import sys
from selenium import webdriver
```
