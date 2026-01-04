resource "google_storage_bucket" "function_source_code_bucket" {
  name     = "function_source_code_bucket_${random_string.random_suffix.lower}"
  location = "europe-west2"
  project  = var.project_id

  public_access_prevention = "enforced"
}

data "archive_file" "hello_world_zip" {
  type        = "zip"
  output_path = "../cloud_functions/hello_world.zip"
  source_dir  = "../cloud_functions/hello_world"
}

resource "google_storage_bucket_object" "hello_world_source_code" {
  name   = "hello_world.zip"
  bucket = google_storage_bucket.function_source_code_bucket.name
  source = data.archive_file.hello_world_zip.output_path
}

