#!/bin/bash

INSTANCE_NAME=sample-bazel-$(date '+%s')
DISK_NAME=${INSTANCE_NAME}


gcloud \
beta \
compute \
--project=yasunori-horikoshi-sandbox \
instances \
create \
${INSTANCE_NAME} \
--zone=asia-northeast1-b \
--machine-type=c2-standard-16 \
--subnet=default \
--network-tier=PREMIUM \
--maintenance-policy=MIGRATE \
--service-account=696806942203-compute@developer.gserviceaccount.com \
--scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append \
--image=$1 \
--image-project=yasunori-horikoshi-sandbox \
--boot-disk-size=20GB \
--boot-disk-type=pd-balanced \
--boot-disk-device-name=${DISK_NAME} \
--reservation-affinity=any
