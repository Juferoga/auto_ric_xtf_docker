#!/bin/sh
# Verifica que el servicio de postgres este activo 
# para poder realizar el proceo en java

set -e

host="$1"
shift
cmd="$@"

sleep 10

# until pg_isready -h "$host" -p "5432" -U "postgres"; do
#   >&2 echo "Postgres is unavailable - sleeping"
#   sleep 1
# done

# >&2 echo "Postgres is up - executing command"
exec $cmd

