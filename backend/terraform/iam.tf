resource "google_cloud_run_service_iam_member" "member" {
  location = google_cloudfunctions2_function.hello_world.location
  service  = google_cloudfunctions2_function.hello_world.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
