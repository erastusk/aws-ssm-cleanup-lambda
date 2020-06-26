module "lambda_params" {
  source         = "./lambda"
  runtime        = "python3.7"
  handler        = "lambda.lambda_handler"
  timeout        = 15
  memory_size    = 128
  sgs            = [" "]
  resource_owner = "github@erastusk"
  name_suffix    = "ssm_lambda_cleaner"
}
