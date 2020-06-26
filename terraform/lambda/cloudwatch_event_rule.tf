resource "aws_cloudwatch_event_rule" "cloudwatch_event_rule" {
  name        = local.name
  description = "Cloudwatch event lambda trigger"
  is_enabled  = true

  depends_on = [
    aws_lambda_function.lambda_function
  ]

  schedule_expression = "cron(0 7 * * ? *)"
}
