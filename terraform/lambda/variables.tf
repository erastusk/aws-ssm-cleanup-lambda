variable "memory_size" {
  description = "mem size"
  type        = string
}
variable "timeout" {
  description = "timeout"
  type        = string
}
variable "handler" {
  description = "handler"
  type        = string
}
variable "runtime" {
  description = "runtime"
  type        = string
}
variable "sgs" {
  type = list(string)
}

variable "resource_owner" {
  description = "The email of the owner of the project."
  type        = string
}

variable "name_suffix" {
  type    = string
  default = "parameter-store-cleanup-lambda"
}
locals {
  name = lower(var.name_suffix)
  tags = {
    "tr:application-name" = local.name
    "tr:resource-owner"   = var.resource_owner
  }
}

