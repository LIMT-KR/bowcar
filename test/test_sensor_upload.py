from bowcar.upload import UploadBowCar

def test_sensor_upload():
    print("Initializing UploadBowCar for Sensor Test...")
    car = UploadBowCar()
    
    # 1. Button Test Logic
    # If 'Up' button is pressed, turn on Red LED.
    with car.bif(car.is_button_pressed('u')):
        car.red('on')
    with car.belse():
        car.red('off')

    # 2. Light Sensor Test Logic
    # If light value > 500, turn on Blue LED.
    with car.bif(car.check_light(500, '>')):
        car.blue('on')
    with car.belse():
        car.blue('off')

    # 3. Distance Sensor Test Logic
    # If distance < 10cm, turn on Buzzer (briefly)
    with car.bif(car.check_distance(10, '<')):
        car.buzzer('on', 'C0', 4, 4)
        car.delay(100)
        car.buzzer('off')
    
    car.delay(100) # Loop delay

    print("Generating and Uploading Code...")
    car.upload_code()

if __name__ == "__main__":
    test_sensor_upload()
