variable "project_id" {
  type    = string
  default = "potent-thought-483207-v4"
}

resource "random_string" "random_suffix" {
  length  = 6
  special = false
}
