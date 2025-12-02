from bowcar.live import LiveBowCar
import time

def test_sensor():
    print("Initializing LiveBowCar...")
    car = LiveBowCar()
    
    print("\n--- Sensor Test ---")
    
    # 1. Button Test
    print("\n1. Button Test (Press 'Up' button)")
    for _ in range(5):
        pressed = car.is_button_pressed('u')
        val = car.get_button('u')
        print(f"Up Button Pressed: {pressed}, Value: {val}")
        time.sleep(0.5)

    # 2. Light Sensor Test
    print("\n2. Light Sensor Test")
    for _ in range(5):
        val = car.get_light()
        check_high = car.check_light(300, '>')
        check_low = car.check_light(800, '<')
        print(f"Light Value: {val}, >300: {check_high}, <800: {check_low}")
        time.sleep(0.5)

    # 3. Sound Sensor Test
    print("\n3. Sound Sensor Test")
    for _ in range(5):
        val = car.get_sound()
        check = car.check_sound(500, '>')
        print(f"Sound Value: {val}, >500: {check}")
        time.sleep(0.5)

    # 4. Line Sensor Test
    print("\n4. Line Sensor Test")
    for _ in range(5):
        l_val = car.get_line('l')
        r_val = car.get_line('r')
        l_check = car.check_line('l', 500, '>')
        print(f"Line L: {l_val} (>{l_check}), R: {r_val}")
        time.sleep(0.5)

    # 5. Distance Sensor Test
    print("\n5. Distance Sensor Test")
    for _ in range(5):
        dist = car.get_distance()
        check = car.check_distance(20, '<')
        print(f"Distance: {dist} cm, <20cm: {check}")
        time.sleep(0.5)

    car.close()
    print("\nTest Complete.")

if __name__ == "__main__":
    test_sensor()
