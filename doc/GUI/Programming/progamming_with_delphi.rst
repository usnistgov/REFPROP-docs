.. _progamming_with_delphi: 

**********************
Progamming with Delphi
**********************

**Progamming with Delphi**

General information for using the REFPROP DLL with Delphi:


1) All the variables must be passed by address (not just the output); for example:

type
 T_Chaine10000 = Array[0..10000] of Char;
 T_Chaine255 = Array[0..255] of Char;
 T_Chaine3 = Array[0..3] of Char;

procedure SETUPdll (var nc: Integer; // number of components
 var hfiles: T_Chaine10000 ; // fluid file names
 var hfmix: T_Chaine255; // mixture file name
 var hrf: T_Chaine3; // reference state
 var ierr: Integer; // error message number
 var herr: T_Chaine255); stdCall; // error message string
 external 'refprop.DLL';

procedure TPFLSHdll(var t: Double; // temperature [K]
 var p: Double; // pressure [kPa]
 var x: Double; // mole fraction array
 var d: Double; // molar density [mol/L]
 var Dl: Double; // liquid density [mol/L]
 var Dv: Double; // vapor density [mol/L]
 var xliq: Double; // liquid mole fraction array
 var xvap: Double; // vapor mole fraction array
 var q: Double; // quality
 var e: Double; // internal energy [J/mol]
 var h: Double; // enthalpy [J/mol]
 var s: Double; // entropy [J/mol-K]
 var Cv: Double; // isochoric heat capacity [J/mol-K]
 var Cp: Double; // isobaric heat capacity [J/mol-K]
 var w: Double; // speed of sound [m/s]
 var ierr: Integer; // error message number
 var herr: T_Chaine255); stdCall; // error message string
 external 'refprop.DLL';


2) The software using the DLL must declare x as an array [0..19]; for example:

 x: Array[0..19] of Double;

 // initialization (for nc = 3)
 x[0]:=0.7812;
 x[1]:=0.0092;
 x[2]:=0.2096;

 // calculate d from T and P by calling the DLL
 TPFLSHdll (t, p, x[0], d, Dl, Dv, xliq[0], xvap[0], q, e, h, s, Cv, Cp, w, ierr, herr);


3) hfiles can be initialized with the '|' separator between each component; for example:

 type
 T_Chaine10000 = Array[0..10000] of Char;
 var
 hfiles: T_Chaine10000;
 hfiles_str: String;

 hfiles_str:= 'fluids\R22.FLD|fluids\R152A.FLD|fluids\R124.FLD|';
 StrPCopy(hfiles, hfiles_str);



