#!/bin/bash
psql -d sensordb -c "REFRESH MATERIALIZED VIEW celsius_daily_average;"
psql -d sensordb -c "REFRESH MATERIALIZED VIEW celsius_weekly_average;"
psql -d sensordb -c "REFRESH MATERIALIZED VIEW celsius_monthly_average;"
psql -d sensordb -c "REFRESH MATERIALIZED VIEW humidity_daily_average;"
psql -d sensordb -c "REFRESH MATERIALIZED VIEW humidity_monthly_average;"
