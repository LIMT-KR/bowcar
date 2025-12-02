BOWCAR Module for Python
========================

infomation
-----------

바우카를 이용하여 파이썬을 배우기 위한 모듈입니다.
this module for study python with bowcar hardware.

arduino-cli 의 설치가 필수입니다.
this module need 'arduino-cli'.

[Arduino-cli 설치](https://arduino.github.io/arduino-cli/1.2/installation/)
이곳에서 설치하시길 바랍니다.
if you want to install 'arduino-cli' click that url.

설치법
------
powershell 등에서 pip을 이용해 설치할 수 있습니다.
```
pip install bowcar
```


명령어
------

0. 시간 지연 관련
    - BowCar.delay(time) : time(ms)만큼 지연

1. led 관련
    - BowCar.red(status) : 빨간 led 제어 (status: 'on' or 'off')
    - BowCar.blue(status) : 파란 led 제어 (status: 'on' or 'off')
3. 버튼 및 센서 관련
    - BowCar.get_button(button) : 버튼 button('u','d','l','r')의 값을 return
    - BowCar.is_button_pressed(button) : 버튼 button('u','d','l','r')이 눌렸는지 확인 (True/False)
    - BowCar.get_light() : 조도 센서 값 읽어오기
    - BowCar.check_light(threshold, condition) : 조도 센서 값이 조건(condition: '>', '<')과 임계값(threshold)을 만족하는지 확인

2. 모터 관련
    - BowCar.motor(left, right) : 왼쪽, 오른쪽 모터 속도 및 방향 제어 (범위: -255 ~ 255)
      - 양수: 전진, 음수: 후진, 0: 정지

4. 사운드 센서 관련
    - BowCar.get_sound() : 사운드 센서 값 읽어오기
    - BowCar.check_sound(threshold, condition) : 사운드 센서 값이 조건(condition: '>', '<')과 임계값(threshold)을 만족하는지 확인

5. 라인 트레이서 관련
    - BowCar.get_line(dir) : dir('l','r') 방향의 라인트레이서 값 읽어오기
    - BowCar.check_line(dir, threshold, condition) : 라인트레이서 값이 조건(condition: '>', '<')과 임계값(threshold)을 만족하는지 확인

6. 초음파 센서 관련
    - BowCar.get_distance() : 초음파 센서로 거리 값 구하기
    - BowCar.check_distance(threshold, condition) : 거리 값이 조건(condition: '>', '<')과 임계값(threshold)을 만족하는지 확인

9. 반복문 관련
    - bfor("변수 초기화; 조건; 변화") : 들여쓰기를 기준으로 for문 작성
    - bwhile("조건") : 들여쓰기를 기준으로 조건을 만족하는 동안 계속 작동하는 while문 생성
    - bbreak() : 반복문에 브레이크 집어넣기

10. 조건문 관련
    - bif("조건") : 조건문 들여쓰기로 작성
    - belif("조건") : 조건문 들여쓰기로 작성
    - belse() : 조건문 들여쓰기로 작성

11. 변수 관련
    - set_value(종류, 이름, 값) : 변수가 없다면 새로 선언하고 저장합니다. 하지만 이미 변수가 있다면 바로 설정합니다.
