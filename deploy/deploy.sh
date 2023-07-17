#!/bin/bash
DIRECTORY=$(cd $(dirname $0) && pwd)

cd ..
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt

cd deploy

sudo ln -s $DIRECTORY/business_meal.supervisor.conf /etc/supervisor/conf.d/business_meal.supervisor.conf
sudo supervisorctl reread
# sudo supervisorctl reload
sudo supervisorctl restart business_meal
echo "enter any key to continue."
read
sudo ln -s $DIRECTORY/business_meal.nginx.conf /etc/nginx/sites-available/

sudo ln -s $DIRECTORY/business_meal.nginx.conf /etc/nginx/sites-available/business_meal.nginx.conf
sudo ln -s /etc/nginx/sites-available/business_meal.nginx.conf /etc/nginx/sites-enabled/business_meal.nginx.conf
sudo nginx -t
echo "enter any key to continue with restarting nginx"
read
sudo service nginx restart
