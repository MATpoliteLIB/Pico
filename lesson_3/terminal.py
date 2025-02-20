import serial
import time
import numpy as np
import matplotlib. pyplot as plt

ser = serial.Serial('COM9', 115200, timeout=1)  # Замените на ваш порт (например, 'COM3' для Windows)
time.sleep(2)  # Дождаться подключения
data=[]
t=int(input("Введите время исследования в целых секундах:"))
start_time = time.perf_counter()

with open('adc_values.txt', 'w') as f:
    while True:
        line = ser.readline().decode('utf-8').strip()  # Чтение строки из последовательного порта
        print(line)  # Вывод в терминал
        data.append(float(line))  # Запись в файл
        end_time = time.perf_counter()
        if ((end_time - start_time)>t):
            break

data=np.array(data)
time=np.linspace(0,t,len(data))
plt.plot(time,data)
plt.show()