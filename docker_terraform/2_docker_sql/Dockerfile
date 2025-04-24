
FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    libpq-dev \
    cmake \
    g++ \
    && pip install --upgrade pip

RUN pip install pandas sqlalchemy psycopg2 pyarrow

WORKDIR /app

COPY data-loading.py data-loading.py

ENTRYPOINT [ "python", "data-loading.py" ]


# docker run -it \
#  -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
#  -e PGADMIN_DEFAULT_PASSWORD="root" \
#  -p 8080:80 \
#  --network=pg-network \
# dpage/pgadmin4

# docker network create pg-network


# docker run -it \
# -e POSTGRES_USER="root" \
# -e POSTGRES_PASSWORD="root" \
# -e POSTGRES_DB="ny_taxi" \
# -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
# -p 5432:5432 \
# --network=pg-network \
# --name pg-database \
# postgres:13

# URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"
# python data-loading.py \
# --user=root \
# --password=root \
# --host=localhost \
# --port=5432 \
# --database=ny_taxi \
# --tb=ny_taxi_data \
# --url=${URL}
# the name helps pg admin to discover postgres

# docker build -t taxi_ingest:v001 .


# URL="https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"

# docker run -it \
#  --network=pg-network \
# taxi_ingest:v001  \
# --user=root \
# --password=root \
# --host=pg-database \
# --port=5432 \
# --database=ny_taxi \
# --tb=ny_taxi_data \
# --url=${URL}