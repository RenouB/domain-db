FROM bitnami/postgresql:12
COPY . /domain_repo
# directly make database, set up users, etc
# then populate the database 
CMD bash /domain_repo/initialize_db.sh

