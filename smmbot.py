import requests
import json
import time
import random
from datetime import datetime
#your email
email='armskyline2022@gmail.com'
#password
password='eYQu1IaMQ04z'

SIGNUP_URL = 'https://jobs.smmshop.com/bot/register'
#login and generate auth token
def login():
    payload = {'email' : email,
          'password' : password,
          'bot_type_id' : 1 }
    resp = requests.post(SIGNUP_URL, payload)
    apiresp=resp.text
    apiresp = json.loads(apiresp)
    key=apiresp['data']['bot_auth_key_hash']
    return key
#get task and wait for next task
def gettask(key):
    payload = {'auth_key_hash' : key}
    resp = requests.post('https://jobs.smmshop.com/bot/task/get', payload)
    apiresp=resp.text
    apiresp = json.loads(apiresp)
    try:
        id=apiresp['data']['task']['id']
        print(id)
        return(id)
    except:
        time.sleep(300)
        return("none")
#submit task
def submittask(id,key):
    x=round(random.uniform(90, 126),0)
    time.sleep(x)
    payload = {'task_id_return' : id,'auth_key_hash' : key, 'version' : '5.1.3'}
    resp = requests.post('https://jobs.smmshop.com/bot/task/report', payload)
    apiresp=resp.text
    print("Task Done - Waiting for next  "+str(datetime.now().time()))
    print('\n')
print("""
Made by BOT HAT from TBN www.thebot.net


Bot Started and waiting for tasks.  """+str(datetime.now().time())+"""


It might take few hours to get some tasks so run this in background and chill.

""")

key=login()
#loop for lifetime
while True:
    id="none"
    id=gettask(key)
    if(id!="none"):
        submittask(id,key)
    else:
        pass
