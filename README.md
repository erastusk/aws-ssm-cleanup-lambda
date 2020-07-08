# lambda.py

A Python script that deletes AWS Parameter Store parameters.

## PURPOSE
A need for this lambda came about due to "orphaned" parameters used for managing Codepipeline stages accumulating. Not all pipelines have a clean up stage and those
that do, parameter deletes after a pipeline execution aren't reliable. The end result is orphaned parameters.


## METHODS OF DEPLOYMENT
### Teraform

```
cd function
bash build_and_deploy_lambda.sh

```

build_and_deploy_lambda.sh
** zips up your python modules and performs a terraform plan/apply


### Severless

```
npm install -g serverless
serverless create -t aws-python
cd lambda-serverless
serverless deploy
```

### SAM
```
pip3 install aws-sam-cli
sam init --runtime python3.8 --name lambda-sam --dependency-manager pip

Which template source would you like to use?
        1 - AWS Quick Start Templates
        2 - Custom Template Location
Choice: 1

Cloning app templates from https://github.com/awslabs/aws-sam-cli-app-templates.git

AWS quick start application templates:
        1 - Hello World Example
        2 - EventBridge Hello World
        3 - EventBridge App from scratch (100+ Event Schemas)
        4 - Step Functions Sample App (Stock Trader)
        5 - Elastic File System Sample App
Template selection: 1

cd lambda-sam




NOTE : `Make sure you have appropriate AWS cicd credentials in your environment`.


## STANDALONE EXECUTION

If you wanted to run this function locally without deploying to AWS:

```
cd function
python3 lambda.py
sam deploy --guided

  Setting default arguments for 'sam deploy'
  =========================================
  Stack Name [sam-app]: lambda-param-delete-stack
  AWS Region [us-east-1]:
  #Shows you resources changes to be deployed and require a 'Y' to initiate deploy
  Confirm changes before deploy [y/N]: y
  #SAM needs permission to be able to create roles to connect to the resources in your template
  Allow SAM CLI IAM role creation [Y/n]: y
  Save arguments to samconfig.toml [Y/n]: y


Previewing CloudFormation changeset before deployment
======================================================
Deploy this changeset? [y/N]: y

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Outputs
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Key                 LambdaParamDeleteFunction
Description         Lambda Function ARN
Value               arn:aws:lambda:us-east-1:191141428331:function:param-delete-lambda
```

## OPTIONS

lambda.py run options.

### AGE

```
import logging
import delete_parameters as dp
SSM_LIMIT = 10
AGE = 0

```
* Age in days up until which you want Parameters retained, anything older will be deleted.

Example:
AGE = 7   -- All parameters older than 7 days will be deleted.

### PARAM_FILTERS

```
PARAM_FILTERS = ["*"]
``` 
* These are the search parameters being used to query the Parameter store. To add a new search query text,
add the text quoted (string)  and add a comma to the previous last text.

* If `PARAM_FILTERS` variable doesn't exist or empty, the lambda will exit otherwise it will returns an empty dict.

* If `PARAM_FILTERS` variable is set to `*` that's an invalid search value, returns an empty dict.

* If `PARAM_FILTERS` variable is set to `" "` all parameters will be deleted, otherwise none exist.
