#trivy:ignore:AVD-AWS-0090
module "bucket" {
  source = "terraform-aws-modules/s3-bucket/aws"

  create_bucket = var.create

  bucket = "${var.name_prefix}-object-store"

  server_side_encryption_configuration = {
    rule = {
      apply_server_side_encryption_by_default = {
        sse_algorithm = "aws:kms"
      }
    }
  }

  tags = var.tags
}