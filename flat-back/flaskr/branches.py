from flask import (Blueprint, jsonify, request)
from git import Repo
from datetime import date
import git 
import json


bp = Blueprint('branches', __name__, url_prefix='/branches')
repo = Repo('flaskr/fullstack-interview-test/')

@bp.route('/', methods=['GET'])
def branch():
  data = []
  for branch in repo.branches:
    data.append(branch.__str__())
  response = jsonify(data)
  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
  return response

@bp.route('/commits/<branch>', methods=['GET'])
def commits(branch):
  data = []
  selected_branch = repo.branches[branch].checkout()
  for commit in repo.iter_commits():
    print(commit.author)
    data.append({
      "commit": commit.__str__(),
      "author": str(commit.author),
      "date": str(commit.committed_datetime),
      "message": commit.message
    })
    print(data)
  response = jsonify(data)
  response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
  return response

@bp.route('/merge/<branches>', methods=['POST'])
def merge(branches):
  if request.method == 'POST':
    branches = json.loads(branches)

    branch_to_merge = repo.branches[branches['branch_to_merge']]
    branch_merge_into = repo.branches[branches['branch_merge_into']]
    base = repo.merge_base(branch_to_merge, branch_merge_into)
    repo.index.merge_tree(branch_merge_into, base=base)
    repo.index.commit('merged in flat test {}'.format(date.today()), parent_commits=(branch_merge_into.commit, branch_to_merge.commit))

    data = {'status': 'ok'}
    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
    return response