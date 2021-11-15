'''
project: Half-Duplex
author: Alfred Espinosa Encarnación
date: 06-05-2021
Description: Software for the FiPy to send an acknowledgement over the LoRaWAN and 4G (CAT-M1) network of KPN.
'''

import pycom # type: ignore the line
# from LIS2HH12 import LIS2HH12 # type: ignore the line
# from pycoproc_1 import Pycoproc # type: ignore the line

import Wifi
import Server
import test

testing = False 
print = Wifi.new_print

if __name__ == '__main__':
    print("test")
    if testing:
        test.main()
    else:
        try:        
            #py = os.fsformat('/flash')

            # fipy = LoRaWAN()
            ship_wifi = Wifi.WiFi()
            # kpn = CATM1()

            # fipy.initLoRa()
            while not ship_wifi.wlan.isconnected():
                ship_wifi.getWLAN()
            # kpn.getLTE()

            pycom.heartbeat(False)
            
            # py = Pycoproc(Pycoproc.PYTRACK)
            # L76 = L76GNSS(pytrack=py)
            # L76.setAlwaysOn()
            #acc = LIS2HH12(py)

            """
                Note: Use GPS only when in outdoor environment. It will get stuck in a loop when used inside to get a fix.
            """
            # L76.get_fix(force=True, debug=False)
            # if L76.fixed():
            #     print('fixed gps')
            #     pycom.rgbled(0x000f00)
            # else:
            #     L76.get_fix(force=True, debug=False)

            # print("coordinates")
            # # returns the coordinates
            # # with debug true you see the messages parsed by the
            # # library until you get a the gps is fixed
            # print(L76.coordinates(debug=False))
            # print(L76.getUTCDateTime(debug=False))
            
            server = Server.Server()

            server.setup_server()

            server.run(ship_wifi)

        except RuntimeError:
            print("exit")