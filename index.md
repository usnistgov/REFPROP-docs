---
layout: default
title: Home
---
# Answers to Frequently Asked Questions

The following information gives answers to some of the most frequently asked questions concerning [the REFPROP program](https://www.nist.gov/srd/nist23.cfm). _To download any of the files listed below, right-click on the file and select **Save Target As...** and then add the file to your Refprop or other appropriate directory._ Sections with new information added during the last several months are identified with a «. For questions not answered here, please see [the user's guide](http://www.nist.gov/srd/upload/REFPROP9.PDF).

«There are a few changes in versions 9.0 and 9.1 that may confuse you when you first run the program. The number of fluids will appear to be much shorter. Look under Substance/Specify Fluid Set and you will see the ability to select a set of fluids rather than list all of them. In the Options/Properties menu, the composition box is now missing from the Thermodynamic tab; you will find it in the Mixtures tab along with other properties that are generally displayed only for mixtures. When copying data from a table, the headers are no longer copied with the data. If you like that feature, select it in Options/Preferences, then save the defaults.prf file under Options/Save Current Options. Concerning the Fortran files and the calling routines to the DLL, all of the inputs/outputs to the routines are the same as those to 8.0 so your own code will not have to be updated. Just replace your old DLL with that from 9.0 or 9.1 and you will be set to go (of course you will also need the new FLD files and the HMX.BNC file).

**General Questions**

1. [Getting Help](#getting-help)
2. [Installation Problems](#installation-problems)
3. [REFPROP is a Program, not a Database Containing Measurements](#refprop-is-a-program-not-a-database-containing-measurements)
4. [Referencing the REFPROP Program in Publications](#referencing-the-refprop-program-in-publications)
5. [Updates to Version 9.1](#updates-to-version-91)
6. [Help File](#help-file)

**Using the Program**

6. [Reference States (enthalpy and entropy differences)](#reference-states-enthalpy-and-entropy-differences)
7. [Multiple and Metastable States](#multiple-and-metastable-states)
8. [Intro to Pure Fluids and 2-Phase States](#intro-to-pure-fluids-and-2-phase-states)
9. [Intro to Mixtures and 2-Phase States](#intro-to-mixtures-and-2-phase-states)

**Programming**

10. [Changing Fluids and Calling SETUP Multiple Times](#changing-fluids-and-calling-setup-multiple-times)
11. [Calculation of the Critical Point and Saturation States in the Critical Region](#calculation-of-the-critical-point-and-saturation-states-in-the-critical-region)
12. [Calculation of Phase Diagrams for Plotting Purposes](#calculation-of-phase-diagrams-for-plotting-purposes)
13. [FLSH Routines and Metastable States](#flsh-routines-and-metastable-states)

**Error Messages**

14. [Convergence Failures and Forcing Phase Calculations](#convergence-failures-and-forcing-phase-calculations)
15. [Mixture Error Messages](#mixture-error-messages)

**Fluids**

16. [GERG-2008 Equation of State for Natural Gas Mixtures](#gerg-2008-equation-of-state-for-natural-gas-mixtures)
17. [HFO-1234yf, 1234ze(E), 1234ze(Z), 1233zd(E), and Refrigerant Mixtures](#hfo-1234yf-1234zee-1234zez-1233zde-and-refrigerant-mixtures)
18. [Humid Air](#humid-air)
19. [Mixture Models](#mixture-models)
20. [Solids](#solids)
21. [Transport Properties for Nitrogen, Oxygen, Argon, and Air](#transport-properties-for-nitrogen-oxygen-argon-and-air)
22. [Transport Properties for Pseudo-pure Fluids; Adding Pure Fluids to a Mixture Setup](#transport-properties-for-pseudo-pure-fluids-adding-pure-fluids-to-a-mixture-setup)
23. [Required Fluids for Distribution](#required-fluids-for-distribution)

**Linking with other Applications**

[This part has moved, click here to go to the new site](https://github.com/usnistgov/REFPROP-wrappers)

## Getting Help

Before contacting us, please look in the Help file – most answers can be found there. If you need to contact us regarding questions that are not answered below, do not send separate emails to those of us that support this work. Rather, include each person in the same email so that it is not necessary for each of us to respond to your question. This will free up resources to develop better products.

Furthermore, when you do report problems with the use of REFPROP, here is information that is crucial for us to know to be able to help you:

- What version of REFPROP do you use?
- What operating system do you use (windows, OSX, linux, etc.)?
- What exactly did you do to cause the problem you see?
- What error message do you get? (The comment "it doesn't work" doesn't help us help you). Screenshots of the failure are very helpful.

Please send questions to Eric Lemmon: <a href="mailto:eric.lemmon@NIST.gov">eric.lemmon@nist.gov</a>

If you send a question and do not receive a response within several days, it is quite likely that your email did not make it or that my email was removed by your system administrators as spam or junk mail.  I try to respond to all emails within two days, so please write/call again if you do not receive a response.)


## Installation Problems.
In some applications where calculations fail after installing versions 9.0 or 9.1, the old
DLL from version 7.0 or 8.0 may be hiding in your ``Windows\System32`` directory. Open up this directory and search for Refprop.dll. If you find it, delete it (it should never be stored in the ``Windows`` directory). The new one belongs in the Refprop directory along with the executable.

If one of the following error messages appears when the graphical interface is launched:
```
run-time error 339
component MSHFLXGD.OCX
or one of its dependencies not correctly registered:
a file is missing or invalid
```
or
```
component COMDLG32.OCX or one of its dependencies not correctly registered:
```

check to see if you have a firewall or antivirus software that can be turned off.&nbsp; Deactivating these will often allow successful installs, especially on Vista machines.&nbsp; If this fails or is not an option, then >download the corresponding file from the link below and save it in your ``Windows\System32`` directory on 32 bit machines or to your ``Windows\SysWOW64`` directory on 64 bit machines. 

- <a href="mshflxgd.ocx">MSHFLXGD.OCX</a>
- <a href="COMDLG32.OCX">COMDLG32.OCX</a>

In some cases where you are not allowed to be the administrator on a machine, this message will appear because it cannot access the System32 directory. Try placing the file in your Windows directory to get the program to work.

If the error message continues, you will need to register the file by running
the appropriate command below for your system and the missing file:

32-bit computers:
```
regsvr32 c:\Windows\system32\comdlg32.ocx
regsvr32 c:\Windows\system32\mshflxgd.ocx
```

64-bit computers:
```
regsvr32 c:\Windows\SysWOW64\comdlg32.ocx
regsvr32 c:\Windows\SysWOW64\mshflxgd.ocx
```

If an error message occurs referencing the file REFPROP.MSI, try the following: Press your Start button, and then click on "Run …". Type in Regedit. If it does not start at the top of registry, scroll to the top and click on "My Computer". Search for "Refprop 8.1.msi", or whatever msi file it is complaining about in the install error message. You should find something like ``HKEY_CLASSES_ROOT\ Installer\ Products\ 6398724E8B370524FA88122E26945D8F``. For every occurrence of the item in the registry, you should either rename or delete it. To rename, simply add an underscore in the sequence of numbers, such as "_6398724...". Then try reinstalling the program.

## REFPROP is a Program, not a Database Containing Measurements
The REFPROP "database" is actually a program and does not contain any experimental information, aside from the critical and triple points of the pure fluids. The program uses equations for the thermodynamic and transport properties to calculate the state points of the fluid or mixture. These equations are the most accurate equations available worldwide. A link to one of these equations for R-125 is given below. Their high accuracy is obtained through many coefficients in the equations, and thus the calculation speed will be slower than other equations such as the Peng-Robinson cubic equations. The equations are generally valid over the entire vapor and liquid regions of the fluid, including supercritical states; the upper temperature limit is usually near the point of decomposition of the fluid, and the upper pressure (or density) limit is defined by the melting line of the substance.

- [Equation of State for HFC-125](R125.PDF)

## Referencing the REFPROP Program in Publications.
The following reference can be used to cite the REFPROP program in publications:

Lemmon, E.W., Huber, M.L., McLinden, M.O.&nbsp; NIST Standard Reference Database 23:&nbsp; Reference Fluid Thermodynamic and Transport Properties-REFPROP, Version 9.1, National Institute of Standards and Technology, Standard Reference Data Program, Gaithersburg, 2013.

Or in BibTeX form:
```text
@Misc{LEMMON-RP91,
  Title                    = {{NIST Standard Reference Database 23: Reference Fluid Thermodynamic and Transport Properties-REFPROP, Version 9.1, National Institute of Standards and Technology}},
  Author                   = {E. W. Lemmon and M. L. Huber and M. O. McLinden},
  Year                     = {2013},
  Doi                      = {http://dx.doi.org/10.18434/T4JS3C},
  Url                      = {https://www.nist.gov/srd/refprop}
}
```

Additionally, users should cite the reference for either the equation of state
or the transport equations used in their work, for example, if you used
calculations for CO<sub>2</sub>, you will find the reference for the equation
of state under the Options/Fluid Information option in Refprop and you should
cite the reference given under that option, like this:

Span, R. and Wagner, W., J. Phys. Chem. Ref. Data, 25(6):1509-1596, 1996.

## Updates to Version 9.1
Version 9.1 is now the current release. Several problems in version 9.0 (listed below) were found after its release, and these have all been corrected in 9.1. There are also a few issues with 9.1. If these affect you, please let us know and we will send you the update.

### Issues with Refprop 9.0

1. The calculation of d<sup>2</sup>p/dT<sup>2</sup> at constant density is incorrect.
2. The reference state for R1234yf and R1234ze(E) should be changed from NBP to IIR. Updated files are given further below.
3. Calculation of isobars for pure fluids at pressures less than the triple point pressure may incorrectly return properties in the liquid phase rather than the vapor phase.
4. The manual REFPROP9.PDF and the UserInformation sheet in Refprop.xls incorrectly listed isobutene instead of isobutane for R430A. (However, the graphical interface and mixture file are correct.)

### Issues with Refprop 9.1

1. Inputs of enthalpy or entropy may not converge, or will converge to the wrong phase.

## Help File
The most recent help file from Refprop is available below. You should download it to your
machine before launching it, otherwise the help file will appear blank.

- [REFPROP.CHM](REFPROP.CHM)

# Using the Program

## Reference States (enthalpy and entropy differences)

For differences in enthalpy and entropy between the Refprop graphical interface and the Refprop Excel sample spreadsheet, or for differences in enthalpy and entropy between Refprop and tables of properties given in handbooks:&nbsp;

The absolute values of enthalpy, entropy, and energy at a single state point are meaningless.&nbsp; It is only the difference between two different state points that matter.&nbsp; Thus, the value for a single state point can be set to any arbitrary value.&nbsp; Many handbooks set the arbitrary state point so that the values of these properties are positive for most liquid or gas states.&nbsp; The user can change the values of the arbitrary state points by going to the _Options/Reference State_ menu.&nbsp;

For mixtures, there are additional options that can be set to affect the manner in which these properties are calculated.&nbsp; The preset values sent out with Refprop 7.0 are different between the graphical interface and the Excel file.&nbsp; In the _Options/Reference State_ menu, there are two choices at the bottom of the menu on the far right.&nbsp; By changing this option, the two programs will then return the same values.&nbsp; This option can be permanently saved in the graphical interface by selecting _Options/Save Options_, and the saving the options under the file name defaults.prf.&nbsp; To change the default in the Excel file, press Alt-F11 to bring up the VB code.&nbsp; If the code does not appear, make sure the project explorer is visible (_View/Project Explorer_), and then click on modules and then on module1.&nbsp; Search for the call to SETREF, and change the second input from 2&amp; to 1&amp;.&nbsp; More information on this can be found in your Refprop\Fortran directory in the file SETUP.FOR under the SETREF subroutine. 

To permanently change the default setting for a pure fluid, edit the fluid file and look at the 14<sup>th</sup> line of the file, which will appear similar to this:
```
IIR !default reference state
```
Remove this line and add two lines in its place, similar to the following: 
```
OTH !default reference state
300.0 1.0 10000.0 100.0  !tref, Pref, Href, Sref
```
These lines will set the enthalpy to 10000 J/mol and the entropy to 100 J/mol-K at 300 K and 1 kPa.&nbsp; These values can be changed to any other desired values.

## Multiple and Metastable States.

There are cases where an input state point can result in two separate valid states.&nbsp; The most common is temperature-enthalpy inputs.&nbsp; Viewing a P-H diagram (or a T-H diagram with very high pressures) will help show how there can be two valid states points for a given input.&nbsp; For example, nitrogen at 140 K and 1000 J/mol can exist at 6.85 MPa and at 60.87 MPa.&nbsp; When this situation occurs, Refprop returns the state with the higher density.&nbsp; For these state points , the character '&lt;' or '&gt;' can be added to the number (before or after) to find the lower or upper root, respectively.&nbsp; In the Excel sample file, the use of these characters was added after the release of version 8.0; the new example file REFPROP.XLS (given in the Excel section) contains new code and an example of its use. These same characters can also be used to find metastable fluid states for temperature and pressure inputs.&nbsp; For example, the saturation pressure for nitrogen at 100 K is 0.778 MPa.&nbsp; Inputs of 100 K and 0.777 MPa will return a vapor state, but inputs of '100' for temperature and '0.777&gt;' for pressure will return a metastable liquid state.&nbsp; See [below](#convergence-failures-and-forcing-phase-calculations) for additional information about the use of the '&gt;' and '&lt;' symbols.</p>

## Intro to Pure Fluids and 2-Phase States. 
Defining the state of a fluid normally requires two inputs, such as pressure-temperature, temperature-enthalpy, pressure-enthalpy, and so forth. This is true for the single-phase states and for two-phase solutions with mixtures of fluids. (Some inputs may have [two solutions](#multiple-and-metastable-states), this was described earlier.) For pure fluids, using inputs of pressure and temperature is not sufficient to describe the state of the fluid since both remain constant between the liquid and vapor states. Some other property, such as quality, enthalpy, or density, is required to specify the two-phase state point for the pure fluid. Once the quality is known, some of the other thermodynamic properties can be calculated with the equation _M=q*M<sub>vap</sub> + (1-q)*M<sub>liq</sub>_, where _M_ is the property of interest and _q_ is the quality. There are several properties that cannot be calculated this way, including the heat capacities, the speed of sound, and the transport properties. These quantities are undefined in the two-phase region for any fluid, except _Cv_, which is defined very differently than one would expect. There are some people who use a different formula to calculate the speed of sound in the two phase, but it is applicable only in certain specific applications. In these situations, it is best to consider the properties of the liquid and of the vapor separately, and how they interact with the application being developed.

As an example, consider _Cp_, which could be calculated from any equation of state using the quality, but thermodynamically is not defined for a two-phase mixture.&nbsp; _Cp_ is the heat capacity along an isobaric process and is equal to d_H_/d_T_|_p_. Since pressure and temperature do not change across the two phase for a pure fluid, then that means _Cp_ would be equal to infinity because the heat capacity changes but the temperature does not, thus the definition makes it thermodynamically impossible to calculate it.&nbsp; The only place that _Cp_ can be infinity is at the critical point.

## Intro to Mixtures and 2-Phase States.
Dealing with saturation or 2-phase states in Refprop can be a bit confusing when first using the program. The text and pictures given below address some of these issues to help users better understand how to obtain properties from the program.

As an example, consider the methane/ethane system with a molar composition of 50% methane and 50% ethane. For mixtures in the 2-phase (or at saturation), it is always best to turn on the composition columns (under Properties/Mixtures/Composition). For saturation states, bring up a saturation table [under Calculate/Saturation Points (at equilibrium)]. The table shows two entries for each property. It is very important to place the known property under the correct column. For example, the input property for bubble points (liquid state) should be placed under the “Liquid” column; dew points (vapor state) should be placed under the “Vapor” column. An example picture is given below. On the first line, 150 K was entered under the liquid column. This calculated a liquid bubble point pressure of 0.552 MPa. The liquid phase mole fractions show the input composition of 0.5/0.5. The vapor phase mole fractions show that the first bit of vapor will have a composition of 0.987/0.013. In the second row, 150 K was entered in the vapor column, producing a dew point pressure of 0.019 MPa. The vapor mole fractions show the input composition of 0.5/0.5. The first drop of liquid to form will have a mole fraction of 0.0074/0.9926.

<img src="http://www.boulder.nist.gov/div838/theory/refprop/Frequently_asked_questions_files/image002.jpg">

For 2-phase states, turn on the option labeled “Bulk, liquid, and vapor properties” under Options/Properties. Then bring up a table under Calculate/Specified State Points. The information obtained above shows that pressures for 2-phase state points at 150 K will lie between 0.019 and 0.552 MPa. Enter 150 K in the temperature column and 0.3 MPa in the pressure column. The program will then calculate the 2-phase point. The output shows that the overall composition of the mixture is still 0.5/0.5. The composition of the fluid in the liquid phase will be 0.246/0.754 and that of the vapor phase will be 0.972/0.028. This is shown in the picture below.

<img src="http://www.boulder.nist.gov/div838/theory/refprop/Frequently_asked_questions_files/image006.jpg">

The Excel sample spreadsheet included in the Refprop directory shows an example for the mixture R410A (between rows 70 and 98).

# Programming

## Changing Fluids and Calling SETUP Multiple Times
Calling SETUP (or SETUPdll) many many times can result in a memory loss error and in a substantial increase of computation speed. In many situations, it is better to load all of the fluids at the start of the program, calling SETUP only once. You can then switch between fluids through the use of calls to SETNC and PUREFLD. The example below shows how this can be done for a mixture combined with several pure fluids. If two different mixtures are required, load all fluids and set the composition to 0 for those fluids not involved in a particular application. This could easily be done by using two different arrays for the composition.

- <a href="EX-MULTI.FOR">EX-MULTI.FOR</a>

## Calculation of the Critical Point and Saturation States in the Critical Region
The calculation of saturation states requires complex algorithms and significant processor time. Version 9.1 introduced the subroutine SATSPLN, which can be called directly after the call to SETUP, and generates spline curves that represent the various properties that are required as initial guesses to the saturation algorithms in order to increase convergence and speed. This new subroutine, however, can take several seconds to implement, and should only be done once at the very beginning. If the composition of the fluid changes significantly, and if you notice problems with convergence, you may need to call it again with the new composition. Although the routine gives estimates only for saturation states, single phase calculations will also be much faster since a call to the saturation routine is required to determine the phase of the input state. The routine is called like this:
```
call SATSPLNdll (x, ierr, herr, 255)
```
(without the “dll” and 255 if calling directly from FORTRAN). Once the splines are generated, you can call the CRITP, MAXT, and MAXP routines to get the critical point and maximum values along the saturation lines (see the SAT_SUB.FOR file for details). The new subroutine SATGV can be called when the SATT, SATP, or SATTP routines fail in the critical region. For graphing the saturation lines without the need for states at any specific temperature or pressure, the SATGV routine can be called with density as the input, ranging from very low values in the gas phase, through the critical region, and then to high densities in the liquid.

In Excel or MATLAB, the call to SATSPLN is included in the code, but is deactivated. To activate this call, enter the code (press Alt-F11 in Excel) and search for this subroutine in the file (under “Modules” in Excel). Then read the comments above the line and activate the routine by removing the first character on that line. You may need to exit and restart Excel or MATLAB for this to work.

## Calculation of Phase Diagrams for Plotting Purposes.
The calculation of the entire phase diagram can be difficult with the routines that require either temperature or pressure as inputs due to the second root in the retrograde region. An alternative routine called SATGV is available that makes this process simple through the use of density as the input; see the file Manual.txt in your Refprop\Fortran directory for a list of the inputs and outputs. In order to use this routine, you must first call subroutine SATSPLN, [see the details above](#calculation-of-the-critical-point-and-saturation-states-in-the-critical-region). Subroutine SATGV can then be called like this:
```
call SATGV (t,p,z,vf,d,1,6,1,rhox,rhoy,x,y,ierr,herr)
```
The inputs are composition in the z array and density (either vapor or liquid phase) in the variable d. The variable vf is double precision and should be set to 1.0. The routine will then return the temperature and pressure at this density. To obtain data points for the entire phase diagram, call this routine starting at a very low density in the vapor phase, and slowly increment the density until you are deep in the liquid phase at low temperatures. The other outputs are not necessary for this application.

## FLSH Routines and Metastable States.

For subroutines such as ENTHAL, ENTRO, CVCP, etc., where temperature and density are the input properties, the output property data will differ from those returned when using routines such as PHFLSH or TPFLSH when in the two-phase region.&nbsp; Any routine (except TDFLSH) that uses temperature and density as inputs will return what appears to be erroneous results in the two-phase region.&nbsp; These results&nbsp;actually show calculations directly from the equation of state without taking into account the fact that the mixture has split into two phases.&nbsp; The results would be valid for such situations where a substance is heated beyond its boiling point (a metastable state), but without boiling (such as water in a glass container being heated in a microwave).&nbsp; The results eventually end up at the spinodal, beyond which it is no longer possible to increase the temperature without boiling the liquid.&nbsp; Thus, for typical results these routines should never be used for two-phase calculations, rather the FLSH routines should be called.&nbsp; The flash routines return the properties in the liquid and vapor states, and these can be used to call routines such as THERM, CVCP, TRNPRP, etc., with the associated liquid or vapor density at the saturated temperature.

# Error Messages

## Convergence Failures and Forcing Phase Calculations.

When using mixtures, error messages will sometimes be reported when Refprop fails to converge during an iteration, usually during the calculation of a VLE state close to the critical point.&nbsp; In some situations you may know that the point is in the single phase and wish to force the calculation in spite of the error message.&nbsp; This can be done with the '&gt;' and '&lt;' symbols.&nbsp; When one of these is attached to a number in the Specified State Points table, Refprop will assume that the point is in the liquid phase when '&gt;' is attached and in the vapor phase when '&lt;' is attached.&nbsp; Care must be taken because metastable states will be returned in the point is in the two phase.&nbsp; When a state point is above the critical point but Refprop reports a nonconvergence, you can use either of these symbols to force the calculation.&nbsp; For example, a 0.5/0.5 mixture of methane/propane will report a nonconvergence at 300 K and 10 MPa.&nbsp; A P-rho diagram shows that the point is above the critical pressure.&nbsp; Entering '300' for temperature and '10&gt;' for pressure will return the valid state point at 10.826 mol/l. For programming convergence errors, see [above](#calculation-of-the-critical-point-and-saturation-states-in-the-critical-region).

## Mixture Error Messages
The error message &quot;<span style='color:red'>No mixture data are available for one or more binary pairs in the specified mixture. The mixing parameters have been estimated.</span>&quot; (message #-117) occurs when an interaction parameter for two different fluids is not available in the program.&nbsp; The most common reason for this occurrence is a lack of experimental data to describe VLE, densities, and so forth for the binary pair.&nbsp; In other situations, such as many mixtures with water, interaction parameters have not been fitted to the REFPROP model even though data exist.&nbsp; An estimation scheme is available in the program to approximate one of the interaction parameters that helps improve bubble and dew point pressures.&nbsp; This error message indicates that you should be aware that calculated properties are estimates only.&nbsp; For similar fluids, especially among the refrigerants, the scheme works fairly well.&nbsp; It breaks down with dissimilar fluids and eventually the scheme will produce large interaction parameters and will report the error message&nbsp; &quot;<span style='color:red'>No mixture data are available for one or more binary pairs in the specified mixture. The mixture is outside the range of the model and calculations will not be made.</span>&quot;

# Fluids

## GERG-2008 Equation of State for Natural Gas Mixtures.
The current equation of state for calculating the properties of natural gas mixtures is the GERG-2008 equation (GERG is the European Gas Research Group). This equation is based on an excess Helmholtz energy approach using pure fluid equations of state (either those specified by GERG, or the current standards that have slightly higher accuracies) and a mixture model that specifies the excess contribution. The 2008 version is an extension of the 2004 version, containing the additional fluids nonane, decane, and hydrogen sulfide in addition to methane, nitrogen, carbon dioxide, ethane, propane, n-butane, isobutane, n-pentane, isopentane, n-hexane, n-heptane, n-octane, hydrogen, oxygen, carbon monoxide, water, helium, and argon. The 2008 edition also replaced the pure fluid equations of state for isopentane and carbon monoxide with published versions. These two models are fully described in the following publications:

Kunz, O. and Wagner, W., The GERG-2008 Wide-Range Equation of State for Natural Gases and Other Mixtures: An Expansion of GERG-2004, to be submitted to J. Chem. Eng. Data, 2012.

Kunz, O., Klimeck, R., Wagner, W., and Jaescke, M., The GERG-2004 Wide-Range Equation of State for Natural Gases and Other Mixtures: GERG Technical Monograph 15 and Fortschr.-Ber. VDI, Reihe 6, Nr. 557, VDI Verlag, Düsseldorf, 2007. [link to PDF](http://www.gerg.eu/public/uploads/files/publications/technical_monographs/tm15_04.pdf)

In the Refprop 9.1 program, the natural gas equation of state has been expanded to include ethylene, propylene, methanol, ethanol, toluene, benzene, cyclohexane, sulfur dioxide, ammonia, dodecane, acetone, and butylene. When selecting the option to use the full GERG-2008 equation of state (either through the GUI or by calling the “GERG2004” subroutine), the use of these additional fluids is still allowed. This is not the same as when the AGA-8 equation of state is selected, in which case only the original 21 fluids (same as those in the GERG-2008 model) are allowed.

## HFO-1234yf, 1234ze(E), 1234ze(Z), 1233zd(E), and Refrigerant Mixtures.
Equations of state are now available for these fluids. The fluid files are located below and should be placed in your ``Refprop\Fluids`` directory. The fluid files included in version 9.0
incorrectly used the NBP reference state.

- [R1234YF.FLD](R1234YF.FLD) (uploaded June 6, 2012 with updated transport equations)
- [R1234ZEE.FLD](R1234ZEE.FLD) (uploaded June 6, 2012 with new CAS number and updated transport equations. This is for R1234ze(E)). **NOTE** The file name for R1234ze(E) has been renamed as R1234zeE.FLD to avoid confusion with R1234ze(Z). You should delete your old R1234ze.FLD file when downloading this version. The contents of the fluid file have not changed.
- [R1234ZEZ.FLD](R1234ZEZ.FLD) (uploaded January 12, 2015 with transport equations. This is for R1234ze(Z)).
- [R1233ZDE.FLD](R1233ZDE.FLD) (uploaded November 9, 2015)

New refrigerant predefined mixture files are available, such as that for R-448A. To add these to Refprop, unzip the file below in your ``Refprop\Mixtures`` directory:

- [NEWMIX.ZIP](NEWMIX.ZIP) (uploaded October 24, 2016 with 10 new mixtures. For mixtures with R1234ze(E), you will need to download the renamed file above for this fluid.)

«On November 10, 2015, we released a new mixture file (HMX.BNC) that now contains mixing parameters for every binary of the fluids R-32, R-125, R-134a, R-1234yf, and R-1234ze(E). With these, mixtures such as R-448A that contain all five of these no longer use the predictive methods to get the interaction parameters. If you would like this file, please contact us. 

## Humid Air.
Although version 9.1 allows mixtures of nitrogen, argon, oxygen, and water as a consequence from the addition of the new natural gas mixture model, calculations for moist air have not been tested yet.&nbsp; It is likely that calculated values are reasonable, however, Refprop may not return results because the saturation routines may fail.&nbsp; The program calls the saturation routines to determine if the state is vapor, liquid, or two-phase.&nbsp; If you know that your state point is in the vapor phase, you can avoid the call to the saturation routines by using TPRHO instead of TPFLSH.&nbsp; The Fortran file FLSH_SUB.FOR gives additional information concerning the inputs to these routines.&nbsp; In the graphical interface, see the section [below](#convergence-failures-and-forcing-phase-calculations) on forcing phase calculations. A moist air mixture could be made up starting with the composition of dry air used in Refprop:&nbsp; 0.7812 nitrogen, 0.0092 argon, and 0.2096 oxygen (on a mole basis).&nbsp; A small amount of water could be added to this composition and then normalized.

## Mixture Models.
The LJ6 mixture model has been removed in version 9.1 and replaced with KW0. This was necessary to implement a more efficient and stable algorithm. For most situations, this change will be completely transparent, and calculated values will not change. For those that have fitted mixture parameters to their own data (e.g., for proprietary mixtures), you can simply insert the lines from your old ``HMX.BNC`` file for a particular binary mixture into the new ``HMX.BNC`` file that comes with 9.1 (be sure that no other block exists for that mixture). When running SETUP, you may receive an error message about the LJ6 mixture model not found (``ierr = –117``); this should be ignored because the values are later internally converted to the KW0 model (this error message will be removed in future versions). Conversion of LJ6 to KW0 converts the LJ6 xeta parameter (for the reducing temperature) to the KW0 gammaT and betaT values. The numerical values of the parameters are different, but the calculated properties will be identical. For those wishing to fit mixing parameters to new experimental VLE data, KW0 should be used for the fitting process and only the gammaT value should be fitted.

## Solids
The REFPROP program does not know the location of the solid-liquid interface&nbsp;for a mixture.&nbsp; For many of the pure fluids, melting line auxiliary equations are available and can be used to calculate liquid properties at the point where solids begin to form and can be used to keep the program from entering the solid phase.&nbsp; When melting lines are not available, the program uses the liquid phase density at the triple point as the maximum density, thus valid states between this density and the melting line will not be available.&nbsp; The location of the solid-liquid boundary can be calculated under the Calculate/Saturation Tables option.&nbsp; This option will also print out the vapor phase properties along the sublimation line if requested (and if an auxiliary equation is available).

## Transport Properties for Nitrogen, Oxygen, Argon, and Air.
The transport properties for nitrogen, argon, and oxygen in version 7.0 did not include the thermal conductivity enhancement for the critical region and did not represent the experimental data as well as possible.&nbsp; The transport equations for these fluids have been redone and now represent the data to within their experimental uncertainties.&nbsp; The publication below documents the new equations and shows all of the comparisons to data.

- [N2-Ar-O2 Transport equations documentation](NAO.PDF)

## Transport Properties for Pseudo-pure Fluids; Adding Pure Fluids to a Mixture Setup.
The ability to load both a mixture and a pure fluid not associated with the mixture is now possible. For example, a natural gas mixture of methane, ethane, and propane could be loaded, along with R134a, which is not part of the mixture. By calling SETNC and PUREFLD, properties for either the mixture or the pure fluid can be made without ever calling SETUP more than once at the beginning. This is also useful for calculating transport properties when the pseudo-pure fluid equation of state is in use (for R-404A, R-407C, R-410A, and R-507A). Since transport properties are not available in the PPF files, the full mixture has to be loaded as well. The example program below gives all the details.

- [PPF-EX.FOR](PPF-EX.FOR)

## Required Fluids for Distribution. 
There are several fluid files that Refprop accesses in order to run properly.&nbsp; These are ``NITROGEN.FLD``, ``PROPANE.FLD``, ``R134A.FLD``, and ``C12.FLD`` (dodecane).&nbsp; These fluids are used as reference fluids in extended corresponding states methods employed in Refprop to predict transport properties for some instances.&nbsp; These fluids (and the hmx.bnc file) should be distributed in addition to those required in a particular application if the Refprop routines have been incorporated into a software package. Note that a licensing agreement must be purchased before distributing your software to others.


Last modified: February 23, 2017.