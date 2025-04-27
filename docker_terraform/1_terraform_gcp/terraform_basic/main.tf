terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "6.32.0"
    }
  }
}

provider "google" {
  project = "terraform-basics-458014"
  region  = "europe-west1"
} 

resource "google_storage_bucket" "demo-bucket" {
  name          = "terraform-basics-458014-terra-bucket"
  location      = "EU"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}