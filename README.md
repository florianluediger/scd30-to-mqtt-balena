# Smart Office SCD30 Raspberry Pi

This repository contains the configuration of the balena container that runs SCD30 sensors in the Smart Office.

To run this container in Balena, do the following:

On your Balena host set `MQTT_SERVER` to the mqtt server URL e.g. `something.iot.eu-central-1.amazonaws.com`

On your Balena host create certificate files:

- `echo "<certificate content>" > /var/lib/docker/volumes/1_scd30-data/_data/AmazonRootCA1.pem`
- `echo "<certificate content>" > /var/lib/docker/volumes/1_scd30-data/_data/private.pem.key`
- `echo "<certificate content>" > /var/lib/docker/volumes/1_scd30-data/_data/certificate.pem.crt`