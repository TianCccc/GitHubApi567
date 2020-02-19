"""
Date: 02/18/2020
Author:Tiancheng Xu
Homework 04a

Requirements:
Input: Github user ID
Output: Repositories name and commits
"""
import requests
import json

# read user ID from input
def get_user_ID():
    ID = input("Please input your user_ID: ")
    return ID

# get the user's repo
def get_user_repo(ID):
    api = "https://api.github.com/users/" + ID + "/repos"
    user = requests.get(api)
    repos = json.loads(user.text)
    repo_lst = []
    for repository in repos:
        try:
            repo_lst.append(repository.get("name"))
        except:
            repos = []
    return repo_lst

# get the repo's commits
def get_user_commit(ID, repo):
    api = "https://api.github.com/repos/"+ID+"/"+repo+"/commits"
    repodata = requests.get(api)
    commits = json.loads(repodata.text)
    return len(commits)

if __name__ == "__main__":
    username = get_user_ID()
    reponame = get_user_repo(username)
    # print("User: " +username)
    for repository in reponame:
        num = get_user_commit(username, repository)
        print("Repo: "+ repository + " Number of commits: "+ str(num))