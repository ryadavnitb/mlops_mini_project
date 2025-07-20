# to check setup with dagsub


import dagshub
dagshub.init(repo_owner='ryadavnitb', repo_name='mlops_mini_project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)