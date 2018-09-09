'''
This module initializes the tunnel for sharing data between the SunSpec Client and the MQTT client. It also starts both the clients.
'''
import sunspec_client_critical as sunspec_client
import mqtt_client_critical as mqtt_client
import mqtt_sunspec_tunnel as tunnel
from datetime import datetime, date

client_timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
tunnel.init()
mqtt_client.publish_thread_start()
sunspec_client.run(timestamp=client_timestamp, server_port=8899, server_address='10.76.56.2', protocol='TCP', slave_id=1)

