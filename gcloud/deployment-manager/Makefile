# cf: https://cloud.google.com/deployment-manager/docs/quickstart

deploy: vm.yaml
	gcloud deployment-manager deployments create quickstart-deployment --config vm.yaml

stop:
	gcloud compute instances stop quickstart-deployment-vm
