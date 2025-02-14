import requests
import sys
import json 
from collections import defaultdict

def get_commits(events):
    commit_dict  = defaultdict(int)
    push_events = [event for event in events if event["type"] ==
                       "PushEvent"]
    for event in push_events:
        repo_name = event["repo"]["name"]
        for commit in event["payload"]["commits"]:
            commit_dict[repo_name] += 1

    for repo,count in commit_dict.items():
        print(f"Pushed {count} commits in {repo}")

def get_started(events):
    new_repo_events = [event for event in events if event["type"] ==
        "CreateEvent"]
    for event in new_repo_events:
        repo_name = event ["repo"]["name"]
        print(f"New repository created {repo_name}")

def get_issues(events):
    issue_events = [event for event in events if event["type"] == "IssuesEvent"]
    for event in issue_events:
        repo_name= event["repo"]["name"]
        action = event.get("payload", {}).get("action")
        if action == "opened":  
            print(f"New issue opened in {repo_name}")

def main():
    if(len(sys.argv) >= 2):
        user = sys.argv[1]
        response = requests.get(f"https://api.github.com/users/{user}/events")
        if response.status_code == 200:
            events = response.json()
            get_commits(events)
            get_issues(events)
    else:
        print("Error 1: Please provide a username.")

main()


