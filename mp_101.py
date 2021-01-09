import machine
import time
import esp  # micropython utils for an esp board

# test that the board is connected and works by making an LED blink
pin = machine.Pin(2, machine.Pin.OUT)  # my board has an led on pin 2. check docs.

for _ in range(3):
    time.sleep(0.1)
    pin.on()
    time.sleep(0.2)
    pin.off()

# ok i want a board with a built in simple display which can print stuff
print("The light should have blinked a few times!")


# connect to wifi
# check if there is a wifi light on the board
def do_connect(ssid="*****", password="*****", wait=3):
    "connects to the network and returns sta_if"
    import network

    sta_if = network.WLAN(network.STA_IF)

    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, password)

        # while loop to wait until it connects with a timeout
        timeout = time.time() + wait  # wait seconds from now
        while not sta_if.isconnected():
            if time.time() < timeout:
                pass
            else:
                print("Timed out...")
                break

    print("network config:", sta_if.ifconfig())
    return sta_if


wifi = do_connect()  # often fails to connect, why?
