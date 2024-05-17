# chapter 2 exercise 4 page 87
# given non rotating geocentric coordiantes, get orbital elements (angles in degrees)
import numpy as np


earth_gm = 3.9860044e14  # m3/s2

def cart_to_kep(cart):
    """
    Converts from Cartesian state to Keplarian Elements
    Parameters:
        cart (array): Array of cartesian states (x, y, z, vx, vy, vz)

    Returns:
        kep (array): Array of 6 keplarian elements (sma, ecc, inc (rad), raan (rad), arg (rad), mean (rad))
    """
    position = cart[:3]
    velocity = cart[3:]

    r_mag = np.linalg.norm(position)
    v_mag = np.linalg.norm(velocity)
    r_dot_v = np.dot(position, velocity)

    angular_momentum = np.cross(position, velocity)  # Orbital angular momentum
    e_vector = ((np.cross(velocity, angular_momentum)) / earth_gm) - (
        position / r_mag
    )  # Eccentricity Vector
    eccentricity = np.linalg.norm(e_vector)  # Eccentricity
    n_vector = np.cross(np.array([0, 0, 1]), angular_momentum)

    if np.dot(position, velocity) >= 0:
        true_anomaly = np.arccos(
            (np.dot(e_vector, position))
            / (np.linalg.norm(e_vector) * np.linalg.norm(position))
        )
    else:
        true_anomaly = 2 * np.pi - np.arccos(
            (np.dot(e_vector, position))
            / (np.linalg.norm(e_vector) * np.linalg.norm(position))
        )

    inclination = np.arccos(angular_momentum[2] / np.linalg.norm(angular_momentum))

    eccentric_anomaly = 2 * np.arctan(
        (np.tan(true_anomaly / 2)) / np.sqrt((1 + eccentricity) / (1 - eccentricity))
    )

    if n_vector[1] >= 0:
        raan = np.arccos(n_vector[0] / np.linalg.norm(n_vector))
    else:
        raan = 2 * np.pi - np.arccos(n_vector[0] / np.linalg.norm(n_vector))

    if e_vector[2] >= 0:
        arg = np.arccos(
            np.dot(n_vector, e_vector)
            / (np.linalg.norm(n_vector) * np.linalg.norm(e_vector))
        )
    else:
        arg = 2 * np.pi - np.arccos(
            np.dot(n_vector, e_vector)
            / (np.linalg.norm(n_vector) * np.linalg.norm(e_vector))
        )
    mean_anomaly = eccentric_anomaly - eccentricity * np.sin(eccentric_anomaly)
    sma = 1 / ((2 / r_mag) - (v_mag ** 2 / earth_gm))

    return np.array(
        [sma, eccentricity, np.rad2deg(inclination), np.rad2deg(raan),
         np.rad2deg(arg), np.rad2deg(mean_anomaly), np.rad2deg(eccentric_anomaly)]
    )


if __name__ == "__main__":
    initial_state = np.array([7088580.789,-64.326,920514,
                          -10.20544809,-522.85385193,7482.07514112])  # m , m/s
    result = cart_to_kep(initial_state)
    print(result)