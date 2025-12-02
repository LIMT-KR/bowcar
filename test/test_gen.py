import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bowcar.upload import UploadBowCar

def test_generation():
    car = UploadBowCar()
    
    # Test LED
    car.red('on')
    car.delay(1000)
    car.red('off')
    
    car.blue('on')
    car.delay(1000)
    car.blue('off')
    
    car.all_light('on')
    car.delay(1000)
    car.all_light('off')
    
    # Test Buzzer
    car.buzzer('on', 'C0', 4, 4)
    car.delay(500)
    car.buzzer('off')
    
    print(car.get_full_code())

if __name__ == "__main__":
    test_generation()
