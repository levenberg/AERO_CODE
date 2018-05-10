#!/usr/bin/python
from dronekit import connect, VehicleMode, LocationGlobalRelative
import time

vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
print "Arming motors:"
vehicle.mode    = VehicleMode("GUIDED")
print "Global Location (relative altitude): %s" % vehicle.location.global_relative_frame

