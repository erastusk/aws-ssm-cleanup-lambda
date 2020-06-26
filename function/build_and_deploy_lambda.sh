#!/bin/bash
# shellcheck disable=SC2035

set -ex
lambda_zip="lambda.zip"

# Add lambda python files to zip file
zip -r9 "${lambda_zip}"  lambda.py
zip -g "${lambda_zip}" delete_parameters.py

# Naviage to terraform directory and apply 
cd ../terraform
terraform init
terraform destroy -auto-approve
terraform apply -auto-approve
