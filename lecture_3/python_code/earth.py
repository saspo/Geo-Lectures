import math
from typing import NamedTuple

# Gravitational constant in m^3 kg^-1 s^-2
gravitational_constat = 6.67408E-11
mass = 5.972E24 # kg
radius = 6371E3 # m

def get_grativity():
    '''
    Computes the Earth's  gravitational acceleration.
    return: 
    The Earth's  gravitational acceleration.
    '''
    g = - gravitational_constat*mass / (radius * radius)
    return g

def get_weight(mass):
    '''
    Computes the force due to a given mass.
    @param mass: The mass to compute the weight. Mass should be a number.
    return: The force of gravity over the mass.
	F = mass * g
    '''
    weight = mass * get_grativity()
    return weight

# python class structure 
class OrbitalParameters(NamedTuple):
    '''
    Data structure for the orbital parameters.
    '''
    radius: float
    theta: float
    angular_velocity: float
    radial_velocity: float

    def __repr__(self):
      return "OrbitalParameters({},{},{},{}".format(self.radius,self.theta,
                                                  self.angular_velocity, self.radial_velocity)
    def __str__(self):
      return "R = {}, Theta = {}, Vc = {}, Vr = {}".format(self.radius,self.theta,
                                                  self.angular_velocity, self.radial_velocity)


# Integrate the orbit.
def get_next_state(op: OrbitalParameters, dt):
    r, theta, vc, vr = op
    
    # Solve the moviment equations.
    r_next = r + vr * dt
    theta_next = theta - vc * dt / r
    vr_next = vr + dt * (vc * vc - 1./ r) / r
    vc_next = vc * ( 1 - vr * dt / r)
    return OrbitalParameters(r_next, theta_next, vc_next, vr_next)
    
def solve_motion_equation(radius, theta , radial_velocity):
    '''
    Solve the 2D motion equations for a grativational potential equal to 1/r.
    The units here are arbitrary since GM = 1.
    @param radius: The initial distance of the particle from the central body.
    @param theta: The initial angle 0 is at x-axis and 90 at the y-axis.
    @param radial_velocity: The initial radial vecolicy.
    yield: The orbital parameters for each step.
    '''
    # setup initial conditions.
    r, theta , vr = radius, theta , radial_velocity
    vc = math.sqrt(1./r) # pure circular motion.
    number_of_points_per_orbit = 1000
    orbits = 10 
    period = 2.* math.pi * r / vc
    delta_time = period / number_of_points_per_orbit
    number_of_steps = int (orbits * period / delta_time)
    print("Radius = {}, Angular velocity = {} , Radial velocity = {}".format(r, vc, vr))
    
    # generate orbit points.
    op = OrbitalParameters(r, theta ,vc, vr)
    for i in range(number_of_steps):
        yield op
        op = get_next_state(op, delta_time)

	
