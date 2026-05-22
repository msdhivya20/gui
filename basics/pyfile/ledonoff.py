from machine import Pin
import sys
import uselect

led = Pin(15, Pin.OUT)

poll_obj = uselect.poll()
poll_obj.register(sys.stdin, 1)

while True:

    if poll_obj.poll(1):

        command = sys.stdin.readline().strip()

        if command == "ON":
            led.value(1)

        elif command == "OFF":
            led.value(0)

""" Save this file into Pico and select the correct port, then run the program.
Check the port number and include that port number in the `views.py` page.
After that, disconnect Thonny or any serial monitor connected to Pico.

Now run the Django server again in the Anaconda Prompt:

python manage.py runserver


Finally, open the LED web page and use the ON/OFF buttons to control the LED.
""" 

"""import network
import socket
from machine import Pin
from time import sleep

ssid = 'YOUR_WIFI_NAME'
password = 'YOUR_WIFI_PASSWORD'

led = Pin(15, Pin.OUT)

# Connect WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(ssid, password)

while not wifi.isconnected():
    pass

print("Connected")
print(wifi.ifconfig())

# Create server
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

server = socket.socket()
server.bind(addr)
server.listen(1)

print("Server running")

while True:

    client, addr = server.accept()

    request = client.recv(1024)
    request = str(request)

    if '/on' in request:
        led.value(1)

    if '/off' in request:
        led.value(0)

    response = """
    HTTP/1.1 200 OK

    LED CONTROL
    """

    client.send(response)
    client.close()"""

    """import requests
from django.shortcuts import render

PICO_IP = "192.168.1.5"

def led_control(request):

    status = "OFF"

    if request.method == "POST":

        led = request.POST.get("led")

        if led == "on":
            requests.get(f"http://{PICO_IP}/on")
            status = "ON"

        elif led == "off":
            requests.get(f"http://{PICO_IP}/off")
            status = "OFF"

    return render(request, "led.html", {"status": status})"""


    """Save this code into Raspberry Pi Pico W and connect the Pico W to WiFi.
Run the program using Thonny IDE and note the IP address displayed in the shell.

Find Pico W IP Address

After running code, Thonny shows:

('192.168.1.5', '255.255.255.0', ...)

Your Pico W IP:

192.168.1.5

Include the Pico W IP address in the `views.py` page of your Django project.

Django:Install requests:pip install requests

After that, run the Django server in Anaconda Prompt:

python manage.py runserver

Now open the LED control web page and use the ON/OFF buttons to control 
the LED wirelessly through Pico W."""
