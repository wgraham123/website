terraform {
  required_version = ">= 1.5.7"

  required_providers {
    google = {
      version = "~> 7.14.1"
      source  = "hashicorp/google"
    }
  }

  backend "gcs" {
    bucket = "website_terraform_state"
    prefix = "terraform/state"
  }
}

provider "google" {
  project = var.project_id
  region  = var.location
}
