resource "google_cloudfunctions_function" "function" {
  name        = "hello_world_${random_string.random_suffix.result}"
  description = "Test function"
  runtime     = "python39"

  available_memory_mb   = 128
  source_archive_bucket = google_storage_bucket.function_source_code_bucket.name
  source_archive_object = google_storage_bucket_object.hello_world_source_code.name
  trigger_http          = true
  entry_point           = "main"
}

# IAM entry for all users to invoke the function
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.function.project
  region         = google_cloudfunctions_function.function.region
  cloud_function = google_cloudfunctions_function.function.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}
