# Dark Star Modeling

Modeling Dark Matter clumping under various pressure and energy densities using the **Tolman-Oppenheimer-Volkoff equations**

$$\frac{dP}{dr} = - \left(\frac{Gm(r)\rho(r)}{r^{2} c^{2}}\right) \left(1 + \frac{P(r)}{\rho(r)} \right) \left(1 + \frac{4 \pi r^{3}P(r)}{m(r)} \right) \left(1 - \frac{2Gm(r)}{rc^{2}} \right)^{-1}$$

$$\frac{dM}{dr} = 4 \pi r^{2} \rho(r)$$

Started in 2022 under the guidance of Professor William Spinella

## Abstract
Dark matter is an unknown substance that accounts for most of the mass within the universe. Researchers try to understand the properties of dark matter and its interactions with other particles.

This study aims to reproduce the findings within “Asymmetric dark matter stars” and "Dark stars: Gravitational and electromagnetic observables” by constructing mass-radius relationships for dark matter clumping, or Dark Stars, and to further observe any trends that may occur from different parameters.

A theoretical model for Dark Stars was implemented, allowing the Tolman-Oppenheimer-Volkoff (TOV) equations to be solved and producing Dark Star mass-radius curves. Experimentation was done on parameter values and the resulting curves were compared to identify trends among different Dark Stars properties.

## Introduction
The information known about dark matter is detailed but quite sparse. For instance, the existence of dark matter particles is crucial to explain the high velocities of many galaxies and galaxy clusters, as the observable mass within them alone isn’t enough to maintain their velocities. As a result, it has been concluded that a majority of the mass within these galaxies and galaxy clusters is due to dark matter particles that interact weakly with other types of matter outside of gravitational interactions, making it difficult to directly detect dark matter. The current state of technology and experiments isn’t sufficient enough to directly detect dark matter, but it is possible to infer concentrations of dark matter.

Figure 1 is an image of galaxy cluster Abell 1698, which shows a distribution of Dark Matter concentrations produced by researchers at NASA. The tints of blue are the inferred Dark Matter concentrations within the galaxy cluster.

<div style="text-align: center;">
  <img src="Images/STScI-01EVT51HJBMFAP17EQNFS2HFV2.jpg" alt="Abell 1698" style="width: 500; height: auto;">
  <p><strong>Figure 1:</strong> NASA, ESA, and D. Coe (JPL/Caltech and STScl)</p>
</div>


With so much unknown about dark matter, large amounts of research is devoted to the study of dark matter and their characteristics. For instance, it has been theorized that the self-interactions of dark matter are purely gravitational, leading to the clumping of dark matter or the formation of Dark Stars. Research into the clumping of dark matter is usually referenced with the formation of Neutron Stars, which are composed primarily of neutrons and are the densest objects observable within the universe [[1]](https://imagine.gsfc.nasa.gov/science/objects/neutron_stars1.html).  

For comparison, neutrons have a mass of about $939.565 MeV$, while some studies have theorized and modeled dark matter with mass values between $1000 MeV$ all the way to $1,000,000 MeV$ [Kouvaris and Maselli Papers]. While these similarities aren’t perfect, Neutron Stars are the only observable objects that can be referenced because of their extreme density and resulting gravitational properties, characteristics uniquely shared with Dark Stars.

**Dark Matter Interactions**     \
Interactions between Dark Matter particles can depend on multiple variables:     
 - Dark Matter Particles ($\chi$) and their mass ($m_{\chi}$)
 - Field Mediators ($\mu$) and their mass ($m_{\mu}$)
 - Interaction Coupling Strength ($\alpha$)

## Methods / Results
In this study, dark matter self interactions are assumed to be repulsive and depend on multiple variables like the dark matter particles ($\chi$), field mediator ($\mu$), and interaction coupling strength ($\alpha$). Figure 2 is a Feynman diagram visualizing the self interactions between dark matter particles.

<div style="text-align: center;">
  <img src="Images/Feynman_DarkMatterInteraction.png" alt="Feynman Diagram - Dark Matter Interaction" style="width: 500; height: auto;">
  <p><strong>Figure 2:</strong> Feynman Diagram - Dark Matter Interaction</p>
</div>


As the dark matter particles approach each other, the field mediator is an intermediary particle that passes the interaction coupling strength between the two dark matter particles. In a sense, the field mediator is a messenger particle “carrying” the interaction coupling strength, determining the type of interaction that occurs between the dark matter particles. However, the interaction isn’t completely dependent on the field mediator. 

Each of the variables affect the interaction in different ways. For the dark matter particles and field mediators, they affect the interaction through their masses, while the interaction coupling strength directly affects the interaction.

These variables are then applied to the following equations to calculate the repulsive Yukawa potential energy (1), kinetic pressure (2) and kinetic energy (3) values for dark matter clumping.

$$
\begin{equation}
    \rho_{Yukawa} = \frac{g_{s}^{2} \alpha}{18 \pi^{3}} \frac{m_{\chi}^{3}}{\mu^{2}} x^{6} \tag{1}
\end{equation}
$$

$$
\begin{equation}
    P_{kinetic} = \frac{g_{s}}{2} m_{\chi}^{4} \, \psi(x) \tag{2}
\end{equation}
$$

$$
\begin{equation}
    \rho_{kinetic} = \frac{g_{s}}{2} m_{\chi}^{4} \, \xi(x) \tag{3}
\end{equation}
$$


In equation (1), the x variable is a measure of how relativistic a particle is, or how much their behavior is influenced by the principles of Einstein’s theory of relativity [Kouvaris]. Non-relativistic particles move much slower than the speed of light, and can be described using classical physics. While relativistic particles move significant fractions of the speed of light, and can only be described using the laws of relativity. The general ranges of x and their meaning are as follows:
- $x = 0 \, \qquad$            [particle is at rest]
- $x > 1 \, \qquad$            [particle is non-relativistic, moving at slow speeds]
- $x \approx 1 \, \qquad$      [particle is relativistic, moving at significant fractions of the speed of light]
- $x \gg 1 \qquad$          [particle is highly relativistic, moving close to the speed of light]

Within this study, the relativistic parameter was kept to a range of 0 to 1, testing particles that are non-relativistic and relativistic. Additionally, the $\xi(x)$ and $\psi(x)$ equations within the Kinetic Pressure and Kinetic Energy equations were provided in “Asymmetric dark matter stars,” and are the following equations below [Kouvaris et al].

$$
\begin{equation}
    \xi(x) = \frac{1}{8 \pi^{2}} \left[x \sqrt{1 + x^{2}} (1 + 2x^{2}) - ln\left(x + \sqrt{1 + x^{2}}\right) \right] \tag{4}
\end{equation}
$$

$$
\begin{equation}
    \psi(x) = \frac{1}{8 \pi^{2}} \left[x \sqrt{1 + x^{2}} (\frac{2 x^{2}}{3} - 1) + ln\left(x + \sqrt{1 + x^{2}}\right) \right] \tag{5}
\end{equation}
$$

After these values are calculated, they are then summed up to determine the total pressure and energy density for dark matter clumping.

$$
\begin{equation}
    P_{total} = P_{kinetic} + \rho_{Yukawa} \notag
\end{equation}
$$

$$
\begin{equation}
    P_{total} = \frac{g_{s}}{2} m_{\chi}^{4} \, \psi(x) + \frac{g_{s}^{2} \alpha}{18 \pi^{3}} \frac{m_{\chi}^{3}}{\mu^{2}} x^{6} \tag{6}
\end{equation}
$$


$$
\begin{equation}
    \rho_{total} = \rho_{kinetic} + \rho_{Yukawa} \notag
\end{equation}
$$

$$
\begin{equation}
    \rho_{total} = \frac{g_{s}}{2} m_{\chi}^{4} \, \xi(x) + \frac{g_{s}^{2} \alpha}{18 \pi^{3}} \frac{m_{\chi}^{3}}{\mu^{2}} x^{6} \tag{7}
\end{equation}
$$

With these values calculated, an equation of state has been established for dark matter clumping, which describes the relationship between the pressure density and energy density of dark matter. An example graph of the pressure density and energy density with the following parameters: 

$$m_{\chi} = 1000 MeV / c^{2} \qquad m_{\mu} = 10 MeV / c^{2} \qquad \alpha = 10^{-3}$$

<div style="text-align: center;">
  <img src="results_density_graphs/density_graph chi_1000MeV mu_10MeV alpha_1e-03.png" alt="Pressure and Energy Density Example Graph" style="width: 500; height: auto;">
  <p><strong>Figure 3:</strong> Example Pressure and Energy Density Graph</p>
</div>

With an array of corresponding pressure density and energy density values, the Tolman-Oppenheimer-Volkoff equations are solved numerically for each pair of density values. Where pairs of pressure density and energy density values are used as central density values to calculate the mass and radius for that Dark Star. Within the graph, the total masses are expressed as solar mass multiples, where one solar mass ($M_{\odot}$) is equal to $1.989 \times 10^{30} kg$. 


