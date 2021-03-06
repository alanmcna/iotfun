# iotfun
Long term goal of mine is to be able to spin up raspberry pis (zeros ideally) to do remote 'sensing' within wifi range. My first sensor was a IR camera my second is a UV sensor so now I'm seeing the need for consistency in set-up, reporting and centralised view.

This MVP is just getting a single sensor recording to a DB, generation of a JSON (MVP API/static feed) and visualisation. Looking to build on this in a more generic fashion going forward.

## Set-up 

### Base

- Install postgres, supervisord, nginx, python ... (see todo :)
- Create DB from schema 

### Sensor and auto-start

In this example I'm using an Adafruit MCP3008 analog to digital converter with a dfrobot ML8511 to measure UV Index

- Install the dependencies, for this demo this is the Adafruit MCP3008 python library (built and installed)
- Test run the sensor_uvindex.py or similar (inserting sensor data into DB) 
- Copy the supervisor file into /etc/supervisor/conf.d

#### Links
- https://github.com/adafruit/Adafruit_Python_MCP3008
- https://www.dfrobot.com/wiki/index.php/UV_Sensor_v1.0-ML8511_SKU:SEN0175

### Web / API

- Build JSON from the data being recorded in the DB makeC3JSON.py
-- Currently I'm running this from cron and writing stdout to the web folder
- Install the dependencies to get the chart.html working
    - Get C3 and D3 (last v3 version to work with C3)
```
cd www
wget https://github.com/c3js/c3/archive/v0.4.14.zip
unzip v0.4.14.zip
ln -s c3-0.4.14 c3
rm v0.4.14.zip

wget https://github.com/d3/d3/releases/download/v3.5.17/d3.zip
unzip d3.zip
```

## Todo 

- Move sensor scripts into a (.d) folder for sequential execution
- Ansible (pi) build
