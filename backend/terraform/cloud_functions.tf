resource "google_cloudfunctions2_function" "hello_world" {
  name        = "hello-world"
  location    = var.location
  description = "Test function"

  build_config {
    runtime     = "python314"
    entry_point = "hello_world"
    source {
      storage_source {
        bucket = google_storage_bucket.function_source_code_bucket.name
        object = google_storage_bucket_object.hello_world_source_code.name
      }
    }
  }

  service_config {
    max_instance_count = 1
    available_memory   = "128M"
    timeout_seconds    = 15
  }
}
