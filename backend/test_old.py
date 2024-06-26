#!/usr/bin/python3
""" Fichier de test de l'application backend
"""

import json
import logging

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mainUrl = "http://127.0.0.1:5000/"
# head = {'Authorization': 'token {}'.format(myToken)}
headers = {"content-type": "application/json"}
user = "testuser"
pwd = "testpwd"
name = "tester"
surname = "testersurname"
email = "tester@test.com"


def auth():
    myParams = {}
    myParams["username"] = user
    myParams["password"] = pwd
    myParams["name"] = name
    myParams["surname"] = surname
    myParams["email"] = email
    return json.dumps(myParams)


def postrequest(url):
    myUrl = mainUrl + url
    logger.info("url: %s", myUrl)
    params = auth()
    response = requests.post(myUrl, headers=headers, data=params)
    if response.status_code == 200:
        logger.info("Success")
    else:
        logger.error("error %s", response.status_code)
    try:
        r = response.json()
        return r
    except Exception as e:
        logger.error(f"can't get json response, error {e}")


def getrequest(url):
    myUrl = mainUrl + url
    logger.info("url: %s", myUrl)
    params = auth()
    response = requests.get(myUrl, headers=headers, data=params)
    if response.status_code == 200:
        logger.info("Success")
    else:
        logger.error("error %s", response.status_code)
    try:
        r = response.json()
        return r
    except Exception as e:
        logger.error(f"can't get json response, error {e}")


def registration():
    logger.info("Test registration")
    postrequest("registration")


def login():
    logger.info("Test login")
    postrequest("login")


def logout():
    logger.info("Test logout")
    postrequest("logout")


def getsights():
    logger.info("Test getSights")
    getrequest("sights")


if __name__ == "__main__":
    registration()
    login()
    logout()
    getsights()
else:
    print("test.py is being imported into another module")
