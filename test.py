#!/usr/bin/env python
# -*- coding: utf-8 -*-

import model

m = model.Model()

m.m1.speed = 10
m.m2.speed = 10

print("Default model: {}".format(m))

print("### Setting a speed to motor 1 only")
m.m1.speed = 0.1
linear_speed, rotational_speed = m.dk()
print("linear_speed = {}\notational_speed = {}".format(linear_speed, rotational_speed))

print("### Setting a speed to motor 2 only")
m.m2.speed = 0.1
linear_speed, rotational_speed = m.dk()
print("linear_speed = {}\notational_speed = {}".format(linear_speed, rotational_speed))

print("### Setting a speed to both motors")
m.m1.speed = 0.1
m.m2.speed = 0.1
linear_speed, rotational_speed = m.dk()
print("linear_speed = {}\notational_speed = {}".format(linear_speed, rotational_speed))