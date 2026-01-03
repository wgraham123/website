resource "google_storage_bucket" "test_bucket" {
  name     = "test_bucket_fh284"
  location = "europe-west2"
  project  = var.project_id

  public_access_prevention = "enforced"
}
