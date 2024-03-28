import sys
from Adafruit_IO import MQTTClient
import time, random


AIO_FEED_ID = ["button1", "button2"]
AIO_USERNAME = "Dat_iot"
AIO_KEY = "aio_jUql73jkXYrqSlE18qpPmAph5kHt"

def connected(client):
    print("Connect successfully ...")
    for feed in AIO_FEED_ID:
        client.subscribe(feed)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe successfully ...")

def disconnected(client):
    print("Disconnected ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print(format(f"Received: feed id: {feed_id} {payload}"))

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter = 10
while True:
    counter -= 1
    if counter <= 0:
        # Reset counter
        counter = 10
        # Update to server
        print("Publish to server ...")
        temp = random.randint(10,100)
        client.publish(feed_id="sensor1", value=temp)
        light = random.randint(10,1000)
        client.publish(feed_id="sensor2", value=light)
        humid = random.randint(10,100)
        client.publish(feed_id="sensor3", value=humid)

    time.sleep(1)