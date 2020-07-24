### Code by W251-Spring2020 Robot Overlords
import tensorflow as tf
import numpy as np
import paho.mqtt.client as mqtt
import os
import PIL.Image as Image
import time

# Load the model
model = tf.keras.models.load_model('model')

# Set model requirements for image size
IMG_HEIGHT = 224
IMG_WIDTH = 224

# Set folder for testing images
test_drive="test_route"

# MQTT Client details
# Broker
host = "broker" 
# Port
port = 1883
# Message topic
topic = "signs"


client = mqtt.Client()
client.connect("broker")
#client.on_message = on_message

# Define function to specify when the program is connected to host
def on_message(client,userdata, msg):
  try:
    print("message received!")
    # Throw Exception if there is an error
  except:
    print("Unexpected error:", sys.exc_info()[0])

def run_inference(file):
    """ Opens the img file, runs it through the classifier and returns a class number (int)."""
    sign = Image.open(test_drive+"/"+file).resize((IMG_WIDTH,IMG_HEIGHT))
    sign.show() # Display the image being tested for audience.
    sign  = np.array(sign)/255.0
    result = model.predict(sign[np.newaxis, ...])
    predicted_class = np.argmax(result[0], axis=-1)
    return predicted_class

# Loop for running MQTT. 
# Open folder of images for testing
for img in os.listdir(test_drive):
    # Run prediction on image
    prediction = run_inference(img)
    # Print the filename and predictoni
    print("sign: ",img,",pred: ", int(prediction))
    # Publish the prediction onto the MQTT topic. Note it will arrive as type byte
    client.publish(topic,int(prediction))
    # Delay the loop to minimize lost packets on MQTT.
    time.sleep(0.5)
    

