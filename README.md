Commands: <br>
docker compose -f "airflow-statsd.yaml" up <br>
docker compose -f "airflow-statsd.yaml" down

Selective service build:
docker compose  -f "AirflowXGrafana\airflow-statsd-docker-compose.yaml" up -d --build postgres airflow-init airflow-scheduler airflow-webserver
docker compose  -f "AirflowXGrafana\airflow-statsd-docker-compose.yaml" up -d --build postgres-load prometheus statsd-exporter grafana 

.env file is only required while executing airflow-basic-docker-compose.yaml to get rid of the warning "AIRFLOW_UID not set!"

Install dbeaver separately and fill in the necessary details for the airflow postgres connection to see postgres-airflow <br>
Add statsd.yaml as mapping config so that later on we can easily set up Grafana Dashboard

DAGS branch added to add new DAGs only.


Adding node exporter for system metrices

Will be adding nginix for port forewarding so that airflow can be accessed via a single port