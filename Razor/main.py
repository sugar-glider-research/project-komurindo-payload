import serial_read_fix

serial_read_fix.calculate()
yaw = serial_read_fix.get_yaw()
pitch = serial_read_fix.get_pitch()
roll = serial_read_fix.get_roll()

print yaw
print pitch
print roll

