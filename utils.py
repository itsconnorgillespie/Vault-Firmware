import machine
import ujson
import settings
import umqtt
import utime
import network


def log(message: str, error: bool = False):
    timestamp = utime.localtime()
    level = "ERROR" if error else "INFO"
    print(f"{timestamp[0]}-{timestamp[1]:02d}-{timestamp[2]:02d} {timestamp[3]:02d}:{timestamp[4]:02d}:{timestamp[5]:02d} {level} {message}")


def connect_network(attempts: int = 10) -> network.WLAN | None:
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(settings.NETWORK_SSID, settings.NETWORK_PASSWORD)

    attempt = 0
    while attempt < attempts and not wlan.isconnected():
        attempt += 1
        log(f"Attempt #{attempt} Connecting | SSID: {settings.NETWORK_SSID} | Password: {settings.NETWORK_PASSWORD}")
        utime.sleep(1)

    if wlan.isconnected():
        log(f"Network Connected | {settings.NETWORK_SSID}")
        return wlan
    return None


def connect_mqtt() -> umqtt.MQTTClient:
    client = umqtt.MQTTClient(settings.DEVICE_UUID, settings.MQTT_HOST, settings.MQTT_PORT, settings.MQTT_USERNAME, settings.MQTT_PASSWORD)
    client.connect()
    log(f"Broker Connected | {settings.MQTT_HOST}:{settings.MQTT_PORT}")
    return client


def publish_readings(temperature: float,
                     humidity: float):
    client = connect_mqtt()
    data = ujson.dumps({
        "temperature": temperature,
        "humidity": humidity,
    })
    client.publish(f"devices/{settings.DEVICE_UUID}/readings", data)
    log(f"Readings Published | devices/{settings.DEVICE_UUID}/readings")
    client.disconnect()


def blink_led(led: machine.Pin, blinks: int = 1):
    for blink in range(blinks):
        led.value(True)
        utime.sleep_ms(250)
        led.value(False)
        utime.sleep_ms(250)
