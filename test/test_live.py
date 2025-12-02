import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bowcar.live import LiveBowCar
import time

def test_live():
    print("Initializing LiveBowCar...")
    try:
        car = LiveBowCar()
    except Exception as e:
        print(f"Failed to initialize LiveBowCar: {e}")
        return

    if not car.port:
        print("Arduino not found. Exiting test.")
        return

    print("Uploading Firmware...")
    try:
        car._upload_firmware()
    except Exception as e:
        print(f"Firmware upload failed: {e}")
        return
    
    print("Testing LEDs...")
    print("RED ON")
    car.red('on')
    time.sleep(1)
    print("RED OFF")
    car.red('off')
    time.sleep(0.5)

    print("BLUE ON")
    car.blue('on')
    time.sleep(1)
    print("BLUE OFF")
    car.blue('off')
    time.sleep(0.5)

    print("ALL LIGHT ON")
    car.all_light('on')
    time.sleep(1)
    print("ALL LIGHT OFF")
    car.all_light('off')
    time.sleep(0.5)

    print("Testing Buzzer...")
    print("Buzzer C4")
    car.buzzer('on', 'C0', 4, 4) # C4, quarter note
    # Note: live.buzzer with 'on' already includes a sleep if duration/note > 0
    
    print("Buzzer OFF")
    car.buzzer('off')

    print("Test Complete.")
    car.close()

if __name__ == "__main__":
    test_live()
