.. _saturationtables: 

*****************
Saturation Tables
*****************

**Saturation Tables**

There are several different types of saturation tables. For a pure fluid, when the Saturation Tables command is selected, the type of calculations to be made is specified by selecting one item from each list displayed. After the OK button is selected, another window appears in which the range and increment of the property to be varied are specified. After the second OK button is selected, calculations are initiated and a table displaying the results appears. The columns are initially shown in a preselected order and with a default format. The format and column position of each column can be changed by right-clicking in the column header to bring up the :ref:`Format and Column Position <formatcolumnposition>`  dialog.

For mixtures, the window contains additional items that allow you a variety of methods for calculating saturation conditions. The first option in the 'Composition basis' menu ('Liquid and vapor at the same composition') calculates state points that are NOT in equilibrium with each other. The composition of the liquid and vapor state points are the same as that of the specified mixture, and at the specified temperature or pressure. The second two options calculate properties that are in equilibrium, but that will be at different compositions (except in the case of azeotropes, or azeotrope-like mixtures). The composition should be displayed (see :ref:`Properties <properties>` ) to view the full state of the system. Different properties can be selected to vary in the table. The first four items that can be selected under the 'Vary' label generate points at the composition of the mixture; the last two items calculate properties at different compositions and have no connection to the composition specified when the system was set up. The red dots in the example picture indicate which points will be calculated. The gray lines connect points that will be displayed on the same row of the table.

If the composition of the mixture is to be varied, an additional window will appear. The temperature is entered at the upper left. The composition will be linearly varied from the condition indicated in the 'Initial' column to that in the 'Final' column using the number of points indicated at the upper right. With 11 points, the composition of this binary system is varied from pure component 1 to pure component 2 with increments of 0.1 in mole fraction.

For solid-fluid saturation calculations (sublimation or melting), the properties displayed are the equilibrium fluid phase for either the liquid or the vapor. Properties for the coexisting solid are not available.


