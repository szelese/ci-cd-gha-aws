set -e

# EB app mappa (AL2/AL2023 eset)
cd /var/app/staging 2>/dev/null || cd /var/app/current

# venv aktiválás (wildcard, mert a mappa neve verziófüggő)
if [ -d "/var/app/venv" ]; then
  source /var/app/venv/*/bin/activate
fi

# Django parancsok
python manage.py migrate --noinput
python manage.py collectstatic --noinput
