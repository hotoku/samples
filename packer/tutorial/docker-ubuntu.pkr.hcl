packer {
  required_plugins {
    docker = {
      version = ">= 0.8.7"
      source  = "github.com/hashicorp/docker"
    }
  }
}

variable "docker_image"{
  type = string
  default = "ubuntu:xenial"  
}

source "docker" "ubuntu" {
  image  = var.docker_image
  commit = true
}

source "docker" "ubuntu-bionic" {
  image = "ubuntu:bionic"
  commit = true
}

build {
  sources = [
    "source.docker.ubuntu",
    "source.docker.ubuntu-bionic"
  ]
  provisioner "shell" {
    environment_vars = [
      "FOO=hello world!"
    ]
    inline = [
      "echo Adding file to Docker container",
      "echo \"FOO is $FOO\" > example.txt"
    ]
  }
  provisioner "shell" {
    inline = [ 
     "echo Running ${var.docker_image}"
    ]    
  }
}
