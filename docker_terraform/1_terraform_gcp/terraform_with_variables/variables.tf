

variable "project" {
    description = "Project"
    default = "terraform-basics-458014"
  
}

variable "region" {
    description = "region"
    default = "europe-west1"
}

variable "location" {
    description = "Project Location"
    default = "EU"
}

variable "bq_dataset_name" {
    description = "BigQuery dataset name"
    default = "demo_dataset"
  
}

variable "gcs_storage_class" {
    description = "Bucket Storage Class"
    default = "STANDARD"  
}

variable "gcs_bucket_name" {
    description = "Storage Bucket Name"
    default = "terraform-basics-458014-terra-bucket"
  
}