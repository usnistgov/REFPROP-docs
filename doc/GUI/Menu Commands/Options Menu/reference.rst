.. _reference: 

***************
Reference State
***************

**Reference State**

*When large differences in enthalpy and entropy occur between REFPROP and tables of properties given in handbooks, please note:*

The absolute values of enthalpy, entropy, and energy at a single state point are meaningless. It is only the difference between two different state points that matter. Thus, the value for a single state point can be set to any arbitrary value. Many handbooks set the arbitrary state point so that the values of these properties are positive for most liquid or gas states. You can change the values of the arbitrary state points by going to the Options/Reference State menu. Your choice of options can be permanently saved in the graphical interface by selecting Options/Save Options, and then saving the options under the file name 'defaults.prf'.

To change the default in the Excel file, press Alt-F11 to bring up the VB code. If the code does not appear, make sure the project explorer is visible (View/Project Explorer), then click on modules, and then on module1. Then search for the call to SETREF, and change the second input from 2& to 1&. More information on this can be found in your REFPROP\Fortran directory in the file SETUP.FOR under the SETREF subroutine.

The reference states for enthalpy and entropy are entered in the Reference dialog. There are three common choices for the reference state on which the values of enthalpy and entropy are based. These three common choices are:

1. Setting enthalpy and entropy to zero for the saturated liquid at the normal boiling point (designated as NBP).

2. Setting enthalpy and entropy to zero for the saturated liquid at -40 °C (designated as ASHRAE).

3. Setting enthalpy to 200 kJ/kg and entropy to 1.0 kJ/(kg-K) for the saturated liquid at 0 °C (designated as IIR).

In addition, the reference state can be set manually by specifying values of the enthalpy (h) and entropy (s) at arbitrary values of temperature (T) and pressure (P).

When working with mixtures, the default setting can be used for each pure fluid, or the reference state values of enthalpy and entropy can be specified at the currently defined composition.

The exergy reference state and definition can be selected based on the user's preference.

The reference state choices are saved with other :ref:`preferences <preferences>`  when the :ref:`Save Current Options <savecurrentoptions>`  command is selected. It is restored to a previously saved option with the :ref:`Retrieve Options <retrieveoptions>`  command or :ref:`Open <opensession>`  command.


