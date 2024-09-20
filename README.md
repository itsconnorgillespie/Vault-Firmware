### Vault Firmware
For the Information Assurance (ITT-380) course at [Grand Canyon University](https://gcu.edu), students were tasked with protecting a snack-sized chocolate bar. The student who most creatively maintains the integrity of this chocolate bar will receive extra points. The catch is that students must present this chocolate bar whenever requested by the professor. Since Grand Canyon University is located in Phoenix, Arizona, where temperatures can surpass 110 degrees Fahrenheit, chocolate melting is a major issue. To combat this issue, I created the Vault. The Vault is a cloud application and embedded system that monitors the environment of an enclosure. (Learn more about the cloud application [here](https://github.com/itsconnorgillespie/Vault-Firmware)) The embedded system sends temperature and humidity data via MQTT to a FastAPI application in the cloud. This data is then stored in a MySQL database and later displayed on graphs on an analytical frontend. If the temperature or humidity surpasses a configurable amount, a notification is sent via SMTP. 

Outside maintaining the integrity of a chocolate bar, I have found the Vault application useful for monitoring a DIY filament drybox I created. This application has helped ensure the humidity of the drybox remains within the set parameters to maintain the integrity of my filament when not in use. Below is a photo of the drybox and the Vault application in action.

### Disclaimer

This application was created in under one week. With this in mind, there is no guarantee that the following application is secure or bug-free. If you encounter a bug in the application, feel free to submit an Issue and I will attempt to fix it as soon as possible. Thanks for understanding.

### RPi Pico W & Micropython

This firmware is designed using Micropython specifically for use with the Raspberry Pi (RPi) Pico W development board. The RPi Pico W can be purchased [here](https://www.microcenter.com/product/650108/raspberry-pi-pico-w) on Microcenter's website. To install Micropython on the RPi Pico W, a detailed guide can be found [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) on Raspberry Pi's website. 


### Sensors

To collect the temperature and humidity of the environment, a DTH22 sensor is used. I purchased the sensors from [here](https://www.amazon.com/HiLetgo-Temperature-Humidity-Electronic-Practice/dp/B0795F19W6/ref=asc_df_B0795F19W6/?tag=hyprod-20&linkCode=df0&hvadid=692875362841&hvpos=&hvnetw=g&hvrand=13977344509611099852&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9029977&hvtargid=pla-2281435180298&mcid=84e36b67ede23d50a31d5fc6eed59ac6&hvocijid=13977344509611099852-B0795F19W6-&hvexpln=73&th=1) on Amazon. It should be noted that although the accuracy is much greater on the DTH22, a DTH11 can also be used, but this will require some edits in the `main.py` file to work properly. The pin I chose to use was GPIO 22, but this pin can be configured differently in the `settings.py` file. 

### License
[Vault-Firmware](https://github.com/connorgillespie/Vault-Firmware) © 2024 by [Connor Gillespie](https://github.com/connorgillespie) is licensed under [CC BY-NC-ND 4.0](http://creativecommons.org/licenses/by-nc-nd/4.0/?ref=chooser-v1)  
![Creative Commons SVG](http://i.creativecommons.org/l/by-nc-nd/3.0/88x31.png)
