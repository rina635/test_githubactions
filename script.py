import requests
import json
import os

SECRET_KEY = os.environ['SECRET_KEY']
REPO_ID = os.environ['REPO_ID']
CLUSTER_ID = os.environ['CLUSTER_ID']
instance_id = 'fcn-fiscalnote-workspace.cloud.databricks.com'

api_version = '/api/2.0'
#Repo ID for production/FN-Tetris-Deploy where code will be pushed to.
api_command = f'/repos/{REPO_ID}'
url = f'https://{instance_id}{api_version}{api_command}'

#Cluster_ID used is dependent upon branch code is pushed to (See deploy.yml)
params = {
  'cluster_id': CLUSTER_ID,
  'branch':'main'
}

response = requests.patch(
  url = url,
  json= params,
  headers = {"Authorization": "Bearer {}".format(SECRET_KEY)}
)

print(response.status_code)
print(json.dumps(json.loads(response.text), indent = 2))
