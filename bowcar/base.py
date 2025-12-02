from typing import Union
from abc import ABC, abstractmethod

class BowCarBase(ABC):
    """
    모든 BowCar 모드의 기반이 되는 추상 베이스 클래스입니다.
    이 클래스는 직접 객체로 만들지 않으며, LiveBowCar와 GenerateBowCar가 상속받아
    각자의 방식으로 메소드를 구현하는 '설계도' 역할을 합니다.
    """

    # --- LED 제어 메소드 ---
    @abstractmethod
    def red(self, status: str):
        """빨간색 LED를 제어합니다. status: 'on' or 'off'"""
        pass

    @abstractmethod
    def blue(self, status: str):
        """파란색 LED를 제어합니다. status: 'on' or 'off'"""
        pass

    @abstractmethod
    def all_light(self, status: str):
        """모든 LED를 제어합니다. status: 'on' or 'off'"""
        pass

    # --- 부저 제어 메소드 ---
    @abstractmethod
    def buzzer(self, status: str, scale: str = "C0", octave: int = 4, note: int = 4):
        """버저를 제어합니다. status: 'on' or 'off'"""
        pass

    @abstractmethod
    def set_duration(self, time: int = 2000):
        """버저 등의 지속 시간을 설정합니다."""
        pass

    # --- 모터 제어 메소드 ---
    @abstractmethod
    def motor(self, left: int, right: int):
        """모터를 제어합니다. left, right: -255 ~ 255"""
        pass

    # --- 센서 제어 메소드 (New API) ---
    @abstractmethod
    def is_button_pressed(self, button: str = 'u') -> Union[bool, str]:
        """버튼(u, d, l, r)이 눌렸는지 확인합니다."""
        pass

    @abstractmethod
    def check_light(self, threshold: int = 500, condition: str = '>') -> Union[bool, str]:
        """조도 센서 값이 임계값과 조건(>, <)을 만족하는지 확인합니다."""
        pass

    @abstractmethod
    def check_sound(self, threshold: int = 500, condition: str = '>') -> Union[bool, str]:
        """소리 센서 값이 임계값과 조건(>, <)을 만족하는지 확인합니다."""
        pass

    @abstractmethod
    def check_line(self, dir: str = 'l', threshold: int = 500, condition: str = '>') -> Union[bool, str]:
        """IR 센서(l, r) 값이 임계값과 조건(>, <)을 만족하는지 확인합니다."""
        pass

    @abstractmethod
    def check_distance(self, threshold: int = 10, condition: str = '<') -> Union[bool, str]:
        """초음파 센서 거리가 임계값과 조건(>, <)을 만족하는지 확인합니다."""
        pass

    # --- 센서 값 직접 가져오기 메소드 ---
    @abstractmethod
    def get_light(self) -> Union[int, str]:
        """조도 센서의 현재 값을 가져옵니다."""
        pass

    @abstractmethod
    def get_button(self, button: str = 'u') -> Union[int, str]:
        """버튼(u, d, l, r)의 현재 상태 값을 가져옵니다."""
        pass

    @abstractmethod
    def get_sound(self) -> Union[int, str]:
        """소리 센서의 현재 값을 가져옵니다."""
        pass

    @abstractmethod
    def get_line(self, dir: str = 'l') -> Union[int, str]:
        """IR 센서(l, r)의 현재 값을 가져옵니다."""
        pass

    @abstractmethod
    def get_distance(self) -> Union[float, str]:
        """초음파 센서로 측정한 현재 거리를 cm 단위로 가져옵니다."""
        pass

    # --- 시간 제어 메소드 ---
    @abstractmethod
    def delay(self, ms: int):
        """지정된 시간(밀리초)만큼 프로그램을 지연시킵니다."""
        pass