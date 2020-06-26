resource "aws_cloudwatch_event_target" "cloudwatch_event_target" {
  rule = aws_cloudwatch_event_rule.cloudwatch_event_rule.name
  arn  = aws_lambda_function.lambda_function.arn
}
