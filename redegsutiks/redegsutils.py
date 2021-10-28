import time
import smtplib
from email.message import EmailMessage
import subprocess, sys
from subprocess import Popen, PIPE
import datetime, psutil, requests, os, shutil
from zipfile import ZipFile



def email(bot, botpassword, subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = bot
    msg['from'] = user
    password = botpassword

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()

def checkforprocess(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;


def downloadfile(filelink, path):
    url = filelink
    r = requests.get(url, allow_redirects=True)

    open(path, 'wb').write(r.content)

def unzip(path):
    with ZipFile(path, 'r') as zipObj:
        # Extract all the contents of zip file in current directory
        zipObj.extractall()

def deletefile(path):
    os.remove(path)

def movefile(path, newpath):
    original = path
    target = newpath

    shutil.move(original, target)

def testprint():
    print("hello world")
## https://codeload.github.com/RedEgs/RedEgsTools/zip/refs/heads/main