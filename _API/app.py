from flask import Flask
import os
from git import Repo

app = Flask(__name__)

local_repo_path = os.path.join(os.getcwd(), 'fullstack-interview-test')
base_branch = 'master'

def clone_get_set():
    if os.path.exists(local_repo_path):
        repo = Repo(local_repo_path)
        origin = repo.remotes.origin
        origin.pull(base_branch)
    else:    
        Repo.clone_from("https://github.com/davidgzu/fullstack-interview-test.git", local_repo_path, branch=base_branch)
 
clone_get_set()


if __name__ == '__main__':
    app.run(debug = True)
