.. _specifiedstatepoints: 

**********************
Specified State Points
**********************

**Specified State Points**

The blank grid allows you to select two independent properties to fix the state of the fluid. The remaining thermodynamic and transport properties corresponding to this fixed state will then be calculated.

The values of the independent properties can be entered in three ways (in addition to :ref:`reading data from a file <readdata>` ), as listed below.

1.  Values can be simply typed into the cells of the property table.

2.  Values can be automatically entered in a systematic manner by right-clicking on the header at the top of the column. This action brings up the :ref:`Automatic Data Entry <formatcolumnposition>`  window.

3.  Values can be pasted into the independent variable cells from another application, such as a spreadsheet. Copy the values to the clipboard using the other application's Copy command. Then, click the mouse in the first cell in the REFPROP table and select the :ref:`Paste <paste>`  command.

**Using the Specified State Points Table**
Whether the independent properties are read from a file or entered manually, as soon as two valid input properties have been entered, the table will calculate the remaining properties and display them in the appropriate columns. Note that you can then change the inputs or select new inputs (which causes the calculated values in that row to be erased) and repeat the calculation process.

Saturation or melting-line states can be calculated by adding the letters 'l', 'v', or 'm', respectively, before or after the value of temperature, pressure, density, enthalpy, or entropy. Note that 'm' returns liquid properties at the solid-liquid boundary. REFPROP does not calculate solid properties. In the case where 'l' or 'v' is entered, and there is only one valid liquid or vapor state point, that point is returned regardless of whether or not it is in the liquid or vapor state. If a liquid density is entered with a 'v', the liquid state is calculated internally; however, the vapor state is returned. The same is true for a vapor state entered with 'l'. The properties at the critical point can be calculated easily by entering 'cr', and the properties at the triple point can be calculated by entering 'tr' (liquid properties can be obtained with 'trl' and vapor properties with 'trv').

For state points that are double valued (see the :ref:`Cautions <cautions>`  menu for more information), the character '&lt;' or '&gt;' can be added to the number (before or after) to find the lower or upper root, respectively. These same characters can also be used to find metastable fluid states for temperature and pressure inputs. For example, the saturation pressure for nitrogen at 100 K is 0.778 MPa. Inputs of 100 K and 0.777 MPa will return a vapor state, but inputs of '100' for temperature and '0.777&gt;' for pressure will return a metastable liquid state.

For mixtures, the composition of the mixture can be entered on a line, but this must be done BEFORE the two valid state points are entered. For convenience, the Specified State Points (varying composition) command can be chosen. This command places the composition fields at the beginning of the table (and activates them if they were not selected in the :ref:`properties <properties>`  menu). The composition fields can be moved permanently by selecting the :ref:`property order <propertyorder>`.

The position and format of any column can be changed, if desired, by right-clicking on the :ref:`column header <formatcolumnposition>`.


