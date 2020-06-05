# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle():
    """ Base Class """
    pass

class GroundVehicle(Vehicle):
    """ Ground Vehicle class"""
    pass

class FlightVehicle(Vehicle):
    """ Flight Vehicle class """
    pass
class Car(GroundVehicle):
    """ Four wheeled ground vehicles """
    pass

class Motorcycle(GroundVehicle):
    """ Two wheeled ground vehicles """
    pass

class Starship(FlightVehicle):
    """ Space vehicle class """
    pass

class Airplane(FlightVehicle):
    """ Aircraft (propeller/jet) vehicle class """
    pass