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

NOTE : `Make sure you have appropriate AWS cicd credentials in your environment`.


## STANDALONE EXECUTION

If you wanted to run this function locally without deploying to AWS:

```
cd function
python3 lambda.py

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
