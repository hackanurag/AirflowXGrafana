commands
docker compose -f "airflow-statsd.yaml" up <br>
docker compose -f "airflow-statsd.yaml" down

.env file is only required while executing airflow-basic-docker-compose.yaml to get rid of the warning "AIRFLOW_UID not set!"

Install dbeaver separately to see airflow postgres
Add  statsd.yaml as mapping cnfig so that later on we can easily set up Grafana Dashboard

.env file is only required while executing airflow-basic-docker-compose.yaml to get rid of the warning "AIRFLOW_UID not set!"