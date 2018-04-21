import gps

longitude = 0
lattitude = 0
altitude = 0

# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

def catch_value():
        global lon
        global lat
        global alt
        
        try:
		report = session.next()
	#print report
		
	# Wait for a 'TPV' report and display the current time
	# To see all report data, uncomment the line below
	# print report
		if report['class'] == 'TPV':
	  		if hasattr(report, 'alt'):
	   			print report.alt
	   			altitude = report.alt
			if hasattr(report, 'lon'):
				print report.lon
				longitude = report.lon
			if hasattr(report, 'lat'):
				print repost.lat
				lattitude = report.lat
       	except KeyError:
		pass
       	except KeyboardInterrupt:
		quit()
       	except StopIteration:
		session = None
		print "GPSD has terminated"

def get_lon():
        global longitude
        return longitude

def get_lat():
        global lattitude
        return lattitude

def get_alt():
        global altitude
        return altitude
