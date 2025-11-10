#!/usr/bin/env bash
set -euo pipefail

#EB app folder/ EB app mappa (AL2023/AL2)
cd /var/app/staging 2>/dev/null || cd /var/app/current || exit 0

if [ -d "/var/app/venv" ]; then
  # shellcheck disable=SC1090
  source /var/app/venv/*/bin/activate
fi

python manage.py migrate --noinput || echo "[WARN] migrate failed (demo)"
python manage.py collectstatic --noinput || echo "[WARN] collectstatic failed"

exit 0
