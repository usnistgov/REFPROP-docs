.. _excel_spreadsheets: 

******************
Excel Spreadsheets
******************

**Excel Spreadsheets**

The REFPROP software includes dynamic link library ('.dll') support that allows a broad variety of applications to take advantage of REFPROP's capabilities. REFPROP is distributed with front-end software that links Microsoft Excel applications to fluid property functions.

The REFPROP Excel front-end is supplied as a Microsoft Visual Basic module. Excel automatically incorporates Visual Basic as a macrofunction execution, scripting and interface utility. When the REFPROP front-end module is imported into an Excel spreadsheet, REFPROP functions become accessible to the user. The proceedure for doing this is described below.

The information given below demonstrates the front end usage; however, the user is not bound to this format; rather, the preferred method would be to write one's own visual basic code that calls the DLL directly. A dedicated module will increase the speed of the application and give the ability to use the REFPROP functions to their fullest.



The following supplementary instructions are intended for users who wish to create and modify their own spreadsheets that utilize the REFPROP functions based on the front-end module. The Excel application included with the software is called REFPROP.xls and is located in the directory where the REFPROP program was installed. Sample :ref:`FORTRAN <sample_fortran_code>`  and :ref:`Visual Basic <sample_visual_basic_code>`  files are also included.

Properties are calculated by calling various functions. For example, the following line would be placed in a cell to calculate the density of argon at 300 K and 10 MPa:

=Density("argon","TP","SI",300,10)

Other properties can be calculated by using any of the following functions:

Temperature
Pressure
Density
CompressibilityFactor
LiquidDensity
VaporDensity
Volume
Energy
Enthalpy
Entropy
IsochoricHeatCapacity (or Cv)
IsobaricHeatCapacity (or Cp)
SpeedOfSound (or Sound)
Quality
HeatOfVaporization (or LatentHeat)
JouleThompson
IsentropicExpansionCoef
IsothermalCompressibility
VolumeExpansivity
AdiabaticCompressibility
AdiabaticBulkModulus
IsothermalExpansionCoef
IsothermalBulkModulus
Viscosity
ThermalConductivity
Prandtl
SurfaceTension
DielectricConstant
MolarMass
EOSMax
EOSMin
MoleFraction
MassFraction
LiquidMoleFraction
VaporMoleFraction
Mole2Mass
Mass2Mole

The first input in the call to the function is the pure fluid name or mixture string. The file name located in the fluids directory where REFPROP was installed should be used as the fluid name (without the .fld extension).

For mixtures, the fluid names and compositions (in mole fractions) of the constituents in the mixture are placed in a single cell as in the following example for dry air:

nitrogen;0.7812;argon;0.0092;oxygen;0.2096

A more convenient way is to use the FluidString phrase to join multiple cells:

=FluidString(A1:A3,B1:B3)

where the fluid names are stored in A1, A2, and A3, and the mole fractions are stored in B1, B2, and B3. The stored mixture files (*.MIX) can also be read by simply replacing the fluid name with the name of the mixture file:

=Enthalpy("R410A.MIX","TD","molar SI",300,5)

The second input to the function is the combination of input properties being sent to the function. Thus, for a given pressure and temperature, the second input would be "PT" (or "TP", depending on the order in which the properties are sent). Other valid inputs include the density (D), energy (E), enthalpy (H), entropy (S), and quality (Q). Valid combinations include: TP, TD, TH, TS, TE, TQ, PD, PH, PS, PE, PQ, DH, DS, DE, and HS. For saturation states, the second input is Tliq or Tvap for a given saturated temperature, Pliq or Pvap for a given saturated pressure, or Dliq or Dvap for a saturated density. Liquid properties are returned when these inputs contain "liq" and vapor properties are returned when "vap" is used.

The third input to the property functions defines the units. This input can be one of the following: "SI", "SI with C", "Molar SI", "E", "cgs", "mks", "M". If left blank, the default is SI. The "SI with C" input can be shorted to just "C". The units that correspond to these inputs are:

<SPAN STYLE="width: 71pt">SI:  </span>K, MPa, kg/m^3, kJ/kg, kJ/kg-K, m/s, uPa-s, mW/m-K, mN/m
<SPAN STYLE="width: 71pt">SI with C:  </span>C, MPa, kg/m^3, kJ/kg, kJ/kg-K, m/s, uPa-s, mW/m-K, mN/m
<SPAN STYLE="width: 71pt">Molar SI:  </span>K, MPa, mol/dm^3, J/mol, J/mol-K, m/s, uPa-s, mW/m-K, mN/m
<SPAN STYLE="width: 71pt">mks:  </span>K, kPa, kg/m^3, kJ/kg, kJ/kg-K, m/s, uPa-s, W/m-K, mN/m
<SPAN STYLE="width: 71pt">cgs:  </span>K, MPa, g/cm^3, J/g, J/g-K, cm/s, uPa-s, mW/m-K, dyn/cm
<SPAN STYLE="width: 71pt">E:  </span>F, psia, lbm/ft^3, Btu/lbm, Btu/lbm-R, ft/s, lbm/ft-s, Btu/h-ft-F, lbf/ft
<SPAN STYLE="width: 71pt">M:  </span>K, psia, g/cm^3, J/g, J/g-K, m/s, uPa-s, mW/m-K, mN/m

For example, the following line would be placed in a cell to calculate the density of argon at 100 F and 250 psia (the result will be in units of lbm/ft^3):

=Density("argon","TP","E",100,250)

The independent variables in the equations of state used in REFPROP are temperature and density. If more than one property is needed, it is best to first determine these quantities from the given set of initial inputs, and then determine the other properties with the temperature and density. This will greatly speed-up the calculation. This is particularly important when properties for pure fluids that are within the two-phase region are calculated. For example, to calculate the energy, enthalpy, and entropy given the pressure and quality of a two-phase system, place the fluid name in cell A1, the pressure in B1, and the quality in C1. Put the following in cells A2 through A5:

=Temperature($A$1,"PQ","SI",$B$1,$C$1)
=Density($A$1,"PQ","SI",$B$1,$C$1)
=Energy($A$1,"TD","SI",$A$2,$A$3)
=Enthalpy($A$1,"TD","SI",$A$2,$A$3)
=Entropy($A$1,"TD","SI",$A$2,$A$3)

The functions LiquidDensity and VaporDensity will return the saturated liquid and vapor densities of a two-phase state. These densities, along with the temperature, can then be used to calculate all other thermodynamic and transport properties at the saturation boundaries using the functions outlined above.

The inputs "Tmelt", "Pmelt", "Tsubl", and "Psubl" return melting line or sublimation line values. To calculate the melting pressure for argon at 90 K, enter:

=Pressure("argon","Tmelt","SI",90)

To calculate the melting temperature, enter "Pmelt" as the second input and the melting pressure as the fourth input.

=Temperature("argon","Pmelt","SI",25)

The critical point or triple point is returned in a similar manner via the inputs "crit" or "trip", along with inputs of the fluid name and the units. The molar mass (molecular weight) is returned using the function MolarMass with an input of the fluid name only. All of these functions are shown in the REFPROP.xls file.


The latest instructions for permanently linking REFPROP to EXCEL are contained on the :ref:`REFPROP FAQ <faq>`  `website <http://www.boulder.nist.gov/div838/theory/refprop/Frequently_asked_questions.htm>`_.


