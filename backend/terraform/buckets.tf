resource "google_storage_bucket" "function_source_code_bucket" {
  name     = "test_bucket_fh285"
  location = "europe-west2"
  project  = var.project_id

  public_access_prevention = "enforced"
}

resource "google_storage_bucket_object" "hello_world_source_code" {
  name   = "hello_world.zip"
  bucket = google_storage_bucket.function_source_code_bucket.name
  source = "../cloud_functions/hello_world.zip"
}

