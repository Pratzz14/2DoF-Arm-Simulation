'''
Inverse Kinematics for 2DoF robotic ARM
Imagining a SCARA ARM moving in 2D

Author: Pratik Mahankal - pratik.mahankal14@gmail.com

If math not mathing: https://robotacademy.net.au/lesson/inverse-kinematics-for-a-2-joint-robot-arm-using-geometry/

-- Inputs:
---- x and y cords in quadrant 1 or 2
---- Length of two arm L1 and L2

-- Two main type outputs:
---- Return possible value true if it is possible considering the length of the arm
---- Returns the two angle (Arm1 angle, Arm2 angle)

'''

import math
import pytest

def inverse_k2dof(x,y,l1,l2):

    # q2 angle
    upper = x**2 + y**2 - l1**2 - l2**2
    lower = 2 * l1 * l2

    try:
        temp = math.acos(upper/lower) # breaks if not possible TT, guess its a feature now
    except:
        return (False,0,0)
    
    q2 = math.degrees(temp)
    
    # q1 angle
    if x == 0:
        a = 1.57079633 # GOD just divide by 0
    else:
        a = math.atan(y/x)
    
    a1 = (l2 * math.sin(math.radians(q2)))
    b1 = l1 + (l2 * math.cos(math.radians(q2)))
    c = math.radians(a1)/math.radians(b1)

    b= math.atan(c)
    q1 = math.degrees(a-b)
    
    return True,int(q1),int(q2)

def test_answer():
    assert inverse_k2dof(275, 900, 800, 500) == (1, 40,90)
    assert inverse_k2dof(-100, 300, 300, 200) == (1, -109, 104)

