import dronekit as dk 


vehicle = dk.connect("127.0.0.1:14550", wait_ready=True,baud=57600)
