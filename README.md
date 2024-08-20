# terraform-aws-example-lambda-service
An example repository to demonstrate building / testing / publishing a terraform module with lambda functions.

## Usage

```hcl

module "example" {
  source = "https://github.com/ben-cart3r/terraform-aws-example-lambda-service"
  version = "v0.1.0"

  tags             = local.tags
}
```
<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.0.1 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 5.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | ~> 5.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_create_object"></a> [create\_object](#module\_create\_object) | terraform-aws-modules/lambda/aws | 7.7.1 |
| <a name="module_get_object"></a> [get\_object](#module\_get\_object) | terraform-aws-modules/lambda/aws | 7.7.1 |

## Resources

| Name | Type |
|------|------|
| [aws_iam_policy_document.create_object](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |
| [aws_iam_policy_document.get_object](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/iam_policy_document) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_create"></a> [create](#input\_create) | Controls whether resources should be created. | `bool` | `true` | no |
| <a name="input_create_package"></a> [create\_package](#input\_create\_package) | Controls whether Lambda package should be created. Can be used with var.create=false to ensure the function package builds during CI. | `bool` | `true` | no |
| <a name="input_name_prefix"></a> [name\_prefix](#input\_name\_prefix) | Prefix to apply to all resource names. | `string` | `""` | no |
| <a name="input_tags"></a> [tags](#input\_tags) | A map of tags to assign to resources. | `map(string)` | `{}` | no |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_create_object_function"></a> [create\_object\_function](#output\_create\_object\_function) | Attributes associated with the create object lambda function. |
| <a name="output_get_object_function"></a> [get\_object\_function](#output\_get\_object\_function) | Attributes associated with the get object lambda function. |
<!-- END_TF_DOCS -->