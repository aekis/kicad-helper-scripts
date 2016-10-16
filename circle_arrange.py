#!/usr/bin/env python3

import math, argparse

description = """Calculates rotation and x,y position of a number of parts that shall be arranged on a circle
Conventions from KICAD: 0 degree is x=0,y=radius; y axis points downwards 
Output: One line for each part: [angle {0.1*degree}, x {mm}, y {mm}]
"""
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description=description)
parser.add_argument("number", help="number of parts to arrange on the circle", type=int)
parser.add_argument("radius", help="the circle's radius in {mm}", type=float)
parser.add_argument("-a", "--angle_offset", help="offset from starting at 0 degree. interpreted as percent of the angle beetween two parts. {0..1}", type=float)
parser.add_argument("-r", "--rotate", help="angle to rotate the parts by {0,90,180,270}", type=int)
parser.add_argument("-x", "--xoffset", help="circle centerpoint offset in x in {mm}", type=float)
parser.add_argument("-y", "--yoffset", help="circle centerpoint offset in y in {mm}", type=float)
args = parser.parse_args()


angle = 360/args.number
radius = args.radius

angle_offset = 0
if args.angle_offset:
    angle_offset = args.angle_offset*angle

rotate = 0
if args.rotate:
    rotate = args.rotate

x_offset = 0
if args.xoffset:
    x_offset = args.xoffset

y_offset = 0
if args.yoffset:
    y_offset = args.yoffset

coordinates = []

for i in range(args.number):
    x = radius*math.cos((i*angle+angle_offset+90)*math.pi/180) + x_offset
    y = (-1) * ( radius*math.sin((i*angle+angle_offset+90)*math.pi/180) - y_offset )
    coordinates.append([round(10*(i*angle+angle_offset+rotate),3),round(x,3),round(y,3)])

for coordinate in coordinates:
    print(coordinate,"\n")
