DATABASE_NAME := primary_app_db
ZIP_FILE := Dump20220506.zip
SQL_DIR := $(subst .zip,,$(ZIP_FILE))
USER_NAME := loganalysis
$(eval ROOT_PASSWORD := $(shell read -s -p 'password for root? ' password && echo $${password}))


.PHONY: user
user: restore
	$(eval PASSWORD := $(shell read -s -p 'password for $(USER_NAME)? ' password && echo $${password}))
	@echo "create user if not exists $(USER_NAME)@localhost identified by '$(PASSWORD)'" | mysql -u root -p"$(ROOT_PASSWORD)"
	@echo "grant select, create, insert, drop on $(DATABASE_NAME).* to $(USER_NAME)@localhost" | mysql -u root -p"$(ROOT_PASSWORD)"


.PHONY: restore
restore: $(ZIP_FILE) database
	unzip -o $<
	@cat $(SQL_DIR)/*.sql | mysql -u root -p"$(ROOT_PASSWORD)" $(DATABASE_NAME)


.PHONY: database
database:
	@echo "create database if not exists $(DATABASE_NAME)" | mysql -u root -p"$(ROOT_PASSWORD)"


$(ZIP_FILE):
	@echo "Download $@ from https://drive.google.com/drive/folders/1MRyzxPnyF_D-ff3_WsxVN9TBHZEpRBpJ"
	@false


.PHONY: clean
clean:
	@echo "drop database if exists $(DATABASE_NAME)" | mysql -u root -p"$(ROOT_PASSWORD)"
	@echo "drop user if exists $(USER_NAME)" | mysql -u root -p"$(ROOT_PASSWORD)"
	rm -rf $(SQL_DIR) $(ZIP_FILE)
