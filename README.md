# crimes-on-map

Hosted url: http://theta-anchor-215617.appspot.com/map/chicago
`
To deploy the app:

cd crimes-app/web/
FLASK_APP=main.py FLASK_DEBUG=1 python -m flask run

Google Cloud App Engine:

cd crimes-app/web/
gcloud app deploy
