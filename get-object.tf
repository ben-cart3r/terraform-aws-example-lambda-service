module "get_object" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "7.7.1"

  create_function = var.create
  create_package  = var.create_package
  create_role     = var.create

  function_name = "${var.name_prefix}-get-object"
  description   = "Simple lambda that creates an S3 object"
  handler       = "src/lambda_handler.handle_event"
  runtime       = "python3.11"
  timeout       = 30

  attach_policy_json = var.create
  policy_json        = var.create ? data.aws_iam_policy_document.hello_world[0].json : null

  source_path = [
    {
      path           = "${path.module}/functions/get-object"
      patterns       = ["!tests/.*"]
      poetry_install = true
    }
  ]

  tags = merge(
    var.tags,
    {
      Name = "${var.name_prefix}-get-object"
    }
  )
}

data "aws_iam_policy_document" "get_object" {
  count = var.create ? 1 : 0

  statement {
    effect = "Allow"

    actions = [
      "s3:GetObject"
    ]

    resources = [
      "*"
    ]
  }
}
