terraform {
  backend "s3" {
    encrypt = "true"
    bucket  = " "           # Your bucket
    region  = "us-east-1"
    key     = "terraform.tfstate"   # Your bucket key
  }
}
