# HomeAutomation

### Android Implementation :
1. Rename Wifi Name and Password to that of your wifi

1. Set values for Static IP, Gateway(Your routers IP), dns, port (remember values of IP and port since you will have to provide it in app)

1. Flash NodeMCU_Android.ino on your NodeMCU (set Baud rate to 9600 if you are using the older version)

1. Connect NodeMCU's GPIO 5,4,0,2 pins to relay switch (in that order) and enjoy.

1. Link to android app project : https://github.com/AnmolMajithia/HomeAutomationAndroid

### Web Server Implementation :
1.Rename Wifi Name and Password to that of your home wifi

2.Flash nodemcu_server.ino on your NodeMCU and just plug up GPIO 5,4,0 and 2 to the input pins of your relay switch, Vin to Relay's Vcc and Gnd to Gnd

3.Give power to NodeMCU and check its I.P. Address on the serial monitor and just enter that into the search bar of any browser on any device connected to that WiFi
You'll be shown 4 buttons for the 4 switches of your relay switch which can be controlled



Python Script is just to test sockets in python and Kivy animations, not as practical as the HTML or Android approach.
