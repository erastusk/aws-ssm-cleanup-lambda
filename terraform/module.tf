module "lambda_params" {
  source         = "./lambda"
  runtime        = "python3.7"
  handler        = "lambda.lambda_handler"
  timeout        = 15
  memory_size    = 128
  sgs            = ["sg-04d531dc807886504"]
  resource_owner = "github@erastusk"
  name_suffix    = "ssm_lambda_cleaner"
}
