.. _definenewmixture: 

******************
Define New Mixture
******************

The Define Mixture dialog provides a means for defining a fluid system consisting of 2 to 20 components. Select the mixture constituents from the list on the left by clicking on the fluid name, and then on the Add button (or simply double click). That fluid then moves from the list on the left to the list on the right. The fluids in the right list become part of the selected fluid system. To remove a fluid from the right list, click on the fluid name and then click the Remove button (or simply double click).

In addition, multiple selections can be made by either holding down the Ctrl key while selecting multiple fluids, or by holding down the Shift key to mark all fluids between the currently marked fluid, and the selected one. You can also use the arrow keys to select a fluid, and press Alt-A to add it. The period or '>' keys will also add a fluid. Removing the fluid can be done with either Alt-R, a comma, or '<'. Fluids can be highlighted by typing in the first few letters of their names; for example, pressing 'pr' will select propane; to get propylene, type 'propy'.

These alternate ways of adding fluids make it easier to find and select a fluid. For example, defining a mixture of R32, R125, R134a, and Propane is quickest by typing the following sequence: 'r3.r125.r134.pr.' If a wrong letter or number is entered, use the backspace, thus if 'r124' is entered in this example, press the backspace and then a '5', and the program will jump to R125.

Clicking the Info button displays key fixed point parameters for the selected pure fluid. More information in given in the :ref:`fluidinformation`  dialog.

The fluid boxes use the same sorting techniques that were set up in the :ref:`purefluid`  dialog and the fluid set defined in the :ref:`specifyfluidset`  dialog.

After the OK button is selected, the :ref:`specifycomposition` window appears, in which the mass or mole fractions of the components must be specified. In addition, the mixture can be given a name and optionally stored for later use.