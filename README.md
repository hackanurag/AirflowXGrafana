Commands: <br>
docker compose -f "airflow-statsd.yaml" up <br>
docker compose -f "airflow-statsd.yaml" down

.env file is only required while executing airflow-basic-docker-compose.yaml to get rid of the warning "AIRFLOW_UID not set!"

Install dbeaver separately and fill in the necessary details for the airflow postgres connection to see postgres-airflow <br>
Add statsd.yaml as mapping config so that later on we can easily set up Grafana Dashboard

DAGS branch added to add new DAGs only.