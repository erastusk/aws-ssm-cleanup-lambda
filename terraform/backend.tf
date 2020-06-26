terraform {
  backend "s3" {
    encrypt = "true"
    bucket  = "scripts-terraform-backend"
    region  = "us-east-1"
    key     = "terraform/lambda/lambda.tfstate"
  }
}
