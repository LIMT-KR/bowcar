import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from bowcar.live import LiveBowCar
import time

def run_experiment():
    print("Initializing LiveBowCar...")
    car = LiveBowCar()
    
    print("\n[Step 1] Uploading Firmware...")
    # Explicitly calling the protected method as requested by the user for this experiment
    car._upload_firmware()
    
    print("\n[Step 2] Starting Motor Experiment...")
    
    print("1. Forward (Speed 100)")
    car.motor(100, 100)
    time.sleep(2)
    
    print("2. Stop")
    car.motor(0, 0)
    time.sleep(1)
    
    print("3. Backward (Speed 100)")
    car.motor(-100, -100)
    time.sleep(2)
    
    print("4. Stop")
    car.motor(0, 0)
    time.sleep(1)
    
    print("5. Turn Left (Rotate)")
    car.motor(-100, 100)
    time.sleep(2)
    
    print("6. Stop")
    car.motor(0, 0)
    time.sleep(1)
    
    print("7. Turn Right (Rotate)")
    car.motor(100, -100)
    time.sleep(2)
    
    print("8. Stop")
    car.motor(0, 0)
    
    car.close()
    print("\nExperiment Complete.")

if __name__ == "__main__":
    run_experiment()
