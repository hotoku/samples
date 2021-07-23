packer {
  required_plugins {
    googlecompute = {
      version = ">= 0.0.1"
      source  = "github.com/hashicorp/googlecompute"
    }
  }
}

source "googlecompute" "basic-example" {
  project_id          = "yasunori-horikoshi-sandbox"
  source_image        = "ubuntu-1804-bionic-v20210720"
  ssh_username        = "packer"
  zone                = "asia-northeast1-b"
  startup_script_file = "startup.sh"
}

build {
  sources = [
    "sources.googlecompute.basic-example"
  ]
}
