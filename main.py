import dht
import machine
import utime
import utils
import settings
import gc


sensor = dht.DHT22(machine.Pin(settings.DHT22_PIN))  # Change "DTH22" -> "DTH11" if using DTH11 sensor.
led = machine.Pin("LED", machine.Pin.OUT)
wlan = None
gc.enable()

# Blink twice to notify setup was successful.
utils.blink_led(led, blinks=2)

while True:
    if wlan is None or not wlan.isconnected():
        # Reconnect to internet if device looses connection.
        wlan = utils.connect_network()
    else:
        # Read and send DTH22 values to MQTT broker at defined interval.
        sensor.measure()
        humidity = sensor.humidity()
        temperature = sensor.temperature()
        utils.publish_readings(temperature, humidity)
        utils.log(f"Temperature: {temperature} C | Humidity: {humidity} %")
        if settings.LED_BLINK_SUCCESSFUL:
            utils.blink_led(led)
        utime.sleep(settings.DHT22_INTERVAL_SECONDS)

    # Free unnecessary RAM to prevent crashing.
    gc.collect()
