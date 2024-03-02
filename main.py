import sys
from Adafruit_IO import MQTTClient
import time
import random
from simpleAI import *
from uart import *

AIO_FEED_ID = ["button1", "button2"]
AIO_USERNAME = "dinhvan2211"
AIO_KEY = "aio_lkYI86BXAXcAJFNNMmOHOFqNQCQ6"


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


client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 10
counter_AI = 5
sensorcounter = 0
ai_result = ""
previous_result = ""
while True:
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 10
    #     print("Publish du lieu ...")
    #     if sensorcounter == 0:
    #         sensorcounter = 1
    #         print("Publish du lieu nhiet do...")
    #         temp = random.randint(20, 40)
    #         client.publish("cambien1", temp)
    #     elif sensorcounter == 1:
    #         sensorcounter = 2
    #         print("Publish du lieu do am...")
    #         humidity = random.randint(50, 100)
    #         client.publish("cambien2", humidity)
    #     elif sensorcounter == 2:
    #         sensorcounter = 0
    #         print("Publish du lieu do sang...")
    #         light = random.randint(0, 100)
    #         client.publish("cambien3", light)
    counter_AI = counter_AI - 1
    if counter_AI <= 0:
        counter_AI = 5
        ai_result = image_detector()
        print("AI_Ouput: ", ai_result)
        if previous_result != ai_result:
            client.publish("AI", ai_result)
    readSerial(client)
    time.sleep(1)
