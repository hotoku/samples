terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "3.5.0"
    }
  }
}

provider "google" {
  credentials = file("/Users/hotoku/.config/gcloud/legacy_credentials/yasunori.horikoshi@jdsc.ai/adc.json")

  project = "yasunori-horikoshi-sandbox"
  region  = "asia-northeast1"
  zone    = "asia-northeast1-b"
}

resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}
