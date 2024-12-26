# Script is called Dark_Star_Properties.py

import numpy as np
import matplotlib.pyplot as plt

''' - - - - - - - - - - Initial Notes / Assumptions - - - - - - - - - - '''
# Dark Matter particles are notated as χ or \chi
#       The mass of Dark Matter particles are notated as m_particle
#
# The interaction between Dark Matter particles depends on their mass, the
# field mediator (specifically its mass), and the interaction coupling strength
#
# The Field Mediator [notated as μ or \mu] is an intermediary between Dark
# Matter particles containing a mass and determining the interaction coupling
# strength
#       The mass of the Field Mediator is notated as m_mediator
#       The Interaction Coupling Strength is notated as alpha
#
# Assuming that a Dark Star is composed of purely Dark Matter, and that Dark
# Matter has a temperature of 0 Kelvin

''' - - - - - Constants - - - - - '''
g_spin = 2.0                    # g_s = 2; from Pauli exclusion principle
# Planck's constant and the speed of light
Planck_constant = 4.136 * pow(10, -15)      # Units: eV-s
speed_light = 2.99792458 * pow(10, 8)       # Units: m/s

# Reduced Planck's constant [h bar] times the speed of light
h_bar_c = 197.327                           # Units: MeV-fm

# Gravitational constant
gravitational_constant = 6.67430 * pow(10, -11)     # Units: m^3 / (kg-s^2)
G_with_c_squared = 1.189763 * pow(10, 5)    # Units: (fm^3 - c^2) / (MeV-s^2)
G = G_with_c_squared / pow(speed_light, 2)          # Units: fm^3 / (MeV-s^2)

''' - - - - - - - - Functions - - - - - - - - '''
def Yukawa_force(m_chi, m_mu, alpha, x):
    # Dark Star particle mass       - m_chi
    # Field Mediator mass           - m_mu
    # Interaction coupling strength - alpha

    yukawa_potential = ((pow(g_spin, 2) * alpha * pow(m_chi, 6) * pow(x, 6)) /
                        (18.0 * pow(np.pi, 3) * pow(m_mu, 2)))

    return yukawa_potential


def calculate_pressure_density(x, m_chi, m_mu, alpha):
    # Dark Star particle mass       - m_chi
    # Field Mediator mass           - m_mu
    # Interaction coupling strength - alpha

    sqrt_x = np.sqrt(1 + pow(x, 2))

    # psi function [ψ] (Equation 7 within "Asymmetric dark matter stars")
    psi = ((x * sqrt_x * (2 * (pow(x, 2) / 3) - 1) + np.log(x + sqrt_x)) /
          (8.0 * pow(np.pi, 2)))

    pressure_kinetic = (g_spin / 2) * pow(m_chi, 4) * psi

    yukawa_potential = Yukawa_force(m_chi, m_mu, alpha, x)

    pressure_density_calculated = np.array((pressure_kinetic + yukawa_potential)
                                / pow(h_bar_c, 3))
    # Natural Units: MeV / fm^3
    # Non-Natural Units: MeV / (fm^3 - c^8)

    return pressure_density_calculated


def calculate_energy_density(x, m_chi, m_mu, alpha):
    # Dark Star particle mass       - m_chi
    # Field Mediator mass           - m_mu
    # Interaction coupling strength - alpha

    sqrt_x = np.sqrt(1 + pow(x, 2))

    # xi function [ξ] (Equation 6 within "Asymmetric dark matter stars")
    xi = ((x * sqrt_x * (1 + 2 * pow(x, 2)) - np.log(x + sqrt_x)) /
           (8.0 * pow(np.pi, 2)))

    energy_kinetic = (g_spin / 2) * pow(m_chi, 4) * xi

    yukawa_potential = Yukawa_force(m_chi, m_mu, alpha, x)

    energy_density_calculated = np.array((energy_kinetic + yukawa_potential)
                              / pow(h_bar_c, 3))
    # Natural Units: MeV / fm^3
    # Non-Natural Units: MeV / (fm^3 - c^8)

    return energy_density_calculated


def dark_star_mass_radius(energy_density_array, pressure_density_array):
    # Initializing array for storing Dark Star mass and radius values
    darkstar_mass = []
    darkstar_radius = []

    # Constant Values


    # Will be looping through each pressure density value given. Each pressure
    # density value is used as the central pressure for that dark star
    for i, central_pressure in enumerate(pressure_density_array):
        # Initial Values / Dark Star Properties at its core
        initial_mass = 0.0
        initial_energy = energy_density_array[i]
        initial_pressure = central_pressure
        radial_step = 1.0 * pow(10, 17)             # Units in fm [femto-meter]

        # Current Values
        # Energy and Pressure have Non-Natural Units of MeV / (fm^3 - c^8)
        current_energy = initial_energy         # Natural Units: MeV / (fm^3)
        current_pressure = initial_pressure     # Natural Units: MeV / (fm^3)

        # Non-Natural Units: Mass [MeV / c^8] and Radius [fm]
        current_mass = initial_mass             # Natural Units: MeV / c^2
        current_radius = radial_step            # Natural Units: fm


    return darkstar_mass, darkstar_radius


''' - - - - - - - - Explanation - - - - - - - - '''
# x is a measure of how relativistic a particle is (how much their behavior is
# influenced by the principles of Einstein's theory of relativity)
#       >> Non-relativistic particle - particle moves much slower than the
#       speed of light. Behavior can be described using classical physics
#       >> Relativistic particle - particle moves at speeds close to the speed
#       of light. Behavior is affected by relativity [time and space behave
#       differently for relativistic particles]
# x = 0 [particle is at rest];          x > 1 [particle is non-relativistic]
# x ≈ 1 [particle is relativistic; moves at significant fraction of speed of light]
# x > 1 [particle is highly relativistic; moves close to the speed of light]

# Array of values that to test non-relativistic and relativistic behavior
relativity_parameter = np.arange(0.01, 2.00, 0.001)

# Dark Star particle mass and Field Mediator mass
m_particle = 1000.0             # Units: MeV / c^2
m_mediator = 10.0               # Units: MeV / c^2

coupling_strength = 1.0 * pow(10, -3)   # Yukawa's interaction coupling strength

''' - - - - - - - - Main Code - - - - - - - - '''

pressure_density \
    = calculate_pressure_density(x=relativity_parameter, m_chi=m_particle,
                                 m_mu=m_mediator, alpha=coupling_strength)

energy_density \
    = calculate_energy_density(x=relativity_parameter, m_chi=m_particle,
                               m_mu=m_mediator, alpha=coupling_strength)



