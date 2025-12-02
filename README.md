# BowCar Module for Python

[한국어](#korean) | [English](#english)

---

<a name="korean"></a>
## 🇰🇷 한국어 (Korean)

**BowCar**는 파이썬을 이용해 아두이노 기반의 바우카 하드웨어를 제어하고 학습하기 위한 모듈입니다.

### 설치 방법

이 모듈을 사용하기 위해서는 **[Arduino CLI](https://arduino.github.io/arduino-cli/latest/installation/)** 설치가 필수입니다.

```bash
pip install bowcar
```

### 명령어 목록

#### 0. 시간 제어
| 함수 | 설명 |
|---|---|
| `BowCar.delay(time)` | `time`(ms)만큼 프로그램을 지연시킵니다. |

#### 1. LED 및 네오픽셀 제어
| 함수 | 설명 |
|---|---|
| `BowCar.red(status)` | 빨간색 LED를 제어합니다. (`status`: 'on'/'off') |
| `BowCar.blue(status)` | 파란색 LED를 제어합니다. (`status`: 'on'/'off') |
| `BowCar.all_light(status)` | 모든 LED를 제어합니다. (`status`: 'on'/'off') |
| `BowCar.neopixel(index, r, g, b)` | 특정 인덱스(0~3)의 네오픽셀 색상을 설정합니다. (0~255) |
| `BowCar.neopixel_all(r, g, b)` | 모든 네오픽셀의 색상을 설정합니다. |
| `BowCar.neopixel_clear()` | 모든 네오픽셀을 끕니다. |
| `BowCar.neopixel_brightness(val)` | 네오픽셀의 밝기를 조절합니다. (0~255) |

#### 2. 모터 제어
| 함수 | 설명 |
|---|---|
| `BowCar.motor(left, right)` | 왼쪽/오른쪽 모터 속도 및 방향을 제어합니다. (-255 ~ 255)<br>양수: 전진, 음수: 후진, 0: 정지 |

#### 3. 센서 값 읽기
| 함수 | 설명 |
|---|---|
| `BowCar.get_button(button)` | 버튼 상태를 확인합니다. (`button`: 'u', 'd', 'l', 'r') |
| `BowCar.is_button_pressed(btn)` | 버튼이 눌렸는지 확인합니다. (True/False) |
| `BowCar.get_light()` | 조도 센서 값을 읽어옵니다. (0~1023) |
| `BowCar.get_sound()` | 소리 센서 값을 읽어옵니다. (0~1023) |
| `BowCar.get_line(dir)` | 라인 센서 값을 읽어옵니다. (`dir`: 'l', 'r') |
| `BowCar.get_distance()` | 초음파 센서 거리 값을 읽어옵니다. (cm) |

#### 4. 센서 조건 확인
모든 조건 함수는 `threshold`(임계값)와 `condition`(조건: '>', '<')을 인자로 받습니다.

| 함수 | 설명 |
|---|---|
| `BowCar.check_light(th, cond)` | 조도 센서 조건 확인 |
| `BowCar.check_sound(th, cond)` | 소리 센서 조건 확인 |
| `BowCar.check_line(dir, th, cond)` | 라인 센서 조건 확인 |
| `BowCar.check_distance(th, cond)` | 거리 센서 조건 확인 |

#### 5. 코드 생성 제어문 (Upload 모드 전용)
| 함수 | 설명 |
|---|---|
| `bfor("초기화; 조건; 변화")` | C++ 스타일의 for문을 생성합니다. |
| `bwhile("조건")` | while문을 생성합니다. |
| `bif("조건")`, `belif`, `belse` | if-else 조건문을 생성합니다. |
| `bbreak()` | 반복문을 탈출합니다. |
| `set_value(type, name, val)` | 변수를 선언하거나 값을 설정합니다. |

---

<a name="english"></a>
## 🇺🇸 English

**BowCar** is a Python module for controlling and learning with the Arduino-based BowCar hardware.

### Installation

**[Arduino CLI](https://arduino.github.io/arduino-cli/latest/installation/)** is required to use this module.

```bash
pip install bowcar
```

### Command List

#### 0. Time Control
| Function | Description |
|---|---|
| `BowCar.delay(time)` | Delays the program for `time` milliseconds. |

#### 1. LED & NeoPixel Control
| Function | Description |
|---|---|
| `BowCar.red(status)` | Controls Red LED. (`status`: 'on'/'off') |
| `BowCar.blue(status)` | Controls Blue LED. (`status`: 'on'/'off') |
| `BowCar.all_light(status)` | Controls all LEDs. (`status`: 'on'/'off') |
| `BowCar.neopixel(idx, r, g, b)` | Sets color of specific NeoPixel (idx: 0~3). (0~255) |
| `BowCar.neopixel_all(r, g, b)` | Sets color of all NeoPixels. |
| `BowCar.neopixel_clear()` | Turns off all NeoPixels. |
| `BowCar.neopixel_brightness(val)` | Sets brightness of NeoPixels. (0~255) |

#### 2. Motor Control
| Function | Description |
|---|---|
| `BowCar.motor(left, right)` | Controls motor speed and direction. (-255 ~ 255)<br>Positive: Forward, Negative: Backward, 0: Stop |

#### 3. Read Sensors
| Function | Description |
|---|---|
| `BowCar.get_button(button)` | Gets button status. (`button`: 'u', 'd', 'l', 'r') |
| `BowCar.is_button_pressed(btn)` | Checks if button is pressed. (True/False) |
| `BowCar.get_light()` | Reads light sensor value. (0~1023) |
| `BowCar.get_sound()` | Reads sound sensor value. (0~1023) |
| `BowCar.get_line(dir)` | Reads line sensor value. (`dir`: 'l', 'r') |
| `BowCar.get_distance()` | Reads ultrasonic sensor distance. (cm) |

#### 4. Check Sensor Conditions
All check functions take `threshold` and `condition` ('>', '<') as arguments.

| Function | Description |
|---|---|
| `BowCar.check_light(th, cond)` | Checks light sensor condition. |
| `BowCar.check_sound(th, cond)` | Checks sound sensor condition. |
| `BowCar.check_line(dir, th, cond)` | Checks line sensor condition. |
| `BowCar.check_distance(th, cond)` | Checks distance sensor condition. |

#### 5. Code Generation Control (Upload Mode Only)
| Function | Description |
|---|---|
| `bfor("init; cond; step")` | Generates C++ style for loop. |
| `bwhile("condition")` | Generates while loop. |
| `bif("cond")`, `belif`, `belse` | Generates if-else statements. |
| `bbreak()` | Generates break statement. |
| `set_value(type, name, val)` | Declares variable or sets value. |
