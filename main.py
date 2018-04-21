import razor
import gpsCode
import time

while True:
#   try:
# Get Data Razor
	#razor.calculate()
	#yaw = razor.get_yaw()
	#pitch = razor.get_pitch()
	#roll = razor.get_roll()

# Get Data GPS
	gpsCode.catch_value()
	longitude = gpsCode.get_lon()
	latitude = gpsCode.get_lat()
	altitude = gpsCode.get_alt()

# Print Data Razor
	#print yaw
	#print pitch
	#print roll

# Print Data GPS
	#print longitude
	#print latitude
	#print altitude
	
	#time.sleep(2)
#   except OSError:
#	pass
#   except ValueError:
#	pass
#   except NameError:
#	pass
#   finally:
#	print "oopss"
#   else:
#	print "door"
#   except SerialException:
#	pass
