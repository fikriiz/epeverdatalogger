import csv
from turtle import delay
from epevermodbus.driver import EpeverChargeController
from datetime import datetime
import time

controller = EpeverChargeController("COM14", 1)
n = 0
try:
    with open('datalog.csv','a') as f:
        while n<3:
            now = datetime.now()
            nowTime = '{0:%Y/%m/%d %H:%M:%S}'.format(now)
            solar_voltage = str(controller.get_solar_voltage())
            solar_current = str(controller.get_solar_current())
            solar_power= str(controller.get_solar_power())
            load_voltage = str(controller.get_load_voltage())
            load_current = str(controller.get_load_current())
            load_power = str(controller.get_load_power())
            battery_voltage=str(controller.get_battery_voltage())
            battery_current_l = str(controller.get_battery_current_l())
            battery_current_h = str(controller.get_battery_current_h())
            battery_state_of_charge = str(controller.get_battery_state_of_charge())
            battery_temperature = str(controller.get_battery_temperature())
            remote_battery_temperature = str(controller.get_remote_battery_temperature())
            controller_temperature = str(controller.get_controller_temperature())
            max_battery_voltage_today = str(controller.get_maximum_battery_voltage_today())
            min_battery_voltage_today = str(controller.get_minimum_battery_voltage_today())

            data1 = solar_voltage
            data2 = solar_current
            data3 = solar_power
            data4 = load_voltage
            data5 = load_current
            data6 = load_power
            data7 = battery_voltage
            data8 = battery_current_l
            data9 = battery_current_h
            data10 = battery_state_of_charge
            data11 = battery_temperature
            data12 = remote_battery_temperature
            data13 = controller_temperature
            data14 = max_battery_voltage_today
            data15 = min_battery_voltage_today

            writeStr = nowTime + ',' + data1 + ',' + data2 + ',' +data3 + ',' + data4 + ',' +data5 + ',' + data6 + ',' +data7 + ',' + data8 + ','+data9 + ',' + data10 + ',' +data11 + ',' + data12 + ',' + data13 + ',' +data14 + ',' + data15
            writeStr = writeStr.split(',')

            #Confirmation of the written character string
            #Example:'2020/03/06 15:00:00','data1','data2','data3'
            print('writeStr = %s' % writeStr)

            writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(writeStr)

            n += 1
            time.sleep(3)
            

except FileNotFoundError as e:
    print(e)
except csv.Error as e:
    print(e)
