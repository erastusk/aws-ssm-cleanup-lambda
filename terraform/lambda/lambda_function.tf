resource "aws_lambda_function" "lambda_function" {
  function_name = local.name
  role          = "arn:aws:iam::191141428331:role/lambda_role"
  filename      = "../function/lambda.zip"
  handler       = var.handler
  runtime       = var.runtime
  memory_size   = var.memory_size
  timeout       = var.timeout
  publish       = true
  tracing_config {
    mode = "Active"
  }
  description = "This lambda function retrieves ssm pipeline parameters for deletion"
  tags        = local.tags
}
