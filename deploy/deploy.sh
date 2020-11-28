cd /root/oxigen_api
git pull
docker-compose -f production.yml build
docker-compose -f production.yml restart

