# CP3 : Command-line captive portal connection

CP3 is a python script that provides connection to Quantic Telecom's Captive Portal without needing any graphic interface.
It can be helpful espcially for raspberry pi users that connect through SSH to their pi or any other type of command-line interfaces.

<img align="right" src=https://user-images.githubusercontent.com/67024413/120048394-43d8e200-c017-11eb-959a-d8abe24b0795.png height="150px">

> The script is supported on both ```Windows``` and ```Linux``` distributions.

## Prerequisites

### Python modules

In order to work this script needs some python3 compatible modules :
```py
import requests
import argparse
import time
import os
import ping3
from selenium import webdriver
```
Those can be downloaded by running this command in the python console :
```
pip install requests argparse time os ping3 selenium
```

### PhantomJS executable

You will also need ```PhantomJS``` to execute the js script which will allow us to connect to the captive portal.
To download the executable , go to this page : https://phantomjs.org/download.html and download the proper executable according to your exploitation system.
> Note : PhantomJS doesn't support Raspbian OS, you will need to get an adapted version of the software on this repository :
> ```sh 
> git clone https://github.com/piksel/phantomjs-raspberrypi
> ```

Remember the path to the executable! You will need to write it in the variable ```PhantomJS_path``` at the top of the script, for example : 
```py
PhantomJS_path = "C:\\Users\\John\\Documents\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe"
```

## Lauching the script

### Parameters

Once all of the prerequisites are installed, you can launch the script to attempt connecting to the captive portal. The script take 2 required parameters which are ```email``` and ```password```.
```sh
python3 CP3.py -l email -p password
or
./CP3.py -l email -p password
```
## Connection processus steps

### Connecting to captive portal server

The script will first try to contact the portal server through his url (```https://www.quantic-telecom.net/connexion-reseau```).
It will grab the HTML data of the page using ```requests``` module: 
```py
requests.get(url, 'html.parser', allow_redirects=True)
```

You will see this message if the operation is a success : 
```diff
[+] Connection established! (https://www.quantic-telecom.net/connexion-reseau) - Status : 200
```

### Execute JavaScript to log

Once ```PhantomJS``` connected to the webpage with his ```webdriver``` module, it will now execute a ```javascript``` script to inject the provided email and password into the form and submit them.
```py
driver.execute_script("document.getElementById('email').value=\'"+email+"\'")
driver.execute_script("document.getElementById('password').value=\'"+password+"\'")
driver.execute_script("document.getElementById('form-continue').click()")
```
Once it is done, the script will attempt pinging ```8.8.8.8``` (Google primary DNS server) in order to see if the internet connection is permitted and established.
After 30 secondes of trying the program will prompt an error message and exit.


## Common errors

### Web portal connection fail

```html
<font color="red">This is some text!</font>
[-] ERROR! Status code : 404 - "https://www.quantic-telecom.net/connexion-reseau"
```
> This error will appear only if the url changed, don't hesitate to contact me in this case.

```diff
[-] Unable to connect to Captive Portal: You are already connected to internet!
```
> This error will appear if you are already connected to internet through the Quantic's network.

```diff
[-] Connexion réseau impossible: You are not connected to Quantic Telecom's network.
     Exiting program.
```
> This error will appear if you are trying to connect to Quantic Telecom's network without being connected to their network.

```diff
[-] Connexion réseau impossible: Unable to access captive portal, network seems down.
     Exiting program.
```
> This error will appear if your computer isn't able to connect to the captive portal server. It should never happen.

### Credentials injection fail

```diff
[-] Email injection failed: This may be due to an invalid character.
     Exiting program.
```
> This error will appear if the script isn't able to inject the email adresse into the form. It shouldn't happen.

```diff
[-] Password injection failed: This may be due to an invalid character.
     Exiting program.
```
> This error will appear if the script isn't able to inject the password into the form. It shouldn't happen.

```diff
[-]  Submission failed: This may be due to an invalid element name in the js query.
     Exiting program.
```
> This error will appear if the script isn't able to submit your credentials to the portal. It shouldn't happen.

### Authentification error

```diff
[-] Failed to connect: Unknown error.
     Exiting program.
```
> This error will appear if the script isn't able to connect with the given credentials. Try seeing if you didn't do any typing mistake.

