Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> vertical_velocity = 9.09
>>> horizontal_velocity = 0.3
>>> a = vertical_velocity
>>> b = horizontal_velocity
>>> print(a)
9.09
>>> a = float(a)
>>> b = float(b)
>>> import math
>>> total_velocity = math.sqrt(a * a + b * b)
>>> print(total_velocity)
9.09494914774129
>>> distance_initial
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    distance_initial
NameError: name 'distance_initial' is not defined
>>> distance_initial = 30
>>> time = 3
>>> distance_now = distance_initial + total_velocity * time
>>> print(distance_now)
57.28484744322387
>>> distance_now = distance_initial + vertical_velocity * time
>>> print(distance_now)
57.269999999999996
>>> vertical_velocity = -9.09
>>> distance_now = distance_initial + vertical_velocity * time
>>> 
SyntaxError: multiple statements found while compiling a single statement
>>> distance_now = distance_initial + vertical_velocity * time
>>> print(distance_now)
2.7300000000000004
>>> acceleration_gravity = -1.625
>>> distance_now = distance_initial + vertical velocity * time + 0.5 * acceleration_gravity * time ** 2
SyntaxError: invalid syntax
>>> distance_now = distance_initial + vertical_velocity * time + 0.5 * acceleration_gravity * time ** 2
>>> print(distance_now)
-4.5825
>>> weight = 15103
>>> thrust = 45000
>>> acceleration_thruster = thrust / weight
>>> print(acceleration_thruster)
2.97954048864464
>>> print(acceleration_gravity)
-1.625
>>> print(acceleration_gravity + acceleration_thruster)
1.35454048864464
>>> distance_initial = 0
>>> distance_now = distance_initial + 0.5 * (acceleration_gravity + acceleration_thruster) * time ** 2
>>> print(distance_now)
6.0954321989008795
>>> distance_initial = 30
>>> distance_final = 0
>>> acceleration = acceleration_thrust + acceleraction_gravity
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    acceleration = acceleration_thrust + acceleraction_gravity
NameError: name 'acceleration_thrust' is not defined
>>> acceleration = acceleration_thrust + acceleration_gravity
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    acceleration = acceleration_thrust + acceleration_gravity
NameError: name 'acceleration_thrust' is not defined
>>> acceleration = acceleration_thruster + acceleration_gravity
>>> time = (-velocity_vertical + math.sqrt(vertical_velocity ** 2 - 4 * (0.5 * acceleration) * distance_initial)) / (2 * acceleration)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    time = (-velocity_vertical + math.sqrt(vertical_velocity ** 2 - 4 * (0.5 * acceleration) * distance_initial)) / (2 * acceleration)
NameError: name 'velocity_vertical' is not defined
>>> time = (-vertical_velocity + math.sqrt(vertical_velocity ** 2 - 4 * (0.5 * acceleration) * distance_initial)) / (2 * acceleration)
>>> print(time)
3.7851702497275626
>>> time = (-vertical_velocity - math.sqrt(vertical_velocity ** 2 - 4 * (0.5 * acceleration) * distance_initial)) / (2 * acceleration)
>>> print(time)
2.925592607642245
>>> velocity_vertical = vertical_velocity
>>> print(vertical_velocity ** 2 - 4 * (0.5 * acceleration) * distance_initial)
1.3556706813216124
>>> print(time)
2.925592607642245
>>> time = (-vertical_velocity + math.sqrt(vertical_velocity ** 2 - 4 * (0.5 * acceleration) * distance_initial)) / (2 * acceleration)
>>> print(time)
3.7851702497275626
>>> time = (-vertical_velocity - math.sqrt(vertical_velocity ** 2 - 4 * (0.5 * acceleration) * distance_initial)) / (2 * (0.5 * acceleration))
>>> print(time)
5.85118521528449
>>> time = (-vertical_velocity + math.sqrt(vertical_velocity ** 2 - 4 * (0.5 * acceleration) * distance_initial)) / (2 * (0.5 * acceleration))
>>> print(time)
7.570340499455125
>>> answer_v1 = (-vertical_velocity - math.sqrt(vertical_velocity ** 2 - 4 * (0.5 * acceleration) * distance_initial)) / (2 * (0.5 * acceleration))
>>> answer_v2 = (-vertical_velocity + math.sqrt(vertical_velocity ** 2 - 4 * (0.5 * acceleration) * distance_initial)) / (2 * (0.5 * acceleration))
>>> print(f"Negative one: {answer_v1}\nPositive one: {answer_v2}")
Negative one: 5.85118521528449
Positive one: 7.570340499455125
>>> impact_velocity = vertical_velocity + acceleration * 5.85118521528449
>>> print(impact_velocity)
-1.1643327193382538
>>> impact_velocity = vertical_velocity + acceleration * 7.570340499455125
>>> print(impact_velocity)
1.1643327193382529
>>> 