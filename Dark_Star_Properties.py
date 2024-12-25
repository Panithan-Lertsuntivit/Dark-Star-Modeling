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
speed_light = 3.00 * pow(10, 8)             # Units: m/s

# Reduced Planck's constant [h bar] times the speed of light
h_bar_c = 197.327                           # Units: MeV-fm

# Dark Star particle mass and Field Mediator mass
m_particle = 1000.0             # Units: MeV / c^2
m_mediator = 10.0               # Units: MeV / c^2

alpha = 1.0 * pow(10, -3)       # Yukawa's interaction coupling strength
