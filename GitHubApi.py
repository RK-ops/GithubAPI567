# By Shashank Ramesh Kumar
import requests
import json

def getrepo(username):
    object = requests.get("https://api.github.com/users/" + username + "/repos")
    if object.status_code != 200:
        print("User Invalid")
        return False
    object = object.json()
    if len(object) == 0:
        print("There are no repository")
        return False
    for repo in object:
        repoObj = requests.get(repo['commits_url'].split("{")[0])
        repoObj = repoObj.json()
        print("Repo: " + repo['name'] + "      Number Of Commits: " + str(len(repoObj)))
    return True
