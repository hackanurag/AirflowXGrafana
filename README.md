commands
docker compose -f "airflow-statsd.yaml" up
docker compose -f "airflow-statsd.yaml" down

Install dbeaver separately to see airflow postgres
Add  statsd.yaml as mapping cnfig so that later on we can easily set up Grafana Dashboard