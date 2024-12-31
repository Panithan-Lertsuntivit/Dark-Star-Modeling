# Script is called Part2-Dark_Star_Comparison.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import itertools


''' - - - - - - - - Functions - - - - - - - - '''
def maxSolarMass_fromcsv(folder_name, alpha_value, m_chi_values, m_mu_values):
    # Function takes in a folder name and different variable values
    # and returns a 2D array of the max Solar Masses for each combination
    # Each row represents a dark matter particle mass, and each column
    # represents a mediator mass

    # Identifying needed size of numpy array
    rows = len(m_chi_values)
    columns = len(m_mu_values)

    # Initialize numpy array
    array_maxsolarmasses = np.zeros((rows, columns), dtype=float)

    # Sorting [increasing order] and Formatting values
    chi_ordered_GeV = np.array(sorted(m_chi_values)) / 1000
    chi_formatted_GeV = chi_ordered_GeV.astype(int)

    mu_ordered_MeV = np.array(sorted(m_mu_values))

    # For loop - to loop through each combination and get the maximum solar mass
    alpha_file_segment = f"alpha_{alpha_value:0.0e}"
    for i_idx, chi_value in enumerate(chi_formatted_GeV):
        # Chi = Dark Matter particle [constant in each row]
        chi_file_segment = f"chi_{chi_value}GeV"

        for j_idx, mu_value in enumerate(mu_ordered_MeV):
            # Mu = Mediator [constant in each column]
            mu_file_segment = f"mu_{mu_value}MeV"

            # csv path, and reading the file contents into DataFrame
            csv_path = (f"{folder_name}/{chi_file_segment} {mu_file_segment} "
                        f"{alpha_file_segment}.csv")
            darkstar_df = pd.read_csv(csv_path)

            print(f"Read contents from: {csv_path}")

            # Collecting only the SolarMass column and finding the max value
            column_names = darkstar_df.columns
            solarmass_label = column_names[2]
            max_solarmass = max(darkstar_df[solarmass_label])

            print(max_solarmass)

            array_maxsolarmasses[i_idx, j_idx] = max_solarmass

    print(array_maxsolarmasses)

    return 0


# Dark Star particle mass and Field Mediator mass values
# Mass Units: [Natural: MeV]        [Non-Natural: MeV/c^2]
m_chi_values = [1000, 2000, 3000, 4000]
m_mu_values = [8, 10, 12]

# Yukawa's Interaction Coupling Strength [Unitless]
alpha_values = [1.0 * pow(10, -3), 1.0 * pow(10, -4), 1.0 * pow(10, -5)]
alpha_val = [1.0 * pow(10, -3)]

csv_folder = f"results_csv"

file_name = f"chi_1GeV mu_10MeV alpha_1e-03.csv"

file_path = f"{csv_folder}/{file_name}"

tester = pd.read_csv(file_path)

result = maxSolarMass_fromcsv(csv_folder, alpha_val[0], m_chi_values, m_mu_values)
