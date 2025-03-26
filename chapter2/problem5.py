# given the same position and velocity as problem 4, predict position and velocity
# at t=3000sec. Assume two body motion. 
# Determine radial and horizontal compotents of velocity and the flight path angle

import numpy as np
from scipy.integrate import solve_ivp

earth_gm = 3.9860044e14  # m3/s2

# define the two body problem ODE
def twoBodyODE(t,Xdot):
    r = np.sqrt((Xdot[0]**2)+(Xdot[1]**2)+(Xdot[2]**2))
    
    X = np.zeros(6)
    X[0] = Xdot[3]
    X[1] = Xdot[4]
    X[2] = Xdot[5]
    X[3] = -(earth_gm/r**3)*(Xdot[0])
    X[4] = -(earth_gm/r**3)*(Xdot[1])
    X[5] = -(earth_gm/r**3)*(Xdot[2])
    
    return X

def twoBodyProp(initial_state,tspan):
    """
    Defines 2 body propagation
    """

    sol = solve_ivp(twoBodyODE, (tspan[0],tspan[-1]), initial_state,
                    t_eval = tspan, rtol = 1.0e-10, atol = 1.0e-10)
    
    # get the last state
    #resulting vectos#
    ephemeris = list(zip(sol.y[0],sol.y[1],sol.y[2],
                          sol.y[3],sol.y[4],sol.y[5]))
    return ephemeris[-1]



if __name__ == "__main__":
    initial_state = np.array([7088580.789,-64.326,920514,
                          -10.20544809,-522.85385193,7482.07514112])  # m , m/s
    
    # example 2.2.4.1, space shuttle initial condition
    initial_shuttle_state = np.array([5492000.34,3984001.40,2955.81,
                          -3931.046491,5498.676921,3665.980697])  # m , m/s
    # example 2.25 shuttle space after 30 minutes
    shuttle_state_after_30 = np.array([-5579681.52,2729244.60,2973901.72,
                          3921.809270,6300.799313,1520.178404])  # m , m/s
    
    #time interval
    tspan = np.arange(0,3000,0.001)
    result = twoBodyProp(initial_shuttle_state,tspan)
    print(result)