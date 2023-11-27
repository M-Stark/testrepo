import RPi.GPIO as GPIO
import time

# Установка номеров GPIO пинов
STEP_PIN = 20
DIR_PIN = 21

# Настройка режима нумерации GPIO пинов
GPIO.setmode(GPIO.BCM)

# Настройка пинов как выходные
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(DIR_PIN, GPIO.OUT)

try:
    # Установка начального направления (например, 1 - вперед, 0 - назад)
    GPIO.output(DIR_PIN, 1)

    # Выполнение нескольких шагов
    for _ in range(200):  # Измените количество шагов по вашему усмотрению
        GPIO.output(STEP_PIN, 1)
        time.sleep(0.005)  # Измените задержку в зависимости от требований вашего мотора
        GPIO.output(STEP_PIN, 0)
        time.sleep(0.005)  # Измените задержку в зависимости от требований вашего мотора

    # Можно изменить направление и выполнить еще несколько шагов
    # GPIO.output(DIR_PIN, 0)
    # for _ in range(200):
    #     GPIO.output(STEP_PIN, 1)
    #     time.sleep(0.005)
    #     GPIO.output(STEP_PIN, 0)
    #     time.sleep(0.005)

finally:
    # Очистка настроек GPIO перед выходом
    GPIO.cleanup()
