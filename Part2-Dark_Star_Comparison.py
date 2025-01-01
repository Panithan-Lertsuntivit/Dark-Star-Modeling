# Script is called Part2-Dark_Star_Comparison.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


''' - - - - - - - - Functions - - - - - - - - '''


def solarmass_heatmap_fromcsv(folder_name, alpha_value,
                                m_chi_array, m_mu_array):
    # Function takes in a folder name and different variable values
    # and returns a 2D array of the max Solar Masses for each combination
    # Each row represents a dark matter particle mass, and each column
    # represents a mediator mass

    # Identifying needed size of numpy array
    rows = len(m_chi_array)
    columns = len(m_mu_array)

    # Initialize numpy array
    array_maxsolarmasses = np.zeros((rows, columns), dtype=float)

    # Sorting [increasing order] and Formatting values
    chi_ordered_MeV = np.array(sorted(m_chi_array, reverse=True))

    mu_ordered_MeV = np.array(sorted(m_mu_array))

    # For loop - to loop through each combination and get the maximum solar mass
    alpha_file_segment = f"alpha_{alpha_value:0.0e}"
    for i_idx, chi_value in enumerate(chi_ordered_MeV):
        # Chi = Dark Matter particle [constant in each row]
        chi_file_segment = f"chi_{chi_value}MeV"

        for j_idx, mu_value in enumerate(mu_ordered_MeV):
            # Mu = Mediator [constant in each column]
            mu_file_segment = f"mu_{mu_value}MeV"

            # csv path, and reading the file contents into DataFrame
            csv_path = (f"{folder_name}/{chi_file_segment} {mu_file_segment} "
                        f"{alpha_file_segment}.csv")
            darkstar_df = pd.read_csv(csv_path)

            # Reading contents from csv file
            print(f"Read contents from: {csv_path}")

            # Collecting only the SolarMass column and finding the max value
            column_names = darkstar_df.columns
            solarmass_label = column_names[2]
            max_solarmass = max(darkstar_df[solarmass_label])

            # print(max_solarmass)

            array_maxsolarmasses[i_idx, j_idx] = max_solarmass

    # # Print 2D array to check with heatmap
    # print(array_maxsolarmasses)

    # Custom diverging normalization: Midpoint at 1 [for 1 Solar Mass].
    # Neutron stars with a solar mass of 1 are the minimum allowable mass
    # according to some sources.
    # The maximum is set to 3, to encapsulate the max result
    diverging_norm = mcolors.TwoSlopeNorm(vmin=0, vcenter=1, vmax=3)

    # Creating a Heat map [figsize=(width, height) to define size]
    fig, ax = plt.subplots(figsize=(8, 9))

    cax = ax.imshow(array_maxsolarmasses, cmap='RdBu', aspect='auto',
                    norm=diverging_norm)
    # Color bar and color bar label
    cbar = fig.colorbar(mappable=cax, ax=ax)
    cbar.set_label(r"Solar Mass [M$_{\odot}$]")

    # Title and Labels
    # [x_axis = mediator (μ or \mu)] [y_axis = DM particle (χ or \chi)]
    title_name = f"Max Solar Mass at $\\alpha = {alpha_value:0.0e}$"
    ax.set_title(title_name, fontweight='bold', fontsize=14)
    ax.set_xlabel(r"Field Mediator Mass (M$_{\mu}$) [MeV]")
    ax.set_ylabel(r"Dark Matter Particle Mass (M$_{\chi}$) [MeV]")

    # Tick marks
    ax.set_xticks(range(len(mu_ordered_MeV)))
    ax.set_xticklabels(mu_ordered_MeV)
    ax.set_yticks(range(len(chi_ordered_MeV)))
    ax.set_yticklabels(chi_ordered_MeV)

    plt.tight_layout()

    plt.show()


''' - - - - - - - - Main Code - - - - - - - - '''
# Dark Star particle mass and Field Mediator mass values
# Mass Units: [Natural: MeV]        [Non-Natural: MeV/c^2]
m_chi_values = [500, 1000, 1500, 2000, 2500, 3000]
m_mu_values = [6, 8, 10, 12]

# Yukawa's Interaction Coupling Strength [Unitless]
alpha_values = [1.0 * pow(10, -3), 5.0 * pow(10, -4), 1.0 * pow(10, -4)]

alpha_val = [1.0 * pow(10, -3)]

csv_folder = f"results_csv"

result = solarmass_heatmap_fromcsv(csv_folder, alpha_values[0], m_chi_values, m_mu_values)
result2 = solarmass_heatmap_fromcsv(csv_folder, alpha_values[1], m_chi_values, m_mu_values)
result3 = solarmass_heatmap_fromcsv(csv_folder, alpha_values[2], m_chi_values, m_mu_values)



