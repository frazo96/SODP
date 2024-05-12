# Obrit Determination Schutz
# Chapter 1 Problem 1

import numpy as np
from scipy.optimize import fsolve

def rho(x0,xs,xd0,t,y0,ys,yd0,g):
    """
    non linear equation for /rho
    """
    return np.sqrt((x0-xs+xd0*t)**2 + (y0-ys+yd0*t-g/2*t**2)**2)


def rhoUniformGravity(vehicle, tracking_station, observations):
    """
    Estimate rho initital condidtions with vehicle initial conditions and 4 observations
    """
    # estimate true values for x0,y0,xd0,yd0,g
    def func(vehicle=vehicle,tracking_station=tracking_station):
        return [
            rho(vehicle[0],tracking_station[0],vehicle[2],observations[0][0],vehicle[1],tracking_station[1],vehicle[3],vehicle[4])-observations[0][1],
            rho(vehicle[0],tracking_station[0],vehicle[2],observations[1][0],vehicle[1],tracking_station[1],vehicle[3],vehicle[4])-observations[1][1],
            rho(vehicle[0],tracking_station[0],vehicle[2],observations[2][0],vehicle[1],tracking_station[1],vehicle[3],vehicle[4])-observations[2][1],
            rho(vehicle[0],tracking_station[0],vehicle[2],observations[3][0],vehicle[1],tracking_station[1],vehicle[3],vehicle[4])-observations[3][1],
            rho(vehicle[0],tracking_station[0],vehicle[2],observations[4][0],vehicle[1],tracking_station[1],vehicle[3],vehicle[4])-observations[4][1]
        ]
    root = fsolve(func,initial_condiditon)
    return root

if __name__ == '__main__':
    # Unitless initial conditions
    x0 = 1.5
    y0 = 10
    xd0 = 2.2
    yd0 = 0.5
    g = 0.3
    # tracking station positions
    xs = 1
    ys = 1

    initial_condiditon = np.array([x0,y0,xd0,yd0,g])
    tracking_station = np.array([xs,ys])

    # Time and Range Observations
    observations = np.array([
        [0,7.0],
        [1,8.00390597],
        [2,8.94427191],
        [3,9.801147892],
        [4,10.630145813],
    ])
    estimates = rhoUniformGravity(initial_condiditon,tracking_station,observations)
    # answer
    answer = [1.0,8.0,2.0,1.0,0.5]
    print(estimates)
    print(np.isclose(estimates,answer,1e-4))

