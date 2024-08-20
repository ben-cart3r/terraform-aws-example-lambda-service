resource "aws_s3_bucket" "this" {
  bucket = "${var.name_prefix}-object-store"

  tags = var.tags
}