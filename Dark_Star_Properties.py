# Script is called Dark_Star_Properties.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools

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
# Assuming that a Dark Star is composed of purely Dark Matter.
# Additionally, we are assuming that Dark Matter is nonbaryonic [it is "cold",
# and move nonrelativitically in the early universe] and only has weak
# interactions with other matter through gravity.
# Since Dark Matter is nonbaryonic, it has a temperature of 0 Kelvin


''' - - - - - Constants - - - - - '''
g_spin = 2.0                    # g_s = 2; from Pauli exclusion principle
# Planck's constant and the speed of light
Planck_constant = 4.136 * pow(10, -15)          # Units: eV-s
speed_light = 2.99792458 * pow(10, 8)           # Units: m/s
speed_light_fm = speed_light * pow(10, 15)      # Units: fm/s

# Reduced Planck's constant [h bar] times the speed of light
h_bar_c = 197.327                           # Units: MeV-fm

# Gravitational constant
gravitational_constant = 6.67430 * pow(10, -11)     # Units: m^3 / (kg-s^2)
G_with_c_squared = 1.189763 * pow(10, 5)    # Units: (fm^3 - c^2) / (MeV-s^2)
# G / c^2 has units of (fm - c^2) / (MeV)
G_divide_c_squared = G_with_c_squared / pow(speed_light_fm, 2)

# Solar Mass Conversion
solar_mass = 1.989 * pow(10, 30)

''' - - - - - - - - Functions - - - - - - - - '''
def Yukawa_force(m_chi, m_mu, alpha, x):
    # Input [Natural Units] -> Output [Natural Units]
    # Dark Star particle mass       - m_chi     [Natural Units: MeV]
    # Field Mediator mass           - m_mu      [Natural Units: MeV]
    # Interaction coupling strength - alpha     [Unitless]

    yukawa_potential = ((pow(g_spin, 2) * alpha * pow(m_chi, 6) * pow(x, 6)) /
                        (18.0 * pow(np.pi, 3) * pow(m_mu, 2)))
    # Yukawa potential [Natural Units: MeV]

    return yukawa_potential


def calculate_pressure_density(x, m_chi, m_mu, alpha):
    # Input [Natural Units] -> Output [Natural Units]
    # Dark Star particle mass       - m_chi     [Natural Units: MeV]
    # Field Mediator mass           - m_mu      [Natural Units: MeV]
    # Interaction coupling strength - alpha     [Unitless]

    sqrt_x = np.sqrt(1 + pow(x, 2))

    # psi function [ψ] (Equation 7 within "Asymmetric dark matter stars")
    psi = ((x * sqrt_x * (2 * (pow(x, 2) / 3) - 1) + np.log(x + sqrt_x)) /
          (8.0 * pow(np.pi, 2)))

    pressure_kinetic = (g_spin / 2) * pow(m_chi, 4) * psi

    yukawa_potential = Yukawa_force(m_chi, m_mu, alpha, x)

    pressure_density_calculated = np.array((pressure_kinetic + yukawa_potential)
                                / pow(h_bar_c, 3))
    # Natural Units: [MeV / fm^3]

    return pressure_density_calculated


def calculate_energy_density(x, m_chi, m_mu, alpha):
    # Input [Natural Units] -> Output [Natural Units]
    # Dark Star particle mass       - m_chi     [Natural Units: MeV]
    # Field Mediator mass           - m_mu      [Natural Units: MeV]
    # Interaction coupling strength - alpha     [Unitless]

    sqrt_x = np.sqrt(1 + pow(x, 2))

    # xi function [ξ] (Equation 6 within "Asymmetric dark matter stars")
    xi = ((x * sqrt_x * (1 + 2 * pow(x, 2)) - np.log(x + sqrt_x)) /
           (8.0 * pow(np.pi, 2)))

    energy_kinetic = (g_spin / 2) * pow(m_chi, 4) * xi

    yukawa_potential = Yukawa_force(m_chi, m_mu, alpha, x)

    energy_density_calculated = np.array((energy_kinetic + yukawa_potential)
                              / pow(h_bar_c, 3))
    # Natural Units: MeV / fm^3

    return energy_density_calculated


def dark_star_mass_radius(energydensity, pressuredensity):
    # Input [Natural Units] -> Output [Non-Natural Units / SI Units]
    # Initializing array for storing Dark Star mass and radius values
    darkstar_radius = np.array([])
    darkstar_mass = np.array([])
    darkstar_solarmass = np.array([])

    # Will be looping through each pressure density value given. Each pressure
    # density value is used as the central pressure for that dark star
    for i, central_pressure in enumerate(pressuredensity):
        # Initial Values / Dark Star Properties at its core
        initial_mass = 0.0
        initial_energy = energydensity[i]
        initial_pressure = central_pressure
        radial_step = 1.0 * pow(10, 17)             # Units in fm [femto-meter]

        # Current [i] / Next [i + 1] Values
        energy_i = initial_energy           # Natural Units: MeV / (fm^3)
        pressure_i = initial_pressure       # Natural Units: MeV / (fm^3)

        mass_i = initial_mass               # Natural Units: MeV
        next_radius = radial_step           # Natural Units: fm

        counter = 1

        while (counter > 0):
            # Using TOV equations to calculate the next mass and pressure values
            # Mass [Natural Units: MeV]
            next_mass = mass_i + (4 * np.pi * pow(next_radius, 2)
                                  * energy_i * radial_step)

            # Pressure [Natural: MeV/fm^3]
            next_pressure \
                = (pressure_i - ((energy_i + pressure_i) * (
                    mass_i + 4 * np.pi * pow(next_radius, 3) * pressure_i) * (
                    G_divide_c_squared * radial_step)) / (
                    pow(next_radius, 2) *
                    (1 - (2 * G_divide_c_squared * mass_i)/next_radius)))

            if (next_pressure <= 0):
                # Converting from Natural to Non-Natural Units
                # Mass: [MeV] -> [MeV/c^2] -> [J/c^2] = [(N-m)/(m/s)^2] = [kg]
                star_mass_kg = (next_mass / pow(speed_light, 2) *
                             (1.602 * pow(10, -13)))

                # Convert from [km] to solar masses
                star_solarmass = star_mass_kg / solar_mass

                # Radius: [fm] -> [km]
                star_radius_km = next_radius / pow(10, 18)

                # Saving to initialized array
                darkstar_mass = np.append(darkstar_mass, [star_mass_kg])
                darkstar_radius = np.append(darkstar_radius, [star_radius_km])
                darkstar_solarmass = np.append(darkstar_solarmass,
                                               [star_solarmass])
                # print(star_mass_kg)
                # Changing counter to exit while loop
                counter = -1

            else:
                # Updating Values (for next iteration)
                mass_i = next_mass
                pressure_i = next_pressure
                next_radius = next_radius + radial_step
                # Linear Interpolation for energy density
                energy_i = np.interp(pressure_i, pressuredensity, energydensity)

    # Output is in Non-Natural Units [mass = kg; radius = km]

    return darkstar_radius, darkstar_mass, darkstar_solarmass


def filtering(unfiltered_radius, unfiltered_mass, unfiltered_solarmass):
    # Filtering out data points that don't align with the expected pattern

    """ Stage 1 - Filtering out low mass values """
    solarmass_tolerance = 0.01
    low_mass_filter_idx = (unfiltered_solarmass > solarmass_tolerance)

    # Applying the first filtering
    radius_filter1 = unfiltered_radius[low_mass_filter_idx]
    mass_filter1 = unfiltered_mass[low_mass_filter_idx]
    solarmass_filter1 = unfiltered_solarmass[low_mass_filter_idx]

    """ Stage 2 - Filtering out unexpected pattern """
    difference_array = np.diff(radius_filter1)
    logic_array = difference_array > 0

    unexpected_pattern_idx = np.where(logic_array == 1)[0]

    if unexpected_pattern_idx.size == 0:
        start_unexpected_pattern = -1
    else:
        # Add +1 to the result, because the difference array has (n - 1) terms
        start_unexpected_pattern = unexpected_pattern_idx[0] + 1

    # Applying second filtering
    radius_filtered = radius_filter1[0:start_unexpected_pattern]
    mass_filtered = mass_filter1[0:start_unexpected_pattern]
    solarmass_filtered = solarmass_filter1[0:start_unexpected_pattern]

    return radius_filtered, mass_filtered, solarmass_filtered


''' - - - - - - - - Explanation - - - - - - - - '''
# x is a measure of how relativistic a particle is (how much their behavior is
# influenced by the principles of Einstein's theory of relativity)
#       >> Non-relativistic particle - particle moves much slower than the
#       speed of light. Behavior can be described using classical physics
#       >> Relativistic particle - particle moves at speeds close to the speed
#       of light. Behavior is affected by relativity [time and space behave
#       differently for relativistic particles]
# x = 0 [particle is at rest];          x > 1 [particle is non-relativistic]
# x ≈ 1 [particle is relativistic; moves at significant fraction of light speed]
# x > 1 [particle is highly relativistic; moves close to the speed of light]

# Array of values that to test non-relativistic and relativistic behavior
relativity_parameter = np.arange(0.01, 1.00, 0.001)

# Dark Star particle mass and Field Mediator mass values
# Mass Units: [Natural: MeV]        [Non-Natural: MeV/c^2]
m_chi_values = [500, 1000, 1500, 2000, 2500, 3000]
m_mu_values = [6, 8, 10, 12]

# Yukawa's Interaction Coupling Strength [Unitless]
alpha_values = [1.0 * pow(10, -3), 5.0 * pow(10, -4), 1.0 * pow(10, -4)]

''' - - - - - - - - Main Code - - - - - - - - '''
for coupling_strength, m_particle, m_mediator in \
        itertools.product(alpha_values, m_chi_values, m_mu_values):

    # Initialize pandas DataFrame
    dark_star = pd.DataFrame()
    dark_star['Radius'] = ''
    dark_star['Mass'] = ''
    dark_star['SolarMass'] = ''
    dark_star['Comments'] = ''

    # Description and save location
    save_description = (f"chi_{m_particle}MeV mu_{m_mediator}MeV "
                        f"alpha_{coupling_strength:.0e}")
    plot_description = (fr"$\chi$ = {m_particle} MeV, "
                        fr"$\mu$ = {m_mediator} MeV, "
                        fr"$\alpha$ = {coupling_strength:0.0e}")

    csv_folder = "results_csv"
    plot_folder = "results_plots"
    csv_save_path = f"{csv_folder}/{save_description}.csv"
    plot_save_path = f"{plot_folder}/{save_description}.png"

    # When calculating the pressure and energy density, the inputs are in
    # Natural Units and the output is in Natural Units
    pressure_density \
        = calculate_pressure_density(x=relativity_parameter, m_chi=m_particle,
                                     m_mu=m_mediator, alpha=coupling_strength)

    energy_density \
        = calculate_energy_density(x=relativity_parameter, m_chi=m_particle,
                                   m_mu=m_mediator, alpha=coupling_strength)

    # When calculating the dark star mass and radius, the inputs are in Natural
    # Units but the output is in Non-Natural Units [SI Units]
    [orig_dark_star_radius, orig_dark_star_mass, orig_dark_star_solarmass] \
        = dark_star_mass_radius(energydensity=energy_density,
                                pressuredensity=pressure_density)

    # Filtering data points
    [dark_star_radius, dark_star_mass, dark_star_solarmass] \
        = filtering(unfiltered_radius=orig_dark_star_radius,
                    unfiltered_mass=orig_dark_star_mass,
                    unfiltered_solarmass=orig_dark_star_solarmass)

    # Saving to Dark Star radius and mass values to DataFrame
    dark_star['Radius'] = pd.Series(dark_star_radius)
    dark_star['Mass'] = pd.Series(dark_star_mass)
    dark_star['SolarMass'] = pd.Series(dark_star_solarmass)

    # Commments about the values
    dark_star.loc[1, 'Comments'] = f"m_chi = {m_particle} MeV"
    dark_star.loc[3, 'Comments'] = f"m_mu = {m_mediator} MeV"
    dark_star.loc[5, 'Comments'] = f"alpha = {coupling_strength}"

    # Saving results to csv file
    dark_star.to_csv(csv_save_path, index=False)
    print(f"Saved data point results to: {csv_save_path}")

    # Plotting the result
    plt.plot(dark_star_radius, dark_star_solarmass)

    # Title and labels
    plt.title(plot_description)
    plt.xlabel("Dark Star Radii [km]")
    solarmass_symbol = r"M$_{\odot}$"
    plt.ylabel(f"Dark Star Mass [{solarmass_symbol}]")

    # Formatting and saving plot
    plt.tight_layout()
    plt.savefig(plot_save_path, dpi=300)
    print(f"Saved plot result to: {plot_save_path} \n")

    plt.close('all')


''' - - - - - - - - - - Variable Reasoning - - - - - - - - - -  
Yukawa's Interaction Coupling Strength [Unit-less]
alpha = 1x10^-3; 5x10^-4; 1x10^-4

# These give an observable trend that can be seen when progressing from 1x10^-3 
to 1x10^-4. It would have been nice if 1x10^-2 continued the pattern, but for 
some reason, no Dark Stars are possible at that interaction coupling strength

Dark Matter Particle Mass   [Natural: MeV]    [Non-Natural: MeV/c^2]
m_chi = 500 MeV; 1000 MeV; 1500 MeV; 2000 MeV; 2500 MeV; 3000 MeV 

# Looked at Maselli's paper and decided on [1000 MeV; 2000 MeV; 3000 MeV; 
4000 MeV; 5000 MeV] but reduced the max to be 3000 MeV, when it was apparently 
that larger mass values aren't supported in any circumstance

Field Mediator Mass         [Natural: MeV]    [Non-Natural: MeV/c^2]
m_mu = 6 MeV; 8 MeV; 10 MeV; 12 MeV

# Looked at Maselli's paper and decided on [6 MeV; 8 MeV; 10 MeV; 12 MeV; 
14 MeV] but reduced the max to be 12 MeV, when it was apparent that larger 
mediator masses aren't supported after 12 MeV

'''