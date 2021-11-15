---
layout: default
title: Home
---

# Version 10.0!  

Version 10.0 of REFPROP has been released.  See [see below](#updates-to-version-100) for information about REFPROP version 10.0

# Answers to Frequently Asked Questions

The following information gives answers to some of the most frequently asked questions concerning [the REFPROP program](https://www.nist.gov/srd/nist23.cfm). _To download any of the files listed below, right-click on the file and select **Save Target As...** and then add the file to your Refprop or other appropriate directory._ Sections with new information added during the last several months are identified with a «. For questions not answered here, please see [the user's guide](https://trc.nist.gov/refprop/REFPROP.PDF).

**General Questions**

1. [Getting Help](#getting-help)
2. [Errors in Version 10](#errors-in-version-10)
3. [Purchasing REFPROP](#purchasing-refprop)
4. [Installation Problems](#installation-problems)
5. [OSX and linux](#osx-and-linux)
6. [REFPROP is a Program, not a Database Containing Measurements](#refprop-is-a-program-not-a-database-containing-measurements)
7. [Referencing the REFPROP Program in Publications](#referencing-the-refprop-program-in-publications)
8. [Updates to Version 10.0](#updates-to-version-100)
9. [Updates to Version 9.1](#updates-to-version-91)
10. [Help File](#help-file)
11. [List of Fluids](#list-of-fluids)

**Using the Program**

12. [Reference States (enthalpy and entropy differences)](#reference-states-enthalpy-and-entropy-differences)
13. [Multiple and Metastable States](#multiple-and-metastable-states)
14. [Intro to Pure Fluids and 2-Phase States](#intro-to-pure-fluids-and-2-phase-states)
15. [Intro to Mixtures and 2-Phase States](#intro-to-mixtures-and-2-phase-states)

**Programming**

16. [Changing Fluids and Calling SETUP Multiple Times](#changing-fluids-and-calling-setup-multiple-times)
17. [Calculation of the Critical Point and Saturation States in the Critical Region](#calculation-of-the-critical-point-and-saturation-states-in-the-critical-region)
18. [Calculation of Phase Diagrams for Plotting Purposes](#calculation-of-phase-diagrams-for-plotting-purposes)
19. [FLSH Routines and Metastable States](#flsh-routines-and-metastable-states)

**Error Messages**

20. [Convergence Failures and Forcing Phase Calculations](#convergence-failures-and-forcing-phase-calculations)
21. [Mixture Error Messages](#mixture-error-messages)

**Fluids**

22. [List of fluids](#list-of-fluids)
23. [List of predefined mixtures](#list-of-predefined-mixtures)
24. [GERG-2008 Equation of State for Natural Gas Mixtures](#gerg-2008-equation-of-state-for-natural-gas-mixtures)
25. [HFO-1234yf, 1234ze(E), 1234ze(Z), 1233zd(E), and Refrigerant Mixtures](#hfo-1234yf-1234zee-1234zez-1233zde-and-refrigerant-mixtures)
26. [Humid Air](#humid-air)
27. [Mixture Models](#mixture-models)
28. [Solids](#solids)
29. [Transport Properties for Nitrogen, Oxygen, Argon, and Air](#transport-properties-for-nitrogen-oxygen-argon-and-air)
30. [Transport Properties for Mixtures](#transport-properties-for-mixtures)
31. [Transport Properties for Pseudo-pure Fluids; Adding Pure Fluids to a Mixture Setup](#transport-properties-for-pseudo-pure-fluids-adding-pure-fluids-to-a-mixture-setup)
32. [Required Fluids for Distribution](#required-fluids-for-distribution)

**Excel**

32. [Resolving Problems Linking with Excel](#resolving-problems-linking-with-excel)
33. [Other Issues Related to the Use of Refprop in Excel](#other-issues-related-to-the-use-of-refprop-in-excel)

**Linking with other Applications**

[This part has moved, click here to go to the new site](https://github.com/usnistgov/REFPROP-wrappers)

## Getting Help

In addition to this page, further answers can be found at GitHub: [REFPROP-issues](https://github.com/usnistgov/REFPROP-issues/issues).  Please use the GitHub site to post new bugs or questions so that all REFPROP users may learn from the correspondence.  If you still need assistance, or have other matters that you need to discuss, email refprop@nist.gov and we will get back to you as soon as we can.

## Errors in Version 10

1.  Incorrect fluid file for R507A.PPF.  The following fluid file should be placed in your REFPROP\FLUIDS directory.

- [R507A.PPF](https://trc.nist.gov/refprop/FAQ/R507A.PPF)

2.  The function RPVersion does not return the correct output.
3.  Valid liquid-phase states below the triple point of water may return a message that the point is out of bounds or in the solid phase given certain inputs such as pressure-enthalpy.
4.  Calling ABFLSH directly with mass inputs for the input/output properties can result in incorrect output values for energy, enthalpy, entropy, Cv, and Cp, however, the density will be returned correctly (in mass units).

## Purchasing REFPROP

There are three ways to purchase REFPROP:  For your use only, for company wide use, or for use in distribution in your code.  These are all explained at https://www.nist.gov/srd/refprop.  If you purchase the program for your use only, the copy you will receive can be installed on all machines that you use (not including servers where others can also access the program).  You do not need to purchase a copy for each machine you own.  There is no protection in the REFPROP installer or program, we trust that you will use the program and license appropriately.

For those looking for the "Accessibility Conformance Report (ACR) based on VPAT 2.4" for REFPROP 10.0, it can be obtained at this link: [here](https://github.com/usnistgov/REFPROP-docs/raw/master/PAT2.4Rev508--February2020.NIST23REFPROP.pdf)

## Installation Problems

### Upgrading from 9.x

1.  Uninstall all Refprop versions on your machine.
2.  Check if you have a ``Refprop`` directory in your ``Program files (x86)`` directory, if you do, delete it.
3.  In your users directory is a hidden system directory called ``AppData``.  Check if you have the following subdirectory:  "Local\VirtualStore\Program Files\REFPROP".  If so, delete that folder.
4.  Do a full system search (including Windows directories) for ``REFPROP.DLL`` and ``REFPRP64.DLL`` (or better:  ``REFPR*.DLL``), if you find it, delete it and anything else related to Refprop in that directory.
5.  Install version 10.
6.  If version 9.1 still shows up, uninstall 10, then install 9.1, uninstall it, and reinstall 10. (It’s painful, but seems to be the only way around this that we know of so far).  If you don’t have the installer for version 9.1, let us know.
7.  If one of the beta versions for Refprop 9.4.x still appears, install it and then uninstall it.  If you don't have the installer, email us to get access to it.
8.  If problems continue, go to Windows explorer, right click on the C: drive, go to Properties, and choose Disk Cleanup.  If this is not available, go to Start and in the search menu type in "Clean up".  Then click on Clean Up System Files and have it delete everything.
9.  Sometimes checking to make sure all Windows updates have been done and then rebooting the computer can fix problems, especially problems when using the Excel files.  Be sure you go to "Windows Updates" in the Start menu, not just the updates that it tells you to install from time to time.


### OCX issues
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

- [MSHFLXGD.OCX](https://trc.nist.gov/refprop/FAQ/mshflxgd.ocx)
- [COMDLG32.OCX](https://trc.nist.gov/refprop/FAQ/COMDLG32.OCX)

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

## OSX and linux

For users on OSX or linux, you are invited to compile REFPROP yourself with the cmake-based build system provided at [https://github.com/usnistgov/REFPROP-cmake](https://github.com/usnistgov/REFPROP-cmake).  You'll need to install REFPROP onto a windows machine to get access to the ``FLUIDS``, ``MIXTURES``, and ``FORTRAN`` folders. Any issues with compilation should be reported as an issue in that repository: [https://github.com/usnistgov/REFPROP-cmake/issues](https://github.com/usnistgov/REFPROP-cmake/issues).

If you are feeling brave, you can also try to install REFPROP into the ``wine`` environment (a windows-emulation environment).  Once you have installed ``wine`` (via homebrew on OSX, or via package manager of your linux distribution, google for more information), you can install REFPROP (along with its GUI) into wine with (for instance with REFPROP 10):

```
wine NIST2310.exe
```

To force 32-bit mode on 64-bit OS (recommended for REFPROP, it doesn't seem to work in a 64-bit wine environment) see [how to foce wine into acting like 32-bit windows on 64-bit ubuntu](https://askubuntu.com/questions/136714/how-to-force-wine-into-acting-like-32-bit-windows-on-64-bit-ubuntu)

## REFPROP is a Program, not a Database Containing Measurements
The REFPROP "database" is actually a program and does not contain any experimental information, aside from the critical and triple points of the pure fluids. The program uses equations for the thermodynamic and transport properties to calculate the state points of the fluid or mixture. These equations are the most accurate equations available worldwide. A link to one of these equations for R-125 is given below. Their high accuracy is obtained through many coefficients in the equations, and thus the calculation speed will be slower than other equations such as the Peng-Robinson cubic equations. The equations are generally valid over the entire vapor and liquid regions of the fluid, including supercritical states; the upper temperature limit is usually near the point of decomposition of the fluid, and the upper pressure (or density) limit is defined by the melting line of the substance.

- [Equation of State for HFC-125](https://trc.nist.gov/refprop/FAQ/R125.PDF)

## Referencing the REFPROP Program in Publications.
The following reference can be used to cite the REFPROP program in publications:

Lemmon, E.W., Bell, I.H., Huber, M.L., McLinden, M.O.&nbsp; NIST Standard Reference Database 23:&nbsp; Reference Fluid Thermodynamic and Transport Properties-REFPROP, Version 10.0, National Institute of Standards and Technology, Standard Reference Data Program, Gaithersburg, 2018.

Or in BibTeX form:
{% raw %}
```text
@Misc{LEMMON-RP10,
  Title                    = {{NIST Standard Reference Database 23: Reference Fluid Thermodynamic and Transport Properties-REFPROP, Version 10.0, National Institute of Standards and Technology}},
  Author                   = {E. W. Lemmon and I.H. Bell and M. L. Huber and M. O. McLinden},
  Year                     = {2018},
  Doi                      = {https://doi.org/10.18434/T4/1502528},
  Url                      = {https://www.nist.gov/srd/refprop}
}
```
{% endraw %}

Additionally, users should cite the reference for either the equation of state
or the transport equations used in their work, for example, if you used
calculations for CO<sub>2</sub>, you will find the reference for the equation
of state under the Options/Fluid Information option in Refprop and you should
cite the reference given under that option, like this:

Span, R. and Wagner, W., J. Phys. Chem. Ref. Data, 25(6):1509-1596, 1996.

## Updates to Version 10.0

Enhancements have been made to most areas of the NIST REFPROP program, including the equations of state for many of the pure fluids and mixtures, the transport equations, the graphical interface, the Excel spreadsheet, the Fortran files (i.e., core property routines), the sample programs in Python, C++, MATLAB, VB, etc. Some of the more important improvements are listed below: 

* A new Excel file with many more examples and additional documentation.
* All of the Fortran code was highly optimized resulting in increased calculation speed and improved convergence.  Many new flags were added to allow the user to specify better how the programs works.
* A new function is available to allow users to call Refprop with one single command that replaces most other calls from 9.1 (thus removing the need to learn what routines to use and the inputs/outputs for each routine, such as TPFLSH, THERM, etc.)  However, the old routines are still available for backwards compatibility.
* New shortcut keywords to load fluids and mixtures and other methods to simplify use of the code.
* New shared library for the Mac; this allows use of Refprop with, for example, Python or Excel 2011.  A CMake-based build system allows for compilation on any platform (windows, OSX, Linux) : https://github.com/usnistgov/REFPROP-cmake
* The vapor-liquid equilibrium calculations for tracing isotherms and isobars (T-x and p-x diagrams) are greatly improved (doi: [10.1002/aic.16074](https://doi.org/10.1002/aic.16074)).
* New reference equations of state for ammonia, helium, and heavy water.  The ammonia equation of state introduces the first change to the Helmholtz energy functional form in over 25 years of development of equations for the thermodynamic properties of fluids.
* The addition of the following refrigerants:  R1123, R1224yd(Z), R1233zd(E), R1234ze(Z), R1243zf, and R1336mzz(Z).
* The addition of the following fluids:  1,3-butadiene, 1-butyne, 1-pentene, 2,2-dimethylbutane, 2,3-dimethylbutane, 3-methylpentane, acetylene, chlorine, chlorobenzene, cyclobutene, 1,2-dichloroethane, diethanolamine, docosane, ethylene glycol, ethylene oxide, hexadecane, monoethanolamine, perfluorohexane, propadiene, propylene oxide, and vinyl chloride.
* New equations of state have been developed for cyclopentane, D4, heptane, hexane, hydrogen chloride, MDM, MD2M, MM, neon, octane, pentane, perfluorobutane, perfluoropentane, R-1233zd(E), R-161, R-245fa, R-E347mcc (HFE-7000), and sulfur dioxide.  The development of an equation of state is a complex process requiring many months of work for each one.
* Mixture model of Gernert implemented for selected mixtures with water, including water+CO2 and moist air.
* Transport equations have been added or modified for acetone, acetylene, ammonia, benzene, butane, 1,3-butadiene, 1-butene, 1-butyne, 2,2-dimethylbutane, 2,3-dimethylbutane, carbon dioxide, carbon monoxide, carbonyl sulfide, chlorine, chlorobenzene,  cis-butene, cyclobutene, cyclohexane, cyclopentane, cyclopropane, D4, D5, D6, 1,2-dichloroethane(R150), diethanolamine, diethyl ether, dimethyl carbonate, dimethyl ether, docosane, ethane, ethylbenzene, ethylene, ethylene glycol, ethylene oxide, fluorine, heptane, hexane, hexadecane, hydrogen chloride, hydrogen sulfide, isobutene, isohexane, isooctane, isopentane, krypton, methyl palmitate, methyl linolenate, methyl linoleate, methyl oleate, methyl stearate, m-xylene, MD2M, MD3M, MD4M, MDM, MM, methylcyclohexane, 3-methylpentane, monoethanolamine, neon, neopentane, nitrous oxide, Novec-649, o-xylene, p-xylene, pentane,1-pentene, propadiene, propylcyclohexane, propylene, propylene oxide, propyne, perfluorobutane, perfluoropentane, perfluorohexane, propane, R1123, R143a, R114, R161, R1224yd(Z), R1233zd(E), R1234yf, R1234ze(Z), R1234ze(E), R1243zf, R13I1 (CF3I), R1336mzz(Z), R218, R236fa, R236ea, R245ca, R245fa, R365mfc, RE143a, RE245cb2, RE245fa2,RE347mcc, RC318, R40, sulfur dioxide, trans-butene, toluene, undecane, vinyl chloride, and xenon.
* New mixture models for ammonia + water and ethylene glycol + water.
* Approximately 400 binary pairs have been added from the work of Bell and Lemmon (doi: [10.1021/acs.jced.6b00257](https://pubs.acs.org/doi/abs/10.1021/acs.jced.6b00257) )
* Mixture parameters were fitted (or refitted) for the following binary mixtures:  R1234yf with R32, R125, R134a, and R1234ze(E), R1234ze(E) with R125 and R134a, and many others.  These new mixing parameters with R1234yf and R1234ze(E) are currently the standard used in the refrigeration industry and Version 10 puts all users in compliance with the property values now in use world-wide.  All new ASHRAE predefined mixtures except those with trans-1,2-dichloroethylene (t-EDC) (due to the lack of a pure fluid equation) are included.
* New estimation schemes were developed for selected families of binary mixtures (n-alkane + n-alkane mixtures, mixtures with CO2, etc.) to obtain estimated interaction parameters for mixtures that have not been fitted.
* A reverse Polish type notation was added to read any functional form for the transport properties, eliminating the need to compile a new DLL as new correlations are published.  The notation and corresponding coefficients of the equation are simply added to the fluid files and the new code will read and interpret the supplied text.
* The DOI for each primary equation was added to the fluid files.  A link in the GUI is now available to load the publication if access to the journal is available.
* Henry's constant estimation scheme to obtain better starting values for VLE of mixtures to improve convergence.
* Additional code to identify type III mixtures for use in phase determination.
* Most surface tension equations for the pure fluids have been updated, and an improved surface tension model for mixtures was added.
* New code to calculate heat of formation or the mass flux for a Venturi nozzle.

### Breaking changes

In general the high-level interface exposed through the DLL is 100% backwards compatible with version 9.1.1.  Some non-backwards-compatible changes were necessary:

* The errorcodes from the functions exposed through the DLL were modified.  If you have been interrogating the error codes from the high-level routines, you may need to reconsider how you handle errors.

## Updates to Version 9.1
Several problems in version 9.0 (listed below) were found after its release, and these have all been corrected in 9.1. There are also a few issues with 9.1. If these affect you, please let us know and we will send you the update.

### Issues with Refprop 9.0

1. The calculation of d<sup>2</sup>p/dT<sup>2</sup> at constant density is incorrect.
2. The reference state for R1234yf and R1234ze(E) should be changed from NBP to IIR. Updated files are given further below.
3. Calculation of isobars for pure fluids at pressures less than the triple point pressure may incorrectly return properties in the liquid phase rather than the vapor phase.
4. The manual REFPROP9.PDF and the UserInformation sheet in Refprop.xls incorrectly listed isobutene instead of isobutane for R430A. (However, the graphical interface and mixture file are correct.)

### Issues with Refprop 9.1

1. Inputs of enthalpy or entropy may not converge, or will converge to the wrong phase.

## Help File
The most recent help file from Refprop is available below. You should download it to your
machine before launching it, otherwise the help file will appear blank.  The PDF is an alternative form of the documentation that may be more convenient for you.  The most up-to-date version of the documentation is at http://refprop-docs.readthedocs.io/en/latest/

- [REFPROP.CHM](https://trc.nist.gov/refprop/REFPROP.CHM)
- [REFPROP.PDF](https://trc.nist.gov/refprop/REFPROP.PDF)

## List of Fluids

This is the list of pure fluids that are included in REFPROP 10 (a more comprehensive list is available in the Refprop 10 Excel file REFPROP.XLS):

<table>
<tr>
<td><b>Fluid File</b></td><td><b>Name</b></td><td><b>Synonym</b></td><td><b>Chemical Formula</b></td>
</tr>
<tr>
<td>13BUTADIENE.FLD</td><td>1,3-Butadiene</td><td>Vinylethylene</td><td>C4H6</td>
</tr>
<tr>
<td>1BUTENE.FLD</td><td>Butene</td><td>1-Butylene</td><td>C4H8</td>
</tr>
<tr>
<td>1BUTYNE.FLD</td><td>1-Butyne</td><td>Ethylacetylene</td><td>C4H6</td>
</tr>
<tr>
<td>1PENTENE.FLD</td><td>1-Pentene</td><td>Propylethylene</td><td>C5H10</td>
</tr>
<tr>
<td>22DIMETHYLBUTANE.FLD</td><td>2,2-Dimethylbutane</td><td>Neohexane</td><td>C6H14</td>
</tr>
<tr>
<td>23DIMETHYLBUTANE.FLD</td><td>2,3-Dimethylbutane</td><td>Butane, 2,3-dimethyl-</td><td>C6H14</td>
</tr>
<tr>
<td>3METHYLPENTANE.FLD</td><td>3-Methylpentane</td><td>Pentane, 3-methyl-</td><td>C6H14</td>
</tr>
<tr>
<td>ACETONE.FLD</td><td>Acetone</td><td>Dimethyl ketone</td><td>C3H6O</td>
</tr>
<tr>
<td>ACETYLENE.FLD</td><td>Acetylene</td><td>Narcylen, vinylene</td><td>C2H2</td>
</tr>
<tr>
<td>AMMONIA.FLD</td><td>Ammonia</td><td>R-717</td><td>NH3</td>
</tr>
<tr>
<td>ARGON.FLD</td><td>Argon</td><td>R-740</td><td>Ar</td>
</tr>
<tr>
<td>BENZENE.FLD</td><td>Benzene</td><td>Benzene</td><td>C6H6</td>
</tr>
<tr>
<td>BUTANE.FLD</td><td>Butane</td><td>R-600</td><td>C4H10</td>
</tr>
<tr>
<td>C11.FLD</td><td>Undecane</td><td>n-Undecane</td><td>C11H24</td>
</tr>
<tr>
<td>C12.FLD</td><td>Dodecane</td><td>n-Dodecane</td><td>C12H26</td>
</tr>
<tr>
<td>C16.FLD</td><td>Hexadecane</td><td>n-Hexadecane</td><td>C16H34</td>
</tr>
<tr>
<td>C1CC6.FLD</td><td>Methylcyclohexane</td><td>Cyclohexylmethane</td><td>C7H14</td>
</tr>
<tr>
<td>C22.FLD</td><td>Docosane</td><td>n-Docosane</td><td>C22H46</td>
</tr>
<tr>
<td>C2BUTENE.FLD</td><td>cis-Butene</td><td>(Z)-2-Butene</td><td>C4H8</td>
</tr>
<tr>
<td>C3CC6.FLD</td><td>Propylcyclohexane</td><td>Propylcyclohexane</td><td>C9H18</td>
</tr>
<tr>
<td>C4F10.FLD</td><td>Perfluorobutane</td><td>Perfluorobutane</td><td>C4F10</td>
</tr>
<tr>
<td>C5F12.FLD</td><td>Perfluoropentane</td><td>Perfluoropentane</td><td>C5F12</td>
</tr>
<tr>
<td>C6F14.FLD</td><td>Perfluorohexane</td><td>Perfluorohexane</td><td>C6F14</td>
</tr>
<tr>
<td>CF3I.FLD</td><td>R13I1</td><td>HFC-13I1</td><td>CF3I</td>
</tr>
<tr>
<td>CHLORINE.FLD</td><td>Chlorine</td><td>Chlorine</td><td>Cl2</td>
</tr>
<tr>
<td>CHLOROBENZENE.FLD</td><td>Chlorobenzene</td><td>Phenyl chloride</td><td>C6H5Cl</td>
</tr>
<tr>
<td>CO.FLD</td><td>Carbon monoxide</td><td>Carbon oxide</td><td>CO</td>
</tr>
<tr>
<td>CO2.FLD</td><td>Carbon dioxide</td><td>R-744</td><td>CO2</td>
</tr>
<tr>
<td>COS.FLD</td><td>Carbonyl sulfide</td><td>Carbon oxysulfide</td><td>COS</td>
</tr>
<tr>
<td>CYCLOBUTENE.FLD</td><td>Cyclobutene</td><td>Cyclobutan-1,2-diyl</td><td>C4H6</td>
</tr>
<tr>
<td>CYCLOHEX.FLD</td><td>Cyclohexane</td><td>Cyclohexane</td><td>C6H12</td>
</tr>
<tr>
<td>CYCLOPEN.FLD</td><td>Cyclopentane</td><td>C5H10</td><td>C5H10</td>
</tr>
<tr>
<td>CYCLOPRO.FLD</td><td>Cyclopropane</td><td>Trimethylene</td><td>C3H6</td>
</tr>
<tr>
<td>D2.FLD</td><td>Deuterium</td><td>Deuterium</td><td>D2</td>
</tr>
<tr>
<td>D2O.FLD</td><td>Heavy water</td><td>Deuterium oxide</td><td>D2O</td>
</tr>
<tr>
<td>D4.FLD</td><td>D4</td><td>D4</td><td>C8H24O4Si4</td>
</tr>
<tr>
<td>D5.FLD</td><td>D5</td><td>D5</td><td>C10H30O5Si5</td>
</tr>
<tr>
<td>D6.FLD</td><td>D6</td><td>D6</td><td>C12H36Si6O6</td>
</tr>
<tr>
<td>DEA.FLD</td><td>Diethanolamine</td><td>bis(2-hydroxyethyl)Amine</td><td>C4H11NO2</td>
</tr>
<tr>
<td>DECANE.FLD</td><td>Decane</td><td>n-Decane</td><td>C10H22</td>
</tr>
<tr>
<td>DEE.FLD</td><td>Diethyl ether</td><td>Ethyl ether</td><td>C4H10O</td>
</tr>
<tr>
<td>DMC.FLD</td><td>Dimethyl carbonate</td><td>DMC</td><td>C3H6O3</td>
</tr>
<tr>
<td>DME.FLD</td><td>Dimethyl ether</td><td>RE-170</td><td>C2H6O</td>
</tr>
<tr>
<td>EBENZENE.FLD</td><td>Ethylbenzene</td><td>Benzene, ethyl-</td><td>C8H10</td>
</tr>
<tr>
<td>EGLYCOL.FLD</td><td>Ethylene glycol</td><td>Glycol alcohol</td><td>C2H6O2</td>
</tr>
<tr>
<td>ETHANE.FLD</td><td>Ethane</td><td>R-170</td><td>C2H6</td>
</tr>
<tr>
<td>ETHANOL.FLD</td><td>Ethanol</td><td>Methyl carbinol</td><td>C2H6O</td>
</tr>
<tr>
<td>ETHYLENE.FLD</td><td>Ethylene</td><td>R-1150</td><td>C2H4</td>
</tr>
<tr>
<td>ETHYLENEOXIDE.FLD</td><td>Ethylene oxide</td><td>Oxirane</td><td>C2H4O</td>
</tr>
<tr>
<td>FLUORINE.FLD</td><td>Fluorine</td><td>Fluorine</td><td>F2</td>
</tr>
<tr>
<td>H2S.FLD</td><td>Hydrogen sulfide</td><td>Dihydrogen monosulfide</td><td>H2S</td>
</tr>
<tr>
<td>HCL.FLD</td><td>Hydrogen chloride</td><td>Hydrogen chloride</td><td>HCl</td>
</tr>
<tr>
<td>HELIUM.FLD</td><td>Helium</td><td>R-704</td><td>He</td>
</tr>
<tr>
<td>HEPTANE.FLD</td><td>Heptane</td><td>n-Heptane</td><td>C7H16</td>
</tr>
<tr>
<td>HEXANE.FLD</td><td>Hexane</td><td>n-Hexane</td><td>C6H14</td>
</tr>
<tr>
<td>HYDROGEN.FLD</td><td>Hydrogen (normal)</td><td>R-702</td><td>H2</td>
</tr>
<tr>
<td>IBUTENE.FLD</td><td>Isobutene</td><td>Methylpropene</td><td>C4H8</td>
</tr>
<tr>
<td>IHEXANE.FLD</td><td>Isohexane</td><td>Methylpentane</td><td>C6H14</td>
</tr>
<tr>
<td>IOCTANE.FLD</td><td>Isooctane</td><td>Isobutyltrimethylmethane</td><td>C8H18</td>
</tr>
<tr>
<td>IPENTANE.FLD</td><td>Isopentane</td><td>R-601a</td><td>C5H12</td>
</tr>
<tr>
<td>ISOBUTAN.FLD</td><td>Isobutane</td><td>R-600a</td><td>C4H10</td>
</tr>
<tr>
<td>KRYPTON.FLD</td><td>Krypton</td><td>R-784</td><td>Kr</td>
</tr>
<tr>
<td>MD2M.FLD</td><td>MD2M</td><td>MD2M</td><td>C10H30Si4O3</td>
</tr>
<tr>
<td>MD3M.FLD</td><td>MD3M</td><td>MD3M</td><td>C12H36Si5O4</td>
</tr>
<tr>
<td>MD4M.FLD</td><td>MD4M</td><td>MD4M</td><td>C14H42O5Si6</td>
</tr>
<tr>
<td>MDM.FLD</td><td>MDM</td><td>MDM</td><td>C8H24O2Si3</td>
</tr>
<tr>
<td>MEA.FLD</td><td>Monoethanolamine</td><td>2-Aminoethanol</td><td>C2H7NO</td>
</tr>
<tr>
<td>METHANE.FLD</td><td>Methane</td><td>R-50</td><td>CH4</td>
</tr>
<tr>
<td>METHANOL.FLD</td><td>Methanol</td><td>Methyl alcohol</td><td>CH4O</td>
</tr>
<tr>
<td>MLINOLEA.FLD</td><td>Methyl linoleate</td><td>Methyl ester(Z,Z)-9,12-octadecadienoic acid</td><td>C19H34O2</td>
</tr>
<tr>
<td>MLINOLEN.FLD</td><td>Methyl linolenate</td><td>Methyl ester linolenic acid</td><td>C19H32O2</td>
</tr>
<tr>
<td>MM.FLD</td><td>MM</td><td>MM</td><td>C6H18OSi2</td>
</tr>
<tr>
<td>MOLEATE.FLD</td><td>Methyl oleate</td><td>Methyl ester oleic acid</td><td>C19H36O2</td>
</tr>
<tr>
<td>MPALMITA.FLD</td><td>Methyl palmitate</td><td>Methyl ester palmitic acid</td><td>C17H34O2</td>
</tr>
<tr>
<td>MSTEARAT.FLD</td><td>Methyl stearate</td><td>Methyl ester stearic acid</td><td>C19H38O2</td>
</tr>
<tr>
<td>MXYLENE.FLD</td><td>m-Xylene</td><td>m-Xylene</td><td>C8H10</td>
</tr>
<tr>
<td>N2O.FLD</td><td>Nitrous oxide</td><td>R-744A</td><td>N2O</td>
</tr>
<tr>
<td>NEON.FLD</td><td>Neon</td><td>R-720</td><td>Ne</td>
</tr>
<tr>
<td>NEOPENTN.FLD</td><td>Neopentane</td><td>Tetramethylmethane</td><td>C5H12</td>
</tr>
<tr>
<td>NF3.FLD</td><td>Nitrogen trifluoride</td><td>Trifluoroamine</td><td>F3N</td>
</tr>
<tr>
<td>NITROGEN.FLD</td><td>Nitrogen</td><td>R-728</td><td>N2</td>
</tr>
<tr>
<td>NONANE.FLD</td><td>Nonane</td><td>n-Nonane</td><td>C9H20</td>
</tr>
<tr>
<td>NOVEC649.FLD</td><td>Novec 649, 1230</td><td>Dodecafluoro-2-methylpentan-3-one</td><td>C6F12O</td>
</tr>
<tr>
<td>OCTANE.FLD</td><td>Octane</td><td>n-Octane</td><td>C8H18</td>
</tr>
<tr>
<td>ORTHOHYD.FLD</td><td>Orthohydrogen</td><td>R-702</td><td>H2</td>
</tr>
<tr>
<td>OXYGEN.FLD</td><td>Oxygen</td><td>R-732</td><td>O2</td>
</tr>
<tr>
<td>OXYLENE.FLD</td><td>o-Xylene</td><td>o-Xylene</td><td>C8H10</td>
</tr>
<tr>
<td>PARAHYD.FLD</td><td>Parahydrogen</td><td>R-702p</td><td>H2</td>
</tr>
<tr>
<td>PENTANE.FLD</td><td>Pentane</td><td>R-601</td><td>C5H12</td>
</tr>
<tr>
<td>PROPADIENE.FLD</td><td>Propadiene</td><td>Allene</td><td>C3H4</td>
</tr>
<tr>
<td>PROPANE.FLD</td><td>Propane</td><td>R-290</td><td>C3H8</td>
</tr>
<tr>
<td>PROPYLEN.FLD</td><td>Propylene</td><td>R-1270</td><td>C3H6</td>
</tr>
<tr>
<td>PROPYLENEOXIDE.FLD</td><td>Propylene oxide</td><td>Methyloxirane</td><td>C3H6O</td>
</tr>
<tr>
<td>PROPYNE.FLD</td><td>Propyne</td><td>Methyl acetylene</td><td>C3H4</td>
</tr>
<tr>
<td>PXYLENE.FLD</td><td>p-Xylene</td><td>p-Xylene</td><td>C8H10</td>
</tr>
<tr>
<td>R11.FLD</td><td>R11</td><td>CFC-11</td><td>CCl3F</td>
</tr>
<tr>
<td>R1123.FLD</td><td>R1123</td><td>HFO-1123</td><td>C2HF3</td>
</tr>
<tr>
<td>R113.FLD</td><td>R113</td><td>CFC-113</td><td>C2Cl3F3</td>
</tr>
<tr>
<td>R114.FLD</td><td>R114</td><td>CFC-114</td><td>C2Cl2F4</td>
</tr>
<tr>
<td>R115.FLD</td><td>R115</td><td>CFC-115</td><td>C2ClF5</td>
</tr>
<tr>
<td>R116.FLD</td><td>R116</td><td>FC-116</td><td>C2F6</td>
</tr>
<tr>
<td>R12.FLD</td><td>R12</td><td>CFC-12</td><td>CCl2F2</td>
</tr>
<tr>
<td>R1216.FLD</td><td>R1216</td><td>Hexafluoropropylene</td><td>C3F6</td>
</tr>
<tr>
<td>R1224YDZ.FLD</td><td>R1224yd(Z)</td><td>HCFO-1224yd(Z)</td><td>C3HClF4</td>
</tr>
<tr>
<td>R123.FLD</td><td>R123</td><td>HCFC-123</td><td>C2HCl2F3</td>
</tr>
<tr>
<td>R1233ZDE.FLD</td><td>R1233zd(E)</td><td>HFO-1233zd(E)</td><td>C3H2ClF3</td>
</tr>
<tr>
<td>R1234YF.FLD</td><td>R1234yf</td><td>R-1234yf</td><td>C3F4H2</td>
</tr>
<tr>
<td>R1234ZEE.FLD</td><td>R1234ze(E)</td><td>HFO-1234ze(E)</td><td>C3F4H2</td>
</tr>
<tr>
<td>R1234ZEZ.FLD</td><td>R1234ze(Z)</td><td>R-1234ze(Z)</td><td>C3F4H2</td>
</tr>
<tr>
<td>R124.FLD</td><td>R124</td><td>HCFC-124</td><td>C2HClF4</td>
</tr>
<tr>
<td>R1243ZF.FLD</td><td>R1243zf</td><td>HFO-1243zf</td><td>C3H3F3</td>
</tr>
<tr>
<td>R125.FLD</td><td>R125</td><td>HFC-125</td><td>C2HF5</td>
</tr>
<tr>
<td>R13.FLD</td><td>R13</td><td>CFC-13</td><td>CClF3</td>
</tr>
<tr>
<td>R1336MZZZ.FLD</td><td>R1336mzz(Z)</td><td>HFO-1336mzz(Z)</td><td>C4H2F6</td>
</tr>
<tr>
<td>R134A.FLD</td><td>R134a</td><td>HFC-134a</td><td>C2H2F4</td>
</tr>
<tr>
<td>R14.FLD</td><td>R14</td><td>FC-14</td><td>CF4</td>
</tr>
<tr>
<td>R141B.FLD</td><td>R141b</td><td>HCFC-141b</td><td>C2H3Cl2F</td>
</tr>
<tr>
<td>R142B.FLD</td><td>R142b</td><td>HCFC-142b</td><td>C2H3ClF2</td>
</tr>
<tr>
<td>R143A.FLD</td><td>R143a</td><td>HFC-143a</td><td>C2H3F3</td>
</tr>
<tr>
<td>R150.FLD</td><td>Dichloroethane</td><td>R-150</td><td>C2H4Cl2</td>
</tr>
<tr>
<td>R152A.FLD</td><td>R152a</td><td>HFC-152a</td><td>C2H4F2</td>
</tr>
<tr>
<td>R161.FLD</td><td>R161</td><td>Ethyl fluoride</td><td>C2H5F</td>
</tr>
<tr>
<td>R21.FLD</td><td>R21</td><td>HCFC-21</td><td>CHCl2F</td>
</tr>
<tr>
<td>R218.FLD</td><td>R218</td><td>Perfluoropropane</td><td>C3F8</td>
</tr>
<tr>
<td>R22.FLD</td><td>R22</td><td>HCFC-22</td><td>CHClF2</td>
</tr>
<tr>
<td>R227EA.FLD</td><td>R227ea</td><td>HFC-227ea</td><td>C3HF7</td>
</tr>
<tr>
<td>R23.FLD</td><td>R23</td><td>HFC-23</td><td>CHF3</td>
</tr>
<tr>
<td>R236EA.FLD</td><td>R236ea</td><td>HFC-236ea</td><td>C3H2F6</td>
</tr>
<tr>
<td>R236FA.FLD</td><td>R236fa</td><td>HFC-236fa</td><td>C3H2F6</td>
</tr>
<tr>
<td>R245CA.FLD</td><td>R245ca</td><td>HFC-245ca</td><td>C3H3F5</td>
</tr>
<tr>
<td>R245FA.FLD</td><td>R245fa</td><td>HFC-245fa</td><td>C3H3F5</td>
</tr>
<tr>
<td>R32.FLD</td><td>R32</td><td>HFC-32</td><td>CH2F2</td>
</tr>
<tr>
<td>R365MFC.FLD</td><td>R365mfc</td><td>HFC-365mfc</td><td>C4H5F5</td>
</tr>
<tr>
<td>R40.FLD</td><td>R40</td><td>Methyl chloride</td><td>CH3Cl</td>
</tr>
<tr>
<td>R41.FLD</td><td>R41</td><td>HFC-41</td><td>CH3F</td>
</tr>
<tr>
<td>RC318.FLD</td><td>RC318</td><td>FC-C318</td><td>C4F8</td>
</tr>
<tr>
<td>RE143A.FLD</td><td>RE143a</td><td>HFE-143a</td><td>C2H3F3O</td>
</tr>
<tr>
<td>RE245CB2.FLD</td><td>RE245cb2</td><td>HFE-245cb2</td><td>C3H3F5O</td>
</tr>
<tr>
<td>RE245FA2.FLD</td><td>RE245fa2</td><td>HFE-245fa2</td><td>C3H3F5O</td>
</tr>
<tr>
<td>RE347MCC.FLD</td><td>RE347mcc (HFE-7000)</td><td>HFE-7000</td><td>C4H3F7O</td>
</tr>
<tr>
<td>SF6.FLD</td><td>Sulfur hexafluoride</td><td>Sulfur fluoride</td><td>SF6</td>
</tr>
<tr>
<td>SO2.FLD</td><td>Sulfur dioxide</td><td>R-764</td><td>O2S</td>
</tr>
<tr>
<td>T2BUTENE.FLD</td><td>trans-Butene</td><td>(E)-2-Butene</td><td>C4H8</td>
</tr>
<tr>
<td>TOLUENE.FLD</td><td>Toluene</td><td>Toluene</td><td>C7H8</td>
</tr>
<tr>
<td>VINYLCHLORIDE.FLD</td><td>Vinyl chloride</td><td>R-1140</td><td>C2H3Cl</td>
</tr>
<tr>
<td>WATER.FLD</td><td>Water</td><td>R-718</td><td>H2O</td>
</tr>
<tr>
<td>XENON.FLD</td><td>Xenon</td><td>Xenon</td><td>Xe</td>
</tr>
</table>

## List of predefined mixtures

The following predefined mixtures are included in the ASHRAE 34 Standard and are supported by REFPROP. In REFPROP 10, many of the predefined mixture files are already included, and additional ones can be generated with the script at [https://github.com/usnistgov/REFPROP-issues/issues/358#issuecomment-872394368](https://github.com/usnistgov/REFPROP-issues/issues/358#issuecomment-872394368)

Warning: if interaction parameters are estimated, you should be somewhat skeptical of the model results, and confirm model accuracy against experimental measurements.  A good place to start to figure out whether the model might be adequate for your use case, is the survey of measurements and models in  [https://pubs.acs.org/doi/abs/10.1021/acs.jced.1c00192](https://pubs.acs.org/doi/abs/10.1021/acs.jced.1c00192)

R401A [22/152A/124] (53.0/13.0/34.0 by mass)

R401B [22/152A/124] (61.0/11.0/28.0 by mass)

R401C [22/152A/124] (33.0/15.0/52.0 by mass)

R402A [125/PROPANE/22] (60.0/2.0/38.0 by mass)

R402B [125/PROPANE/22] (38.0/2.0/60.0 by mass)

R403A [PROPANE/22/218] (5.0/75.0/20.0 by mass) !!warning: estimated parameters!!

R403B [PROPANE/22/218] (5.0/56.0/39.0 by mass)

R404A [125/143A/134A] (44.0/52.0/4.0 by mass)

R405A [22/152A/142B/C318] (45.0/7.0/5.5/42.5 by mass) !!warning: estimated parameters!!

R406A [22/ISOBUTAN/142B] (55.0/4.0/41.0 by mass) !!warning: estimated parameters!!

R407A [32/125/134A] (20.0/40.0/40.0 by mass)

R407B [32/125/134A] (10.0/70.0/20.0 by mass)

R407C [32/125/134A] (23.0/25.0/52.0 by mass)

R407D [32/125/134A] (15.0/15.0/70.0 by mass)

R407E [32/125/134A] (25.0/15.0/60.0 by mass)

R407F [32/125/134A] (30.0/30.0/40.0 by mass)

R407G [32/125/134A] (2.5/2.5/95.0 by mass)

R407H [32/125/134A] (32.5/15.0/52.5 by mass)

R407I [32/125/134A] (19.5/8.5/72.0 by mass)

R408A [125/143A/22] (7.0/46.0/47.0 by mass)

R409A [22/124/142B] (60.0/25.0/15.0 by mass)

R409B [22/124/142B] (65.0/25.0/10.0 by mass)

R410A [32/125] (50.0/50.0 by mass)

R410B [32/125] (45.0/55.0 by mass)

R411A [PROPYLEN/22/152A] (1.5/87.5/11.0 by mass)

R411B [PROPYLEN/22/152A] (3.0/94.0/3.0 by mass)

R412A [22/218/142B] (70.0/5.0/25.0 by mass) !!warning: estimated parameters!!

R413A [218/134A/ISOBUTAN] (9.0/88.0/3.0 by mass)

R414A [22/124/ISOBUTAN/142B] (51.0/28.5/4.0/16.5 by mass) !!warning: estimated parameters!!

R414B [22/124/ISOBUTAN/142B] (50.0/39.0/1.5/9.5 by mass)

R415A [22/152A] (82.0/18.0 by mass)

R415B [22/152A] (25.0/75.0 by mass)

R416A [134A/124/BUTANE] (59.0/39.5/1.5 by mass) !!warning: estimated parameters!!

R417A [125/134A/BUTANE] (46.6/50.0/3.4 by mass)

R417B [125/134A/BUTANE] (79.0/18.3/2.7 by mass)

R417C [125/134A/BUTANE] (19.5/78.8/1.7 by mass)

R418A [PROPANE/22/152A] (1.5/96.0/2.5 by mass)

R419A [125/134A/DME] (77.0/19.0/4.0 by mass)

R419B [125/134A/DME] (48.5/48.0/3.5 by mass)

R420A [134A/142B] (88.0/12.0 by mass)

R421A [125/134A] (58.0/42.0 by mass)

R421B [125/134A] (85.0/15.0 by mass)

R422A [125/134A/ISOBUTAN] (85.1/11.5/3.4 by mass)

R422B [125/134A/ISOBUTAN] (55.0/42.0/3.0 by mass)

R422C [125/134A/ISOBUTAN] (82.0/15.0/3.0 by mass)

R422D [125/134A/ISOBUTAN] (65.1/31.5/3.4 by mass)

R422E [125/134A/ISOBUTAN] (58.0/39.3/2.7 by mass)

R423A [134A/227EA] (52.5/47.5 by mass)

R424A [125/134A/ISOBUTAN/BUTANE/IPENTANE] (50.5/47.0/0.9/1.0/0.6 by mass)

R425A [32/134A/227EA] (18.5/69.5/12.0 by mass)

R426A [125/134A/BUTANE/IPENTANE] (5.1/93.0/1.3/0.6 by mass)

R427A [32/125/143A/134A] (15.0/25.0/10.0/50.0 by mass)

R428A [125/143A/PROPANE/ISOBUTAN] (77.5/20.0/0.6/1.9 by mass)

R429A [DME/152A/ISOBUTAN] (60.0/10.0/30.0 by mass) !!warning: estimated parameters!!

R430A [152A/ISOBUTAN] (76.0/24.0 by mass)

R431A [PROPANE/152A] (71.0/29.0 by mass)

R432A [PROPYLEN/DME] (80.0/20.0 by mass)

R433A [PROPYLEN/PROPANE] (30.0/70.0 by mass)

R433B [PROPYLEN/PROPANE] (5.0/95.0 by mass)

R433C [PROPYLEN/PROPANE] (25.0/75.0 by mass)

R434A [125/143A/134A/ISOBUTAN] (63.2/18.0/16.0/2.8 by mass)

R435A [DME/152A] (80.0/20.0 by mass) !!warning: estimated parameters!!

R436A [PROPANE/ISOBUTAN] (56.0/44.0 by mass)

R436B [PROPANE/ISOBUTAN] (52.0/48.0 by mass)

R436C [PROPANE/ISOBUTAN] (95.0/5.0 by mass)

R437A [125/134A/BUTANE/PENTANE] (19.5/78.5/1.4/0.6 by mass) !!warning: estimated parameters!!

R438A [32/125/134A/BUTANE/IPENTANE] (8.5/45.0/44.2/1.7/0.6 by mass)

R439A [32/125/ISOBUTAN] (50.0/47.0/3.0 by mass)

R440A [PROPANE/134A/152A] (0.6/1.6/97.8 by mass)

R441A [ETHANE/PROPANE/ISOBUTAN/BUTANE] (3.1/54.8/6.0/36.1 by mass)

R442A [32/125/134A/152A/227EA] (31.0/31.0/30.0/3.0/5.0 by mass)

R443A [PROPYLEN/PROPANE/ISOBUTAN] (55.0/40.0/5.0 by mass)

R444A [32/152A/1234ZEE] (12.0/5.0/83.0 by mass) !!warning: estimated parameters!!

R444B [32/152A/1234ZEE] (41.5/10.0/48.5 by mass)

R445A [CO2/134A/1234ZEE] (6.0/9.0/85.0 by mass)

R446A [32/1234ZEE/BUTANE] (68.0/29.0/3.0 by mass) !!warning: estimated parameters!!

R447A [32/125/1234ZEE] (68.0/3.5/28.5 by mass)

R447B [32/125/1234ZEE] (68.0/8.0/24.0 by mass)

R448A [32/125/1234YF/134A/1234ZEE] (26.0/26.0/20.0/21.0/7.0 by mass)

R449A [32/125/1234YF/134A] (24.3/24.7/25.3/25.7 by mass)

R449B [32/125/1234YF/134A] (25.2/24.3/23.2/27.3 by mass)

R449C [32/125/1234YF/134A] (20.0/20.0/31.0/29.0 by mass)

R450A [134A/1234ZEE] (42.0/58.0 by mass)

R451A [1234YF/134A] (89.8/10.2 by mass)

R451B [1234YF/134A] (88.8/11.2 by mass)

R452A [32/125/1234YF] (11.0/59.0/30.0 by mass)

R452B [32/125/1234YF] (67.0/7.0/26.0 by mass)

R452C [32/125/1234YF] (12.5/61.0/26.5 by mass)

R453A [32/125/134A/227EA/BUTANE/IPENTANE] (20.0/20.0/53.8/5.0/0.6/0.6 by mass) !!warning: estimated parameters!!

R454A [32/1234YF] (35.0/65.0 by mass)

R454B [32/1234YF] (68.9/31.1 by mass)

R454C [32/1234YF] (21.5/78.5 by mass)

R455A [CO2/32/1234YF] (3.0/21.5/75.5 by mass)

R456A [32/134A/1234ZEE] (6.0/45.0/49.0 by mass)

R457A [32/1234YF/152A] (18.0/70.0/12.0 by mass)

R458A [32/125/134A/227EA/236FA] (20.5/4.0/61.4/13.5/0.6 by mass) !!warning: estimated parameters!!

R459A [32/1234YF/1234ZEE] (68.0/26.0/6.0 by mass)

R459B [32/1234YF/1234ZEE] (21.0/69.0/10.0 by mass)

R460A [32/125/134A/1234ZEE] (12.0/52.0/14.0/22.0 by mass)

R460B [32/125/134A/1234ZEE] (28.0/25.0/20.0/27.0 by mass)

R460C [32/125/134A/1234ZEE] (2.5/2.5/46.0/49.0 by mass)

R461A [125/143A/134A/227EA/ISOBUTAN] (55.0/5.0/32.0/5.0/3.0 by mass) !!warning: estimated parameters!!

R462A [32/125/143A/134A/BUTANE] (9.0/42.0/2.0/44.0/3.0 by mass)

R463A [CO2/32/125/1234YF/134A] (6.0/36.0/30.0/14.0/14.0 by mass)

R464A [32/125/1234ZEE/227EA] (27.0/27.0/40.0/6.0 by mass) !!warning: estimated parameters!!

R465A [32/PROPANE/1234YF] (21.0/7.9/71.1 by mass) !!warning: estimated parameters!!

R500 [12/152A] (73.8/26.2 by mass)

R501 [22/12] (75.0/25.0 by mass)

R502 [22/115] (48.8/51.2 by mass)

R503 [23/13] (40.1/59.9 by mass)

R504 [32/115] (48.2/51.8 by mass)

R507A [125/143A] (50.0/50.0 by mass)

R508A [23/116] (39.0/61.0 by mass)

R508B [23/116] (46.0/54.0 by mass)

R509A [22/218] (44.0/56.0 by mass)

R510A [DME/ISOBUTAN] (88.0/12.0 by mass)

R511A [PROPANE/DME] (95.0/5.0 by mass)

R512A [134A/152A] (5.0/95.0 by mass)

R513A [1234YF/134A] (56.0/44.0 by mass)

R513B [1234YF/134A] (58.5/41.5 by mass)

R515A [1234ZEE/227EA] (88.0/12.0 by mass) !!warning: estimated parameters!!

R516A [1234YF/134A/152A] (77.5/8.5/14.0 by mass)

R469A [CO2/32/125] (35.0/32.5/32.5 by mass)

R470A [CO2/32/125/134A/1234ZEE/227EA] (10.0/17.0/19.0/7.0/44.0/3.0 by mass) !!warning: estimated parameters!!

R470B [CO2/32/125/134A/1234ZEE/227EA] (10.0/11.5/11.5/3.0/57.0/7.0 by mass)

R457B [32/1234YF/152A] (35.0/55.0/10.0 by mass)

R472A [CO2/32/134A] (69.0/12.0/19.0 by mass)

R515B [1234ZEE/227EA] (91.1/8.9 by mass) !!warning: estimated parameters!!

R466A [32/125/13I1] (49.0/11.5/39.5 by mass) !!warning: estimated parameters!!

R467A [32/125/134A/ISOBUTAN] (22.0/5.0/72.4/0.6 by mass)

# Using the Program

## Reference States (enthalpy and entropy differences)

For differences in enthalpy and entropy between the Refprop graphical interface and the Refprop Excel sample spreadsheet, or for differences in enthalpy and entropy between Refprop and tables of properties given in handbooks:&nbsp;

The absolute values of enthalpy, entropy, and energy at a single state point are meaningless.&nbsp; It is only the difference between two different state points that matter.&nbsp; Thus, the value for a single state point can be set to any arbitrary value.&nbsp; Many handbooks set the arbitrary state point so that the values of these properties are positive for most liquid or gas states.&nbsp; The user can change the values of the arbitrary state points by going to the _Options/Reference State_ menu.&nbsp;

For mixtures, there are additional options that can be set to affect the manner in which these properties are calculated.&nbsp; In the _Options/Reference State_ menu, there are two choices at the bottom of the menu on the far right.&nbsp; By changing this option, the two programs will then return the same values.&nbsp; This option can be permanently saved in the graphical interface by selecting _Options/Save Options_, and the saving the options under the file name defaults.prf.&nbsp; To change the default in the Excel file, press Alt-F11 to bring up the VB code.&nbsp; If the code does not appear, make sure the project explorer is visible (_View/Project Explorer_), and then click on modules and then on module1.&nbsp; Search for the call to SETREF, and change the second input from 2&amp; to 1&amp;.&nbsp; More information on this can be found in your Refprop\Fortran directory in the file SETUP.FOR under the SETREF subroutine. 

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

## Multiple and Metastable States

There are cases where an input state point can result in two separate valid states.&nbsp; The most common is temperature-enthalpy inputs.&nbsp; Viewing a P-H diagram (or a T-H diagram with very high pressures) will help show how there can be two valid states points for a given input.&nbsp; For example, nitrogen at 140 K and 1000 J/mol can exist at 6.85 MPa and at 60.87 MPa.&nbsp; When this situation occurs, Refprop returns the state with the higher density.&nbsp; For these state points , the character '&lt;' or '&gt;' can be added to the number (before or after) to find the lower or upper root, respectively.&nbsp; The example file REFPROP.XLS contains new code and an example of its use. These same characters can also be used to find metastable fluid states for temperature and pressure inputs.&nbsp; For example, the saturation pressure for nitrogen at 100 K is 0.778 MPa.&nbsp; Inputs of 100 K and 0.777 MPa will return a vapor state, but inputs of '100' for temperature and '0.777&gt;' for pressure will return a metastable liquid state.&nbsp; See [below](#convergence-failures-and-forcing-phase-calculations) for additional information about the use of the '&gt;' and '&lt;' symbols.

## Intro to Pure Fluids and 2-Phase States
Defining the state of a fluid normally requires two inputs, such as pressure-temperature, temperature-enthalpy, pressure-enthalpy, and so forth. This is true for the single-phase states and for two-phase solutions with mixtures of fluids. (Some inputs may have [two solutions](#multiple-and-metastable-states), this was described earlier.) For pure fluids, using inputs of pressure and temperature is not sufficient to describe the state of the fluid since both remain constant between the liquid and vapor states. Some other property, such as quality, enthalpy, or density, is required to specify the two-phase state point for the pure fluid. Once the quality is known, some of the other thermodynamic properties can be calculated with the equation _M=q*M<sub>vap</sub> + (1-q)*M<sub>liq</sub>_, where _M_ is the property of interest and _q_ is the quality. There are several properties that cannot be calculated this way, including the heat capacities, the speed of sound, and the transport properties. These quantities are undefined in the two-phase region for any fluid, except _Cv_, which is defined very differently than one would expect. There are some people who use a different formula to calculate the speed of sound in the two phase, but it is applicable only in certain specific applications. In these situations, it is best to consider the properties of the liquid and of the vapor separately, and how they interact with the application being developed.

As an example, consider _Cp_, which could be calculated from any equation of state using the quality, but thermodynamically is not defined for a two-phase mixture. _Cp_ is the heat capacity along an isobaric process and is equal to _dH/dT_ at constant _p_. Since pressure and temperature do not change across the two phase for a pure fluid, then that means _Cp_ would be equal to infinity because the heat capacity changes but the temperature does not, thus the definition makes it thermodynamically impossible to calculate it.&nbsp; The only place that _Cp_ can be infinity is at the critical point.

## Intro to Mixtures and 2-Phase States.
Dealing with saturation or 2-phase states in Refprop can be a bit confusing when first using the program. The text and pictures given below address some of these issues to help users better understand how to obtain properties from the program.

As an example, consider the methane/ethane system with a molar composition of 50% methane and 50% ethane. For mixtures in the 2-phase (or at saturation), it is always best to turn on the composition columns (under Properties/Mixtures/Composition). For saturation states, bring up a saturation table [under Calculate/Saturation Points (at equilibrium)]. The table shows two entries for each property. It is very important to place the known property under the correct column. For example, the input property for bubble points (liquid state) should be placed under the “Liquid” column; dew points (vapor state) should be placed under the “Vapor” column. An example picture is given below. On the first line, 150 K was entered under the liquid column. This calculated a liquid bubble point pressure of 0.552 MPa. The liquid phase mole fractions show the input composition of 0.5/0.5. The vapor phase mole fractions show that the first bit of vapor will have a composition of 0.987/0.013. In the second row, 150 K was entered in the vapor column, producing a dew point pressure of 0.019 MPa. The vapor mole fractions show the input composition of 0.5/0.5. The first drop of liquid to form will have a mole fraction of 0.0074/0.9926.

<img src="https://trc.nist.gov/refprop/FAQ/image002.jpg">

For 2-phase states, turn on the option labeled “Bulk, liquid, and vapor properties” under Options/Properties. Then bring up a table under Calculate/Specified State Points. The information obtained above shows that pressures for 2-phase state points at 150 K will lie between 0.019 and 0.552 MPa. Enter 150 K in the temperature column and 0.3 MPa in the pressure column. The program will then calculate the 2-phase point. The output shows that the overall composition of the mixture is still 0.5/0.5. The composition of the fluid in the liquid phase will be 0.246/0.754 and that of the vapor phase will be 0.972/0.028. This is shown in the picture below.

<img src="https://trc.nist.gov/refprop/FAQ/image006.jpg">

The Excel sample spreadsheet included in the Refprop directory shows an example for the mixture R410A (between rows 70 and 98).

# Programming

## Changing Fluids and Calling SETUP Multiple Times
Calling SETUP (or SETUPdll) many many times can result in a memory loss error and in a substantial decrease of computation speed. In many situations, it is better to load all of the fluids at the start of the program, calling SETUP only once. You can then switch between fluids through the use of calls to SETNC and PUREFLD. The example below shows how this can be done for a mixture combined with several pure fluids. If two different mixtures are required, load all fluids and set the composition to 0 for those fluids not involved in a particular application. This could easily be done by using two different arrays for the composition.

- [EX-MULTI.FOR](https://trc.nist.gov/refprop/FAQ/EX-MULTI.FOR)

## Calculation of the Critical Point and Saturation States in the Critical Region
The calculation of saturation states requires complex algorithms and significant processor time. Version 9.1 introduced the subroutine SATSPLN, which can be called directly after the call to SETUP, and generates spline curves that represent the various properties that are required as initial guesses to the saturation algorithms in order to increase convergence and speed. This new subroutine, however, can take several seconds to implement, and should only be done once at the very beginning. If the composition of the fluid changes significantly, and if you notice problems with convergence, you may need to call it again with the new composition. Although the routine gives estimates only for saturation states, single phase calculations will also be much faster since a call to the saturation routine is required to determine the phase of the input state. The routine is called like this:
```
call SATSPLNdll (x, ierr, herr, 255)
```
(without the “dll” and 255 if calling directly from FORTRAN). Once the splines are generated, you can call the CRITP, MAXT, and MAXP routines to get the critical point and maximum values along the saturation lines (see the SAT_SUB.FOR file for details). The new subroutine SATGV can be called when the SATT, SATP, or SATTP routines fail in the critical region. For graphing the saturation lines without the need for states at any specific temperature or pressure, the SATGV routine can be called with density as the input, ranging from very low values in the gas phase, through the critical region, and then to high densities in the liquid.

In Excel or MATLAB, the call to SATSPLN is included in the code, but is deactivated. To activate this call, enter the code (press Alt-F11 in Excel) and search for this subroutine in the file (under “Modules” in Excel). Then read the comments above the line and activate the routine by removing the first character on that line. You may need to exit and restart Excel or MATLAB for this to work.

## Calculation of Phase Diagrams for Plotting Purposes
The calculation of the entire phase diagram can be difficult with the routines that require either temperature or pressure as inputs due to the second root in the retrograde region. An alternative routine called SATGV is available that makes this process simple through the use of density as the input; see the file Manual.txt in your Refprop\Fortran directory for a list of the inputs and outputs. In order to use this routine, you must first call subroutine SATSPLN, [see the details above](#calculation-of-the-critical-point-and-saturation-states-in-the-critical-region). Subroutine SATGV can then be called like this:
```
call SATGV (t,p,z,vf,d,1,6,1,rhox,rhoy,x,y,ierr,herr)
```
The inputs are composition in the z array and density (either vapor or liquid phase) in the variable d. The variable vf is double precision and should be set to 1.0. The routine will then return the temperature and pressure at this density. To obtain data points for the entire phase diagram, call this routine starting at a very low density in the vapor phase, and slowly increment the density until you are deep in the liquid phase at low temperatures. The other outputs are not necessary for this application.

## FLSH Routines and Metastable States

For subroutines such as ENTHAL, ENTRO, CVCP, etc., where temperature and density are the input properties, the output property data will differ from those returned when using routines such as PHFLSH or TPFLSH when in the two-phase region.&nbsp; Any routine (except TDFLSH) that uses temperature and density as inputs will return what appears to be erroneous results in the two-phase region.&nbsp; These results&nbsp;actually show calculations directly from the equation of state without taking into account the fact that the mixture has split into two phases.&nbsp; The results would be valid for such situations where a substance is heated beyond its boiling point (a metastable state), but without boiling (such as water in a glass container being heated in a microwave).&nbsp; The results eventually end up at the spinodal, beyond which it is no longer possible to increase the temperature without boiling the liquid.&nbsp; Thus, for typical results these routines should never be used for two-phase calculations, rather the FLSH routines should be called.&nbsp; The flash routines return the properties in the liquid and vapor states, and these can be used to call routines such as THERM, CVCP, TRNPRP, etc., with the associated liquid or vapor density at the saturated temperature.

# Error Messages

## Convergence Failures and Forcing Phase Calculations

When using mixtures, error messages will sometimes be reported when Refprop fails to converge during an iteration, usually during the calculation of a VLE state close to the critical point.&nbsp; In some situations you may know that the point is in the single phase and wish to force the calculation in spite of the error message.&nbsp; This can be done with the '&gt;' and '&lt;' symbols.&nbsp; When one of these is attached to a number in the Specified State Points table, Refprop will assume that the point is in the liquid phase when '&gt;' is attached and in the vapor phase when '&lt;' is attached.&nbsp; Care must be taken because metastable states will be returned in the point is in the two phase.&nbsp; When a state point is above the critical point but Refprop reports a nonconvergence, you can use either of these symbols to force the calculation.&nbsp; For example, a 0.5/0.5 mixture of methane/propane will report a nonconvergence at 300 K and 10 MPa.&nbsp; A P-rho diagram shows that the point is above the critical pressure.&nbsp; Entering '300' for temperature and '10&gt;' for pressure will return the valid state point at 10.826 mol/l. For programming convergence errors, see [above](#calculation-of-the-critical-point-and-saturation-states-in-the-critical-region).

## Mixture Error Messages
The error message &quot;<span style='color:red'>No mixture data are available for one or more binary pairs in the specified mixture. The mixing parameters have been estimated.</span>&quot; (message #-117) occurs when an interaction parameter for two different fluids is not available in the program.&nbsp; The most common reason for this occurrence is a lack of experimental data to describe VLE, densities, and so forth for the binary pair.&nbsp; In other situations, such as many mixtures with water, interaction parameters have not been fitted to the REFPROP model even though data exist.&nbsp; An estimation scheme is available in the program to approximate one of the interaction parameters that helps improve bubble and dew point pressures.&nbsp; This error message indicates that you should be aware that calculated properties are estimates only.&nbsp; For similar fluids, especially among the refrigerants, the scheme works fairly well.&nbsp; It breaks down with dissimilar fluids and eventually the scheme will produce large interaction parameters and will report the error message&nbsp; &quot;<span style='color:red'>No mixture data are available for one or more binary pairs in the specified mixture. The mixture is outside the range of the model and calculations will not be made.</span>&quot;

# Fluids

## List of fluids

The following is a list of fluids that come with REFPROP

## GERG-2008 Equation of State for Natural Gas Mixtures
The current equation of state for calculating the properties of natural gas mixtures is the GERG-2008 equation (GERG is the European Gas Research Group). This equation is based on an excess Helmholtz energy approach using pure fluid equations of state (either those specified by GERG, or the current standards that have slightly higher accuracies) and a mixture model that specifies the excess contribution. The 2008 version is an extension of the 2004 version, containing the additional fluids nonane, decane, and hydrogen sulfide in addition to methane, nitrogen, carbon dioxide, ethane, propane, n-butane, isobutane, n-pentane, isopentane, n-hexane, n-heptane, n-octane, hydrogen, oxygen, carbon monoxide, water, helium, and argon. The 2008 edition also replaced the pure fluid equations of state for isopentane and carbon monoxide with published versions. These two models are fully described in the following publications:

Kunz, O. and Wagner, W., The GERG-2008 Wide-Range Equation of State for Natural Gases and Other Mixtures: An Expansion of GERG-2004, to be submitted to J. Chem. Eng. Data, 2012.

Kunz, O., Klimeck, R., Wagner, W., and Jaescke, M., The GERG-2004 Wide-Range Equation of State for Natural Gases and Other Mixtures: GERG Technical Monograph 15 and Fortschr.-Ber. VDI, Reihe 6, Nr. 557, VDI Verlag, Düsseldorf, 2007. [link to PDF](https://www.gerg.eu/public/uploads/files/publications/technical_monographs/tm15_04.pdf)

The natural gas equation of state has been expanded to include ethylene, propylene, methanol, ethanol, toluene, benzene, cyclohexane, sulfur dioxide, ammonia, dodecane, acetone, and butylene. When selecting the option to use the full GERG-2008 equation of state (either through the GUI or by calling the “GERG2004” subroutine), the use of these additional fluids is still allowed. This is not the same as when the AGA-8 equation of state is selected, in which case only the original 21 fluids (same as those in the GERG-2008 model) are allowed.

## HFO-1234yf, 1234ze(E), 1234ze(Z), 1233zd(E), and Refrigerant Mixtures.
Equations of state are now available for these fluids. R1234yf and R1234ze(E) were included in versions 9.0 and 9.1, but version 9.0 incorrectly used the NBP reference state instead of IIR, as done with all other refrigerants.  The file name for R1234ze(E) has been renamed as ``R1234ZEE.FLD`` to avoid confusion with R1234ze(Z). You should delete your old ``R1234ZE.FLD`` file when downloading the fluid file for R1234ze(E) (the contents of the fluid file have not changed). The fluid files are located below and should be placed in your ``Refprop\Fluids`` directory for both versions 9.0 and 9.1.  This fluid file works with both versions 9.0 and 9.1 of Refprop.  R1234yf only needs to be downloaded if you are using version 9.0. The fluid files included in version 9.0 incorrectly used the NBP reference state.

- [R1234YF.FLD](https://trc.nist.gov/refprop/FAQ/R1234YF.FLD) (uploaded June 6, 2012 with updated transport equations)
- [R1234ZEE.FLD](https://trc.nist.gov/refprop/FAQ/R1234ZEE.FLD) (uploaded June 6, 2012 with new CAS number and updated transport equations. This is for R1234ze(E)). 
- [R1234ZEZ.FLD](https://trc.nist.gov/refprop/FAQ/R1234ZEZ.FLD) (uploaded January 12, 2015 with transport equations. This is for R1234ze(Z)).
- [R1233ZDE.FLD](https://trc.nist.gov/refprop/FAQ/R1233ZDE.FLD) (uploaded November 9, 2015)

New refrigerant predefined mixture files are available, such as that for R-448A. To add these to Refprop, unzip the file below in your ``Refprop\Mixtures`` directory:

- [NEWMIX.ZIP](https://trc.nist.gov/refprop/FAQ/NEWMIX.ZIP) For mixtures with R1234ze(E), you will need to download the renamed file above for this fluid.

«On November 10, 2015, we released a new mixture file (``HMX.BNC``) that now contains mixing parameters for every binary of the fluids R-32, R-125, R-134a, R-1234yf, and R-1234ze(E). With these, mixtures such as R-448A that contain all five of these no longer use the predictive methods to get the interaction parameters. This file works with both versions 9.0 and 9.1 of Refprop. If you would like this file, please contact us. 

## Humid Air
Although Refprop allows mixtures of nitrogen, argon, oxygen, and water as a consequence from the addition of the new natural gas mixture model, calculations for moist air have not been tested yet.&nbsp; It is likely that calculated values are reasonable, however, Refprop may not return results because the saturation routines may fail.&nbsp; The program calls the saturation routines to determine if the state is vapor, liquid, or two-phase.&nbsp; If you know that your state point is in the vapor phase, you can avoid the call to the saturation routines by using TPRHO instead of TPFLSH.&nbsp; The Fortran file FLSH_SUB.FOR gives additional information concerning the inputs to these routines.&nbsp; In the graphical interface, see the section [below](#convergence-failures-and-forcing-phase-calculations) on forcing phase calculations. A moist air mixture could be made up starting with the composition of dry air used in Refprop:&nbsp; 0.7812 nitrogen, 0.0092 argon, and 0.2096 oxygen (on a mole basis).&nbsp; A small amount of water could be added to this composition and then normalized.

## Mixture Models
The LJ6 mixture model has been replaced with KW0. This was necessary to implement a more efficient and stable algorithm. For most situations, this change will be completely transparent, and calculated values will not change. For those that have fitted mixture parameters to their own data (e.g., for proprietary mixtures), you can simply insert the lines from your old ``HMX.BNC`` file for a particular binary mixture into the new ``HMX.BNC`` file that comes with 9.1 (be sure that no other block exists for that mixture). When running SETUP, you may receive an error message about the LJ6 mixture model not found (``ierr = –117``); this should be ignored because the values are later internally converted to the KW0 model (this error message will be removed in future versions). Conversion of LJ6 to KW0 converts the LJ6 xeta parameter (for the reducing temperature) to the KW0 gammaT and betaT values. The numerical values of the parameters are different, but the calculated properties will be identical. For those wishing to fit mixing parameters to new experimental VLE data, XR0 should be used for the fitting process and only the gammaT value should be fitted.

## Solids
The REFPROP program does not know the location of the solid-liquid interface&nbsp;for a mixture.&nbsp; For many of the pure fluids, melting line auxiliary equations are available and can be used to calculate liquid properties at the point where solids begin to form and can be used to keep the program from entering the solid phase.&nbsp; When melting lines are not available, the program uses the liquid phase density at the triple point as the maximum density, thus valid states between this density and the melting line will not be available.&nbsp; The location of the solid-liquid boundary can be calculated under the Calculate/Saturation Tables option.&nbsp; This option will also print out the vapor phase properties along the sublimation line if requested (and if an auxiliary equation is available).

## Transport Properties for Nitrogen, Oxygen, Argon, and Air
The transport properties for nitrogen, argon, and oxygen in version 7.0 did not include the thermal conductivity enhancement for the critical region and did not represent the experimental data as well as possible.&nbsp; The transport equations for these fluids have been redone and now represent the data to within their experimental uncertainties.&nbsp; The publication below documents the new equations and shows all of the comparisons to data.

- [N2-Ar-O2 Transport equations documentation](https://trc.nist.gov/refprop/FAQ/NAO.PDF)

## Transport Properties for Mixtures
The transport properties for mixtures can be calculated (or estimated) for nearly all mixtures, except for: mixtures with more than 5% (by mole) water, and mixtures with alcohols. The user should be cautioned that experimental data coverage for transport properties of mixtures are very sparse, and the extended corresponding states approach for transport properties is used in fully predictive mode for many mixtures. Please see [Chicester and Huber's NIST internal report](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=832196) for a description of this methodology.

## Transport Properties for Pseudo-pure Fluids; Adding Pure Fluids to a Mixture Setup
The ability to load both a mixture and a pure fluid not associated with the mixture is now possible. For example, a natural gas mixture of methane, ethane, and propane could be loaded, along with R134a, which is not part of the mixture. By calling SETNC and PUREFLD, properties for either the mixture or the pure fluid can be made without ever calling SETUP more than once at the beginning. This is also useful for calculating transport properties when the pseudo-pure fluid equation of state is in use (for R-404A, R-407C, R-410A, and R-507A). Since transport properties are not available in the PPF files, the full mixture has to be loaded as well. The example program below gives all the details.

- [PPF-EX.FOR](https://trc.nist.gov/refprop/FAQ/PPF-EX.FOR)

## Required Fluids for Distribution
There are several fluid files that Refprop accesses in order to run properly.&nbsp; These are ``NITROGEN.FLD``, ``PROPANE.FLD``, ``R134A.FLD``, and ``C12.FLD`` (dodecane).&nbsp; These fluids are used as reference fluids in extended corresponding states methods employed in Refprop to predict transport properties for some instances.&nbsp; These fluids (and the hmx.bnc file) should be distributed in addition to those required in a particular application if the Refprop routines have been incorporated into a software package. Note that a licensing agreement must be purchased before distributing your software to others.

## Resolving Problems Linking with Excel

Before reading the items below, we highly advise you to either uninstall and reinstall the REFPROP program outside of the Windows system directories (such as on a different drive or in your Users directory) or to simply move the installed directory outside the Windows protected locations.  This will decrease many of the frustrations caused by not having control over saving and changing files.  If you move the directory, see the information below about changing the path and the RPprefix variables.

Additional information not included below can be found at https://github.com/usnistgov/REFPROP-wrappers/tree/master/wrappers/Excel

1.  Open the REFPROP.XLS file to see if the calculations work in that file.

2.  Check the path statement to ensure that the directory where Refprop was installed is included in the path.  This can be found under Control Panel/System/Advanced System Settings/Environment Variables.  

3.  Check carefully the RPprefix environment variable found in the same location as the path (as described in #2 directly above).  This variable may appear in both the top and bottom sections, if so, delete the one in the bottom section.  The path it lists may not be the correct path to the Refprop directory, sometimes it may show "C:\Program Files\REFPROP" when it actually should be "C:\Program Files (x86)\REFPROP".  Additional information is given here: https://github.com/usnistgov/REFPROP-wrappers/issues/298

4.  In your Users directory is a hidden system directory called ``AppData``.  Check if you have the following subdirectory:  "AppData\Local\VirtualStore\Program Files\REFPROP".  If so, delete that folder.  Look for another subdirectory in your Users directory labeled "AppData\Roaming\Microsoft\addins" and check for any Refprop files there.  If found, delete them.

5.  Do a full system search for REFPRP64.DLL and REFPROP.DLL, including Windows and hidden directories, and delete anything that is not in your newly installed directory for version 10.  (In one situation, a new computer was purchased and all files from the old computer were copied over, including the REFPRP64.DLL file from version 9.1; somehow Windows latched on to that file rather than the new one from version 10.)

6.  Go to the REFPROP.XLA file (assuming that it has already been selected as an Add-in) by pressing Alt-F11.  Open up the item labeled REFPROP.XLA in the list on the left, click on Modules, and then on Refprop10Code.  Near the top you will find …Sub REFPROPdll Lib "REFPRP64.DLL"…  Change this to …Sub REFPROPdll Lib "c:\Program Files (x86)\REFPROP\REFPRP64.DLL"…  If using a 32 bit version of Excel, add the same path to the line two lines below this one.

7.  If this works, you will need to save the .XLA file to keep the changes permanent.  Go to File/Save.  If your computer does not allow you to overwrite the file in the Program Files directories, sometimes deleting the old one first and then saving the new one works, but be sure to save it as a 2003 Excel add-in with an extension of .xla.  You could also save it as a .xlam file, but you will need to remove the REFPROP.XLA file from your add-ins, and then add this new file as its replacement.  See the “Welcome” screen in the REFPROP.XLS file for more information.

8.  When Excel cannot find the DLL, cells will show “NAME”.  When it has been found but not working, cells will show “VALUE”.  Check if the problems are simply that the fluid files cannot be found by entering the command =REFPROP("DLL#"). If this works but no other commands do, the problem is usually fixed by correcting the RPprefix variable (described above).

9.  If your spreadsheet contains Refprop 9.1 commands, you can either convert them with a macro (see the “Welcome” screen in the REFPROP.XLS file for more information), or (but not preferably) you can use the add-in from version 9.1, which can be found here:
https://trc.nist.gov/refprop/10-PATCH/REFPRP91.XLA.

10.  The macro for converting from 9.1 to 10 will only convert items that start as “=ENTHALPY(…”.  We recently updated this macro to not include the equal sign so that all commands will be converted properly.  The new files are located here:
https://trc.nist.gov/refprop/10-PATCH/REFPROP.XLS
https://trc.nist.gov/refprop/10-PATCH/REFPROP.XLA
If you cannot access or save these files, you can add a new macro to your worksheet called Refprop91code and simply add the text from the file below.
https://trc.nist.gov/refprop/FAQ/REFPROP91macros.txt

12.  The macro to do this conversion does not show up in the View Macros option in Excel.  Again, see the “Welcome” screen in the REFPROP.XLS file for more information.

13.  Some users have reported that the original Office was installed via the "Microsoft Store", which installs as a “Microsoft App” rather than installing the full software.  The installation via the “Microsoft Store” is often done when purchasing a computer with Office pre-installed.  Uninstalling office and reinstalling from office.com/myaccount may solve any issues.

14.  If problems still persist, it would be very useful if we can log into your machine remotely to try to find the problem and then include the solution here.

15.  If you find errors in the directions above, and especially if you find better solutions, please contact us.

16.  The best way to contact us is to use the github system so that others can see the problems and solutions.  You will find that here:  https://github.com/usnistgov/REFPROP-issues/issues.  This website is loaded with answers to many other Refprop questions; be sure to search through the issues, and if you wish, change your Watch status so that you receive updates every time something is posted.  We try to put up much more detailed answers there than would be received by a simple email request.  For linking issues with other programs, be sure to look at https://github.com/usnistgov/REFPROP-wrappers/issues.

17.  For very simple comments such as misspellings, or for private conversations with us, our email addresses are   Eric.Lemmon@nist.gov  and   Ian.Bell@nist.gov

18.  If the equations work in the REFPROP.XLS file but not in a new blank workbook (the error #VALUES is returned), try adding the file paths of the Refprop DLLs to the REFPROP.XLA file.  Simply search for Lib "REFPROP.DLL" and change this to something like Lib "C:\Program files (x86)\REFPROP\REFPROP.DLL", or wherever the DLLs for Refprop are located.  Do this for the REFPRP64.DLL occurrence as well.

## Other Issues Related to the Use of Refprop in Excel

9.1 to 10.0 Conversions: If the macro (called RefpropConversion in the ConvertRefprop9to10 Module) for converting existing Excel files with REFPROP 9.x or earlier to the new REFPROP 10.0 format does not appear when trying to View Macros in Excel, first view the Welcome page in the REFPROP.XLS file.  If the information there does not help, copy the ConvertRefprop9to10 Module under REFPROPExcelSpreadsheet in the REFPROP.XLA file to the Modules section of your own spreadsheet, which will hopefully allow you to see and run it.  If you Ctrl+click or Shift+click to select multiple spreadsheet tabs, then run the macro, all of the selected tabs will update.  Once done, the Module can be deleted from your spreadsheet.

10.0 to 9.1 Back Conversions:  A new macro called RefpropBackConversionto91 is now available in case you wish to undo what happened when you ran the forward conversions.

If you experience that the REFPROP Addin link in Excel breaks down when used on SharePoint/OneDrive or Dropbox after a short time, see https://github.com/usnistgov/REFPROP-wrappers/issues/360.  If you have experience with this and can us with further information, please post it on that github site at the bottom of issue #360.

New files:  You can find the updated files at [https://github.com/usnistgov/REFPROP-wrappers/tree/master/wrappers/Excel](https://github.com/usnistgov/REFPROP-wrappers/tree/master/wrappers/Excel).

9.1 Macros:  To continue using the commands from version 9.1 with the new 10.0 DLL, download the following xla file and include it as an Excel add-in: [https://trc.nist.gov/refprop/10-PATCH/REFPRP91.XLA](https://trc.nist.gov/refprop/10-PATCH/REFPRP91.XLA)

Last modified: March 29, 2021.

[Go to the source of this file](https://github.com/usnistgov/REFPROP-docs/blob/nist-pages/index.md)

