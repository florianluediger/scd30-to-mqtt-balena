import time
from scd30_i2c import SCD30
from datetime import datetime
import paho.mqtt.publish as publish
import os

# configuration
measurement_interval = 60
upload_interval = 300

# set up SCD30 sensor
scd30 = SCD30()

scd30.set_measurement_interval(measurement_interval)
scd30.start_periodic_measurement()

time.sleep(2)

mqtt_server = os.environ.get('MQTT_SERVER')

while 1:
    if scd30.get_data_ready():
        m = scd30.read_measurement()
        if m is not None:
            publish.single('scd30/raspberry',
                           '{' + '"time":"{}","co2":{},"temperature":{},"humidity":{}'.format(datetime.now(),
                                                                                                    m[0], m[1],
                                                                                                    m[2]) + '}',
                           hostname=mqtt_server,
                           port=8883,
                           tls={'ca_certs': "data/AmazonRootCA1.pem", 'certfile': "data/certificate.pem.crt",
                                'keyfile': "data/private.pem.key"})
        time.sleep(upload_interval)
    else:
        time.sleep(1)
