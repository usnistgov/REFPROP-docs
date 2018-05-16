.. _saturationpointsequilibrium: 

**********************************
Saturation Points (at equilibrium)
**********************************

**Saturation Points (at equilibrium)**

The blank grid allows you to select either the saturated temperature, pressure, or density to fix the state of the fluid. The remaining thermodynamic and transport properties corresponding to this saturation state will then be calculated. For mixtures, the properties of the corresponding phase will be in equilibrium with the specified phase. The 'Composition' option should be selected (see :ref:`Properties <properties>` ) to show the composition of the equilibrium phase.

Use the :ref:`Saturation Points (bubble and dew points at same composition) <saturationpointsbubbledew>`  table to calculate vapor and liquid saturated properties where the phases are at the same temperature, pressure, and specified composition. The liquid and vapor states in this table are not in equilibrium with each other.

The values of the independent properties can be entered in three ways (in addition to :ref:`reading data from a file <readdata>` ), as listed below.

1.  Values can be simply typed into the cells of the property table.

2.  Values can be automatically entered in a systematic manner by right-clicking on the header at the top of the column. This action brings up the :ref:`Automatic Data Entry <formatcolumnposition>`  window.

3.  Values can be pasted into the independent variable cells from another application, such as a spreadsheet. Copy the values to the clipboard using the other application's Copy command. Then, click the mouse in the first cell in the REFPROP table and select the :ref:`Paste <paste>`  command.

**Using the Saturation Points (at equilibrium) Table**
Whether the independent properties are read from a file or entered manually, as soon as a valid input property has been entered, the table will calculate the remaining properties and display them in the appropriate columns. Note that you can then change the input or select a new input (which causes the calculated values in that row to be erased) and repeat the calculation process.

For mixtures, the composition of the mixture can be entered on a line, but this must be done BEFORE the input property is entered. This can allow you to vary the composition and view the effect while holding temperature or pressure constant. The composition fields can be moved permanently to the beginning of the table by selecting the :ref:`property order <propertyorder>`  to make it easier to enter the values.

When entering temperatures or pressures, it is important that the value is placed in the appropriate column. Placing the temperature in the 'Liquid phase temperature' column will calculate a bubble point with its corresponding vapor state at some equilibrium condition. Entering the temperature in the 'Vapor phase temperature' column will calculate a dew point with its equilibrium liquid condition. These two lines will be completely different, and can be confusing if the compositions are not displayed.

The position and format of any column can be changed, if desired, by right-clicking on the :ref:`column header <formatcolumnposition>` .


