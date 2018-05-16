.. _preferences: 

***********
Preferences
***********

**Preferences**

The Preferences dialog allows various options to be selected:

If the 'Prompt to save session when closing' option is selected, you will be prompted when the program is terminated to :ref:`save to a file <filesave>`  before closing. This file can then be retrieved using the :ref:`Open <opensession>`  command when the program is run again.

The 'Prompt before deleting row' option asks for confirmation (after either pressing Shift-del or selecting the :ref:`Delete Row <deleterow>`  option while editing a table) before a row is deleted. A row cannot be recovered after it has been deleted.

The 'Ignore all error messages' option will cause all error and warning messages to be ignored that occur during property calculations. While this option may relieve you of having to clear each error message, it may cause confusion when properties are not returned after entering inputs out of range or when the program does not converge. The 'Ignore all warning messages' option will cause all warning messages to be ignored, but will still display the serious error messages.

The 'Copy table headers to clipboard with table data' option can be used to select whether or not the headers at the top of each table are included when :ref:`copying to the clipboard <copytabledata>` .

When the 'Show saturation boundaries in tables' option is selected, a blank line will appear between the single and two-phase state points and the boundary between the liquid and vapor phases.

The steam conversion option will use the conversion 1 cal = 4.184 J when not selected, and the conversion 1 cal = 4.1868 J when selected. The latter value is generally used in the literature with the calculation of water and steam properties. The former value (4.184 J) is generally used with other fluids and mixtures.

In certain applications, such as using Asian settings with Microsoft Windows, the degree sign, the superscript 2, and the superscript 3 may not be properly displayed, causing unit conversions to not work and displaying units with funny symbols. In such cases, the nonstandard characters should be turned off (by clicking on the 'Use nonstandard symbols' option), resulting in the loss of the degree signs. The text '^2' and '^3' will be used in place of the superscript 2 and 3.

The 'Reset bounds when units or fluid are changed' option will reset the starting and ending default values that are displayed when the saturation or isoproperty table menus are brought up after the units or fluid have been changed. The values in the plot menus will also be changed to better default values based on the fluid or units selected. Deselect this option to preserve the bounds that you have set up.

The 'Flip usage of commas and periods in numbers' allows the use of a comma as a decimal point. For the most part, REFPROP will recognize the user's country settings and this option will not be needed.

The 'Add Notes button to graphs' option will add a small command button in the upper left corner of each plot that allows the user to add notes to a particular graph. These notes will be printed out under the plot when File/Print is selected. If this option is deselected, the notes that correspond to each plot will not be lost, but will not be accessible.

The option to 'add a comment column to tables' will add one or more extra columns (up to 10) in each table that can be used to enter comments or user data. The values in these fields will be ignored, but numerical values can be plotted in the same manner as calculated properties. Adding text in each field can aid in labeling each state point, and the size of the comment field can be enlarged as explained in :ref:`Tables <tables>` .

The 'Show options used for analyzing Equations of State' will add the rectilinear diameter to all plots, additional plot items, and the 'Show 2-phase' option for plotting metastable states for pure fluids.

The mixture models used in REFPROP vary by type of mixture (e.g., refrigerant mixtures use different models than hydrocarbon mixtures). The mixture model can be specified by selecting the appropriate radio button in the Preferences menu. Constituents typically found in natural gas are modeled by the latest GERG model (completed in 2004 and extended in 2008). The mixing part of the model (the excess contribution) is similar to that used for the refrigerant mixtures. The pure fluid equations of state have been shortened and differ from the default equations in REFPROP. The calculations using these shorter equations are somewhat faster than the default equations, but are slightly less accurate. If the user wishes to use the shorter equations specified by the GERG-2008 model, the 'Use full GERG-2008 natural gas mixture model' option should be selected. This will result in slightly different values than the default values. In either situation, the mixing interaction parameters remain the same. The documentation for this model was published in the following:

Kunz, O., Klimeck, R., Wagner, W., Jaeschke, M. The GERG-2004 Wide-Range Reference Equation of State for Natural Gases and Other Mixtures. GERG Technical Monograph 15, Fortschr.-Ber. VDI, VDI-Verlag, Düsseldorf, 2007.

Kunz, O. and Wagner, W. The GERG-2008 Wide-Range Equation of State for Natural Gases and Other Mixtures: An Expansion of GERG-2004. J. Chem. Eng. Data, 57(11):3032-3091, 2012.

Calculations from the American Gas Association program for natural gas mixtures can also be made by selecting the 'Calculate mixture properties using the AGA8 equation'. This equation is not valid in the liquid phase or in the extended region near the critical point and users of this model should be aware of the uncertainties in the equation in the various regions where they calculate numbers. The default equations in REFPROP are used to calculate the phase boundaries since the AGA8 model does not allow this calculation.

The 'Use Peng-Robinson equation for all calculations' option switches from the default equations to the less accurate Peng-Robinson equation. This equation is not recommended for general use in REFPROP.

In addition to these options, the number of digits in the tables can be selected on a global basis, rather than individually selecting the number of digits as described in the :ref:`Format and Column Position <formatcolumnposition>`  menu. Changes in the number of digits displayed will be applied to the currently displayed tables if the 'Apply to existing tables' option is selected. The 'Fixed digits' option allows a fixed number of total digits, including those before and after the decimal point. The 'Fixed decimal' option allows a fixed number of digits to be specified to the right of the decimal point. The 'Scientific notation' option allows the number to be displayed in that format.

The font size used in the tables can be specified. The size in previously generated tables will be changed if the 'Apply to existing tables' option is selected. The label font size used in the graphs can also be modified.

The preferences are saved when the :ref:`Save Current Options <savecurrentoptions>`  command is issued. You can restore options at any time with the :ref:`Retrieve Options <retrieveoptions>`  command.


