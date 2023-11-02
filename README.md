# track and trace
## Tracking API by DRF

<p>
This API used to track shipments via tracking_number
or carrier.

Gives the shipments data along with weather data for sender location and
receiver location

- Utilized **Django Rest Framework** to serve HTTP API
- Utilized **Celery** for retrieving weather data periodically
</p>

<h2>Usage</h2>

clone the repo

<pre>
git clone https://github.com/cybera3s/track-and-trace.git
</pre>

change directory to project root
<pre>
cd track-and-trace
</pre>

Create a .env file in django root folder
<pre>
touch track_and_trace/.env
</pre>

Fill the .env file like the provided env sample 

<pre>
DEBUG=on or off
SECRET_KEY=some super secret key

# general
SITE_NAME=website name

# OpenWeather
OPEN_WEATHER_API_KEY=API KEY from openweather website

# Celery
CELERY_BROKER_URL=broker url for celery
</pre>

then Build and run using docker

<pre>
docker compose up --build
</pre>

head over to http://localhost:8000/swagger/ for api docs

# Test
Run tests
<pre>
docker compose exec api bash -c "pytest -sv ."
</pre>