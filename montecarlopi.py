#!/usr/bin/python

# Demo using a monte carlo procedure to calculate pi

# Consider a square of side length (d = 2r) 10 containing a circle of radius (r) 5
# The area of the square is 4r^2 while the area of the circle is pi * r^2
# The ratio of the areas (circle/square) = x = (pi * r^2) / 4r^2 = pi / 4
# x is also the probability that a point randomly chosen within the square is inside the circle also
# If we work out x empirically we can multiply it by 4 to calculate pi!

# To calculate x empirically we want to randomly choose points within the square
# If the distance of a point is less than r from the origin, it is within the circle
# By counting how many points fall within the circle (n_in) vs the total number of points
# we can calculate x = n_in / (n_in + n_out)

# Load helpful python modules
import random
import math
import sys
import matplotlib.pyplot as plt
import time

# Check for the required arguments
if len(sys.argv) != 3:
    print('ERROR: you need to specify the number of points and plotting delay (in seconds)')
    print('e.g. python montecarlopi.py 100 0.01')
    # If an argument is missing, exit and raise an error
    sys.exit(1)

# Set the radius of the circle (and size of square)
r = 5.0

# Set the number of points to test
n_points = int(sys.argv[1])

# Set the plotting delay time
plot_sleep = float(sys.argv[2])

# Initialise the counters for inside and outside the circle
n_in = 0
n_out = 0

# Set up the plot
plt.axis([0, n_points, 0, 5])
plt.ion()
plt.show()
plt.xlabel('Point')
plt.ylabel('Calculated pi value')
plt.title('Calculating pi using a Monte-Carlo procedure')

# Add a horizontal line to the plot showing the actual value of pi
plt.axhline(y=math.pi, xmin=0, xmax=n_points, hold=None)

# Loop over each point
while (n_in + n_out) < n_points:
    # Pick a point randomly in the square centred at the origin (0.0,0.0)
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)

    # Calculate the distance of the point from the origin
    distance = math.sqrt(x**2 + y**2)

    # If the distance from the origin is less than the radius, the point is in the circle
    if distance < r:
        #print("Point is within the circle")
        # Add one to the counter for points in the circle
        n_in += 1
    # OTherwise it is outside
    else:
        #print("Point is not within the circle")
        # Add one to the counter for points outside the circle
        n_out += 1

# Calculating pi: x = pi / 4
    
    # We calculate x as the number of points that landed in the circle over the total points picked so far
    x = float(n_in) / (float(n_out) + float(n_in))

    # pi is therefore 4 * x
    pi_calc = 4 * x

    # Print the number of points picked and the current value of pi we have calculated
    print (n_in + n_out), pi_calc

    # Update the plot
    plt.scatter((n_in + n_out), pi_calc)
    plt.plot((n_in + n_out), pi_calc)
    # BUG: this redraws EVERYTHING so slows down very quickly. Should change to line plot, updating y data only
    plt.draw()

    # Wait for plotting
    time.sleep(plot_sleep)
