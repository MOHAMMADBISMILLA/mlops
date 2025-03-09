import mlflow
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/mohammedbismilla76/mlops.mlflow")


dagshub.init(repo_owner='mohammedbismilla76', repo_name='mlops', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)