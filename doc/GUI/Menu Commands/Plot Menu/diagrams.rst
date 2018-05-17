.. _diagrams: 

********
Diagrams
********

Diagrams can be generated for the selected fluid. The types of diagrams that can be plotted include:

* Temperature vs. Entropy
* Temperature vs. Enthalpy
* Temperature vs. Density
* Pressure vs. Enthalpy
* Pressure vs. Density
* Pressure vs. Volume
* Pressure vs. Temperature
* Compressibility Factor vs. Pressure
* Enthalpy vs. Entropy
* Isochoric Heat Capacity vs. Temperature
* Isobaric Heat Capacity vs. Temperature
* Speed of Sound vs. Temperature
* Exergy vs. Enthalpy
* Isothermal Compressibility vs. Temperature
* Viscosity vs. Temperature
* Thermal Conductivity vs. Temperature
* Temperature vs. Composition (for binary mixtures only)
* Pressure vs. Composition (for binary mixtures only)

Each diagram type will allow different combinations. In the case of a pressure vs. enthalpy diagram, lines of constant temperature, density, entropy, and quality can be displayed. To specify plotting isotherms, place a check in the box to the left of the label. You can then specify a range of temperatures to be plotted and/or up to 12 individual isotherms. In addition, values in the two-phase region can also be plotted. Generally, this option is not selected, and a straight line is drawn between the saturated liquid state and the saturated vapor states. For mixtures, showing two-phase values will be very computationally intensive. When plotting isotherms for a pure fluid, the two-phase option works differently from what might be expected: values of the metastable fluid states are shown, both real and inaccessible. However, you should realize that there are virtually no data for metastable states of most fluids, and values shown will be extrapolations of the equations of state. In addition, calculated values can be extremely large, and plotting these values can result in unexpected plots in the two-phase region. See the :ref:`properties`  dialog for additional information.

For cases where multipliers are preferred rather than increments in the 'From...To...Step' inputs, the character '*' can be added in front of the step input. Thus, inputs of 'From: 0.001, To: 1000, Step: \*10' would produce isolines of 0.001, 0.01, 0.1, 1, 10, 100, and 1000. The More/Less button can be selected to include/exclude additional boxes where property values can be individually added.

The starting and ending values of the x and y axis can be modified. These values can be changed later with the :ref:`modifyplot`  command; however, some data may not be calculated beyond the ranges indicated in these boxes, and a new diagram will have to be generated with larger bounds.

Labels identifying the isoproperties are automatically generated if the 'Include labels' option is selected. You can change or delete these text items or add additional text using the :ref:`addlabel`  command. If too many labels are being placed on a plot, the 'Unlabeled lines' option can be used to specify that labels should occur on every other line, every third line, and so on. The appearance of the plot can be modified with the :ref:`modifyplot`  command and with the controls in the :ref:`plotwindow`  window.

The amount of data calculated, resulting in fine or coarse plots, can be selected in the 'Point spacing' option. Several additional options are available to control whether the saturation lines are drawn, the melting line is drawn, and the saturated liquid and vapor states are connected by lines. The 'Swap density for specific volume' option will change the density inputs to volume inputs. The 'Add s and v lines at saturated temperature' option will draw a vapor phase isochore and a vapor phase isentrope for each isotherm that is plotted, using the value of volume and entropy at the saturated vapor state point.

Once a plot has been generated, other data may be superimposed on it using the :ref:`overlayplot`  command.

**Other diagrams**

Other properties can be plotted as well using these same techniques. Under the 'Axis scaling' label in the plot dialog, the x and y properties can be changed by selecting the down arrows and clicking on the desired property. Most of the properties available in the :ref:`properties`  dialog can be plotted on the y axis. Properties allowed on the x axis include temperature, pressure, density, volume, energy, enthalpy, entropy, compressibility factor, exergy, -1/T, and composition. In order to avoid problems where one of the four columns at the top of the plot dialog matches one the properties on the x or y axis, you should carefully select as a starting point one of the diagrams in the Plot pull down menu that contains your x or y property. For example, to generate a plot showing the Prandtl number vs. temperature, you could start with a T-s diagram so that the upper four columns show pressure, density, enthalpy, and quality. If a T-h plot was selected, then the third column would contain entropy instead of enthalpy. Once this is done, the x axis property should be changed to temperature and the y axis property should be changed to the Prandtl number. Even better in this case would have been to select a Cv vs. T plot so that temperature is already placed in the x-axis option. Once the initial plot is setup, you can then go to the Plot/Other Diagrams option to modify your previous settings.