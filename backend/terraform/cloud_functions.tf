data "google_secret_manager_secret" "firebase_sa_key" {
  secret_id = "firebase_sa_key"
}

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
    available_memory   = "256M"
    timeout_seconds    = 15

    secret_environment_variables {
      key        = "FIREBASE_SA_KEY"
      project_id = data.google_secret_manager_secret.firebase_sa_key.project
      secret     = data.google_secret_manager_secret.firebase_sa_key.secret_id
      version    = "latest"
    }
  }
}
