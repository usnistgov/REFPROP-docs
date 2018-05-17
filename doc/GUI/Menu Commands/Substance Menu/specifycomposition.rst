.. _specifycomposition: 

*******************
Specify Composition
*******************

The Specify Composition dialog serves two purposes. First, it provides a means of specifying the composition of a mixture. The composition can be specified in terms of either mass or mole fractions. The choice is made by clicking in the box containing the words 'Mass fraction' or 'Mole fraction' followed by clicking on the name of the desired base. If you click the mouse on the name of a pure component, the :ref:`fluidinformation` dialog appears, providing property information for that fluid.

The mass or mole fractions must be entered for each component and they must sum to 1 (or 100 if percentages are used) if the 'Normalize compositions to one' checkbox is not selected. If the 'Normalize compositions to one' checkbox is selected, the value of each mass or mole fraction is set to the entered value divided by the sum of the values. This option is most convenient if you want to specify the composition of a mixture by specifying the mass of each component.

The second function served by this dialog provides an opportunity to store the fluid system so that it can later be selected with the :ref:`predefinedmixture` command. The name appearing in the Predefined Mixture window and the :ref:`statusline` at the bottom of the screen is entered in the 'Mixture name' field. Click the Store button to save this information.

The Add or Remove Fluid buttons allow you to enter or delete fluids in the list without having to start back at the :ref:`definenewmixture` dialog. The Add Fluid button will bring up the pure fluid list and the desired component should be selected. To remove a fluid, put the cursor in the composition box for that fluid and press the Remove Fluid button. You will be prompted for confirmation before the fluid is removed.

The Copy button places the fluid names and compositions (separated by tabs) onto the clipboard so that they can be pasted into other applications. The Paste button will paste the values that are on the clipboard into the composition boxes. The paste function is smart enough to search through multiple columns in the information stored on the clipboard for a column that contains numbers that sum to 1. For example, the copy button pastes both the fluid names and compositions to the clipboard. If the paste button is then pressed, the program realizes that the first column does not contain compositions and will paste the second column into the composition boxes.