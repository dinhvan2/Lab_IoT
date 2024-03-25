import sys
from Adafruit_IO import MQTTClient
import time
import random
from uart import *

AIO_FEED_ID = ["button1", "button2"]
AIO_USERNAME = "dinhvan2211"
AIO_KEY = "aio_qfml48QgPWDIQe1umOtqop4CX1yx"


def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_ID:
        client.subscribe(topic)

def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe thanh cong ...")


def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)


def message(client, feed_id, payload):
    print("Nhan du lieu: " + payload + " tu " + feed_id)
    if(feed_id == "button1"):
        if payload == "0":
            writeData("Tat den \n")
        else:
            writeData("Bat den \n")
    if(feed_id == "button2"):
        if payload == "0":
            writeData("Tat may bom \n")
        else:
            writeData("Bat may bom \n")
        

client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:

    readSerial(client)
    time.sleep(1)
