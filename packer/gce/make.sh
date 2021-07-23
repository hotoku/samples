#!/bin/bash

gcloud \
beta \
compute \
--project=yasunori-horikoshi-sandbox \
instances \
create \
sample-007 \
--zone=asia-northeast1-b \
--machine-type=e2-medium \
--subnet=default \
--network-tier=PREMIUM \
--maintenance-policy=MIGRATE \
--service-account=696806942203-compute@developer.gserviceaccount.com \
--scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append \
--image=packer-1627007541 \
--image-project=yasunori-horikoshi-sandbox \
--boot-disk-size=20GB \
--boot-disk-type=pd-balanced \
--boot-disk-device-name=sample-003 \
--reservation-affinity=any
