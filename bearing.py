import math

# Coordinates
N1 = 5659269.84	
E1 = -9903.857 
N2 = 5659465.68	
E2 = -9903.478

# Differences
delta_N = N2 - N1
delta_E = E2 - E1

# Compute Bearing (radians)
theta_radians = math.atan2(delta_E, delta_N)

# To degrees
theta_degrees = math.degrees(theta_radians)

# Ensure withing 0 < angle < 360
bearing = (theta_degrees + 360) % 360
# To DMS
d = math.floor(bearing)
m = math.floor((bearing - d)*60)
s = round((bearing - d - m/60) *3600,2)

# Show
print('angle is', d, "-", m, "-", s)
print('angle is', bearing)