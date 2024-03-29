packer {
  required_plugins {
    googlecompute = {
      version = ">= 0.0.1"
      source  = "github.com/hashicorp/googlecompute"
    }
  }
}

variable "image-suffix" {
  type    = string
  default = "no-suffix"
}

source "googlecompute" "basic-example" {
  project_id          = "yasunori-horikoshi-sandbox"
  source_image        = "ubuntu-1804-bionic-v20210720"
  ssh_username        = "packer"
  zone                = "asia-northeast1-b"
  startup_script_file = "startup.sh"
  image_name          = "bazel-sample-${var.image-suffix}"
}

build {
  sources = [
    "sources.googlecompute.basic-example"
  ]

  # provisionは、必ずしも`startup.sh`のあとに実行されるわけではなさそう
  # というか、むしろ、startupの前に実行される模様
  provisioner "shell" {
    inline = [
      "sudo mkdir -p /hotoku",
      "sudo touch /hotoku/provisioned",
      "sudo chmod 777 /hotoku"
    ]
  }

  provisioner "file" {
    source = "./setup.sh"
    destination = "/hotoku/setup.sh"
  }
}
