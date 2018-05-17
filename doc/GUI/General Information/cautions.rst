.. _cautions: 

********
Cautions
********

Users of the REFPROP program should be aware of several potential pitfalls:

If you experience large differences in your expected values of enthalpy or entropy as compared to those calculated by the program, see information on :ref:`reference`.

Changing the units in the Options/Units menu does not change the units on the tables already created, but only for new tables and plots.

The equation parameters for mixtures composed of natural gas fluids come from the 2008 GERG model (see :ref:`preferences` for the reference). The default pure fluid equations of state in REFPROP are not the same as those used in the GERG model, rather they are more complex with lower uncertainties. The GERG equations for the pure fluids are shorter, less complex, and faster, but slightly less accurate. To use the GERG model, as published, choose the corresponding option under Options/Preferences. The preference screen also has an option to use the AGA8 model for natural gas calculations.

The NIST REFPROP program is designed to provide the most accurate thermophysical properties currently available for pure fluids and their mixtures. The present version is limited to vapor-liquid equilibrium (VLE) only and does not address liquid-liquid equilibrium (LLE), vapor-liquid-liquid equilibrium (VLLE) or other complex forms of phase equilibrium. The program does not know the location of the freezing line for mixtures. Certain mixtures can potentially enter into these areas without giving warnings to the user.

Some mixtures have components with a wide range of volatilities (i.e., large differences in boiling points), as indicated by a critical temperature ratio greater than 2. Certain calculations, especially saturation calculations, may fail without generating warnings. Plotting the calculation results may reveal such cases--looking for discontinuities in density is a good check. Such mixtures, including many with hydrogen, helium, or water, may not have Type I critical behavior, that is they do not have a continuous critical line from one pure component to the other. The estimated critical parameters specified in the Substance/Fluid Information screen for these types of mixtures will not be displayed.

There are cases where an input state point can result in two separate valid states. The most common is temperature-enthalpy inputs. Viewing a T-H diagram will help show how there can be two valid state points for a given input. For example, nitrogen at 140 K and 1000 J/mol can exist at 6.85 MPa and at 60.87 MPa. When this situation occurs, REFPROP returns the state with the higher density. See the :ref:`specifiedstatepoints`  section for information on calculating the upper and lower roots.

There are certain properties pertaining only to the saturation line, such as dp/dT. For most cases, displayed properties at saturation states are those for the single phase on the saturation boundary. Thus, derivative properties at saturation as well as saturation properties that are given along constant property paths, such as Cv, Cp, or Csat, pertain to their state in the single phase. Those properties label with a '[sat]' indicate a path along the saturation line.

For pure fluids, when the 'Show 2-phase' option in the plot menu is selected, the generated lines for pressure and temperature represent metastable fluid states and the calculated lines between them. These are calculations from the equation of state disregarding any saturation states and generally have no physical significance.

Two equations of state are available for hydrogen to account for the different quantum spin states of the molecule. Normal hydrogen should be used in applications where it was created and stored at 250 K or above, or when it was cooled to below 250 K and stored without a catalyst for less than a day. The parahydrogen equation should be used where hydrogen was catalyzed or stored for several days at the normal boiling point (NBP) and used at any temperature within 1 day of storage at the NBP. Since the rate of conversion between quantum states is dependent on temperature, pressure, and the storage container, these values are only estimates. For more information, see the Leachman et al. literature reference in the Fluid Information window for hydrogen.