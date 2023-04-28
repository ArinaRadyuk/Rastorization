# Rastorization
## Step by step algorithm
Gradually increasing the x coordinate, calculating the y=kx+b coordinate and then rounding the result to an integer.
## Digital differential analyzer 
A linear DDA starts by calculating the smaller of dy or dx for a unit increment of the other. A line is then sampled at unit intervals in one coordinate and corresponding integer values nearest the line path are determined for the other coordinate.

Considering a line with positive slope, if the slope is less than or equal to 1, we sample at unit x intervals (dx=1) and compute successive y values as

    y_(k + 1) = y_k + m
    x_(k + 1) = x_k + 1
    
Subscript k takes integer values starting from 0, for the 1st point and increases by 1 until endpoint is reached. y value is rounded off to nearest integer to correspond to a screen pixel.

For lines with slope greater than 1, we reverse the role of x and y i.e. we sample at dy=1 and calculate consecutive x values as

    x_(k + 1) = x_k + 1 / m
    y_(k + 1) = y_k + 1

Similar calculations are carried out to determine pixel positions along a line with negative slope. Thus, if the absolute value of the slope is less than 1, we set dx = 1 if x_start < x_end i.e. the starting extreme point is at the left. 
## Bresenham's line algorithm
The basic idea behind Bresenham's line algorithm is to incrementally calculate the pixel positions that lie on the line between the two endpoints. Starting at the first endpoint, the algorithm determines whether the next pixel to be drawn should be to the right, to the upper-right, or to the upper-left of the current pixel. This decision is based on the error between the actual line position and the ideal line position, which is a straight line between the two endpoints. The error is calculated by comparing the difference between the actual and ideal line positions in both the x and y directions.

Once the next pixel position is determined, the algorithm updates the error in both directions and draws the pixel. The algorithm continues to incrementally calculate and draw the next pixel positions until it reaches the second endpoint.
## Bresenham's circle algorithm
The algorithm works by incrementally calculating the pixel positions that lie on the circumference of the circle. It starts by calculating the position of the first point on the circumference, which is at (r, 0), where r is the radius of the circle. It then uses a decision variable to determine the next pixel position to be drawn based on the error between the actual circle position and the ideal circle position.

The decision variable is updated at each step based on the error in both the x and y directions. If the error is negative, the decision variable is incremented in one direction; otherwise, it is incremented in the other direction. The algorithm continues to calculate and draw the next pixel positions until it reaches a point where the y-coordinate is less than or equal to the x-coordinate.
