resource "google_cloudfunctions_function" "hello_world" {
  name        = "hello-world"
  description = "Test function"
  runtime     = "python314"

  available_memory_mb   = 128
  source_archive_bucket = google_storage_bucket.function_source_code_bucket.name
  source_archive_object = google_storage_bucket_object.hello_world_source_code.name
  trigger_http          = true
  entry_point           = "hello_world"
}
