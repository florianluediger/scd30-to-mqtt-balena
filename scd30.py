import time
from scd30_i2c import SCD30
import psycopg2
from datetime import datetime

# configuration
measurement_interval = 60
database_upload_interval = 300

# set up database connection
db = psycopg2.connect(
    host="ip",
    database="sensordata",
    user="postgres",
    password="secret"
)

db_cursor = db.cursor()

# set up SCD30 sensor
scd30 = SCD30()

scd30.set_measurement_interval(measurement_interval)
scd30.start_periodic_measurement()

time.sleep(2)

while 1:
    if scd30.get_data_ready():
        m = scd30.read_measurement()
        if m is not None:
            db_cursor.execute(f"insert into co2sensor (timestamp, co2, temperatur, humidity) values ('{datetime.now()}', {m[0]:.2f}, {m[1]:.2f}, {m[2]:.2f});")
            db.commit()
        time.sleep(database_upload_interval)
    else:
        time.sleep(1)

scd30.stop_periodic_measurement()
