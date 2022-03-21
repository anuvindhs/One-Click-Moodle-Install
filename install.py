import os
import subprocess
import sys
import urllib.request

# check if git installed if not install git 
def check_git():
    if os.system("git --version") != 0:
        print("Git not found. Installing git...")
        subprocess.call(["sudo", "apt-get", "install", "git"])
        print("Git installed.")


# Download a git repository
def download_repo(repo_url, repo_name):
    if os.path.isdir(repo_name):
        print("Repository already exists. Skipping download.")
        return
    print("Downloading repository...")
    subprocess.call(["git", "clone", repo_url, repo_name])
    print("Repository downloaded.")



check_git()

download_repo("https://github.com/moodle/moodle.git","moodle")
    