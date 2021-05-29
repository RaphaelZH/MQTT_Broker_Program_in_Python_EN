import os
import paho.mqtt.client as mqtt
import time
import firebase_admin
from firebase_admin import db

my_key = os.path.expanduser(
    "~/Firebase_Keys/abstract-web-302801-firebase-adminsdk-dpn42-63843286c0.json")

cred_obj = firebase_admin.credentials.Certificate(my_key)
default_app = firebase_admin.initialize_app(cred_obj, {
    'databaseURL': 'https://abstract-web-302801-default-rtdb.europe-west1.firebasedatabase.app/'
})

# The callback for when the client receives a CONNACK response from the server.


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("haozhang@hotmail.fr/IoT")
    print("I subscribed.")

# The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    current_time = int(time.time())
    chain = str(msg.payload.decode("utf-8", "strict"))
    print(chain)
    dict = {}
    id = chain.split("|")[0]
    for i in range(1, len(chain.split("|"))):
        key = "mesure_" + str(i)
        dict[key] = chain.split("|")[i]
    ref = db.reference("Mesures/" + str(current_time))
    ref.update({
        "id_": id,
        "mesures": dict
    })


client = mqtt.Client("RaphaelZH")
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set("haozhang@hotmail.fr", "123456")
client.connect("maqiatto.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
