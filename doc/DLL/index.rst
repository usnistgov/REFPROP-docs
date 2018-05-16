


***********
REFPROP DLL
***********


REFPROP's DLL (shared library)
==============================

Depending on your platform, you either end up with REFPROP.DLL or REFPRP64.dll 

List of High-Level API
----------------------

- :f:func:`REFPROPdll`
- :f:func:`REFPROP1dll`
- :f:func:`ALLPROP1dll`
- :f:func:`ALLPROPSdll`
- :f:func:`ALLPRP200dll`
- :f:func:`ABFLSHdll`
- :f:func:`GETENUMdll`
- :f:func:`ERRMSGdll`
- :f:func:`PHASEdll`
- :f:func:`SETFLUIDSdll`
- :f:func:`SETMIXTUREdll`
- :f:func:`SETPATHdll`
- :f:func:`FLAGSdll`

.. f:subroutine:: ABFL1dll (a, b, z, kph, ab, Dmin, Dmax, T, P, D, ierr, herr, ab_length, herr_length)

    
    General single-phase flash routine given two inputs and composition.
    Valid input properties are temperature, pressure, density, energy,
    enthalpy, or entropy.  The character string ab specifies the inputs,
    which can be T, P, D, E, H, S.  An input of 'EH' (or 'HE') is
    not supported.  The letters in this string must be uppercase.
    
    Care must be taken when sending inputs of T, P, or D, so that the same
    variable is not sent twice.   For example, the following would be wrong::
    
        call ABFL1 ('TH',T,H,z,kph,0,0,Dmin,Dmax,T,P,D,ierr,herr)
    
    Rather, the following are examples of correct inputs::
    
        call ABFL1 ('TH',T,H,z,kph,0,0,Dmin,Dmax,tt,P, D,ierr,herr)
        call ABFL1 ('TP',T,P,z,kph,0,0,Dmin,Dmax,tt,pp,D,ierr,herr)
        call ABFL1 ('DS',D,S,z,kph,0,0,Dmin,Dmax,T, P,dd,ierr,herr)
    
    This routine accepts only single-phase inputs, it is intended primarily
    for use with the more general flash routine ABFLSH, but can be called
    independently for increased calculation speed if the inputs are
    know to be single-phase.  This will avoid the call to the flash routines
    to determine the phase of the inputs.  If this routine is called, but
    the inputs are 2-phase, either an incorrect root or a metastable state
    will be returned (which is OK if the metastable state is desired).
    
    :p double a [in]: First property (either temperature, pressure, density, entropy) 
    :p double b [in]: Second property (pressure, density, energy, enthalpy, or entropy) Possible inputs for these two variables are
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p int kph [in]: Phase flag
    :p char ab [in]: Character*2 string defining the inputs, e.g., 'TH' or 'PS' Valid characters are T, P, D, E, H, S
    :p double Dmin [in]: Lower bound on density [mol/L] (for T inputs) 
    :p double Dmax [in]: Upper bound on density [mol/L] (for T inputs) 
    :p double T [out]: Temperature [K] 
    :p double P [out]: Pressure [kPa] 
    :p double D [out]: Molar density [mol/L] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int ab_length: length of variable ``ab`` (default: 2)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``kph`` flags

        :1: Liquid  (kph is only needed for TP inputs)
        :2: Vapor

        ``ierr`` flags

        :0: Successful
        :248: Single-phase iteration did not converge


.. f:subroutine:: ABFL2dll (a, b, z, kq, ksat, ab, Tbub, Tdew, Pbub, Pdew, Dlbub, Dvdew, ybub, xdew, T, P, Dl, Dv, x, y, q, ierr, herr, ab_length, herr_length)

    
    General flash calculation given two inputs and composition.  Valid
    properties for the first input are temperature, pressure, and density.
    Valid properties for the second are pressure, density, energy, enthalpy,
    entropy, or quality.  The character string ab specifies the inputs.
    
    This routine accepts only two-phase states as inputs; it is intended
    primarily for use by the general flash routines such as THFLSH or
    TSFLSH.  It may be called independently if the state is known to be
    two-phase.  But beware - this routine does not check limits, and it
    will be significantly faster than TSFLSH, etc., when the bubble
    and dew point limits can be provided (ksat=1 option).
    
    This routine calls TPFL2 within a secant-method iteration to find
    a solution.  Initial guesses are based on the liquid density
    at the bubble point and the vapor density at the dew point.
    
    :p double a [in]: First property (either temperature, pressure, or density) 
    :p double b [in]: Second property (pressure, density, energy, enthalpy, entropy, or quality)
    :p double z(20) [in]: Overall composition (array of mole fractions) 
    :p int kq [in]: Flag specifying units for input quality when b=quality
    :p int ksat [in]: Flag for bubble and dew point limits
    :p char ab [in]: Character*2 string defining the inputs, e.g., 'TD' or 'PQ' 
    :p double Tbub [in]: Bubble point temperature [K] at (P and x=z) 
    :p double Tdew [in]: Dew point temperature [K] at (P and y=z) For temperature inputs
    :p double Pbub [in]: Bubble point pressure [kPa] at (T and x=z) 
    :p double Pdew [in]: Dew point pressure [kPa] at (T and y=z) For either case
    :p double Dlbub [in]: Liquid density [mol/L] at bubble point 
    :p double Dvdew [in]: Vapor density [mol/L] at dew point 
    :p double ybub(20) [in]: Vapor composition (array of mole fractions) at bubble point 
    :p double xdew(20) [in]: Liquid composition (array of mole fractions) at dew point 
    :p double T [out]: Temperature [K] (if not an input) 
    :p double P [out]: Pressure [kPa] (if not an input) 
    :p double Dl [out]: Liquid density [mol/L] at bubble point 
    :p double Dv [out]: Vapor density [mol/L] at dew point 
    :p double x(20) [out]: Liquid composition (array of mole fractions) 
    :p double y(20) [out]: Vapor composition (array of mole fractions) 
    :p double q [out]: Vapor quality, the definitions of the values for q are given in the ABFLSH routine. 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int ab_length: length of variable ``ab`` (default: 2)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``kq`` flags

        :1: Quality on molar basis (moles vapor/total moles)
        :2: Quality on mass basis (mass vapor/total mass)

        ``ksat`` flags

        :0: Dew and bubble point limits computed here
        :1: Must provide values for the following: For pressure and density inputs

        ``ierr`` flags

        :0: Successful
        :223: Bubble point calculation did not converge
        :224: Dew point calculation did not converge
        :226: 2-phase iteration did not converge


.. f:subroutine:: ABFLSHdll (ab, a, b, z, iFlag, T, P, D, Dl, Dv, x, y, q, e, h, s, Cv, Cp, w, ierr, herr, ab_length, herr_length)

    
    General flash calculation that handles all inputs of T, P, D, h, e, s, and q.
    
    This includes both blind flash calculations, and situations where
    the phase is known to be liquid, vapor, or 2-phase, and thus the
    calculation time will be much faster.
    
    Many of the 2-phase flash routines can accept initial estimates to
    decrease calculation time and increase convergence.  ABFLSH does
    not accept these, and ABFL2 or other routines will need to be called
    to use the initial estimates.  These routines end in the letters FL2.
    
    Notes:
    
    * Cp and w are not defined for 2-phase states; the flag -9999980 is returned.
    * Cv for 2-phase states is not calculated (use CV2PK); the flag -9999990 is returned.
    
    **Information on ab**
    
    Valid character codes for ab are:
    
    - T - Temperature [K]
    - P - Pressure [kPa]
    - D - Density [mol/L or kg/m^3]
    - E - Internal energy [J/mol or kJ/kg]
    - H - Enthalpy [J/mol or kJ/kg]
    - S - Entropy [J/mol-K or kJ/kg]
    - Q - Quality [mol/mol or kJ/kg]
    
    * For example, 'PH' indicates pressure and enthalpy inputs.
    * For saturation properties, use codes of 'TQ' or 'PQ' for ab, and send b=1
    * The order of the letters does not matter, for example 'DH' = 'HD'
      for saturated vapor values and b=0 for saturated liquid values.
    
    **Information on iFlags**
    
    Three flags are currently allowed, and are sent combined in a three digit
    integer value.  The digit on the right is the mass flag (iMass) defined below, the
    middle digit is the phase flag (kph), and the digit on the left specifies other flags (k).
    
    * iMass: Molar or mass flag
        - 0 - All inputs and outputs are given on a mole basis.
        - 1 - All inputs and outputs are given on a mass basis.
        - 2 - All inputs and outputs are given on a mass basis except
          composition, which is given on a mole basis.
    * kph: Phase flag (except for inputs of Q)
        - 0 - Unknown phase, the saturation routines will be called to determine the phase, which
          adds a substantial amount of time needed to calculate the properties.
        - 1 - State point is in the liquid phase, do not call saturation routine to determine state.
        - 2 - State point is in the vapor phase, do not call saturation routine to determine state.
        - 3 - State point is in the two-phase region.
    * kr,kq: Other flags for inputs of quality and either temperature or pressure (kq flag)
        - 1 - Quality on a molar basis (moles vapor/total moles) (default, the value of 1 is not necessarily needed)
        - 2 - Quality on a mass basis (mass vapor/total mass);
          For inputs of T and either h or e (kr flag)
        - 3 - Return lower density root
        - 4 - Return higher density root
    
    Examples:
    
    * 000 - Default - Phase of state is unknown, molar units will be used everywhere,
      higher density root will be returned.
    * 001 - Use mass based properties for everything except composition.
    * 011 - State is in the liquid, properties are mass based.
    * 300 - Return the lower density root for TH or TE inputs.
    * 200 - All inputs are on a mole basis, but quality is sent on a mass basis.
    
    :p char ab [in]: Character string composed of two letters that indicate the input properties.
    :p double a [in]: Value of the property identified by the first letter in ab 
    :p double b [in]: Value of the property identified by the second letter in ab 
    :p double z(20) [in]: Composition (array of mole fractions) For TQ and PQ inputs, send b=-99 for melting line states and b=-98 for sublimation line states.
    :p int iFlag [in]: Multiple flags combined into one variable (see above) 
    :p double T [out]: Temperature [K] 
    :p double P [out]: Pressure [kPa] 
    :p double D [out]: Density [mol/L or kg/m^3] 
    :p double Dl [out]: Molar density of the liquid phase [mol/L or kg/m^3] 
    :p double Dv [out]: Molar density of the vapor phase [mol/L or kg/m^3] If only one phase is present, Dl = Dv = D.
    :p double x(20) [out]: Composition of the liquid phase (array of mole or mass fractions) 
    :p double y(20) [out]: Composition of the vapor phase (array of mole or mass fractions) If only one phase is present, x = y = z.
    :p double q [out]: Vapor quality on a MOLAR basis (moles of vapor/total moles)
    :p double e [out]: Overall internal energy [J/mol or kJ/kg] 
    :p double h [out]: Overall enthalpy [J/mol or kJ/kg] 
    :p double s [out]: Overall entropy [J/mol-K or kJ/kg-K] 
    :p double Cv [out]: Isochoric (constant D) heat capacity [J/mol-K or kJ/kg-K] 
    :p double Cp [out]: Isobaric (constant P) heat capacity [J/mol-K or kJ/kg-K] 
    :p double w [out]: Speed of sound [m/s] 
    :p int ierr: XXXXXXXXXX
    :p char herr: XXXXXXXXXX
    :p int ab_length: length of variable ``ab`` (default: 2)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``q`` flags

        :q > 0 and q < 1: indicates a 2-phase state
        :q < 0: Subcooled (compressed) liquid
        :q = 0: Saturated liquid
        :q = 1: Saturated vapor
        :q > 1: Superheated vapor
        :q = -998: Subcooled liquid, but quality not defined  (usually P > Pc)
        :q =  998: Superheated vapor, but quality not defined (usually T > Tc)
        :q =  999: Supercritical state (T>Tc and P>Pc)


.. f:subroutine:: AGdll (T, D, z, a, g, )

    
    Compute Helmholtz and Gibbs energies as functions of temperature,
    density, and composition.  These are not residual values (those are
    calculated by GIBBS).
    See warning in subroutines THERM or ALLPROPS.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double a [out]: Helmholtz energy [J/mol] 
    :p double g [out]: Gibbs free energy [J/mol] 



.. f:subroutine:: ALLPROPS0dll (iIn, iOut, iFlag, T, D, z, Output, ierr, herr, herr_length)

    
    Calculate any single phase property defined in the iOut array and
    return the values in the Output array.  This routine should NOT
    be called for two-phase states!
    
    The output array is not reset so that several passes can be made to
    fill in holes left by the previous pass (such as entries at different
    T, D, or z).  The caller should zero out this array if so desired.
    
    This routine is designed with the "superuser" in mind.  It removes all
    string comparisons to approach the speed that could be obtained by
    calling the dedicated functions (such as THERM), but making it easy
    by allowing all inputs to be calculated with one routine.  Since the
    units are not returned here, look in the ALLPROPS documentation under
    the molar column.
    
    :p int iIn [in]: Number of properties to calculate. 
    :p int iOut(200) [in]: Array of enumerated values that identify the property to be calculated.  These values are defined in the COMMONS.INC file and are obtained by a call to GETENUM, as such for the enthalpy::  call GETENUM (0,'H',iEnum,ierr,herr)  To obtain the pure fluid value for some of the inputs, add 10000*ic (where ic is the component number) to the value of the enumerated value.  The properties that can be used for this are given the bottom of the comments section in the ALLPROPS routine.
    :p int iFlag [in]: Not yet used. 
    :p double T [in]: Temperature [K] 
    :p double D [in]: Density [mol/L] 
    :p double z(20): XXXXXXXXXX
    :p double Output(200): XXXXXXXXXX
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: ALLPROPS1dll (hOut, iUnits, T, D, z, c, ierr, herr, hOut_length, herr_length)

    
    Short version of subroutine ALLPROPS that eliminates the arrays but
    allows the calculation of only one property at a time.
    All inputs and outputs are described in the ALLPROPS routine.
    
    :p char hOut [in]: Input string of properties to calculate (of any length). Inputs can be separated by spaces, commas, semicolons, or bars, but should not be mixed.  For example, a proper string would be hOut='T,P,D,H,E,S', whereas an improperly defined string would be hOut='T,P;D H|E,S'. Use of lower or upper case is not important. Some properties will return multiple values, for example, hOut='F,Fc,XMOLE' will return 12 properties for a four component system, these being F(1), F(2), F(3), F(4), Fc(1), Fc(2), etc. To retrieve the property of a single component, use, for example, hOut='XMOLE(2),XMOLE(3)'
    :p int iUnits [in]: See subroutine REFPROP for a complete description of the iUnits input value. A negative value for iUnits indicates that the input temperature is given in K and density in mol/dm^3, (Refprop default units), otherwise T and D will be converted first to K and mol/dm^3.  Do not use the negative value for the iUnits parameter everywhere, only in this one situation.
    :p double T [in]: Temperature, with units based on the value of iUnits. 
    :p double D [in]: Density, with units based on the value of iUnits. 
    :p double z(20) [in]: Composition on a mole or mass basis (array of size ncmax=20) 
    :p double c [out]: Output value (array of size 200 dimensioned as double precision) The number -9999970 will be returned when errors occur or no input was requested.
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int hOut_length: length of variable ``hOut`` (default: 255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: ALLPROPSdll (hOut, iUnits, iMass, iFlag, T, D, z, Output, hUnits, iUCodeArray, ierr, herr, hOut_length, hUnits_length, herr_length)

    
    Calculate the single-phase properties identified in the hOut string
    at the temperature, density, and composition sent to the routine.
    Return the properties in mass or molar units depending on iUnits.
    
    .. warning::
    
        Do NOT call this routine for two-phase states,
        otherwise it will return metastable states if near but inside the
        phase boundary, or complete nonsense at other conditions.  The
        value of q that is returned from the flash routines will indicate
        a two phase state by returning a value between 0 and 1.  In such
        a situation, properties can only be calculated for the saturated
        liquid and vapor states.  For example, when calling PHFLSH:
        call subroutine PHFLSH (P,h,z,T,D,Dl,Dv,x,y,q,e,s,Cv,Cp,w,ierr,herr)
        If q>0 and q<1, then values of the liquid and vapor compositions will
        be returned in the x and y arrays, and the properties of the
        liquid and vapor states can be calculated, for example::
    
            call ENTRO (T,Dl,x,sliq)
            call ENTRO (T,Dv,x,svap)
    
    ALLPROPS was the name of a program developed at the University of
    Idaho under the direction of R.B. Stewart and R.T Jacobsen at the
    Center for Applied Thermodynamic Studies (CATS), with
    S.G. Penoncello and S.W. Beyerlein as professors at this institution.
    The software was distributed for about 10 years until around the
    year 2000 when it was officially replaced by the Refprop program.
    Some of the techniques from ALLPROPS was used in the development of
    Version 6 of Refprop, and was in some ways its forerunner.  The
    original code was DOS based and distributed on 3 1/2" floppy disks
    by regular mail.  A Visual Basic version of ALLPROPS was developed
    in about 1995, and, although rarely distributed, inspired the
    graphical interface included with Version 7.0 and above of Refprop.
    
    The ALLPROPS code was used to develop equations of state at the
    University of Idaho, and many of these are still in use today, such
    as ethanol, neon, R-11, R-12, R-22, R-23, R-143a, and the mixture
    air, along with the architecture behind the GERG-2008 mixture
    model.  The equations of state for ethylene, nitrogen, and oxygen
    were developed in conjunction with the Ruhr University in Bochum,
    Germany, including a six month stay by R. Span from Bochum with
    E.W. Lemmon at Idaho while both worked on their upper degrees.
    The underlying code in the fitting program developed at CATS is
    still in use today, and has been used in nearly all equations of
    state developed over the last 20 years.
    
    The name ALLPROPS was revived here in 2017 in memory of an old but
    not forgotten program whose roots still form the foundation of much
    that goes on behind the scenes in the development of equations of
    state and property software.
    
    **Calling from the DLL**
    
    Two routines are available in the DLL, these are ALLPROPSdll and
    ALLPRP200dll.  Both compress the hUnitsArray array so that it can be passed
    back as a single string.  The segments are divided by the character '|'.
    Both routines use the same list of arguments::
    
        (hOut,iUnits,iMass,iFlag,T,D,zm,Output,hUnits,iUCode,ierr,herr)
    
    In ALLPROPSdll, the hOut string is 255 characters long, the hUnits string is
    1000 characters long, and the Output and iUCode arrays each have a length of 20.
    In ALLPRP200dll, the hOut and hUnits strings are 10000 characters long, and
    the Output and iUCode arrays each have a length of 200.
    
    Below are the labels that can be sent in the hOut string and a very short
    description of the property and units based on either a SI molar system
    (iUnits=1) or SI mass system (iUnits=2, or 3 with temperature in C).
    
    **Note about criticals** The items TC,PC,DC will return the critical point of a pure fluid, or, when SATSPLN
    has been called, the critical point of the mixture (or a very close approximation).
    When the splines have not been set up, the values are the same as TCEST below.
    For the critical points of the pure fluids in a mixture, use TCRIT, etc., explained
    much further below, which is useful when multiple fluids have been loaded.
    parameters in the HMX.BNC file, which, for a binary mixture, are close for Type I
    mixtures, but for a multi-component or non-Type I mixture, can be significantly wrong.
    
    ========== ============================================== =======================  ========================
    Label      Description                                    SI Molar Units           SI Mass Units
    ---------- ---------------------------------------------- -----------------------  ------------------------
    
     Regular properties
    -----------------------------------------------------------------------------------------------------------
    T          Temperature                                    [K]                      [K]
    P          Pressure                                       [kPa]                    [kPa]
    D          Density                                        [mol/dm^3]               [kg/m^3]
    V          Volume                                         [dm^3/mol]               [m^3/kg]
    E          Internal energy                                [J/mol]                  [kJ/kg]
    H          Enthalpy                                       [J/mol]                  [kJ/kg]
    S          Entropy                                        [J/(mol*K)]              [(kJ/kg)/K]
    CV         Isochoric heat capacity                        [J/(mol*K)]              [(kJ/kg)/K]
    CP         Isobaric heat capacity                         [J/(mol*K)]              [(kJ/kg)/K]
    CP/CV      Heat capacity ratio                            [-]                      [-]
    W          Speed of sound                                 [m/s]                    [m/s]
    Z          Compressibility factor                         [-]                      [-]
    JT         Isenthalpic Joule-Thomson coefficient          [K/kPa]                  [K/kPa]
    A          Helmholtz energy                               [J/mol]                  [kJ/kg]
    G          Gibbs energy                                   [J/mol]                  [kJ/kg]
    R          Gas constant                                   [J/(mol*K)]              [(kJ/kg)/K]
    M          Molar mass (or of the mixture)                 [g/mol]                  [g/mol]
    QMASS      Quality (not implemented, q not known)         N.A.                     [kg/kg]
    QMOLE      Quality (not implemented, q not known)         [mol/mol]                N.A.
    
    Not so regular properties
    -----------------------------------------------------------------------------------------------------------
    KAPPA      Isothermal compressibility                     [1/kPa]                  [1/kPa]
    BETA       Volume expansivity                             [1/K]                    [1/K]
    ISENK      Isentropic expansion coefficient               [-]                      [-]
    KT         Isothermal expansion coefficient               [-]                      [-]
    BETAS      Adiabatic compressibility                      [1/kPa]                  [1/kPa]
    BS         Adiabatic bulk modulus                         [kPa]                    [kPa]
    KKT        Isothermal bulk modulus                        [kPa]                    [kPa]
    THROTT     Isothermal throttling coefficient              [dm^3/mol]               [m^3/kg]
    
    Derivatives
    -----------------------------------------------------------------------------------------------------------
    DPDD       dP/dD at constant T                            [(dm^3/mol)*kPa]         [(m^3/kg)*kPa]
    DPDT       dP/dT at constant D                            [kPa/K]                  [kPa/K]
    DDDP       dD/dP at constant T                            [(mol/dm^3)/kPa]         [(kg/m^3)/kPa]
    DDDT       dD/dT at constant P                            [(mol/dm^3)/K]           [(kg/m^3)/K]
    DTDP       dT/dP at constant D                            [K/kPa]                  [K/kPa]
    DTDD       dT/dD at constant P                            [(dm^3/mol)*K]           [(m^3/kg)*K]
    D2PDD2     d^2P/dD^2 at constant T                        [(dm^3/mol)^2*kPa]       [(m^3/kg)^2*kPa]
    D2PDT2     d^2P/dT^2 at constant D                        [kPa/K^2]                [kPa/K^2]
    D2PDTD     d^2P/dTdD                                      [(dm^3/mol)*kPa/K]       [(m^3/kg)*kPa/K]
    D2DDP2     d^2D/dP^2 at constant T                        [(mol/dm^3)/kPa^2]       [(kg/m^3)/kPa^2]
    D2DDT2     d^2D/dT^2 at constant P                        [(mol/dm^3)/K^2]         [(kg/m^3)/K^2]
    D2DDPT     d^2D/dPdT                                      [(mol/dm^3)/(kPa*K)]     [(kg/m^3)/[kPa*K]]
    D2TDP2     d^2T/dP^2 at constant D                        [K/kPa^2]                [K/kPa^2]
    D2TDD2     d^2T/dD^2 at constant P                        [(dm^3/mol)^2*K]         [(m^3/kg)^2*K]
    D2TDPD     d^2T/dPdD                                      [(dm^3/mol)*K/kPa]       [(m^3/kg)*K/kPa]
    
    Enthalpy derivatives
    -----------------------------------------------------------------------------------------------------------
    DHDT_D     dH/dT at constant D                            [(J/mol)/K]              [(kJ/kg)/K]
    DHDT_P     dH/dT at constant P                            [(J/mol)/K]              [(kJ/kg)/K]
    DHDD_P     dH/dD at constant P                            [(J/mol)*(dm^3/mol)]     [(kJ/kg)*(m^3/kg)]
    DHDD_T     dH/dD at constant T                            [(J/mol)*(dm^3/mol)]     [(kJ/kg)*(m^3/kg)]
    DHDP_T     dH/dP at constant T                            [(J/mol)/kPa]            [(kJ/kg)/kPa]
    DHDP_D     dH/dP at constant D                            [(J/mol)/kPa]            [(kJ/kg)/kPa]
    
    Entropy derivatives
    -----------------------------------------------------------------------------------------------------------
    DSDT_D     dS/dT at constant D                            [(J/mol)/K^2]            [(kJ/kg)/K^2]
    DSDT_P     dS/dT at constant P                            [(J/mol)/K^2]            [(kJ/kg)/K^2]
    DSDD_T     dS/dD at constant T                            [(J/mol)*(dm^3/mol)/K]   [(kJ/kg)*(m^3/kg)/K]
    DSDD_P     dS/dD at constant P                            [(J/mol)*(dm^3/mol)/K]   [(kJ/kg)*(m^3/kg)/K]
    DSDP_T     dS/dP at constant T                            [(J/mol)/(kPa*K)]        [(kJ/kg)/[kPa*K]]
    DSDP_D     dS/dP at constant D                            [(J/mol)/(kPa*K)]        [(kJ/kg)/[kPa*K]]
    
    Virial Coefficients
    -----------------------------------------------------------------------------------------------------------
    Bvir       Second virial coefficient                      [dm^3/mol]               [m^3/kg]
    Cvir       Third virial coefficient                       [(dm^3/mol)^2]           [(m^3/kg)^2]
    Dvir       Fourth virial coefficient                      [(dm^3/mol)^3]           [(m^3/kg)^3]
    Evir       Fifth virial coefficient                       [(dm^3/mol)^4]           [(m^3/kg)^4]
    dBvirdT    1st derivative of B with respect to T          [(dm^3/mol)/K]           [(m^3/kg)/K]
    d2BvirdT2  2nd derivative of B with respect to T          [(dm^3/mol)/K^2]         [(m^3/kg)/K^2]
    dCvirdT    1st derivative of C with respect to T          [(dm^3/mol)^2/K]         [(m^3/kg)^2/K]
    d2CvirdT2  2nd derivative of C with respect to T          [(dm^3/mol)^2/K^2]       [(m^3/kg)^2/K^2]
    dDvirdT    1st derivative of D with respect to T          [(dm^3/mol)^3/K]         [(m^3/kg)^3/K]
    d2DvirdT2  2nd derivative of D with respect to T          [(dm^3/mol)^3/K^2]       [(m^3/kg)^3/K^2]
    BA         Second acoustic virial coefficient             [dm^3/mol]               [m^3/kg]
    CA         Third acoustic virial coefficient              [(dm^3/mol)^2]           [(m^3/kg)^2]
    
    EOS testing properties
    -----------------------------------------------------------------------------------------------------------
    GRUN       Gruneisen  parameter                           [-]                      [-]
    PIP        Phase identification parameter                 [-]                      [-]
    RIEM       Thermodyn. curvature (nm^3/molecule)
    (Z-1)/D    (Z-1) over the density                         [dm^3/mol]               [m^3/kg]
    (Z-1)/P    (Z-1) over the pressure                        [1/kPa]                  [1/kPa]
    P*V        Pressure times volume                          [(dm^3/mol)*kPa]         [(m^3/kg)*kPa]
    S*D        Entropy times density                          [J/(mol*K)*(mol/dm^3)]   [(kJ/kg)*(kg/m^3)/K]
    N1/T       Negative reciprocal temperature                [1/K]                    [1/K]
    RD         Rectilinear diameter (Dl+Dv)/2                 [mol/dm^3]               [kg/m^3]
    
    Properties from ancillary equations
    -----------------------------------------------------------------------------------------------------------
    ANC-TP     Vapor pressure from ancillary given T          [kPa]                    [kPa]
    ANC-TDL    Sat. liquid dens. from ancillary given T       [mol/dm^3]               [kg/m^3]
    ANC-TDV    Sat. vapor dens. from ancillary given T        [mol/dm^3]               [kg/m^3]
    ANC-PT     Vapor temp. from ancillary given P             [K]                      [K]
    ANC-DT     Vapor temp. from ancillary given D             [K]                      [K]
    MELT-TP    Melting pressure given T                       [kPa]                    [kPa]
    MELT-PT    Melting temperature given P                    [K]                      [K]
    SUBL-TP    Sublimation pressure given T                   [kPa]                    [kPa]
    SUBL-PT    Sublimation temperature given P                [K]                      [K]
    
    Less common saturation properties
    -----------------------------------------------------------------------------------------------------------
    CSAT       Saturated heat capacity                        [J/(mol*K)]              [(kJ/kg)/K]
    CV2P       Isochoric two-phase heat capacity              [J/(mol*K)]              [(kJ/kg)/K]
    DPDTSAT    dP/dT along the saturation line                [kPa/K]                  [kPa/K]
    DHDZSAT    dH/dZ along the sat. line (Waring)             [J/mol]                  [kJ/kg]
    LIQSPNDL   Density at the liquid spinodal                 [mol/dm^3]               [kg/m^3]
    VAPSPNDL   Density at the vapor spinodal                  [mol/dm^3]               [kg/m^3]
    
    Excess properties
    -----------------------------------------------------------------------------------------------------------
    VE         Excess volume                                  [dm^3/mol]               [m^3/kg]
    EE         Excess energy                                  [J/mol]                  [kJ/kg]
    HE         Excess enthalpy                                [J/mol]                  [kJ/kg]
    SE         Excess entropy                                 [J/(mol*K)]              [(kJ/kg)/K]
    AE         Excess Helmholtz energy                        [J/mol]                  [kJ/kg]
    GE         Excess Gibbs energy                            [J/mol]                  [kJ/kg]
    B12        B12                                            [dm^3/mol]               [m^3/kg]
    
    Ideal gas properties
    -----------------------------------------------------------------------------------------------------------
    P0         Ideal gas pressure                             [kPa]                    [kPa]
    E0         Ideal gas internal energy                      [J/mol]                  [kJ/kg]
    H0         Ideal gas enthalpy                             [J/mol]                  [kJ/kg]
    S0         Ideal gas entropy                              [J/(mol*K)]              [(kJ/kg)/K]
    CV0        Ideal gas isochoric heat capacity              [J/(mol*K)]              [(kJ/kg)/K]
    CP0        Ideal gas isobaric heat capacity               [J/(mol*K)]              [(kJ/kg)/K]
    CP0/CV0    Ideal gas heat capacity ratio                  [-]                      [-]
    W0         Ideal gas speed of sound                       [m/s]                    [m/s]
    A0         Ideal gas Helmholtz energy                     [J/mol]                  [kJ/kg]
    G0         Ideal gas Gibbs energy                         [J/mol]                  [kJ/kg]
    P-P0       Pressure minus ideal gas pressure              [kPa]                    [kPa]
    
    Residual properties
    -----------------------------------------------------------------------------------------------------------
    PR         Residual pressure (P-D*Rxgas*T)                [kPa]                    [kPa]
    ER         Residual internal energy                       [J/mol]                  [kJ/kg]
    HR         Residual enthalpy                              [J/mol]                  [kJ/kg]
    SR         Residual entropy                               [J/(mol*K)]              [(kJ/kg)/K]
    CVR        Residual isochoric heat capacity               [J/(mol*K)]              [(kJ/kg)/K]
    CPR        Residual isobaric heat capacity                [J/(mol*K)]              [(kJ/kg)/K]
    AR         Residual Helmholtz energy                      [J/mol]                  [kJ/kg]
    GR         Residual Gibbs energy                          [J/mol]                  [kJ/kg]
    
    Ideal-gas contributions to the Helmholtz energy
    -----------------------------------------------------------------------------------------------------------
    PHIG00     Red. IG Helmholtz energy A0/RT                 [-]                      [-]
    PHIG10     tau*[d(A0/RT)/d(tau)]                          [-]                      [-]
    PHIG20     tau^2*[d^2(A0/RT)/d(tau)^2]                    [-]                      [-]
    PHIG30     tau^3*[d^3(A0/RT)/d(tau)^3]                    [-]                      [-]
    PHIG01     del*[d(A0/RT)/d(del)]                          [-]                      [-]
    PHIG02     del^2*[d^2(A0/RT)/d(del)^2]                    [-]                      [-]
    PHIG03     del^3*[d^3(A0/RT)/d(del)^3]                    [-]                      [-]
    PHIG11     tau*del*[d^2(A0/RT)/d(tau)d(del)]              [-]                      [-]
    PHIG12     tau*del^2*[d^3(A0/RT)/d(tau)d(del)^2]          [-]                      [-]
    PHIG21     tau^2*del*[d^3(A0/RT)/d(tau)^2d(del)]          [-]                      [-]
    
    Residual contributions to the Helmholtz energy
    -----------------------------------------------------------------------------------------------------------
    PHIR00     Red. resid. Helmholtz energy Ar/RT             [-]                      [-]
    PHIR10     tau*[d(Ar/RT)/d(tau)]                          [-]                      [-]
    PHIR20     tau^2*[d^2(Ar/RT)/d(tau)^2]                    [-]                      [-]
    PHIR30     tau^3*[d^3(Ar/RT)/d(tau)^3]                    [-]                      [-]
    PHIR01     del*[d(Ar/RT)/d(del)]                          [-]                      [-]
    PHIR02     del^2*[d^2(Ar/RT)/d(del)^2]                    [-]                      [-]
    PHIR03     del^3*[d^3(Ar/RT)/d(del)^3]                    [-]                      [-]
    PHIR11     tau*del*[d^2(Ar/RT)/d(tau)d(del)]              [-]                      [-]
    PHIR12     tau*del^2*[d^3(Ar/RT)/d(tau)d(del)^2]          [-]                      [-]
    PHIR21     tau^2*del*[d^3(Ar/RT)/d(tau)^2d(del)]          [-]                      [-]
    
    Critical point and P,T maximums along isopleth (see above)
    -----------------------------------------------------------------------------------------------------------
    TC         Critical temperature of a pure fluid           [K]                      [K]
    PC         Critical pressure of a pure fluid              [kPa]                    [kPa]
    DC         Critical density of a pure fluid               [mol/dm^3]               [kg/m^3]
    TCEST      Estimated critical temperature                 [K]                      [K]
    PCEST      Estimated critical temperature                 [kPa]                    [kPa]
    DCEST      Estimated critical density                     [mol/dm^3]               [kg/m^3]
    TMAXT      Temperature at cricondentherm                  [K]                      [K]
    PMAXT      Pressure at cricondentherm                     [kPa]                    [kPa]
    DMAXT      Density at cricondentherm                      [mol/dm^3]               [kg/m^3]
    TMAXP      Temperature at cricondenbar                    [K]                      [K]
    PMAXP      Pressure at cricondenbar                       [kPa]                    [kPa]
    DMAXP      Density at cricondenbar                        [mol/dm^3]               [kg/m^3]
    
    Reducing parameters
    -----------------------------------------------------------------------------------------------------------
    TRED       Reducing temperature                           [K]                      [K]
    DRED       Reducing density                               [mol/dm^3]               [kg/m^3]
    TAU        Tc/T (or Tred/T)                               [-]                      [-]
    DEL        D/Dc (or D/Dred)                               [-]                      [-]
    
    Limits
    -----------------------------------------------------------------------------------------------------------
    TMIN       Minimum temperature of the EOS                 [K]                      [K]
    TMAX       Maximum temperature of the EOS                 [K]                      [K]
    DMAX       Maximum density of the EOS                     [mol/dm^3]               [kg/m^3]
    PMAX       Maximum pressure of the EOS                    [kPa]                    [kPa]
    
    Transport, etc.
    -----------------------------------------------------------------------------------------------------------
    VIS        Viscosity                                      [uPa*s]
    TCX        Thermal conductivity                           [W/(m*K)]                [W/(m*K)]
    PRANDTL    Prandlt number                                 [-]                      [-]
    TD         Thermal diffusivity                            [cm^2/s]                 [cm^2/s]
    KV         Kinematic Viscosity                            [cm^2/s]                 [cm^2/s]
    STN        Surface tension                                [mN/m]                   [mN/m]
    DE         Dielectric constant                            [-]                      [-]
    
    
    Heating values
    -----------------------------------------------------------------------------------------------------------
    SPHT       Specific heat input                            [J/mol]                  [kJ/kg]
    HFRM       Heat of formation                              [J/mol]                  [kJ/kg]
    HG         Gross (or superior) heating value              [J/mol]                  [kJ/kg]
    HN         Net (or inferior) heating value                [J/mol]                  [kJ/kg]
    HGLQ       Gross Heat. Val. (Liquid)                      [J/mol]                  [kJ/kg]
    HNLQ       Net Heat. Val. (Liquid)                        [J/mol]                  [kJ/kg]
    HGVOL      Gross HV (Ideal gas volume basis)              [MJ/m^3]                 [MJ/m^3]
    HNVOL      Net HV (Ideal gas volume basis)                [MJ/m^3]                 [MJ/m^3]
    HEATVAPZ   Heat of vaporization (for pure fluids)         [J/mol]                  [kJ/kg]
    HEATVAPZ_T ...at constant temperature (for mixtures)      [J/mol]                  [kJ/kg]
    HEATVAPZ_P ...at constant pressure (for mixtures)         [J/mol]                  [kJ/kg]
    HEATVALUE  XXX
    
    Other properties
    -----------------------------------------------------------------------------------------------------------
    PINT       Internal pressure                              [kPa]                    [kPa]
    PREP       Repulsive part of pressure                     [kPa]                    [kPa]
    PATT       Attractive part of pressure                    [kPa]                    [kPa]
    EXERGY     Flow Exergy                                    [J/mol]                  [kJ/kg]
    CEXERGY    Closed System Exergy                           [J/mol]                  [kJ/kg]
    CSTAR      Critical flow factor                           [-]                      [-]
    TMF        Throat mass flux                               [kg/(m^2*s)]             [kg/(m^2*s)]
    FPV        Supercompressibility                           [-]                      [-]
    SUMFACT    Summation Factor                               [-]                      [-]
    RDAIR      Relative Density in air (specific gravity)     [-]                      [-]
    RDH2O      Relative Density in water (specific gravity)   [-]                      [-]
    API        API Gravity                                    [-]                      [-]
    
    Fluid fixed points for mixtures
    -----------------------------------------------------------------------------------------------------------
    At the "true" critical point of the EOS dP/dD=0 and d^P/dD^2=0 at constant temperature
    -----------------------------------------------------------------------------------------------------------
    TCRIT      Critical temperature of component i            [K]                      [K]
    PCRIT      Critical pressure of component i               [kPa]                    [kPa]
    DCRIT      Critical density of component i                [mol/dm^3]               [kg/m^3]
    TCTRUE     True EOS critical temp. of component i         [K]                      [K]
    DCTRUE     True EOS critical density of component i       [mol/dm^3]               [kg/m^3]
    TTRP       Triple point temperature of component i        [K]                      [K]
    PTRP       Triple point pressure of component i           [kPa]                    [kPa]
    DTRP       Triple point density of component i            [mol/dm^3]               [kg/m^3]
    TNBP       Normal boiling point temp. of comp. i          [K]                      [K]
    REOS       Gas constant of component i for EOS            [J/(mol*K)]              [(kJ/kg)/K]
    MM         Molar mass of component i                      [g/mol]                  [g/mol]
    ACF        Acentric factor of component i                 [-]                      [-]
    DIPOLE     Dipole moment of component i                   [debye]                  [debye]
    TREF       Ref. state temperature of component i          [K]                      [K]
    DREF       Ref. state pressure of component i             [kPa]                    [kPa]
    HREF       Ref. state enthalpy of comp. i at T0 and P0    [J/mol]                  [kJ/kg]
    SREF       Ref. state entropy of comp. i at T0 and P0     [J/(mol*K)]              [(kJ/kg)/K]
    
    Transport properties as a function of component number
    -----------------------------------------------------------------------------------------------------------
    Viscosity=ETA0+ETAB2+ETAR+ETAC
    -----------------------------------------------------------------------------------------------------------
    Thermal conductivity=TCX0+TCXR+TCXC
    -----------------------------------------------------------------------------------------------------------
    ETA0       Dilute gas viscosity of component i            [uPa*s]                  [uPa*s]
    ETAB2      2nd virial viscosity of component i            [uPa*s]                  [uPa*s]
    ETAR       Residual viscosity of component i              [uPa*s]                  [uPa*s]
    ETAC       Viscosity critical enhance. of comp. i         [uPa*s]                  [uPa*s]
    TCX0       Dilute gas thermal cond. of comp. i            [W/(m*K)]                [W/(m*K)]
    TCXR       Residual (background) cond. of comp. i         [W/(m*K)]                [W/(m*K)]
    TCXC       Cond. crit. enhancement of comp. i             [W/(m*K)]                [W/(m*K)]
    
    Mixture properties as a function of component number
    -----------------------------------------------------------------------------------------------------------
    K          K value (y/x) (not implemented, y unknown)     [-]                      [-]
    F          Fugacities                                     [kPa]                    [kPa]
    FC         Fugacity coefficients                          [-]                      [-]
    CPOT       Chemical potentials                            [J/mol]                  [kJ/kg]
    DADN       n*partial(alphar)/partial(ni)                  [-]                      [-]
    DNADN      partial(n*alphar)/partial(ni)                  [-]                      [-]
    XMOLE      Composition on a mole basis                    [-]                      [-]
    XMASS      Composition on a mass basis                    [-]                      [-]
    FIJMIX     Binary parameters (see REFPROP)
    ========== ============================================== =======================  ========================
    
    The dimension statements for these variables are (in Fortran)::
    
        parameter (ncmax=20)      ! Maximum number of components in the mixture
        parameter (iPropMax=200)  ! Number of output properties available in ALLPROPS.
        character*10000 hOut      ! hOut can actually be of any length.
        character herr*255,hUnitsArray(iPropMax)*50
        integer ierr,iUnits,iMass,iFlag,iUCodeArray(iPropMax) ! Note: as integer*4
        double precision Tx,Dx,zm(ncmax),Output(iPropMax)
    
    :p char hOut [in]: Input string of properties to calculate (of any length). Inputs can be separated by spaces, commas, semicolons, or bars, but should not be mixed.  For example, a proper string would be hOut='T,P,D,H,E,S', whereas an improperly defined string would be hOut='T,P;D H|E,S'. Use of lower or upper case is not important. Some properties will return multiple values, for example, hOut='F,Fc,XMOLE' will return 12 properties for a four component system, these being F(1), F(2), F(3), F(4), Fc(1), Fc(2), etc. To retrieve the property of a single component, use, for example, hOut='XMOLE(2),XMOLE(3)'
    :p int iUnits [in]: See subroutine REFPROP for a complete description of the iUnits input value. A negative value for iUnits indicates that the input temperature is given in K and density in mol/dm^3, (Refprop default units), otherwise T and D will be converted first to K and mol/dm^3.  Do not use the negative value for the iUnits parameter everywhere, only in this one situation.
    :p int iMass [in]: Specifies if the input composition is mole or mass based
    :p int iFlag [in]: Turn on or off writing of labels and units to hUnitsArray (eventually may be multiple flags combined into one variable, similar to ABFLSH)
    :p double T: XXXXXXXXXX
    :p double D: XXXXXXXXXX
    :p double z(20): XXXXXXXXXX
    :p double Output(200) [out]: Array of properties that were specified in the hOut string. (array of size 200 dimensioned as double precision) The number -9999970 will be returned when errors occur or no input was requested.
    :p char hUnits: XXXXXXXXXX
    :p int iUCodeArray(200) [out]: Array (of size 200) with the values of iUCode(n) described in the REFPROP subroutine.
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255)  
    :p int hOut_length: length of variable ``hOut`` (default: 10000)
    :p int hUnits_length: length of variable ``hUnits`` (default: 10000)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``imass`` flags

        :0: Input compositions given in mole fractions
        :1: Input compositions given in mass fractions

        ``iflag`` flags

        :0: Do not write anything to the hUnitsArray array, thus increasing the calculation speed.  (String handling in Fortran is very computationally expensive.)
        :1: Write labels and units to the hUnitsArray array.
        :2: Return only the string number described under "iUCodeArray" below and the units. (No properties will be calculated.)
        :-1: Write labels and units for only the first item.


.. f:subroutine:: B12dll (T, z, B, )

    
    Compute B12 as a function of temperature and composition for a binary mixture.
    
    :p double T [in]: Temperature [K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double B [out]: B12 [L/mol] 



.. f:subroutine:: BLCRVdll (D, z, T, ierr, herr, herr_length)

    
    Calculate the temperature along the Boyle curve for the input density.
    This line starts at zero density at the temperature where B=0, and
    passes into the liquid phase without crossing the two-phase.  It
    ends at a saturated liquid state very close to the critical point.
    The argument z in this routine is an array with the mole fractions
    of the mixture.  If the input T is non-zero, it is used as the
    initial guess.
    
    :p double D [in]: Density [mol/l] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double T [out]: Temperature [K] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :151: Iteration failed to converge


.. f:subroutine:: CSTARdll (T, P, v, z, Cs, Ts, Ds, Ps, ws, ierr, herr, herr_length)

    
    Calculate the critical flow factor, C*, for nozzle flow of a gas
    (subroutine was originally named CCRIT).
    
    :p double T [in]: Temperature [K] 
    :p double P [in]: Pressure [kPa] 
    :p double v [in]: Plenum velocity [m/s] (Should generally be set to 0 for calculating stagnation conditions.)
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double Cs [out]: Critical flow factor [dimensionless] 
    :p double Ts [out]: Nozzle throat temperature [K] 
    :p double Ds [out]: Nozzle throat molar density [mol/L] 
    :p double Ps [out]: Nozzle throat pressure [kPa] 
    :p double ws [out]: Nozzle throat speed of sound [m/s] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :151: CSTAR did not converge


.. f:subroutine:: CHEMPOTdll (T, D, z, u, ierr, herr, herr_length)

    
    Compute the chemical potentials for each of the nc components of a mixture.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double u(20) [out]: Array (1..nc) of the chemical potentials [J/mol] 
    :p int ierr: XXXXXXXXXX
    :p char herr: XXXXXXXXXX
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: CP0dll (T, z, Cp, )

    
    Calculate Cp0 for a mixture given temperature and composition.
    
    :p double T [in]: Temperature [K] 
    :p double z(20) [in]: Composition array (array of mole fractions) 
    :p double Cp: XXXXXXXXXX



.. f:subroutine:: CRITPdll (z, Tc, Pc, Dc, ierr, herr, herr_length)

    
    Calculate critical parameters as a function of composition.
    The critical parameters are estimates based on polynomial
    fits to the binary critical lines.  For 3 or more components,
    combining rules are applied to the constituent binaries.
    
    If SATSPLN has been called and the input composition sent here is the
    same as that sent to SATSPLN, the values calculated from the splines
    are returned, which are nearly exact.  During the call to SATSPLN,
    the true critical point, maximum pressure point, and maximum
    temperature point along the saturation lines are determined.
    Without the splines and for a system with three or more components,
    the values from this routine are only rough estimates.
    
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double Tc [out]: Critical temperature [K] 
    :p double Pc [out]: Critical pressure [kPa] 
    :p double Dc [out]: Critical density [mol/L] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful (See subroutine CRTHMX for error numbers.)


.. f:subroutine:: CRTPNTdll (z, Tc, Pc, Dc, ierr, herr, herr_length)

    
    Subroutine for the determination of the true critical point of a
    mixture with the use of the method of Michelsen (1984).
    
    The routine requires good initial guess values of Pc and Tc.
    
    On convergence, the values of bb and cc should be close to zero
    and dd > 0 for a two-phase critical point.
    bb=0, cc=0, and dd <= 0 for an unstable critical point.
    
    :p double z(20) [in]: Composition [array of mole fractions] 
    :p double Tc [out]: Critical temperature [K] 
    :p double Pc [out]: Critical pressure [kPa] 
    :p double Dc [out]: Critical density [mol/l] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: CSATKdll (icomp, T, kph, P, D, Csat, ierr, herr, herr_length)

    
    Compute the heat capacity along the saturation line as a function of
    temperature for a given component.
    
    Csat can be calculated in several ways
    Csat = T*(dS/dT[sat])
    Csat = Cp - T*(dV/dT)(dP/dT[sat]) with dVdT at constant pressure
    Csat = Cp - beta/D*hvap/(vliq - vvap)
    where beta is the volume expansivity
    
    :p int icomp [in]: Component number in mixture (1..nc); 1 for pure fluid 
    :p double T [in]: Temperature [K] 
    :p int kph [in]: Phase flag
    :p double P [out]: Saturated pressure [kPa] 
    :p double D [out]: Saturated molar density [mol/L] 
    :p double Csat [out]: Saturated heat capacity [J/mol-K] 
    :p int ierr: XXXXXXXXXX
    :p char herr: XXXXXXXXXX
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``kph`` flags

        :1: Liquid calculation
        :2: Vapor calculation


.. f:subroutine:: CSTARdll (T, P, v, z, Cs, Ts, Ds, Ps, ws, ierr, herr, herr_length)

    
    Calculate the critical flow factor, C*, for nozzle flow of a gas
    (subroutine was originally named CCRIT).
    
    :p double T [in]: Temperature [K] 
    :p double P [in]: Pressure [kPa] 
    :p double v [in]: Plenum velocity [m/s] (Should generally be set to 0 for calculating stagnation conditions.)
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double Cs [out]: Critical flow factor [dimensionless] 
    :p double Ts [out]: Nozzle throat temperature [K] 
    :p double Ds [out]: Nozzle throat molar density [mol/L] 
    :p double Ps [out]: Nozzle throat pressure [kPa] 
    :p double ws [out]: Nozzle throat speed of sound [m/s] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :151: CSTAR did not converge


.. f:subroutine:: CV2PKdll (icomp, T, D, Cv2p, Csat, ierr, herr, herr_length)

    
    Compute the isochoric heat capacity in the two phase (liquid+vapor) region.
    
    :p int icomp [in]: Component number in mixture (1..nc); 1 for pure fluid 
    :p double T [in]: Temperature [K] 
    :p double D [in]: Density [mol/L] if known If D=0, then a saturated liquid state is assumed. 
    :p double Cv2p [out]: Isochoric two-phase heat capacity [J/mol-K] 
    :p double Csat [out]: Saturation heat capacity [J/mol-K] (Although there is already a Csat routine in Refprop, it is also returned here.  However, the calculation speed is slower than Csat.) 
    :p int ierr: XXXXXXXXXX
    :p char herr: XXXXXXXXXX
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: CVCPdll (T, D, z, Cv, Cp, )

    
    :p double T [out]: Temperature [K]
    :p double D [out]: Density [mol/K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double Cv [in]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]



.. f:subroutine:: DBDTdll (T, z, dBT, )

    
    Compute the 1st derivative of B [dBT (L/mol-K)] as a function of
    temperature T (K) and composition x (array of mole fractions).
    This routine approximates dBT.  For pure fluids, the routine VIRBCD is exact.
    
    :p double T [in]: Temperature [K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double dBT [out]: 1st derivative of B with respect to T [L/(mol-K)] 



.. f:subroutine:: DBFL1dll (D, b, z, hab, T, P, ierr, herr, hab_length, herr_length)

    
    General single-phase calculation given density, composition, and either
    pressure, energy, enthalpy, or entropy.  The character string ab
    specifies the inputs.  This routine should ONLY be called by ABFL1.
    
    :p double D [in]: Molar density [mol/L] 
    :p double b [in]: Second property (pressure, energy, enthalpy, or entropy) 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p char hab: XXXXXXXXXX
    :p double T [out]: Temperature [K] 
    :p double P [out]: Pressure [kPa] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int hab_length: length of variable ``hab`` (default: 2)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :207: Density or pressure equal to zero, no solution available
        :208: Iteration did not converge


.. f:subroutine:: DEFL1dll (D, e, z, T, ierr, herr, herr_length)

    
    Iterate for single-phase temperature as a function of density,
    energy, and composition.
    (See subroutine ABFL1 for the description of all variables.)
    
    :p double D [in]: Density [mol/K]
    :p double e [in]: Internal energy [J/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double T [out]: Temperature [K]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: DEFLSHdll (D, e, z, T, P, Dl, Dv, x, y, q, h, s, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given density, energy, and bulk composition.
    (See subroutines ABFLSH or DBFLSH for the description of all variables.)
    
    :p double D [in]: Density [mol/K]
    :p double e [in]: Internal energy [J/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double T [out]: Temperature [K]
    :p double P [out]: Pressure [kPa]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double h [out]: Enthalpy [J/mol]
    :p double s [out]: Entropy [J/mol-K]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: DERVPVTdll (T, D, z, dPdD, dPdT, d2PdD2, d2PdT2, d2PdTD, dDdP, dDdT, d2DdP2, d2DdT2, d2DdPT, dTdP, dTdD, d2TdP2, d2TdD2, d2TdPD, )

    
    Compute 1st and 2nd order derivatives of temperature, pressure, and
    density from core functions for Helmholtz energy equations only.
    See warning in subroutines THERM or ALLPROPS.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double dPdD [out]: dP/dD at constant T [kPa/(mol/dm^3)] 
    :p double dPdT [out]: dP/dT at constant D [kPa/K] 
    :p double d2PdD2 [out]: d^2P/dD^2 at constant T [kPa/(mol/dm^3)^2] 
    :p double d2PdT2 [out]: d^2P/dT^2 at constant D [kPa/K^2] 
    :p double d2PdTD [out]: d^2P/dTdD [J/mol-K]     [kPa/K/(mol/dm^3)] 
    :p double dDdP [out]: dD/dP at constant T [mol/(dm^3-kPa)] 
    :p double dDdT [out]: dD/dT at constant P [mol/(dm^3-K)] 
    :p double d2DdP2 [out]: d^2D/dP^2 at constant T [(mol/dm^3)/kPa^2] 
    :p double d2DdT2 [out]: d^2D/dT^2 at constant P [(mol/dm^3)/K^2] 
    :p double d2DdPT [out]: d^2D/dPdT [J/mol-K]     [(mol/dm^3)/(kPa-K)] 
    :p double dTdP [out]: dT/dP at constant D [K/kPa] 
    :p double dTdD [out]: dT/dD at constant P [K/(mol/dm^3)] 
    :p double d2TdP2 [out]: d^2T/dP^2 at constant D [K/kPa^2] 
    :p double d2TdD2 [out]: d^2T/dD^2 at constant P [K/(mol/dm^3)^2] 
    :p double d2TdPD [out]: d^2T/dPdD [J/mol-K]     [K/kPa/(mol/dm^3)] 



.. f:subroutine:: DHD1dll (T, D, z, dhdt_d, dhdt_p, dhdd_t, dhdd_p, dhdp_t, dhdp_d, )

    
    Compute partial derivatives of enthalpy w.r.t. T, P, or D at constant
    T, P, or D as a function of temperature, density, and composition.
    See warning in subroutines THERM or ALLPROPS.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double dhdt_d [out]: DH/dT at constant density [J/mol-K] 
    :p double dhdt_p [out]: dH/dT at constant pressure [J/mol-K] 
    :p double dhdd_t [out]: dH/dD at constant temperature [(J/mol)/(mol/L)] 
    :p double dhdd_p [out]: dH/dD at constant pressure [(J/mol)/(mol/L)] 
    :p double dhdp_t [out]: dH/dP at constant temperature [J/(mol-kPa)] 
    :p double dhdp_d [out]: dH/dP at constant density [J/(mol-kPa)] 



.. f:subroutine:: DHFL1dll (D, h, z, T, ierr, herr, herr_length)

    
    Iterate for single-phase temperature as a function of density,
    enthalpy, and composition.
    (See subroutine ABFL1 for the description of all variables.)
    
    :p double D [in]: Density [mol/K]
    :p double h [in]: Enthalpy [J/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double T [out]: Temperature [K]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: DHFLSHdll (D, h, z, T, P, Dl, Dv, x, y, q, e, s, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given density, enthalpy, and bulk composition.
    (See subroutines ABFLSH or DBFLSH for the description of all variables.)
    
    :p double D [in]: Density [mol/K]
    :p double h [in]: Enthalpy [J/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double T [out]: Temperature [K]
    :p double P [out]: Pressure [kPa]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double e [out]: Internal energy [J/mol]
    :p double s [out]: Entropy [J/mol-K]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: DIELECdll (T, D, z, de, )

    
    Compute dielectric constant as a function of temperature, density,
    and composition.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double de [out]: Dielectric constant [-] 



.. f:subroutine:: DLSATKdll (icomp, T, D, ierr, herr, herr_length)

    
    Compute pure fluid saturated liquid density with appropriate equation.
    
    :p int icomp [in]: Component i 
    :p double T [in]: Temperature [K] 
    :p double D [out]: Saturated liquid density [mol/L] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :121: Temperature greater than critical point temperature
        :501: No equation available


.. f:subroutine:: DPDD2dll (T, D, z, d2PdD2, )

    
    Compute second partial derivative of pressure w.r.t. density at constant
    temperature as a function of temperature, density, and composition.
    See warning in subroutines THERM or ALLPROPS.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double d2PdD2 [out]: d^2P/dD^2 [kPa-L^2/mol^2] 



.. f:subroutine:: DPTSATKdll (icomp, T, kph, P, D, Csat, dPdT, ierr, herr, herr_length)

    
    Compute the heat capacity and dP/dT along the saturation line as a
    function of temperature for a given component.  See also subroutine CSATK.
    
    :p int icomp [in]: Component number in mixture (1..nc); 1 for pure fluid 
    :p double T [in]: Temperature [K] 
    :p int kph [in]: Phase flag
    :p double P [out]: Saturated pressure [kPa] 
    :p double D [out]: Saturated molar density [mol/L] 
    :p double Csat [out]: Saturated heat capacity [J/mol-K] (same as that called from CSATK) 
    :p double dPdT [out]: dP/dT along the saturation line [kPa/K] (this is not dP/dT at the saturation line for the single phase state, but the change in saturated vapor pressure as the saturation temperature changes.) 
    :p int ierr: XXXXXXXXXX
    :p char herr: XXXXXXXXXX
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``kph`` flags

        :1: Liquid calculation
        :2: Vapor calculation


.. f:subroutine:: DQFL2dll (D, q, z, kq, T, P, Dl, Dv, x, y, ierr, herr, herr_length)

    
    Flash calculation given bulk density, quality, and composition.
    (See subroutine ABFL2 for the description of all variables.)
    
    :p double D [in]: Density [mol/K]
    :p double q [in]: Vapor quality [mol/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p int kq: XXXXXXXXXX
    :p double T [out]: Temperature [K]
    :p double P [out]: Pressure [kPa]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: DSD1dll (T, D, z, dsdt_d, dsdt_p, dsdd_t, dsdd_p, dsdp_t, dsdp_d, )

    
    Compute partial derivatives of entropy w.r.t. T, P, or D at constant
    T, P, or D as a function of temperature, density, and composition.
    See warning in subroutines THERM or ALLPROPS.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double dsdt_d [out]: dS/dT at constant density [J/mol-K^2] 
    :p double dsdt_p [out]: dS/dT at constant pressure [J/mol-K^2] 
    :p double dsdd_t [out]: dS/dD at constant temperature [(J/mol-K)/(mol/L)] 
    :p double dsdd_p [out]: dS/dD at constant pressure [(J/mol-K)/(mol/L)] 
    :p double dsdp_t [out]: dS/dP at constant temperature [J/(mol-K-kPa)] 
    :p double dsdp_d [out]: dS/dP at constant density [J/(mol-K-kPa)] 



.. f:subroutine:: DSFL1dll (D, s, z, T, ierr, herr, herr_length)

    
    Iterate for single-phase temperature as a function of density,
    entropy, and composition.
    (See subroutine ABFL1 for the description of all variables.)
    
    :p double D [in]: Density [mol/K]
    :p double s [in]: Entropy [J/mol-K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double T [out]: Temperature [K]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: DSFLSHdll (D, s, z, T, P, Dl, Dv, x, y, q, e, h, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given density, entropy, and bulk composition.
    (See subroutines ABFLSH or DBFLSH for the description of all variables.)
    
    :p double D [in]: Density [mol/K]
    :p double s [in]: Entropy [J/mol-K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double T [out]: Temperature [K]
    :p double P [out]: Pressure [kPa]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double e [out]: Internal energy [J/mol]
    :p double h [out]: Enthalpy [J/mol]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: DVSATKdll (icomp, T, D, ierr, herr, herr_length)

    
    Compute pure fluid saturated vapor density with appropriate equation.
    
    :p int icomp [in]: Component i 
    :p double T [in]: Temperature [K] 
    :p double D [out]: Saturated vapor density [mol/L] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :121: Temperature greater than critical point temperature
        :501: No equation available


.. f:subroutine:: ENTHALdll (T, D, z, h, )

    
    :p double T [out]: Temperature [K]
    :p double D [out]: Density [mol/K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double h [out]: Enthalpy [J/mol]



.. f:subroutine:: ENTROdll (T, D, z, s, )

    
    :p double T [out]: Temperature [K]
    :p double D [out]: Density [mol/K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double s [out]: Entropy [J/mol-K]



.. f:subroutine:: ERRMSGdll (ierr, herr, herr_length)

    
    Retrieve the last error message saved in calls to ERRNUM (but
    only if the ierr variable is not equal to zero).  Write
    error messages to default output if iErrPrnt is active.
    The variable iErrPrnt in the common blocks must always be zero
    when compiling the DLL.
    
    Outputs depend on variable iErrPrnt in the common blocks
    
    * iErrPrnt= 0 -   Error string not written (default)
    * iErrPrnt=-1 -   Error string written to screen
    * iErrPrnt= 1 -   Error string written to screen only if ierr is positive
    * iErrPrnt=3,-3 - Same as 1 and -1, but program also pauses
    
    :p int ierr [out]: Error number from the last call to ERRNUM  Output:
    :p char herr [out]: Associated error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: ESFLSHdll (e, s, z, T, P, D, Dl, Dv, x, y, q, h, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given bulk energy, entropy, and composition.
    (See subroutines ABFLSH or DBFLSH for the description of all variables.)
    
    :p double e [in]: Internal energy [J/mol]
    :p double s [in]: Entropy [J/mol-K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double T [out]: Temperature [K]
    :p double P [out]: Pressure [kPa]
    :p double D [out]: Density [mol/K]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double h [out]: Enthalpy [J/mol]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: EXCESSdll (T, P, z, kph, D, vE, eE, hE, sE, aE, gE, ierr, herr, herr_length)

    
    Compute excess properties as a function of temperature, pressure,
    and composition.
    
    :p double T [in]: Temperature [K] 
    :p double P [in]: Pressure [kPa] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p int kph [in]: Phase flag
    :p double D [out]: Molar density [mol/L]  (Send a negative density to the routine to use it as an initial guess.) 
    :p double vE [out]: Excess volume [L/mol] 
    :p double eE [out]: Excess energy [J/mol] 
    :p double hE [out]: Excess enthalpy [J/mol] 
    :p double sE [out]: Excess entropy [J/mol-K] 
    :p double aE [out]: Excess Helmholtz energy [J/mol] 
    :p double gE [out]: Excess Gibbs energy [J/mol] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``kph`` flags

        :1: Liquid
        :2: Vapor
        :0: Stable phase


.. f:subroutine:: FGCTY2dll (T, D, z, f, ierr, herr, herr_length)

    
    Compute fugacity for each of the nc components of a mixture by
    analytical differentiation of the dimensionless residual Helmholtz energy.
    These are based on derivations in the GERG-2004 document for natural gas.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double f(20) [out]: Array (1..nc) of fugacities [kPa] 
    :p int ierr: XXXXXXXXXX
    :p char herr: XXXXXXXXXX
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: FGCTYdll (T, D, z, f, )

    
    Old routine to compute fugacity for each of the nc components of a mixture
    by numerical differentiation (with central differences) of the
    dimensionless residual Helmholtz energy.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double f(20) [out]: Array (1..nc) of fugacities [kPa] 



.. f:subroutine:: FLAGSdll (hFlag, jFlag, kFlag, ierr, herr, hFlag_length, herr_length)

    
    Set flags for desired behavior from the program.
    
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``hFlag``           | ``jFlag``                                                                                           |
        +=====================+=====================================================================================================+
        | ``Return errors``   | *  0 - Return only final messages (default).                                                        |
        |                     | *  1 - Return all intermediate messages.                                                            |
        | or ``Errors``       | *  2 - Do not return messages.                                                                      |
        |                     |                                                                                                     |
        |                     | This flag is not reset with a new call to SETUP.                                                    |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Write errors``    | *  0 - Error strings not written to screen (default).                                               |
        |                     | * -1 - Error string written to screen.                                                              |
        | or ``Write``        | *  1 - Error string written to screen only if ierr is positive.                                     |
        |                     | * 3,-3 - Same as 1 and -1, but program also pauses.                                                 |
        |                     |                                                                                                     |
        |                     | This flag is not reset with a new call to SETUP.                                                    |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Dir search``      | * 0 - Search for fluid files in alternate directories (as defined in OPENFL) (default).             |
        |                     | * 1 - Do not search in directories other than the one set by the call to SETPATH,                   |
        | or ``Dir``          |   except for a 'fluids' subdirectory within the folder given in SETPATH.                            |
        |                     |   If the fluid files for the reference fluid(s) are not in the SETPATH directory,                   |
        |                     |   then transport properties may not be calculated.                                                  |
        |                     | * 2 - Make no additional checks if the fluid file is not found after the first attempt to open      |
        |                     |   the file (for example, checking upper and lower case).                                            |
        |                     |                                                                                                     |
        |                     | This flag is never reset.                                                                           |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Flip Cp0``        | * 1 - Change the ideal gas equation to Cp0                                                          |
        |                     | * 2 - Change the ideal gas equation to PH0                                                          |
        |                     |                                                                                                     |
        | or ``Flip``         | The default is set by the value in the fluid file.  A call is made to SETREF after the switch       |
        |                     | to reset the reference states for energy, enthalpy, and entropy.                                    |
        |                     | Calling SETUP resets the equation to its default state as given in the fluid file.                  |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Skip SETREF``     | * 0 - Call the SETREF routine to setup the reference state (default).                               |
        |                     | * 1 - Skip the call to SETREF.  However, this means energy, enthalpy, and entropy will not be       |
        | or ``Skip``         |   correct (but only by an offset to their usual values).                                            |
        |                     |                                                                                                     |
        |                     | This must be called before the call to SETUP, and is never reset.                                   |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        |``Mixture reference``| * 0 - Do nothing (default).                                                                         |
        |                     | * 2 - When calling subroutine REFPROP, call SETREF first with a value of 2 for the second entry.    |
        | or ``SETREF``       |   (See subroutine SETREF for details.)                                                              |
        |                     |                                                                                                     |
        |                     |  This must be called before the call to REFPROP (the subroutine in PROP_SUB.FOR), and is            |
        |                     |  never reset.                                                                                       |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        |``Skip ECS``         | * 0 - Load the ECS fluids required for transport properties (for pure fluids in slots 21-40, and    |
        |                     |   mixtures in slot 41).                                                                             |
        |                     | * 1 - Don't load the ECS fluids, only the requested fluids (this may deactivate pure fluid transport|
        |                     |   properties, and will deactivate all mixture transport calculations.                               |
        |                     |                                                                                                     |
        |                     | This must be called before the call to SETUP, and is never reset.                                   |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        |``Splines off``      | * 1 - Turn the splines off (assuming that they were turned on initially by a call to SATSPLN).      |
        |                     |                                                                                                     |
        |                     | Calling SETUP again will also turn off the splines.                                                 |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Ignore bounds``   | * 0 - Check all errors and respond accordingly (default).                                           |
        |                     | * 1 - Ignore bounds for certain situations, such as calling SATT                                    |
        | or ``Bounds``       |   below the triple point or states above the melting line.                                          |
        |                     |                                                                                                     |
        |                     | This flag is never reset.                                                                           |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Cache``           | * 0 - Cache all calculated values (default).                                                        |
        |                     | * 1 - Cache only low level calculations, such as derivatives calculated in PHIFEQ.                  |
        |                     | * 2 - Cache only calculated properties in major subroutines such as SATT and SATP.                  |
        |                     | * 3 - No caching.                                                                                   |
        |                     |                                                                                                     |
        |                     | This flag is not reset with a new call to SETUP.                                                    |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Reset all``       | * 2 - Call RESETA to reset all cached values.                                                       |
        |                     |   This includes all flags set by calls to this routine, except for the use of a pure fluid in       |
        | or ``RA``           |   a mixture or reducing nc.                                                                         |
        |                     |                                                                                                     |
        |                     | Subroutine RESETA is always called by SETUP, but does not reset the flags set by calls to this      |
        |                     | routine.                                                                                            |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Reset HMX``       | * 1 - Reset the caching flag so that the HMX.BNC file is read again on the next call to SETUP.      |
        |                     |   This option is only useful during fitting mixture models or modifying the HMX.BNC file            |
        | or ``HMX``          |   to add new interaction parameters, otherwise this flag will only slow down the program            |
        |                     |   by forcing a reread of the mixture file.  The output variable kFlag will be 0 or 1 to indicate    |
        |                     |   whether or not the HMX.BNC will be read on the next call to SETUP.                                |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Pure fluid``      | * 0 - Use full mixture equation of state loaded (default).                                          |
        |                     | * <>0 - Use the pure fluid loaded in the slot specified by jFlag.                                   |
        |                     |                                                                                                     |
        | or ``Pure``         | This option is reset during the call to SETUP.                                                      |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Component number``| * nc - Reduce the number of fluids being used to nc.  See SETNC routine for details.                |
        |                     |   The output in kFlag will give the number of fluids in use,                                        |
        | or ``nc``           |   which can be useful even if this option has not been called to set nc.                            |
        |                     |                                                                                                     |
        |                     | This option is reset during the call to SETUP.                                                      |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Peng-Robinson``   | * 0 - Turn off the Peng-Robinson equation of state (default).                                       |
        |                     | * 2 - Use Peng-Robinson equation for all calculations.                                              |
        | or ``PR``           | * 3 - Use Peng-Robinson with translation term deactivated.                                          |
        |                     |                                                                                                     |
        |                     | This option is never reset.                                                                         |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``kij Zero``        | * 0 - Use the fitted kij values found in the HMX.BNC file on the lines with PR1 (default).          |
        |                     | * 1 - Set all kij values to those estimated in ESTPR (thus ignoring the ones on the PR1             |
        |                     |   lines in the HMX.BNC file).                                                                       |
        |                     | * 2 - Set all kij values to zero.                                                                   |
        |                     |                                                                                                     |
        |                     | This option is never reset.                                                                         |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``AGA8``            | * 0 - Turn off AGA8 and return to the fluids loaded from the call to SETUP (default)                |
        |                     | * 1 - Turn on the use of the AGA8 DETAIL equation of state.                                         |
        |                     |                                                                                                     |
        |                     | This option is reset during the call to SETUP.                                                      |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``GERG 2008``       | * 0 - Set a flag to turn off GERG 2008 next time SETUP is called.                                   |
        |                     | * 1 - Turn on the flag that will cause the GERG 2008 equation to be loaded next time SETUP is called|
        |                     |                                                                                                     |
        | or ``GERG``         | This option MUST be called before SETUP.                                                            |
        |                     | When turning off the GERG, call the SETUP routine again after calling this routine.                 |
        |                     | This option is never reset.                                                                         |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Gas constant``    | * 0 - Default is to use the most current gas constant for all fluids except nitrogen, argon, oxygen,|
        |                     |   ethylene, CO2, methane, and ethane.                                                               |
        | or ``R``            | * 1 - Use most current gas constant for all fluids (must be called after call to SETUP).            |
        |                     | * 2 - Use gas constant from fluid files for each equation of state (must be called after call to    |
        |                     |   SETUP).                                                                                           |
        |                     |                                                                                                     |
        |                     | This option is reset during the call to SETUP.                                                      |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Calorie``         | * 0 - Use a calorie to joule conversion value of 4.184 cal/J (default).                             |
        |                     | * 1 - Use the IT value of 4.1868 cal/J.                                                             |
        |  or ``Cal``         |                                                                                                     |
        |                     | This option is never reset.                                                                         |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Debug``           | * 0 - Turn off all debugging.                                                                       |
        |                     | * 1 - In the REFPROP subroutine, write all input variables to a file called input.dat, and all      |
        |                     |   output values to a file called output.dat                                                         |
        |                     | * 2 - In SETUP, write out the full path of the files that were either opened or tried to open.      |
        |                     |                                                                                                     |
        |                     | This option is never reset.                                                                         |
        +---------------------+-----------------------------------------------------------------------------------------------------+
    
    :p char hFlag [in]: Indicator for the option to set (letters in the string are case insensitive). 
    :p int jFlag [in]: Flag to choose what to do in each option. Send -999 to just obtain the current value of the flag.
    :p int kFlag [out]: Current setting of the flag for the option identified by iFlag. (Returned regardless of the value of jFlag.)
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int hFlag_length: length of variable ``hFlag`` (default: 255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: FPVdll (T, D, P, z, Fpvx, )

    
    Compute the supercompressibility factor, Fpv.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double P [in]: Pressure [kPa] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double Fpvx [out]: Fpv = SQRT[Z(60 F, 14.73 psia)/Z(T,P)] 



.. f:subroutine:: FUGCOFdll (T, D, z, phi, ierr, herr, herr_length)

    
    Compute the fugacity coefficient for each of the nc components of a mixture.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double phi(20) [out]: Array (1..nc) of the fugacity coefficients [-] 
    :p int ierr: XXXXXXXXXX
    :p char herr: XXXXXXXXXX
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: GERG04dll (ncomp, iFlag, ierr, herr, herr_length)

    
    This is a duplicate of the GERG08 routine below, and is meant only for use
    with older versions of Refprop.
    
    :p int ncomp [in]: Number of components (1 for pure fluid) 
    :p int iFlag [in]: Set to 1 to load the GERG 2008 equations, set to 0 for defaults 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) (returned from SETMOD) 
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: GERG08dll (ncomp, iFlag, ierr, herr, herr_length)

    
    Use the GERG 2008 formulation for all pure fluid and mixture calculations.
    
    This subroutine must be called before SETUP; it need not be called at all
    if the default (NIST-recommended) models are desired.  To turn off
    the GERG settings, call this routine again with iFlag=0, and then call
    the SETUP routine to reset the parameters of the equations of state.
    Once this routine is called, it need not be called again to keep the
    GERG08 model active, even when calling SETUP.
    
    :p int ncomp [in]: Number of components (1 for pure fluid) 
    :p int iFlag [in]: Set to 1 to load the GERG 2008 equations, set to 0 for defaults 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) (returned from SETMOD) 
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: GETENUMdll (iFlag, hEnum, iEnum, ierr, herr, hEnum_length, herr_length)

    
    Translate a string of letters into an integer value that can be used
    in calls to ALLPROPS0 to increase the speed of property calculations
    by eliminating string comparisons (which are time expensive in Fortran).
    This can be done once at the beginning of a program for all properties
    that will be used, and stored for use as needed later.
    
    The input strings possible are described in subroutines ALLPROPS and
    GETUNIT.
    
    :p int iFlag [in]: Flag to specify which type of enumerated value to return
    :p char hEnum [in]: The string that will be used to return the enumerated value. Only uppercase letters are allowed to decrease the time required to process the values. 
    :p int iEnum [out]: The enumerated value that matches the string sent in hEnum. 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int hEnum_length: length of variable ``hEnum`` (default: 255)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``iflag`` flags

        :0: Check all strings possible.
        :1: Check strings for property units only (e.g., SI, English, etc.).
        :2: Check property strings and those in #3 only.
        :3: Check property strings only that are not functions of T and D. (for example, the critical point, acentric factor, limits of the EOS, etc.)


.. f:subroutine:: GETFIJdll (hmodij, fij, hfij, hmxrul, hmodij_length, hfij_length, hmxrul_length)

    
    Retrieve parameter info for a specified mixing rule.
    
    :p char hmodij [in]: Mixing rule for the binary pair i,j (e.g., LJ6 or KW0) (character*3) 
    :p double fij(6) [out]: Binary mixture parameters (array of dimension nmxpar; currently nmxpar is set to 6). The parameters will vary depending on hmodij.
    :p char hfij [out]: Description of the binary mixture parameters (character*8 array of dimension nmxpar)
    :p char hmxrul [out]: Description of the mixing rule (character*255) 
    :p int hmodij_length: length of variable ``hmodij`` (default: 3)
    :p int hfij_length: length of variable ``hfij`` (default: 255)
    :p int hmxrul_length: length of variable ``hmxrul`` (default: 255)



.. f:subroutine:: GETKTVdll (icomp, jcomp, hmodij, fij, hFmix, hfij, hbinp, hmxrul, hmodij_length, hFmix_length, hfij_length, hbinp_length, hmxrul_length)

    
    Retrieve mixture model and parameters for a specified binary mixture.
    This subroutine should not be called until after SETUP has been called.
    The order of icomp and jcomp do not matter, the routine returns the
    parameters as stored in the HMX.BNC file.  To determine if the
    compositions are backwards, call HMXORDER.  If calling SETMIX with
    the same parameters, an error will be returned if the components
    are backwards.
    
    
    ========================   ==============================
    Kunz-Wagner model (KW0)    Lemmon-Jacobsen model (LJ6)
    ------------------------   ------------------------------
    fij(1) = betaT             fij(1) = zeta
    fij(2) = gammaT            fij(2) = xi
    fij(3) = betaV             fij(3) = Fij
    fij(4) = gammaV            fij(4) = beta
    fij(5) = Fij               fij(5) = gamma
    fij(6) = 'not used'        fij(6) = 'not used'
    ========================   ==============================
    
    :p int icomp [in]: Component i 
    :p int jcomp [in]: Component j 
    :p char hmodij [out]: Mixing rule for the binary pair i,j (e.g., KW0, LJ6, XR0, or LIN) (character*3) 
    :p double fij(6) [out]: Binary mixture parameters (array of dimension nmxpar; currently nmxpar is set to 6); the parameters will vary depending on hmodij;
    :p char hFmix [out]: File name (character*255) containing parameters for the binary mixture model
    :p char hfij [out]: Description of the binary mixture parameters (character*8 array of dimension nmxpar) The parameters will vary depending on hmodij.
    :p char hbinp [out]: Documentation for the binary parameters (character*255) 
    :p char hmxrul [out]: Description of the mixing rule (character*255) 
    :p int hmodij_length: length of variable ``hmodij`` (default: 3)
    :p int hFmix_length: length of variable ``hFmix`` (default: 255)
    :p int hfij_length: length of variable ``hfij`` (default: 255)
    :p int hbinp_length: length of variable ``hbinp`` (default: 255)
    :p int hmxrul_length: length of variable ``hmxrul`` (default: 255)



.. f:subroutine:: GETMODdll (icomp, htype, hcode, hcite, htype_length, hcode_length, hcite_length)

    
    Retrieve citation information for the property models used.
    
    :p int icomp [in]: Pointer specifying component number; zero and negative values are used for ECS reference fluid(s)
    :p char htype [in]: Flag indicating which model is to be retrieved (character*3)
    :p char hcode [out]: Component model used for property specified in htype (character*3)
    :p char hcite [out]: Component model used for property specified in htype; the first 3 characters repeat the model designation of hcode and the remaining are the citation for the source  (character*255)
    :p int htype_length: length of variable ``htype`` (default: 3)
    :p int hcode_length: length of variable ``hcode`` (default: 3)
    :p int hcite_length: length of variable ``hcite`` (default: 255)


    :Flags: 

        ``htype`` flags

        :'EOS': Equation of state
        :'CP0': Ideal-gas heat capacity
        :'ETA': Viscosity
        :'TCX': Thermal conductivity
        :'TKK': Thermal conductivity critical enhancement
        :'STN': Surface tension
        :'DE ': Dielectric constant
        :'MLT': Melting line (i.e., freezing line)
        :'SBL': Sublimation line
        :'PS ': Vapor pressure equation
        :'DL ': Saturated liquid density equation
        :'DV ': Saturated vapor density equation

        ``hcode`` flags

        :'FEQ': Helmholtz energy model
        :'ECS': Extended corresponding states (all fluids)
        :'VS1': The 'composite' model for R134a, R152a, NH3, etc.
        :'VS2': Younglove-Ely model for hydrocarbons
        :'VS4': Generalized friction theory of Quinones-Cisneros and Dieters
        :'VS5': Chung et al. model
        :'VS6': Vesovic form of VS1 model
        :'VS7': Polynomial/exponential model
        :'TC1': The 'composite' model for R134a, R152a, etc.
        :'TC2': Younglove-Ely model for hydrocarbons
        :'TC5': Predictive model of Chung et al. (1988)
        :'ST1': surface tension as f(tau); tau = 1 - T/Tc


.. f:subroutine:: GETREFDIRdll (hpth, hpth_length)

    
    Get the path where the original fluid files are located.  See
    SETREFDIR for more information.
    
    :p char hpth [out]: Location of the original fluid files (character*255) 
    :p int hpth_length: length of variable ``hpth`` (default: 255)



.. f:subroutine:: GIBBSdll (T, D, z, ar, gr, )

    
    Compute residual Helmholtz and Gibbs energies as functions of
    temperature, density, and composition from core functions, calculated as::
    
        G(T,D) - G0(T,P*) = G(T,D) - G0(T,D) + RTln(RTD/P*)
    
    where G0 is the ideal-gas state and P* is a reference pressure that is equal
    to the current pressure of interest.  Since Gr is used only as a difference
    in phase equilibria calculations where the temperature and pressure of the
    phases are equal, the (RT/P*) part of the log term will cancel and is omitted.
    Normal (not residual) A and G are computed by subroutine AG.
    
    See warning in subroutines THERM or ALLPROPS.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double ar [out]: Residual Helmholtz energy [J/mol] 
    :p double gr [out]: Residual Gibbs free energy [J/mol] 



.. f:subroutine:: HEATFRMdll (T, D, z, hFrm, ierr, herr, herr_length)

    
    Compute the heat of formation.
    
    The heat of formation is the heat required to form a compound from its constituent
    elements, with the standard state defined as 298.15 K for the ideal gas.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] (not used) 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double hFrm [out]: Heat of formation [J/mol] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :662: Not all heating values available
        :664: Unknown species in chemical formula
        :665: Error in chemical formula


.. f:subroutine:: HEATdll (T, D, z, hg, hn, ierr, herr, herr_length)

    
    Compute the ideal-gas gross and net heating values.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double hg [out]: Gross (or superior) heating value [J/mol] 
    :p double hn [out]: Net (or inferior) heating value [J/mol] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :662: Not all heating values available
        :665: Error in chemical formula


.. f:subroutine:: HMXORDERdll (i, j, hcasi, hcasj, iFlag, ierr, herr, hcasi_length, hcasj_length, herr_length)

    
    Return the ID numbers in the order given in the HMX.BNC file, and
    a flag that indicates if the loaded fluids are in the same order.
    
    :p int i [in]: Component i 
    :p int j [in]: Component j 
    :p char hcasi: XXXXXXXXXX
    :p char hcasj: XXXXXXXXXX
    :p int iFlag [out]: Flag to indicate if loaded fluids are in the same order as the i,j pair
    :p int ierr [out]: Error number, not currently used here 
    :p char herr [out]: Error message, not currently used here (character*255) 
    :p int hcasi_length: length of variable ``hcasi`` (default: 255)
    :p int hcasj_length: length of variable ``hcasj`` (default: 255)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``iflag`` flags

        :0: Pair is backwards
        :1: Pair is in correct order (or if i=j)
        :2: Pair is not in HMX.BNC


.. f:subroutine:: HSFL1dll (h, s, z, Dmin, Dmax, T, D, ierr, herr, herr_length)

    
    Iterate for single-phase temperature and density as a function of
    enthalpy, entropy, and composition.
    (See subroutine ABFL1 for the description of all variables.)
    
    :p double h [in]: Enthalpy [J/mol]
    :p double s [in]: Entropy [J/mol-K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double Dmin [in]: Lower bound on density [mol/L]
    :p double Dmax [in]: Upper bound on density [mol/L]
    :p double T [out]: Temperature [K]
    :p double D [out]: Density [mol/K]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: HSFLSHdll (h, s, z, T, P, D, Dl, Dv, x, y, q, e, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given bulk enthalpy, entropy, and composition.
    
    :p double h [in]: Overall enthalpy [J/mol] 
    :p double s [in]: Overall entropy [J/mol-K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double T [out]: Temperature [K] 
    :p double P [out]: Pressure [kPa] 
    :p double D [out]: Overall molar density [mol/L] 
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double e [in]: Overall internal energy [J/mol] But only if iflag in common blocks has been set to 1, in which case the value of the internal energy should be sent in h, and the value of the enthalpy will be returned in e.
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) (See subroutine ABFLSH for the description of all other output variables.) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :260: Iterative routine is not available to find a solution.


.. f:subroutine:: IDCRVdll (D, z, T, ierr, herr, herr_length)

    
    Calculate the temperature at the input density where the compressibility
    factor crosses from less than 1 to greater than 1 (i.e., Z=1).  This
    line starts at zero density at the temperature where B=0, and passes
    into the liquid phase without crossing the two-phase.  The argument z
    in this routine is an array with the mole fractions of the mixture.
    If the input T is non-zero, it is used as the initial guess.
    
    :p double D [in]: Density [mol/l] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double T [out]: Temperature [K] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :151: Iteration failed to converge


.. f:subroutine:: INFOdll (icomp, wmm, Ttrp, Tnbpt, Tc, Pc, Dc, Zc, acf, dip, Rgas, )

    
    Provides fluid constants for the specified component.
    
    :p int icomp [in]: Component number in mixture; 1 for pure fluid 
    :p double wmm [out]: Molar mass (molecular weight) [g/mol] 
    :p double Ttrp [out]: Triple point temperature [K] 
    :p double Tnbpt [out]: Normal boiling point temperature [K] 
    :p double Tc [out]: Critical temperature [K] 
    :p double Pc [out]: Critical pressure [kPa] 
    :p double Dc [out]: Critical density [mol/L] 
    :p double Zc [out]: Compressibility factor at critical point [Pc/(Rgas*Tc*Dc)] 
    :p double acf [out]: Acentric factor [-] 
    :p double dip [out]: Dipole moment [debye] 
    :p double Rgas [out]: Gas constant [J/mol-K] 



.. f:subroutine:: JICRVdll (D, z, T, ierr, herr, herr_length)

    
    Calculate the temperature along the Joule-Inversion curve for the
    input density.  This line starts at zero density at the temperature
    where B is at a maximum, and passes into the liquid phase without
    crossing the two-phase.  It ends at very high pressures.
    The argument z in this routine is an array with the mole fractions
    of the mixture.  If the input T is non-zero, it is used as the
    initial guess.
    
    JI is equal to
    d(Z)/d(T) at constant D
    del*d^2(alphar)/d(del)/d(T)
    -del*tau*d^2(alphar)/d(del)/d(tau)/T (can ignore the /T for finding JI=0)
    
    d(JI)/dT  -> tau**2*del*d^3(alphar)/d(del)/d(tau)**2/T**2
                 (One of the /T must be removed to match the one removed in the function.)
    
    :p double D [in]: Density [mol/l] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double T [out]: Temperature [K] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :151: Iteration failed to converge


.. f:subroutine:: JTCRVdll (D, z, T, ierr, herr, herr_length)

    
    Calculate the temperature along the Joule-Thomson curve for the input
    density.  This line starts at zero density at the temperature where
    the Joule-Thomson property (dH/dT) is zero, and passes into the
    liquid phase without crossing the two-phase.  It ends at a saturated
    liquid state far from the critical point.  The argument z in this
    routine is an array with the mole fractions of the mixture.  If the
    input T is non-zero, it is used as the initial guess.
    
    Only the top part in the calculation of hjt is required, the other
    parts do not go to zero and thus do not contribute to finding JT=0.
    
    :p double D [in]: Density [mol/l] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double T [out]: Temperature [K] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :151: Iteration failed to converge


.. f:subroutine:: LIMITKdll (htyp, icomp, T, D, P, Tmin, Tmax, Dmax, Pmax, ierr, herr, htyp_length, herr_length)

    
    Returns limits of a property model (read in from the *.fld files) for
    a mixture component and checks the inputs against those limits.
    
    This routine simply calls the LIMITX routine with an z array where
    all entries are set to zero except that for icomp.
    
    :p char htyp: XXXXXXXXXX
    :p int icomp: XXXXXXXXXX
    :p double T: XXXXXXXXXX
    :p double D: XXXXXXXXXX
    :p double P: XXXXXXXXXX
    :p double Tmin: XXXXXXXXXX
    :p double Tmax: XXXXXXXXXX
    :p double Dmax: XXXXXXXXXX
    :p double Pmax: XXXXXXXXXX
    :p int ierr: XXXXXXXXXX
    :p char herr: XXXXXXXXXX
    :p int htyp_length: length of variable ``htyp`` (default: 3)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: LIMITSdll (htyp, z, Tmin, Tmax, Dmax, Pmax, htyp_length)

    
    Returns limits of a property model as a function of composition.
    Pure fluid limits were read in from the *.fld files; for mixtures, a
    simple mole fraction weighting in reduced variables is used.
    
    :p char htyp [in]: Flag indicating which models are to be checked (character*3) 'EOS' - Equation of state for thermodynamic properties 'ETA' - Viscosity 'TCX' - Thermal conductivity 'STN' - Surface tension
    :p double z(20) [in]: Composition array (array of mole fractions) 
    :p double Tmin [out]: Minimum temperature for model specified by htyp [K] 
    :p double Tmax [out]: Maximum temperature [K] 
    :p double Dmax [out]: Maximum density [mol/L] 
    :p double Pmax [out]: Maximum pressure [kPa] 
    :p int htyp_length: length of variable ``htyp`` (default: 3)



.. f:subroutine:: LIMITXdll (htyp, T, D, P, z, Tmin, Tmax, Dmax, Pmax, ierr, herr, htyp_length, herr_length)

    
    Returns limits of a property model as a function of composition
    and/or checks inputs T, D, and P against those limits.
    
    Pure fluid limits are read in from the *.fld files; for mixtures, a
    simple mole fraction weighting of the reduced variables is used.
    
    Attempting calculations below the minimum temperature and/or above
    the maximum density may result in an error.  These will often
    correspond to a physically unreasonable state; also many equations of
    state do not extrapolate reliably to lower T's and higher D's.
    
    A warning is issued if the temperature is above the maximum but below
    1.5 times the maximum.  Pressures up to twice the maximum
    result in only a warning.  Most equations of state may be
    extrapolated to higher T's and P's.  Temperatures and/or pressures
    outside these extended limits will result in an error.
    
    When calling with an unknown temperature, set T to -1 to avoid performing
    the melting line check.  If inputs are not available, use T=300, P=0, and D=0.
    
    If multiple inputs are outside limits, ierr=SUM(ABS(ierr)),
    with a positive sign if any error greater than zero (calculations not
    possible), or a negative sign for warnings only.
    
    :p char htyp [in]: Flag indicating the model to check (character*3)
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double P [in]: Pressure [kPa] 
    :p double z(20) [in]: Composition array (array of mole fractions) 
    :p double Tmin [out]: Minimum temperature for model specified by htyp [K] 
    :p double Tmax [out]: Maximum temperature [K] 
    :p double Dmax [out]: Maximum density [mol/L] 
    :p double Pmax [out]: Maximum pressure [kPa] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int htyp_length: length of variable ``htyp`` (default: 3)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``htyp`` flags

        :'EOS': Equation of state
        :'ETA': Viscosity
        :'TCX': Thermal conductivity
        :'STN': Surface tension

        ``ierr`` flags

        :0: All inputs within limits
        :-1: 1.5*Tmax > T > Tmax
        :1: T < Tmin or T > 1.5*Tmax
        :2: D > Dmax or D < 0
        :-4: 2*Pmax > P > Pmax
        :4: P < 0 or P > 2*Pmax
        :8: Component composition < 0 or > 1 and/or composition sum <> 1
        :16: P>Pmelt
        :-16: T<Ttrp (important for water)


.. f:subroutine:: LIQSPNDLdll (T, z, D, ierr, herr, herr_length)

    
    Find the liquid spinodal density for a given temperature.  If no
    spinodal exists, return the point of zero curvature.  This only
    happens with a few of the older equations, these being argon, ethane,
    nitrogen, R22, and R124.
    
    :p double T [in]: Temperature [K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double D [out]: Density at liquid spinodal [mol/L] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :121: T>Tc
        :633: Failed to converge
        :-638: Spinodal not found, point of zero curvature returned


.. f:subroutine:: MASSFLUXdll (Tm, P, z, beta, rf, fluxm, Cs, T0, P0, xMach, u, Ts, Ps, ierr, herr, herr_length)

    
    Calculate the theoretical mass flux for a CFV (critical flow venturi) of a gas.
    This is required for high beta; CSTAR can be used for low beta.
    
    :p double Tm [in]: Measured temperature [K] 
    :p double P [in]: Upstream (static) pressure [kPa] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double beta [in]: Ratio of throat diameter to pipe diameter [-] 
    :p double rf [in]: Recovery factor [(Tm-T)/(T0-T)] (T is static temperature, T0 is the stagnation temperature) 
    :p double fluxm [out]: Theoretical mass flux [kg/(m^2-s)] 
    :p double Cs [out]: Critical flow factor [-] 
    :p double T0 [out]: Stagnation temperature [K] 
    :p double P0 [out]: Stagnation pressure [kPa] 
    :p double xMach [out]: Mach number (u/speed of sound) [-] 
    :p double u [out]: Average axial velocity in approach pipe upstream of the CFV [m/s] 
    :p double Ts [out]: Temperature at throat [K] 
    :p double Ps [out]: Pressure at throat [kPa] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :151: Iteration failed to converge


.. f:subroutine:: MAXPdll (z, Tm, Pm, Dm, ierr, herr, herr_length)

    
    Calculate values at the maximum pressure along the saturation line;
    these are returned from the call to SATSPLN and apply only to the
    composition in the z() array sent to SATSPLN.
    
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double Tm [out]: Temperature [K] 
    :p double Pm [out]: Pressure [kPa] 
    :p double Dm [out]: Density [mol/L] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :331: Splines not available for calculation
        :-362: Maximum pressure not known


.. f:subroutine:: MAXTdll (z, Tm, Pm, Dm, ierr, herr, herr_length)

    
    Calculate values at the maximum temperature along the saturation line;
    these are returned from the call to SATSPLN and apply only to the
    composition in the z() array sent to SATSPLN.
    
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double Tm [out]: Temperature [K] 
    :p double Pm [out]: Pressure [kPa] 
    :p double Dm [out]: Density [mol/L] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :331: Splines not available for calculation
        :-361: Maximum temperature not known


.. f:subroutine:: MELTKdll (icomp, T, P, ierr, herr, herr_length)

    
    Compute melting line with appropriate core model.
    
    :p int icomp [in]: Component i (for water and heavy water, send -icomp to obtain the root with the lower pressure at T<Ttrp)
    :p double T [in]: Temperature [K] 
    :p double P [out]: Melting line pressure [kPa] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255)    There are two functional forms for the melting line, labeled in the fluid files as ML1 and ML2: ML1:  P=Pred*Pr ML2:  P=Pred*Exp(Pr) where: Pr=Sum[Nk*Tr^tk]+Sum[Nk*(Tr-1)^tk]+Sum[Nk*(Log Tr)^tk] Tr=T/Tred In the fluid file, Tred and Pred (the reducing values) are given first, followed by the number of terms in each of the summations, and then followed by the coefficients Nk and exponents tk (one term with Nk and tk listed per line).  
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :1: T<Ttrp
        :-4: P<Ptrp (for MELTP routine)
        :501: No equation available
        :502: Unknown melting line equation


.. f:subroutine:: MELTPdll (P, z, T, ierr, herr, herr_length)

    
    Compute the melting line temperature as a function of pressure
    and composition.
    
    :p double P [in]: Melting line pressure [kPa] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double T [out]: Temperature [K] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :-4: Pressure below triple point pressure
        :501: No equation available


.. f:subroutine:: MELTTdll (T, z, P, ierr, herr, herr_length)

    
    Compute the melting line pressure as a function of temperature
    and composition.
    
    :p double T [in]: Temperature [K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double P [out]: Melting line pressure [kPa] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :501: No equation available


.. f:subroutine:: MLTH2Odll (T, P1, P2, )

    
    Compute melting line of water, see fluid file for reference.
    
    :p double T [in]: Temperature [K] 
    :p double P1 [out]: Higher melting line pressure [kPa] 
    :p double P2 [out]: Lower melting line pressure [kPa] Above 273.16 K, only P1 returns a physical answer. Between 251.165 and 273.16 K, two pressures are returned.  If flags of -998 or -999 are sent for the temperature, the value of the lowest temperature possible (251.165 K) is sent back in T, the pressure at that point is sent back in P1, and the density at that point is sent back in P2 if the flag -998 is used. 



.. f:subroutine:: NAMEdll (icomp, hnam, hn80, hcasn, hnam_length, hn80_length, hcasn_length)

    
    Provides name information for the specified component.
    
    :p int icomp [in]: Component number in mixture; 1 for pure fluid 
    :p char hnam [out]: Component name (character*12) (send icomp+1000 to get the fluid hash) 
    :p char hn80 [out]: Component name - long form (character*80) To return the file name used when SETUP was called (without path), send -icomp. If path is also needed, use PASSCMN.  For example: call PASSCMN ('hdir',0,1,0,hfl,i,xx,arr,ierr,herr)
    :p char hcasn [out]: ID (Chemical Abstracts Service) number (character*12) 
    :p int hnam_length: length of variable ``hnam`` (default: 12)
    :p int hn80_length: length of variable ``hn80`` (default: 80)
    :p int hcasn_length: length of variable ``hcasn`` (default: 12)



.. f:subroutine:: PASSCMNdll (hvr, iset, icomp, jcomp, hstr, ilng, dbl, arr, ierr, herr, hvr_length, hstr_length, herr_length)

    
    Get or set values of variables in the common blocks.
    
    Examples (in FORTRAN)::
    
        call PASSCMN ('txeos',  0,3,0, h,i, tmx,z,   ierr,herr) ! get Tmax of component 3
        call PASSCMN ('dxeos',  1,2,0, h,i, dmx,z,   ierr,herr) ! set Dmax of component 2
        call PASSCMN ('tz',     0,1,0, h,i, Tc, z,   ierr,herr) ! get reducing temperature of component 1
        call PASSCMN ('ntermf', 0,1,0, h,nt,v,  z,   ierr,herr) ! get number of terms in the Helmholtz equation for component 1
        call PASSCMN ('coefhmx',1,1,0, h,i, v,  cf,  ierr,herr) ! set the coefficients in the Helmholtz equation for component 1
        call PASSCMN ('acp0',   1,5,0, h,i, v,  cp0, ierr,herr) ! set the coefficients in the cp0 equation for component 5
        call PASSCMN ('fPRkij', 1,1,2, h,i, v,  fpr, ierr,herr) ! set the PR coefficient for the 1,2 binary
    
    :p char hvr [in]: Character string with the common variable's name 
    :p int iset [in]: Flag to indicate the get/set condition
    :p int icomp [in]: Component number 
    :p int jcomp [in]: Second component number for binary mixture variables 
    :p char hstr [out]: Input or output for a character string 
    :p int ilng [out]: Input or output for a long variable 
    :p double dbl [out]: Input or output for a double precision variable 
    :p double arr(100) [out]: Input or output for a double precision array 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int hvr_length: length of variable ``hvr`` (default: 255)
    :p int hstr_length: length of variable ``hstr`` (default: 255)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``iset`` flags

        :0: Get variable value
        :1: Set variable value

        ``ierr`` flags

        :0: Successful
        :113: Inputs out of bounds
        :601: Variable name not recognized


.. f:subroutine:: PDFL1dll (P, D, z, T, ierr, herr, herr_length)

    
    Iterate for single-phase temperature as a function of pressure,
    density, and composition.
    (See subroutine ABFL1 for the description of all variables.)
    
    :p double P [in]: Pressure [kPa]
    :p double D [in]: Density [mol/K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double T [out]: Temperature [K]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: PDFLSHdll (P, D, z, T, Dl, Dv, x, y, q, e, h, s, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given density, pressure, and bulk composition.
    This routine accepts both single-phase and two-phase states as inputs;
    for single-phase calculations, the subroutine PDFL1 is faster.
    (See subroutines ABFLSH or TPDFLSH for the description of all variables.)
    
    :p double P [in]: Pressure [kPa]
    :p double D [in]: Density [mol/K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double T [out]: Temperature [K]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double e [out]: Internal energy [J/mol]
    :p double h [out]: Enthalpy [J/mol]
    :p double s [out]: Entropy [J/mol-K]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: PEFL1dll (P, e, z, kph, T, D, ierr, herr, herr_length)

    
    Iterate for single-phase temperature and density as a function of
    pressure, energy, and composition.
    (See subroutine ABFL1 for the description of all variables.)
    
    :p double P [in]: Pressure [kPa]
    :p double e [in]: Internal energy [J/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p int kph: XXXXXXXXXX
    :p double T [out]: Temperature [K]
    :p double D [out]: Density [mol/K]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: PEFLSHdll (P, e, z, T, D, Dl, Dv, x, y, q, h, s, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given pressure, bulk energy, and bulk composition.
    (See subroutines ABFLSH or PBFLSH for the description of all variables.)
    
    :p double P [in]: Pressure [kPa]
    :p double e [in]: Internal energy [J/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double T [out]: Temperature [K]
    :p double D [out]: Density [mol/K]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double h [out]: Enthalpy [J/mol]
    :p double s [out]: Entropy [J/mol-K]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: PHFL1dll (P, h, z, kph, T, D, ierr, herr, herr_length)

    
    Iterate for single-phase temperature and density as a function of
    pressure, enthalpy, and composition.
    (See subroutine ABFL1 for the description of all variables.)
    
    :p double P [in]: Pressure [kPa]
    :p double h [in]: Enthalpy [J/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p int kph: XXXXXXXXXX
    :p double T [out]: Temperature [K]
    :p double D [out]: Density [mol/K]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: PHFLSHdll (P, h, z, T, D, Dl, Dv, x, y, q, e, s, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given pressure, bulk enthalpy, and bulk composition.
    (See subroutines ABFLSH or PBFLSH for the description of all variables.)
    
    :p double P [in]: Pressure [kPa]
    :p double h [in]: Enthalpy [J/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double T [out]: Temperature [K]
    :p double D [out]: Density [mol/K]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double e [out]: Internal energy [J/mol]
    :p double s [out]: Entropy [J/mol-K]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: PHI0dll (itau, idel, T, D, z, phi00, )

    
    Compute the ideal-gas part of the reduced Helmholtz energy or its
    derivatives as functions of temperature and density for a mixture.
    
    While the real-gas part of the Helmholtz energy is calculated
    in terms of dimensionless temperature and density, the ideal-
    gas part is calculated in terms of absolute temperature and
    density.  (This distinction is necessary for mixtures.)
    
    The Helmholtz energy consists of ideal-gas and residual
    (real-gas) terms; this routine calculates only the ideal part.
    
    :p int itau [in]: Flag specifying the order of the temperature derivative 
    :p int idel [in]: Flag specifying the order of the density derivative (The density derivatives are not used in the calculation of any property.) when itau = 0 and idel = 0, compute A0/RT when itau = 1 and idel = 0, compute 1st temperature derivative when itau = 2 and idel = 0, compute 2nd temperature derivative when itau = 0 and idel = 1, compute 1st density derivative (actually the derivatives are with respect to the dimensionless quantities tau and del)
    :p double T [in]: Temperature [K] 
    :p double D [in]: Density [mol/L] 
    :p double z(20) [in]: Composition array (array of mole fractions) 
    :p double phi00 [out]: Ideal-gas part of the reduced Helmholtz energy (A/RT); derivatives (as specified by itau and idel) are multiplied by the corresponding power of tau or del; i.e., when itau = 1, the quantity returned is tau*[d(PHI0)/d(tau)] when itau = 2, the quantity returned is tau^2*[d^2(PHI0)/d(tau)^2] when itau = 3, the quantity returned is tau^3*d^3(ph0cpp)/d(tau)^3 where tau=Tc/T and del=D/Dc are evaluated for each component. Similarly, the del derivatives (as specified by idel) are multiplied by the corresponding power of del (the derivatives usually appear with this factor and this approach neatly avoids a possible divide by zero). 



.. f:subroutine:: PHIDERVdll (iderv, T, D, z, dadn, dnadn, ierr, herr, herr_length)

    
    Calculate various derivatives required in the calculation of VLE
    for mixtures.  Most of these are based on equations in the GERG-2004
    document for natural gas, and are given below on the lines where
    the code corresponds directly to the equation in that document.
    
    Only the partials of alpha or alpha*n with respect to mole number are
    returned here.  All others are stored in the PHIDR common block for
    access by subroutine SATGV.
    
    :p int iderv [in]: Set to 1 for first order derivatives only (dadn and dnadn) Set to 2 for full calculations
    :p double T [in]: Temperature [K] 
    :p double D [in]: Density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double dadn(20) [out]: n*partial(alphar)/partial(ni)                   Eq. 7.16 
    :p double dnadn(20) [out]: partial(n*alphar)/partial(ni)                   Eq. 7.15 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255)  The outputs below are stored in the PHIDR common block, and can be obtained by a call to PASSCMN.  :text:
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful Error numbers are not set here, but are returned from either the PHIDERVPR (when Peng-Robinson is active) or RDXHMX routines.


.. f:subroutine:: PHIHMXdll (itau, idel, tau, delta, z, phi, )

    
    Compute reduced Helmholtz energy or its derivative as functions
    of dimensionless temperature and density for the mixture Helmholtz
    equation of state.
    
    See notes in function PHIMIX.
    
    :p int itau [in]: Flag specifying the order of the temperature derivative 
    :p int idel [in]: Flag specifying the order of the density derivative when itau = 0 and idel = 0, compute A/RT when itau = 0 and idel = 1, compute 1st density derivative when itau = 1 and idel = 1, compute cross derivative etc.
    :p double tau [in]: Dimensionless temperature (Tr/T) 
    :p double delta [in]: Dimensionless density (D/Dr) 
    :p double z(20) [in]: Composition array (mole fractions) 
    :p double phi [out]: Residual (real-gas) part of the Helmholtz energy, or one of its derivatives (as specified by itau and idel), in reduced form (A/RT) 



.. f:subroutine:: PHIKdll (icomp, itau, idel, tau, delta, phi, )

    
    Compute reduced Helmholtz energy or a derivative as functions
    of dimensionless temperature and density.
    
    The Helmholtz energy consists of ideal and residual (real-gas)
    terms; this routine calculates only the residual part.
    
    This function computes pure component properties only;
    call PHIX instead for mixtures.
    
    The reducing parameters Tr and Dr are often, but not necessarily,
    equal to the critical temperature and density for pure fluids.
    
    :p int icomp [in]: Pointer specifying component (1..nc) 
    :p int itau [in]: Flag specifying the order of the temperature derivative 
    :p int idel [in]: Flag specifying the order of the density derivative When itau = 0 and idel = 0, compute A/RT. When itau = 0 and idel = 1, compute 1st density derivative. When itau = 1 and idel = 1, compute cross derivative. etc.
    :p double tau [in]: Dimensionless temperature (Tr/T) 
    :p double delta [in]: Dimensionless density (D/Dr) 
    :p double phi [out]: Residual (real-gas) part of the Helmholtz energy, or one of its derivatives (as specified by itau and idel), in reduced form (A/RT) 



.. f:subroutine:: PHIMIXdll (i, j, itau, idel, tau, delta, z, phi, )

    
    Compute reduced Helmholtz energy of mixing (or its derivatives)
    for the binary interaction of components i and j as a function of
    composition and dimensionless temperature and density for the
    mixture Helmholtz equation of state.
    
    The Helmholtz energy consists of ideal-gas and residual (real-gas) terms.
    The residual term consists of ideal-solution and mixing terms.  This
    routine calculates only the residual term.
    
    :p int i: XXXXXXXXXX
    :p int j: XXXXXXXXXX
    :p int itau [in]: Flag specifying the order of the temperature derivative 
    :p int idel [in]: Flag specifying the order of the density derivative when itau = 0 and idel = 0, compute Amix/RT when itau = 0 and idel = 1, compute 1st density derivative when itau = 1 and idel = 1, compute cross derivative etc.
    :p double tau [in]: Dimensionless temperature (Tr/T) 
    :p double delta [in]: Dimensionless density (D/Dr) 
    :p double z(20) [in]: Composition array (mole fractions) 
    :p double phi [out]: Mixture interaction (excess) part of the Helmholtz energy, or one of its derivatives (as specified by itau and idel), in reduced form (Amix/RT) 



.. f:subroutine:: PHIXdll (itau, idel, tau, delta, z, phixx, )

    
    Compute reduced Helmholtz energy or a derivative as functions
    of dimensionless temperature and density by calling the appropriate
    mixture model.
    
    The Helmholtz energy consists of ideal-gas and residual (real-
    gas) terms.  The residual term consists of ideal-solution and
    mixing terms.  This routine calculates only the residual term.
    
    :p int itau [in]: Flag specifying the order of the temperature derivative 
    :p int idel [in]: Flag specifying the order of the density derivative When itau = 0 and idel = 0, compute A/RT. When itau = 0 and idel = 1, compute 1st density derivative. When itau = 1 and idel = 1, compute cross derivative. etc.
    :p double tau [in]: Dimensionless temperature (Tr/T) 
    :p double delta [in]: Dimensionless density (D/Dr) 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double phixx [out]: Residual (real-gas) part of the Helmholtz energy, or one of its derivatives (as specified by itau and idel), in reduced form (A/RT) 



.. f:subroutine:: PQFLSHdll (P, q, z, kq, T, D, Dl, Dv, x, y, e, h, s, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given pressure, quality, and bulk composition.
    This routine accepts saturation or two-phase states as inputs.
    (See subroutines ABFLSH or AQFLSH for the description of all variables.)
    
    :p double P [in]: Pressure [kPa]
    :p double q [in]: Vapor quality [mol/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p int kq: XXXXXXXXXX
    :p double T [out]: Temperature [K]
    :p double D [out]: Density [mol/K]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double e [out]: Internal energy [J/mol]
    :p double h [out]: Enthalpy [J/mol]
    :p double s [out]: Entropy [J/mol-K]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: PREOSdll (i, )

    
    Turn on or off the use of the PR cubic equation.  Should be called after
    calling SETUP.
    
    :p int i [in]: Flag specifying use of PR


    :Flags: 

        ``i`` flags

        :0: Use full equation of state (Peng-Robinson off)
        :1: Use full equation of state with Peng-Robinson for sat. conditions (not currently working)
        :2: Use Peng-Robinson equation for all calculations
        :3: Peng-Robinson with translation term deactivated if i=-1, then i is returned with the current status of the PR EOS. A value of zero indicates that it is not in use. When in use, a 2 or 3 will be returned, depending on which option above was previously selected.


.. f:subroutine:: PRESSdll (T, D, z, P, )

    
    Compute pressure as a function of temperature, density, and composition.
    See warning in subroutines THERM or ALLPROPS.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double P [out]: Pressure [kPa] 



.. f:subroutine:: PSATKdll (icomp, T, P, ierr, herr, herr_length)

    
    Compute pure fluid vapor or liquid pressures with the appropriate
    ancillary equation.
    
    :p int icomp [in]: Component i.  For liquid pressure equations (pseudo-pure fluids only), send -i.
    :p double T [in]: Temperature [K] 
    :p double P [out]: Vapor or liquid pressure [kPa] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :121: Temperature greater than critical point temperature


.. f:subroutine:: PSFL1dll (P, s, z, kph, T, D, ierr, herr, herr_length)

    
    Iterate for single-phase temperature and density as a function of
    pressure, entropy, and composition.
    (See subroutine ABFL1 for the description of all variables.)
    
    :p double P [in]: Pressure [kPa]
    :p double s [in]: Entropy [J/mol-K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p int kph: XXXXXXXXXX
    :p double T [out]: Temperature [K]
    :p double D [out]: Density [mol/K]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: PSFLSHdll (P, s, z, T, D, Dl, Dv, x, y, q, e, h, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given pressure, bulk entropy, and bulk composition.
    (See subroutines ABFLSH or PBFLSH for the description of all variables.)
    
    :p double P [in]: Pressure [kPa]
    :p double s [in]: Entropy [J/mol-K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double T [out]: Temperature [K]
    :p double D [out]: Density [mol/K]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double e [out]: Internal energy [J/mol]
    :p double h [out]: Enthalpy [J/mol]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: PUREFLDdll (icomp, )

    
    Change the standard mixture setup so that the properties of one fluid
    can be calculated as if SETUP had been called for a pure fluid.
    Calling this routine will disable all mixture calculations.
    To reset the mixture setup, call this routine with icomp=0.
    
    :p int icomp [in]: fluid number in a mixture to use as a pure fluid (set to zero to reset) 



.. f:subroutine:: QMASSdll (qmol, xl, xv, qkg, xlkg, xvkg, wliq, wvap, ierr, herr, herr_length)

    
    Converts quality and composition on a molar basis to a mass basis.
    
    :p double qmol [in]: Molar quality (moles of vapor/total moles) qmol = 0 indicates saturated liquid qmol = 1 indicates saturated vapor 0 < qmol < 1 indicates a two-phase state qmol < 0 or qmol > 1 are not allowed and will result in warning
    :p double xl(20) [in]: Composition of liquid phase (array of mole fractions) 
    :p double xv(20) [in]: Composition of vapor phase (array of mole fractions) 
    :p double qkg [out]: Quality on mass basis (mass of vapor/total mass) 
    :p double xlkg(20) [out]: Mass composition of liquid phase (array of mass fractions) 
    :p double xvkg(20) [out]: Mass composition of vapor phase (array of mass fractions) 
    :p double wliq [out]: Molar mass of liquid phase [g/mol] 
    :p double wvap [out]: Molar mass of vapor phase [g/mol] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: All inputs within limits
        :-19: Input q < 0 or > 1


.. f:subroutine:: QMOLEdll (qkg, xlkg, xvkg, qmol, xl, xv, wliq, wvap, ierr, herr, herr_length)

    
    Converts quality and composition on a mass basis to a molar basis.
    
    :p double qkg [in]: Quality on mass basis (mass of vapor/total mass) qkg = 0 indicates saturated liquid qkg = 1 indicates saturated vapor 0 < qkg < 1 indicates a two-phase state qkg < 0 or qkg > 1 are not allowed and will result in warning
    :p double xlkg(20) [in]: Mass composition of liquid phase (array of mass fractions) 
    :p double xvkg(20) [in]: Mass composition of vapor phase (array of mass fractions) 
    :p double qmol [out]: Quality on molar basis (moles of vapor/total mass) 
    :p double xl(20) [out]: Molar composition of liquid phase (array of mole fractions) 
    :p double xv(20) [out]: Molar composition of vapor phase (array of mole fractions) 
    :p double wliq [out]: Molar mass of liquid phase [g/mol] 
    :p double wvap [out]: Molar mass of vapor phase [g/mol] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: All inputs within limits
        :-19: Input q < 0 or > 1


.. f:subroutine:: RDXHMXdll (ix, icmp, icmp2, z, Tred, Dred, ierr, herr, herr_length)

    
    Returns reducing parameters and their derivatives associated with
    the mixture Helmholtz EOS; these are used to calculate the 'tau' and 'del'
    that are the independent variables in the EOS.
    
    :p int ix [in]: Flag specifying the order of the composition derivative to calculate, when ix = 0, compute T(red) and D(red) for icmp2=0 when ix = 1, compute 1st derivative with respect to z(icmp) or z(icmp2) when ix = 2, compute 2nd derivative with respect to z(icmp) or z(icmp2) for icmp<>0 and icmp2<>0 when ix = 11, compute cross derivative with respect to z(icmp) and z(icmp2) 
    :p int icmp [in]: Component number for which derivative will be calculated 
    :p int icmp2 [in]: Second component number for which derivative will be calculated 
    :p double z(20) [in]: Composition array (array of mole fractions) 
    :p double Tred [out]: Reducing temperature [K] or derivative 
    :p double Dred [out]: Reducing molar density [mol/L] or derivative of reducing volume [L/mol] (ix=0 - Dc; ix=1 - dVc/dxi; ix=2 - d^2Vc/dxi^2; ix=11 - d^2Vc/dxidxj)
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :301: Mixing rule not found for i,j
        :191: Derivative not available


.. f:subroutine:: REDXdll (z, Tred, Dred, )

    
    Returns the reducing parameters associated with mixture EOS;
    used to calculate the 'tau' and 'del', which are the independent
    variables in the EOS.
    
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double Tred [out]: Reducing temperature [K] 
    :p double Dred [out]: Reducing molar density [mol/L] 



.. f:subroutine:: REFPROP1dll (hIn, hOut, iUnits, iMass, a, b, z, c, q, ierr, herr, hIn_length, hOut_length, herr_length)

    
    Short version of subroutine REFPROP that eliminates the arrays and the
    need to send the fluid names each time.
    
    The variable Output (which is an array) is not included here,
    rather the variable c returns the calculated value as a double
    precision variable, and thus only one value can be returned at a time.
    If the error number (ierr) is zero, the string contained in hUnits
    will be sent back in herr.
    
    If q (quality) returns a value between zero and one (and thus
    the state is two-phase), the REFPROP routine will be needed to obtain
    the equilibrium compositions.
    
    :p char hIn [in]: Input string of properties being sent to the routine. 
    :p char hOut [in]: Output string of properties to be calculated. 
    :p int iUnits [in]: The unit system to be used for the input and output properties (such as SI, English, etc.) See the details in the REFPROP subroutine for a complete description of the iUnits input value. **NOTE** A mass based value for iUnits does not imply that the input and output compositions are on a mass basis, this is specified with the iMass variable.
    :p int iMass [in]: Specifies if the input composition is mole or mass based
    :p double a [in]: First input property as specified in the hIn variable. 
    :p double b [in]: Second input property as specified in the hIn variable. 
    :p double z(20) [in]: Composition on a mole or mass basis depending on the value sent in iMass (array of size ncmax=20). 
    :p double c [out]: Output value. The number -9999970 will be returned when errors occur, and the number -9999990 will be returned when nothing was calculated. Read the comments in the ALLPROPS routine for more information.
    :p double q [out]: Vapor quality on a mole or mass basis depending on the value of iMass.  (See subroutine ABFLSH for the definitions of values returned for this variable).  To obtain the molar quality regardless of iMass, send "qmole" as an input in hIn, and vice-versa for "qmass".
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int hIn_length: length of variable ``hIn`` (default: 255)
    :p int hOut_length: length of variable ``hOut`` (default: 255)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``imass`` flags

        :0: Input compositions given in mole fractions, quality on a molar basis.
        :1: Input compositions given in mass fractions, quality on a mass basis. For two-phase states, the values in x and y will be returned on a mass basis if iMass=1. **NOTE**  If the fluid string sent to this routine contains the word "mass" at the end (and thus contains the composition as well as the names of the fluids), this will have preference over the value of iMass when converting those compositions from a mass to a molar basis.  However, compositions sent back will still be based on the value in iMass.


.. f:subroutine:: REFPROP2dll (hFld, hIn, hOut, iUnits, iFlag, a, b, z, Output, q, ierr, herr, hFld_length, hIn_length, hOut_length, herr_length)

    
    Short version of subroutine REFPROP that eliminates the less used variables such as the x and y composition
    arrays. If the error number (ierr) is zero, the string contained in hUnits will be sent back in herr.
    
    If q (quality) returns a value between zero and one (and thus the state is two-phase), the REFPROP routine
    will be needed to obtain the equilibrium compositions.
    
    See subroutine REFPROP for further information on the input and output variables below.
    
    :p char hFld [in]: Fluid string. 
    :p char hIn [in]: Input string of properties being sent to the routine. 
    :p char hOut [in]: Output string of properties to be calculated. 
    :p int iUnits [in]: The unit system to be used for the input and output properties (such as SI, English, etc.) 
    :p int iFlag [in]: Flag to specify if the routine SATSPLN should be called (where a value of 1 activates the call). 
    :p double a [in]: First input property as specified in the hIn variable. 
    :p double b [in]: Second input property as specified in the hIn variable. 
    :p double z(20) [in]: Molar composition (array of size ncmax=20). 
    :p double Output(200) [out]: Array of properties specified by the hOut string (array of size 200 dimensioned as double precision). The number -9999970 will be returned when errors occur, and the number -9999990 will be returned when nothing was calculated. Read the comments in the ALLPROPS routine to fully understand the contents of this array.
    :p double q [out]: Vapor quality on a mole basis. 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int hFld_length: length of variable ``hFld`` (default: 10000)
    :p int hIn_length: length of variable ``hIn`` (default: 255)
    :p int hOut_length: length of variable ``hOut`` (default: 255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: REFPROPdll (hFld, hIn, hOut, iUnits, iMass, iFlag, a, b, z, Output, hUnits, iUCode, x, y, x3, q, ierr, herr, hFld_length, hIn_length, hOut_length, hUnits_length, herr_length)

    
    Calculate the properties identified in the hOut string for the inputs specified in the hIn string for the
    fluid or mixture given in the hFld string.  The unit identifier for the properties should be passed in
    the iUnits variable (as described below).  Compositions can be sent as mole fractions or mass
    fractions in the zm array depending on the value of iMass.
    
    Several items must be considered before using this routine.  The most important is the speed of calculations.
    The original fortran code that called dedicated functions such as TPRHO, TPFLSH, PHFLSH, and so on (mostly
    given in FLSH_SUB.FOR) and the non-iterative functions such as THERM and TRNPRP requires very little (or none)
    string comparisons and are quite fast.  Multiple string comparisons are made to determine the inputs and outputs
    the user has selected.  Due to the limitation of Fortran in string parsing, this will cause a dramatic
    increase in the time required to make the calculations, such as two to three times as long as the dedicated
    functions.  Thus the ease of use of this REFPROP subroutine versus the speed of calculation from the older
    routines must be considered before developing any application.
    
    **Information on hFld**
    
    For a pure fluid, hfld contains the name of the fluid file (with a path if needed).
    
    For a mixture, it contains the names of the constituents in the mixture separated by semicolons
    or asterisks.  Once the routine has been called with hFld set to the desired fluids, a space can be
    sent for all other calls that use the same fluid(s).  For a predefined mixture, the extension ".mix"
    must be included.  If the composition is included in the hFld variable, or if a predefined mixture is
    selected, the composition will be returned in the zm array (on a molar or mass basis depending on iMass.)
    That composition (or other compositions) must be sent in zm in all subsequent calls to this routine.
    See subroutines SETFLUIDS and SETMIXTURE further below for additional information and examples.
    
    *Note*:  The speed of the program will be increased (sometimes substantially) if you call this routine
    only once with the name of the fluid and then never again unless your fluid or mixture changes.
    If your composition changes, send the new composition in the z array rather then sending
    a new string in the hfld variable.
    
    Examples::
    
        hFld='NITROGEN'
        hFld='C:/Program Files (x86)/REFPROP/FLUIDS/R1234YF.FLD'
        hFld='CARBON DIOXIDE'
        hFld='METHANE;ETHANE;PROPANE;BUTANE;ISOBUTANE'
        hFld='METHANE*ETHANE*PROPANE*BUTANE*ISOBUTANE'
        hFld='R134a;0.3; R1234yf;0.3; R1234ze(Z);0.4'
        hFld='CO2;0.2 * isobutane;0.3 * propadiene;0.5'
        hFld='Nitrogen;Oxygen;Argon|0.4;0.3;0.3'
        hFld='Nitrogen; Oxygen; Argon   ~   0.4; 0.3; 0.3'
        hFld='R410A.MIX'
    
    **Information on hIn**
    
    Valid codes are T, P, D, E, H, S, and Q
    (temperature, pressure, density, energy, enthalpy, entropy, and quality).  Two of these should be
    sent together to identify the contents of the a and b variables.  For example, 'TP' would indicate
    inputs of temperature and pressure, and 'TQ' would indicate inputs of temperature and quality.
    A value of 0 for the quality will return a saturated liquid state, and a value of 1 will return
    a saturated vapor state.  A value between 0 and 1 will return a two-phase state.
    Valid inputs are:  TP, TD, TE, TH, TS, TQ, PD, PE, PH, PS, PQ, DE, DH, DS, DQ, ES, EQ, HS, HQ, SQ
    (or the inverse of any of these, e.g., QT) (hIn is not case sensitive, e.g., 'TQ' = 'tq').
    When q is >0 and <1, then the quality uses a molar basis when iMass=0 and a mass basis
    when iMass=1.  The value of iUnits has no effect on the value of q (as either an input or output).
    The shortcuts Tsat and Psat can be used to specify a saturation state for the liquid for a pure fluid.
    To return, for example, the saturated vapor density, Dvap would be used as an output variable.
    The order of the properties being sent to the routine in the variables a and b has to be the
    same as the letters sent to hIn; for example, if hIn is 'QT', then a=q and b=T.
    
    The ABFLSH routine is called to determine the phase of the inputs (liquid, vapor, or 2-phase), and
    then the appropriate iterative routine will be called to obtain the independent properties of the
    equations of state:  these being temperature and density.  For subsequent calculations for
    properties that are in the single phase, use the code TD&, where the symbol & indicates the single
    phase state.  The time required with the use of TD& is negligible compared to that required for
    the iterative solution called by ABFLSH.  However, the properties sent to this routine and the calculated
    outputs are cached to avoid additional iterative calls when the solution has already been determined.
    Be sure to read the warnings at the top of the ALLPROPS routine for additional information.
    
    Flags to specify certain phases are listed below, for example, 'TD>' would specify an input state
    in the liquid phase but which would normally be two-phase.  Those available are:
    
    - ``**>`` or ``**L``:  When the letter 'L' is attached after the two letters that specify the input properties
      (such as 'TP'), the routine will assume that the input properties are in the single phase
      liquid region, or are within the two-phase area as a metastable state.  For example:
      TP>, PH>, HSL
    
    - ``**<`` or ``**V``: The letter 'V' (or the sign '<') specifies that the input state for the properties listed
      in the first two letters is in the single phase vapor (including metastable states).  For
      example:  TP<, PH<, HSV
    
    - ``TH<`` or ``TH>``: Inputs of temperature and enthalpy (or occasionally temperature and internal energy) generally
      have two valid states.  To obtain the root with the higher pressure, use TH> or TE>,
      and for the lower pressure use TH< or TE<.
    
    - ``*MELT``: Return properties at the melting point where the input property is specified by the ``*``,
      for example TMELT requires the temperature for the input variable a, PMELT requires the
      pressure for input variable a, and so on.
    
    - ``*SUBL``: Return properties at the sublimation point, as described above for the melting point.
    
    - ``CRIT``: Return properties at the critical point (for example, hIn='CRIT' and hOut='S' would return
      the entropy at Tc and Dc).  For a mixture, the critical point defined by the equation of state
      is only available if the SATSPLN routine has been called, otherwise an estimated value
      is returned.
    
    - ``TRIP``: Return liquid phase properties at the triple point.
    
    - ``NBP``: Return properties at the normal boiling point.
    
    - ``DSAT``: Return the saturation properties for the input density.
    
    - ``HSAT``, ``HSAT2``: Enthalpy can be doubled valued in the vapor phase for some fluids.  In such a situation,
      HSAT2 will return the root with the lower temperature.
    
    - ``SSAT``, ``SSAT2``, ``SSAT3``: Entropy can be doubled or triple valued in the vapor phase for some fluids (see butane
      for example).  In such a situation, SSAT will return the root at the highest temperature,
      SSAT2 will return the middle root, and SSAT3 will return the root with the lowest
      temperature.
    
    Various flags are available that can be sent to this routine in the variable hIn to gain access to all other
    features of the Refprop program.  These cannot be combined as multiple inputs in hIn:
    
    - ``FLAGS``: Call the FLAGS routine at the bottom of this file to initialize the options available for
      controlling certain aspects of the Refprop program.  Some of these include caching properties,
      turning on/off different types of equations of state (Peng-Robinson, GERG-2008, and AGA-8), the
      calorie to Joule definition, and so on.  The flag string (the first input to the FLAGS routine)
      should be sent in hOut and the flag option should be sent in iFlag.  The output (3rd variable in the
      routine) is returned in iUCode.  See the FLAGS routine for further information.  The variable hFld
      for the REFPROP routine should be left blank when using this option.
    
    - ``EOSMIN``: Return the property specified in hOut at the minimum temperature allowed in the equation
      of state.  This is generally at the triple point in the liquid phase.  Note that an input
      of P or D will not return the obvious minimum (zero), but the pressure and density at the
      liquid phase triple point (or lower temperature limit for a mixture).  For water, the
      triple point T is still returned, even though lower temperatures are possible.
    
    - ``EOSMAX``: Return the maximum temperature, pressure, or density (as specified in hOut) for the
      equation of state.  The maximum density of the equation of state does not occur at the
      maximum pressure and temperature.  Only T, P, or D can be returned one at a time to
      emphasize that properties at Tmax and Pmax are not the same as at Tmax and Dmax.
    
    - ``SETREF``: Call the SETREF routine.  The reference state (DEF, NBP, IIR, ASH, OTH, OT0, or NA)
      should be sent in hOut.  For the OTH and OT0 options, the values of h0, s0, T0, and P0
      should be included in the hOut variable, separated by semicolons.  For example::
    
               hOut='OTH;10.;1.;323.15;101.325'
    
      This would set the enthalpy to 10 J/mol and the entropy to 1 J/mol-K at 323.15 K
      and 101.325 kPa.  In the GUI is an option for mixtures to set the reference state to
      either the composition in use or to each pure fluid.  To set this option through the DLL,
      a value of either 1 or 2 should be sent to this routine in the variable a.
      This will set the variable labeled ixflag in subroutione SETREF in the SETUP.FOR file.
      All other options for this command are also explained in the SETUP.FOR file.
    
    - ``SETREFOFF``: Turn off the inputs that were sent in the option above.
    
    - ``PATH``: Call the SETPATH routine with the path given in hFld.
    
    - ``SATSPLN``: Call the SATSPLN routine for the input composition (as described in the SAT_SUB.FOR
      file).  The fluid name or mixture names and the composition must be sent with this
      command or have already been setup before this is called.  This command is identical to
      calling this routine with iFlag=1, except that it can be issued at any time.
    
    **Information on hOut**
    
    String output is returned in hUnits.  Numerical output is returned in Output(1).  For flags used to obtain a value
    of a particular fluid in a mixture, the component number should be added after the command, such as NAME(3)
    or FDIR(1).  Only one string output can be requested at a time for the following flags, down to the line
    that says DLL#.  Use the ALLPROPS routine to return multiple strings for all the components in the mixture.
    This is done without using the component number, e.g., sending "NAME" to that routine.  For numerical values,
    multiple inputs can be requested here, and must be separated by spaces, commas, semicolons, or bars, but these
    separators should not be mixed.  See subroutine ALLPROPS (which follows this routine) for further information.
    
    - ``ALTID``: Return the alternative fluid whose mixing rules are used when others are not available.
    - ``CAS#``: Return the CAS number.
    - ``CHEMFORM``: Return the short chemical formula.
    - ``SYNONYM``: Return the synonym found on the fifth line in the fluid files.
    - ``FAMILY``: Return the family class used for several predictive schemes.
    - ``FLDNAME``: Return the fluid file name sent to the SETUP routine.
    - ``HASH``: Return the hash number.
    - ``INCHI``: Return the INCHI string.
    - ``INCHIKEY``: Return the INCHI key.
    - ``LONGNAME``: Return the long fluid name given in the 3rd line of the fluid files.
    - ``SAFETY``: Return the ASHRAE 34 classification.
    - ``NAME``: Return the fluid short name.
    - ``NCOMP``: Return the number of components.
    - ``UNNUMBER``: Return the UN number.
    - ``DOI_###``: Return the DOI of the equation given by the three letters following the underscore, where the valid letters
      are EOS for equation of state, VIS for viscosity, TCX for thermal conductivity, STN for surface tension,
      DIE for dielectic constant, MLT for melting line, and SBL for sublimation line.  For example, DOI_EOS would
      return the DOI for the equation of state.
    - ``WEB_###``: Return the web address for the equation given by the three letters following the underscore, as explained
      in the DOI section.
    - ``REFSTATE``: Return the reference state in use (NBP, IIR, ASH, OTH, etc.)
    - ``GWP``: Return the global warming potential (found in the fluid file header).
    - ``ODP``: Return the ozone depletion potential (found in the fluid file header).
    - ``FDIR``: Return the location (directory) of the fluid file.  The directory is returned in both the hUnits string and in
      herr if no other error occurred (paths that are more than 50 characters long are truncated in hUnits).  An error
      code of -999 will also be returned that can be used to check if herr is the path and not another error message.
      For mixtures, send FDIR(2), etc., to get the path of the second fluid and so on.
    - ``UNITSTRING``: Return the units of the property (e.g., K, psia, kg/m^3, J/mol, etc.) identified in hIn for the unit system
      defined in hFld (e.g., SI, E, etc.).  The input values for hIn are the labels described in the ALLPROPS
      routine.  For example, 'D2DDP2' would return '(kg/m^3)/MPa^2' for 'SI' inputs.
    - ``UNITNUMB``: Return in iUCode the integer value associated with a particular set of units defined in hFld (SI, E, etc.).
      This integer value can then be used in subsequent calls for the iUnits variable.
    - ``UNITS``: Perform both operations in UNITSTRING and UNITNUMB.
    - ``UNITCONV``: Convert the property contained in the variable a from units given in hFLD to units given in hIn.
      The unit strings are given much further below.  When converting from mole to mass units
      (or vice versa), the molar mass must be sent in the variable b.  The type of property
      (as specified in the CONVUNITS subroutine) must be appended to the string in hOut, for example,
      hOut='UNITCONV_T' or hOut='UNITCONV_D'
    - ``UNITUSER``, ``UNITUSER2``: Set a predefined set of units based on the user's need.
      Two different sets can be assigned depending on the input sent to the routine.  The variable hIn
      contains the numbers that are specified by the enumerations in the CONSTS.INC file, separated by semicolons.
      For example, hIn='0;157;0;0;0;403;0;0;0;0' would set the pressure to use units of atm and the
      speed of sound to use units of km/h. The numbers are listed in the order of T, P, D, H, S, W, I, E, K, and N.
      (temperature, pressure, density, enthalpy, entropy, speed of sound, kinematic viscosity, viscosity,
      thermal conductivity, and surface tension).  Because the enumerations might change, it is best to build this
      string with the enumerations listed in the CONSTS.INC file rather than hard coding the numbers as shown above.
    - ``DLL#``: Return the version number of the DLL in iUCode and the string value in hUnits.
    - ``PHASE``: Return the phase of the state for the input fluids and properties.  See subroutine PHASE for a
      listing of all possibilities.  The output is sent back in the hUnits variable.  No other command
      can be sent with this one since hUnits is not an array.
    - ``FULLCHEMFORM``: Return the long chemical formula.
    - ``HEATINGVALUE``: Return the upper heating value.
    - ``LIQUIDFLUIDSTRING``: Return a string that contains the fluid names and compositions for the liquid phase of a two-phase state.
    - ``VAPORFLUIDSTRING``: Likewise for the vapor phase.
      For example, "R32;R125|0.25;0.75".  The string is passed back in hUnits.
    - ``QMOLE``: Return the molar quality for 2-phase states.
    - ``QMASS``: Return the mass quality for 2-phase states.
    - ``XMASS``: Return the mass compositions in the Output array as with the X command.  See comment one line up.
    - ``XLIQ``: Return the mass or molar liquid compositions (depending on the value of iMass) for 2-phase states.
    - ``XVAP``: Return the mass or molar vapor  compositions (depending on the value of iMass) for 2-phase states.
    - ``XMOLELIQ``: Return the liquid compositions for 2-phase states on a mole basis regardless of the iMass variable.
    - ``XMOLEVAP``: Return the vapor  compositions for 2-phase states on a mole basis regardless of the iMass variable.
    - ``XMASSLIQ``: Return the liquid compositions for 2-phase states on a mass basis regardless of the iMass variable.
    - ``XMASSVAP``: Return the vapor  compositions for 2-phase states on a mass basis regardless of the iMass variable.
    - ``*LIQ``: (where * is T, P, D, etc.)
      Return the liquid saturation properties for the property listed as the first letter.
      This is only valid for saturation states or 2-phase states.
    - ``*VAP``: (where * is T, P, D, etc.)
      Return the vapor saturation properties for the property listed as the first letter.
      This is only valid for saturation states or 2-phase states.
    - ``FIJMIX``: Return the mixing parameters in the first six slots of the variable Output for the binary mixture identified
      by the values in the a and b variables (i.e., integer values are sent in double precision variables).
      The mixing rule is returned in the hUnits string.
    
    **Information on iUnits**
    
    Multiple unit systems are available for use in property values, such as the
    SI system, English system, mixed sets, and so forth.  Each set is identified
    with an enumerated value, which is sent as an input code in iUnits.
    
    <FORTRAN ONLY> The enumerated value for the different unit systems are listed below and in
    the ``CONSTS.INC`` file, which can be included in your FORTRAN program, as such::
    
        include 'CONSTS.INC'
    
    .. warning::
    
        Do NOT include any other INC file in your programs
    
    The enumerated values for the unit systems are given by the parameters
    
    - ``iUnitsMolSI``
    - ``iUnitsSI``
    - ...
    
    </FORTRAN ONLY>
    
    In all environments other than FORTRAN, the iUnits variable should be retrieved from the GETENUM function
    with a call like::
    
        GETENUMdll(0,'MOLAR BASE SI',iEnum,ierr,herr)
    
    .. warning::
    
        The integer values for iUnits given below should **NEVER** be used directly, you should always retrieve the enumerated
        value from GETENUM.  This is to allow the developers of Refprop flexibility in the future.
    
    The unit systems used in Refprop are as follows::
    
    
                         DEFAULT     MOLE SI     MASS SI       SI WITH C
        iUnits --->      0           1           2             3
        Temperature      K           K           K             C
        Pressure         KPa         MPa         MPa           MPa
        Density          mol/dm^3    mol/dm^3    kg/m^3        kg/m^3
        Enthalpy         J/mol       J/mol       J/g           J/g
        Entropy          (J/mol)/K   (J/mol)/K   (J/g)/K       (J/g)/K
        Speed            m/s         m/s         m/s           m/s
        Kinematic vis.   cm^2/s      cm^2/s      cm^2/s        cm^2/s
        Viscosity        uPa-s       uPa-s       uPa-s         uPa-s
        Thermal cond.    W/(m-K)     mW/(m-K)    mW/(m-K)      mW/(m-K)
        Surface tension  N/m         mN/m        mN/m          mN/m
        Molar Mass       g/mol       g/mol       g/mol         g/mol
    
                         MOLAR       MASS
                         BASE SI     BASE SI     ENGLISH       MOLAR ENGLISH
        iUnits --->      100         101         5             6
        Temperature      K           K           F             F
        Pressure         Pa          Pa          psia          psia
        Density          mol/m^3     kg/m^3      lbm/ft^3      lbmol/ft^3
        Enthalpy         J/mol       J/kg        Btu/lbm       Btu/lbmol
        Entropy          (J/mol)/K   (J/kg)/K    (Btu/lbm)/R   (Btu/lbmol)/R
        Speed            m/s         m/s         ft/s          ft/s
        Kinematic vis.   m^2/s       m^2/s       ft^2/s        ft^2/s
        Viscosity        Pa-s        Pa-s        lbm/(ft-s)    lbm/(ft-s)
        Thermal cond.    W/(m-K)     W/(m-K)     Btu/(h-ft-R)  Btu/(h-ft-R)
        Surface tension  N/m         N/m         lbf/ft        lbf/ft
        Molar Mass       kg/mol      kg/mol      lbm/lbmol     lbm/lbmol
    
                         MKS         CGS         MIXED         MEUNITS
        iUnits --->      7           8           9             10
        Temperature      K           K           K             C
        Pressure         kPa         MPa         psia          bar
        Density          kg/m^3      g/cm^3      g/cm^3        g/cm^3
        Enthalpy         J/g         J/g         J/g           J/g
        Entropy          (J/g)/K     (J/g)/K     (J/g)/K       (J/g)/K
        Speed            m/s         cm/s        m/s           cm/s
        Kinematic vis.   cm^2/s      cm^2/s      cm^2/s        cm^2/s
        Viscosity        uPa-s       uPa-s       uPa-s         cpoise
        Thermal cond.    W/(m-K)     mW/(m-K)    mW/(m-K)      mW/(m-K)
        Surface tension  mN/m        dyne/cm     mN/m          mN/m
        Molar Mass       g/mol       g/mol       g/mol         g/mol
    
                         USER (can be changed by calling the REFPROP subroutine)
        iUnits --->      11
        Temperature      C
        Pressure         psig
        Density          kg/m^3
        Enthalpy         J/g
        Entropy          (J/g)/K
        Speed            m/s
        Kinematic vis.   cm^2/s
        Viscosity        mPa-s
        Thermal cond.    W/(m-K)
        Surface tension  N/m
        Molar Mass       g/mol
    
    **Information on iUCode output**
    
    The iUCode variable uses a four digit code that specifies the units of the property:
    
    - Left digit         : Energy unit in J/mol or kJ/kg
    - Left middle digit  : Density unit in mol/dm^3 or kg/m^3
    - Right middle digit : Pressure unit in kPa
    - Right digit        : Temperature unit in K
    
    Each digit indicates the power of the unit, for example, a
    value of 2 for the temperature digit corresponding to K^2.
    Values from 6 to 9 specify a negative power digit, for
    example, a value of 8 would be 1/kPa^2.
    
    The following values give other examples::
    
        1000    J/mol
        0100    mol/dm^3
        0010    kPa
        0001    K
        0000    -  (a value of zero assumes a dimensionless unit)
        9000    1/(J/mol)
        0910    kPa/(mol/dm^3)
        0190    (mol/dm^3)/kPa
        8765    K^5/[(J/mol)^2*(mol/dm^3)^3*kPa^4]
        2082    (J/mol)^2*K^2/kPa^2
        0830    kPa^3/(mol/dm^3)^2
        9281    (mol/dm^3)^2*K/[(J/mol)*kPa^2]
        8139    (mol/dm^3)*kPa^3/[(J/mol)^2*K]
        2288    (J/mol)^2*(mol/dm^3)^2/[kPa^2*K^2]
        1764    (J/mol)*K^4/[(mol/dm^3)^3*kPa^4]
        4857    (J/mol)^4*kPa^5/[(mol/dm^3)^2*K^3]
        2730    (J/mol)^2*kPa^3/(mol/dm^3)^3
        6666    1/[(J/mol)^4*(mol/dm^3)^4*kPa^4*K^4]
    
    Negative values represent special units not built on these four property types:
    
    ========================== ============== =====================================
    Property                   Parameter      Current Value (but subject to change)
    -------------------------- -------------- -------------------------------------
    Speed of sound             iUTypeW        -9
    Viscosity                  iUTypeU        -10
    Thermal conductivity       iUTypeK        -11
    Surface tension            iUTypeN        -12
    Quality                    iUType0        -13
    Molar mass                 iUTypeM        -14
    Kinematic viscosity        iUTypeI        -17
    Mass flux                  iUTypeF        -27
    Heating value (volume)     iUTypeG        -37
    Dipole moment              iUTypeB        -38
    ========================== ============== =====================================
    
    The dimension statements for these variables are (in Fortran)::
    
        parameter (ncmax=20)                       !Maximum number of components in the mixture
        parameter (iPropMax=200)                   !Number of output properties available in ALLPROPS.
        character*255 hFld,hIn,hOut,hUnits,herr              !hFld, hIn, and hOut can actually be of any length.
        integer iUnits,iMass,iFlag,ierr,iUCode               !Note: as integer*4
        double precision a,b,q,Output(iPropMax),zm(ncmax),x(ncmax),y(ncmax),x3(ncmax)
    
    :p char hFld [in]: Fluid string.  See above 
    :p char hIn [in]: Input string of properties being sent to the routine. 
    :p char hOut [in]: Various flags are available to gain access to all other features of the Refprop program. 
    :p int iUnits [in]: The unit system to be used for the input and output properties (such as SI, English, etc.) See the details much further below for a complete description of the iUnits input value. **NOTE** A mass based value for iUnits does not imply that the input and output compositions are on a mass basis, this is specified with the iMass variable.
    :p int iMass [in]: Specifies if the input composition is mole or mass based
    :p int iFlag [in]: Flag to specify if the routine SATSPLN should be called (where a value of 1 activates the call).  (Eventually this variable may be used to send multiple flags combined in this flag.)
    :p double a [in]: First input property as specified in the hIn variable 
    :p double b [in]: Second input property as specified in the hIn variable 
    :p double z(20): XXXXXXXXXX
    :p double Output(200) [out]: Array of properties specified by the hOut string (array of size 200 dimensioned as double precision). The number -9999970 will be returned when errors occur, and the number -9999990 will be returned when nothing was calculated. Read the comments in the ALLPROPS routine to fully understand the contents of this array.
    :p char hUnits [out]: The units for the first property in the Output array.  Strings such as a fluid name may also be passed back in this position. To obtain the units for all of the properties sent to the string, call the ALLPROPS routine instead.
    :p int iUCode [out]: Unit code that represents the units of the first property in the Output array. See below for further details. 
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions of size 20) for two-phase states on a mole or mass basis depending on the value of iMass.
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions of size 20) for two-phase states on a mole or mass basis depending on the value of iMass.
    :p double x3(20) [out]: Reserved for returning the composition of a second liquid phase for LLE or VLLE. 
    :p double q [out]: Vapor quality on a mole or mass basis depending on the value of iMass.  (See subroutine ABFLSH for the definitions of values returned for this variable).  To obtain the molar quality regardless of iMass, send "qmole" as an input in hIn, and vice-versa for "qmass".
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255)   
    :p int hFld_length: length of variable ``hFld`` (default: 10000)
    :p int hIn_length: length of variable ``hIn`` (default: 255)
    :p int hOut_length: length of variable ``hOut`` (default: 255)
    :p int hUnits_length: length of variable ``hUnits`` (default: 255)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``imass`` flags

        :0: Input compositions given in mole fractions, quality on a molar basis.
        :1: Input compositions given in mass fractions, quality on a mass basis. For two-phase states, the values in x and y will be returned on a mass basis if iMass=1. **NOTE**  If the fluid string sent to this routine contains the word "mass" at the end (and thus contains the composition as well as the names of the fluids), this will have preference over the value of iMass when converting those compositions from a mass to a molar basis.  However, compositions sent back will still be based on the value in iMass.


.. f:subroutine:: RESIDUALdll (T, D, z, Pr, er, hr, sr, Cvr, Cpr, ar, gr, )

    
    Compute the residual quantities as a function of temperature,
    density, and composition (where the residual is the total property
    minus the ideal gas portion).
    
    This routine is the same as THERM2, except it only calculates the
    residual portions at any temperature and density.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double Pr [out]: Residual pressure [kPa]  (P-D*Rxgas*T) 
    :p double er [out]: Residual internal energy [J/mol] 
    :p double hr [out]: Residual enthalpy [J/mol] 
    :p double sr [out]: Residual entropy [J/mol-K] 
    :p double Cvr [out]: Residual isochoric heat capacity [J/mol-K] 
    :p double Cpr [out]: Residual isobaric heat capacity [J/mol-K] 
    :p double ar [out]: Residual Helmholtz energy [J/mol] 
    :p double gr [out]: Residual Gibbs free energy [J/mol] 



.. f:subroutine:: RIEMdll (T, D, z, riemc, )

    
    RIEM is the thermodynamic curvature in cubic nanometers/molecule.
    It has the magnitude of the correlation volume, is negative for attractive
    interactions, and positive for repulsive interactions, except when its
    magnitude gets smaller than the molecular volume.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double riemc [out]: RIEM [cubic nanometers/molecule] 



.. f:subroutine:: RMIX2dll (z, Rgas, )

    
    Mimic RMIX but return the gas constant as a parameter for use in the DLL.
    
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double Rgas: XXXXXXXXXX



.. f:subroutine:: SATDdll (D, z, kph, kr, T, P, Dl, Dv, x, y, ierr, herr, herr_length)

    
    Iterate for temperature and pressure given density along the
    saturation boundary (including the sublimation and melting
    lines) and the composition.
    
    Either (Dl,x) or (Dv,y) will correspond to the input state with
    the other pair corresponding to the other phase in equilibrium
    with the input state.
    
    The flag kph is for use only with water at densities near the
    triple point (between 0 and 4 C).
    
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p int kph [in]: Flag specifying desired root for multi-valued inputs (typically only water)
    :p int kr [out]: Phase flag
    :p double T [out]: Temperature [K] 
    :p double P [out]: Pressure [kPa] 
    :p double Dl [out]: Molar density of saturated liquid [mol/L] 
    :p double Dv [out]: Molar density of saturated vapor [mol/L] 
    :p double x(20) [out]: Liquid phase composition (array of mole fractions) 
    :p double y(20) [out]: Vapor phase composition  (array of mole fractions) 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``kph`` flags

        :0,1: Return upper root
        :-1: Return middle root
        :3: Return melting line

        ``kr`` flags

        :1: Input state is liquid in equilibrium with vapor.
        :2: Input state is vapor in equilibrium with liquid.
        :3: Input state is liquid in equilibrium with solid. (only for pure fluids)
        :4: Input state is vapor in equilibrium with solid.  (only for pure fluids)

        ``ierr`` flags

        :0: Successful
        :2: D>Dtrp of the liquid
        :3: D<Dtrp of the vapor
        :160: SATD did not converge (See subroutine LIMITX for other possible error numbers.)


.. f:subroutine:: SATESTdll (iFlash, T, P, z, x, y, ierr, herr, herr_length)

    
    Estimate temperature, pressure, and compositions to be used
    as initial guesses to SATTP.
    
    :p int iFlash [in]: Phase flag
    :p double T [out]: Temperature [K] (input or output) 
    :p double P [out]: Pressure [kPa] (input or output) 
    :p double z(20) [in]: Composition (array of mole fractions) The composition for the known x or y array should be sent in this z array, not in the output arrays shown below. 
    :p double x(20) [out]: Liquid phase composition (array of mole fractions) 
    :p double y(20) [out]: Vapor phase composition (array of mole fractions) 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``iflash`` flags

        :0: Flash calculation (T and P known)
        :1: T and x known, P and y returned
        :2: T and y known, P and x returned
        :3: P and x known, T and y returned
        :4: P and y known, T and x returned If this value is negative, the retrograde point will be returned.

        ``ierr`` flags

        :0: Successful
        :999: Unsuccessful


.. f:subroutine:: SATEdll (e, z, kph, nroot, k1, T1, P1, D1, k2, T2, P2, D2, ierr, herr, herr_length)

    
    Iterate for temperature, pressure, and density given energy along
    the saturation boundary and the composition.
    
    :p double e [in]: Molar energy [J/mol] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p int kph [in]: Flag specifying desired root
    :p int nroot: XXXXXXXXXX
    :p int k1: XXXXXXXXXX
    :p double T1: XXXXXXXXXX
    :p double P1: XXXXXXXXXX
    :p double D1: XXXXXXXXXX
    :p int k2: XXXXXXXXXX
    :p double T2: XXXXXXXXXX
    :p double P2: XXXXXXXXXX
    :p double D2: XXXXXXXXXX
    :p int ierr: XXXXXXXXXX
    :p char herr: XXXXXXXXXX
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``kph`` flags

        :0: Return all roots along the liquid-vapor line
        :1: Return only the liquid VLE root
        :2: Return only the vapor VLE roots
        :3: Return liquid SLE root (melting line)
        :4: Return vapor SVE root (sublimation line)


.. f:subroutine:: SATGUESSdll (kph, iprop, x, T, P, D, h, s, Dy, y, ierr, herr, herr_length)

    
    For a pure fluid, call the ancillary equations to obtain close
    estimates for the saturation boundaries.  The difference between
    these values and those from SATT, SATP, etc., depend on how well
    the ancillary equation was fitted, but generally they are within
    0.1%, except for the saturation densities within several degrees
    of the critical temperature.
    
    For a mixture, calculate approximate values from the spline curves for
    the saturation boundary.  Subroutine SATSPLN must be called in order
    for this to work.
    
    The input property should be placed in the corresponding variable
    for T, P, D, h, or s.  Inputs of h and s only work for mixtures
    when SATSPLN has been called.
    
    :p int kph [in]: Input phase; 1-liquid, 2-vapor When maximum in the property does not occur near the critical point, then kph=1 returns the root at the higher density and kph=2 returns the root at the lower density.
    :p int iprop [in]: Input property
    :p double x(20) [in]: Composition (array of mole fractions) 
    :p double T [out]: Temperature [K] 
    :p double P [out]: Pressure [kPa] 
    :p double D [out]: Density [mol/L] 
    :p double h [out]: Enthalpy or energy [J/mol] (not returned for a pure fluid) 
    :p double s [out]: Entropy [J/mol-K] (not returned for a pure fluid) 
    :p double Dy [out]: Equilibrium phase density [mol/L] 
    :p double y(20) [out]: Equilibrium phase composition (array of mole fractions) (h, s, and y are only returned when splines are used to calculate values.)
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``iprop`` flags

        :1: Temperature
        :2: Pressure
        :3: Density
        :4: Enthalpy
        :5: Entropy
        :6: Energy (currently only working for pure fluids)
        :11 to 15: 1st derivative of the property (for iprop-10) returned in Dy with respect to density (only for iFlag=0)
        :21 to 25: 2nd derivative of the property (for iprop-20) returned in Dy with respect to density (only for iFlag=0)
        :101: Check if the x array is identical to those sent to SATSPLN (only for iFlag=0) (for negative values of 1 to 5, find the location of zero slope of the property with respect to D) (only for iFlag=0)

        ``iflag`` flags

        :0: Use default and best methods, generally ancillary equations for pure fluids and splines (calculated from call to SATSPLN) for mixtures
        :11: Use Rackett technique to get density from T and P (value of kph and iprop ignored)
        :12: Use initial guess equations of Lemmon from xxx
        :13: xxx

        ``ierr`` flags

        :0: Successful
        :331: Splines not available for saturation calculations
        :332: Initialize variable d72l first before calling SATGUESS
        :-311: Compositions not identical to that used in the call to SATSPLN


.. f:subroutine:: SATGVdll (T, P, z, vf, b, ipv, ityp, isp, Dx, Dy, x, y, ierr, herr, herr_length)

    
    Calculates the bubble or dew point state with the entropy or density method
    of GV.  The calculation method is similar to the volume based algorithm of GERG.
    The cricondenbar and cricondentherm are estimated with the method in
    Michelsen, Saturation Point Calculations, Fluid Phase Equilibria, 23:181, 1985.
    
    Equations to be solved simultaneously are
    
    Pressure based:
    
    * f(1:n) - LOG(y/x)-LOG((fxi/nxi)/(fyi/nyi))=0
    * f(n+1) - SUM(y(i)-x(i))=0
    * f(n+2) - b/binput-1=0, where b = P, T, D, or s
    
    Volume based:
    
    * f(1:n) - LOG(y/x)-LOG((fxi/nxi)/(fyi/nyi))=0
    * f(n+1) - SUM(y(i)-x(i))=0
    * f(n+2) - py=px
    * f(n+3) - b/binput-1=0, where b = P, T, D, or s
    
    Variables:
    
    * 1 to nc - LOG(k(i))
    * nc+1    - LOG(T)
    * nc+2    - LOG(P) or LOG(Dx)
    * nc+3    -           LOG(Dy)
    
    :p double T [out]: Temperature [K] 
    :p double P [out]: Pressure [kPa] 
    :p double z(20) [in]: Overall composition (array of mole fractions) 
    :p double vf [in]: Vapor fraction (0>=vf>=1; the input value of density can be in either state and does not affect the outputs in Dx, Dy, x, and y)
    :p double b [out]: Input value, either entropy [J/mol-K] or density [mol/L] 
    :p int ipv [out]: Pressure or volume based algorithm
    :p int ityp [out]: Input values
    :p int isp [out]: Use values from Splines as initial guesses if set to 1  Outputs: (initial guesses must be sent in all variables (unless isp=1))
    :p double Dx [out]: Density of x phase [mol/L] 
    :p double Dy [out]: Density of y phase [mol/L] 
    :p double x(20) [out]: Composition of the x array (array of mole fractions) 
    :p double y(20) [out]: Composition of the y array (array of mole fractions) 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255)   
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``vf`` flags

        :vf=0,ityp=0,1: Dew phase inputs, state in equilibrium returned in Dy and y
        :vf=1,ityp=0,1: Liquid phase inputs, state in equilibrium returned in Dx and x
        :vf=0,ityp=6: Inputs are returned in Dx and the x array

        ``ipv`` flags

        :1: Pressure based
        :2: Volume based

        ``ityp`` flags

        :0: Given P, calculate T
        :1: Given T, calculate P
        :2: Cricondentherm condition, calculate T,P (ipv=1 only)
        :3: Cricondenbar condition, calculate T,P (ipv=1 only)
        :5: Given entropy, calculate T,P
        :6: Given density, calculate T,P

        ``ierr`` flags

        :0: Successful
        :2: Input D<=0
        :151: No convergence
        :172: vf<0 or vf>1
        :191: Derivatives are not available in PR or RDXHMX
        :321: Trivial solution
        :200: Density out of range (See subroutine LIMITX for other possible error numbers.)


.. f:subroutine:: SATHdll (h, z, kph, nroot, k1, T1, P1, D1, k2, T2, P2, D2, ierr, herr, herr_length)

    
    Iterate for temperature, pressure, and density given enthalpy along
    the saturation boundary and the composition.
    
    The second root is always set as the root in the vapor at temperatures
    below the maximum enthalpy on the vapor saturation line.  If kph is
    set to 2, and only one root is found in the vapor (this occurs when h<hcrit)
    the state point will be placed in k2,T2,P2,D2.  If kph=0 and this situation
    occurred, the first root (k1,T1,P1,d1) would be in the liquid (k1=1, k2=2).
    
    :p double h [in]: Molar enthalpy [J/mol] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p int kph [in]: Flag specifying desired root
    :p int nroot [out]: Number of roots.  Value is set to one for kph=1,3,4 if ierr=0 
    :p int k1 [out]: Phase of first root (1-liquid, 2-vapor, 3-melt, 4-subl) 
    :p double T1 [out]: Temperature of first root [K] 
    :p double P1 [out]: Pressure of first root [kPa] 
    :p double D1 [out]: Molar density of first root [mol/L] 
    :p int k2 [out]: Phase of second root (1-liquid, 2-vapor, 3-melt, 4-subl) 
    :p double T2 [out]: Temperature of second root [K] 
    :p double P2 [out]: Pressure of second root [kPa] 
    :p double D2 [out]: Molar density of second root [mol/L] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``kph`` flags

        :0: Return all roots along the liquid-vapor line
        :1: Return only liquid VLE root
        :2: Return only vapor VLE roots
        :3: Return liquid SLE root (melting line)
        :4: Return vapor SVE root (sublimation line) kph = 3,4 presently working only for pure components

        ``ierr`` flags

        :0: Successful
        :181: SATH did not converge for one of the roots
        :54: h < hmin
        :55: h > hmax
        :56: h > htrp (for sublimation inputs) (See subroutine LIMITX for other possible error numbers.)


.. f:subroutine:: SATESTdll (iFlash, T, P, z, x, y, ierr, herr, herr_length)

    
    Estimate temperature, pressure, and compositions to be used
    as initial guesses to SATTP.
    
    :p int iFlash [in]: Phase flag
    :p double T [out]: Temperature [K] (input or output) 
    :p double P [out]: Pressure [kPa] (input or output) 
    :p double z(20) [in]: Composition (array of mole fractions) The composition for the known x or y array should be sent in this z array, not in the output arrays shown below. 
    :p double x(20) [out]: Liquid phase composition (array of mole fractions) 
    :p double y(20) [out]: Vapor phase composition (array of mole fractions) 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``iflash`` flags

        :0: Flash calculation (T and P known)
        :1: T and x known, P and y returned
        :2: T and y known, P and x returned
        :3: P and x known, T and y returned
        :4: P and y known, T and x returned If this value is negative, the retrograde point will be returned.

        ``ierr`` flags

        :0: Successful
        :999: Unsuccessful


.. f:subroutine:: SATPdll (P, z, kph, T, Dl, Dv, x, y, ierr, herr, herr_length)

    
    Iterate for saturated liquid and vapor states given pressure
    and the composition of one phase.
    
    :p double P [in]: Pressure [kPa] If T is negative, all other variables are used as initial guesses at ABS(T).
    :p double z(20) [in]: Composition (array of mole fractions) (phase specified by kph) 
    :p int kph [in]: Phase flag
    :p double T [out]: Temperature [K] 
    :p double Dl [out]: Molar density of saturated liquid [mol/L] 
    :p double Dv [out]: Molar density of saturated vapor [mol/L] For a pseudo pure fluid, the density of the equilibrium phase is not returned.  Call SATP twice, once with kph=1 to get Tliq and Dl, and once with kph=2 to get Tvap and Dv.
    :p double x(20) [out]: Liquid phase composition (array of mole fractions) 
    :p double y(20) [out]: Vapor phase composition  (array of mole fractions) 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``kph`` flags

        :1: Input z is liquid composition (bubble point)
        :2: Input z is vapor composition (dew point)
        :3: Input z is liquid composition (freezing point)
        :4: Input z is vapor composition (sublimation point)

        ``ierr`` flags

        :0: Successful
        :141: P > Pcrit
        :144: Pure fluid iteration did not converge (See subroutine LIMITX for other possible error numbers.)


.. f:subroutine:: SATSPLNdll (z, ierr, herr, herr_length)

    
    Calculates the phase boundary of a mixture at a given composition,
    along with the critical point, cricondentherm, and cricondenbar.
    
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :355: Saturation routine failed


.. f:subroutine:: SATSdll (s, z, kph, nroot, k1, T1, P1, D1, k2, T2, P2, D2, k3, T3, P3, D3, ierr, herr, herr_length)

    
    Iterate for temperature, pressure, and density given entropy along
    the saturation boundary and the composition.
    
    The second root is always set as the root in the vapor at temperatures
    below the maximum entropy on the vapor saturation line.  If kph is
    set to 2, and only one root is found in the vapor (this occurs when s<scrit)
    the state point will be placed in k2,T2,P2,D2.  If kph=0 and this situation
    occurred, the first root (k1,T1,P1,D1) would be in the liquid (k1=1, k2=2).
    
    The third root is the root with the lowest temperature.  For fluids
    with multiple roots, when only one root is found in the vapor phase
    (this happens only at very low temperatures past the region where three
    roots are located), the value of the root is still placed in
    k3,T3,P3,D3.  For fluids that never have more than one root (when there
    is no maximum entropy along the saturated vapor line), the value of the
    root is always placed in k1,T1,P1,D1.
    
    :p double s [in]: Molar entropy [J/mol-K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p int kph [in]: Flag specifying desired root
    :p int nroot [out]: Number of roots.  Set to one for kph=1,3,4 if ierr=0 
    :p int k1 [out]: Phase of first root (1-liquid, 2-vapor, 3-melt, 4-subl) 
    :p double T1 [out]: Temperature of first root [K] 
    :p double P1 [out]: Pressure of first root [kPa] 
    :p double D1 [out]: Molar density of first root [mol/L] 
    :p int k2 [out]: Phase of second root (1-liquid, 2-vapor, 3-melt, 4-subl) 
    :p double T2 [out]: Temperature of second root [K] 
    :p double P2 [out]: Pressure of second root [kPa] 
    :p double D2 [out]: Molar density of second root [mol/L] 
    :p int k3 [out]: Phase of third root (1-liquid, 2-vapor, 3-melt, 4-subl) 
    :p double T3 [out]: Temperature of third root [K] 
    :p double P3 [out]: Pressure of third root [kPa] 
    :p double D3 [out]: Molar density of third root [mol/L] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``kph`` flags

        :0: Return all roots along the liquid-vapor line
        :1: Return only liquid VLE root
        :2: Return only vapor VLE roots
        :3: Return liquid SLE root (melting line)
        :4: Return vapor SVE root (sublimation line) kph = 3,4 presently working only for pure components

        ``ierr`` flags

        :0: Successful
        :192: SATS did not converge for one or more roots
        :66: s < smin
        :67: s > smax
        :68: s > strp (for sublimation inputs) (See subroutine LIMITX for other possible error numbers.)


.. f:subroutine:: SATESTdll (iFlash, T, P, z, x, y, ierr, herr, herr_length)

    
    Estimate temperature, pressure, and compositions to be used
    as initial guesses to SATTP.
    
    :p int iFlash [in]: Phase flag
    :p double T [out]: Temperature [K] (input or output) 
    :p double P [out]: Pressure [kPa] (input or output) 
    :p double z(20) [in]: Composition (array of mole fractions) The composition for the known x or y array should be sent in this z array, not in the output arrays shown below. 
    :p double x(20) [out]: Liquid phase composition (array of mole fractions) 
    :p double y(20) [out]: Vapor phase composition (array of mole fractions) 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``iflash`` flags

        :0: Flash calculation (T and P known)
        :1: T and x known, P and y returned
        :2: T and y known, P and x returned
        :3: P and x known, T and y returned
        :4: P and y known, T and x returned If this value is negative, the retrograde point will be returned.

        ``ierr`` flags

        :0: Successful
        :999: Unsuccessful


.. f:subroutine:: SATTPdll (T, P, z, iFlsh, iGuess, D, Dl, Dv, x, y, q, ierr, herr, herr_length)

    
    Calculate saturation properties for bubble, dew, or 2-phase states
    with the use of analytical derivatives of the Helmholtz energy with
    respect to composition.
    
    :p double T [in]: Temperature [K] (input or output) 
    :p double P [in]: Pressure [kPa] (input or output) 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p int iFlsh [in]: Phase flag
    :p int iGuess [in]: If set to 1, the parameters Dl, Dv, x, and y are used as initial guesses for the calculation. If Dl and Dv are set to zero when iGuess=1, then the densities are obtained from the first call to TPRHO. If Dl and Dv are not zero when iGuess=1, those values are used as initial values. If set to 2 and splines have been calculated, use inputs rather than spline values. 
    :p double D [out]: Overall density [mol/L] 
    :p double Dl [out]: Molar density of saturated liquid [mol/L] 
    :p double Dv [out]: Molar density of saturated vapor [mol/L] 
    :p double x(20) [out]: Liquid phase composition (array of mole fractions) 
    :p double y(20) [out]: Vapor phase composition  (array of mole fractions) 
    :p double q [out]: Quality 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``iflsh`` flags

        :0: Flash calculation (T and P known)
        :1: T and x known, P and y returned
        :2: T and y known, P and x returned
        :3: P and x known, T and y returned
        :4: P and y known, T and x returned If this value is negative, the retrograde point will be returned.

        ``ierr`` flags

        :0: Successful
        :121: T>Tmax (maxcondentherm)
        :141: P>Pmax (maxcondenbar)
        :151: Iteration failed
        :156: Probable Type III mixture with no liquid solution
        :159: Wrong input value for iFlsh (See subroutine LIMITX for other possible error numbers.)


.. f:subroutine:: SATTdll (T, z, kph, P, Dl, Dv, x, y, ierr, herr, herr_length)

    
    Iterate for saturated liquid and vapor states given temperature
    and the composition of one phase.
    
    :p double T [in]: Temperature [K] If T is negative, all other variables are used as initial guesses at ABS(T).
    :p double z(20) [in]: Composition (array of mole fractions) (phase specified by kph) 
    :p int kph [in]: Phase flag
    :p double P [out]: Pressure [kPa] 
    :p double Dl [out]: Molar density of saturated liquid [mol/L] 
    :p double Dv [out]: Molar density of saturated vapor [mol/L] For a pseudo pure fluid, the density of the equilibrium phase is not returned.  Call SATT twice, once with kph=1 to get Pliq and Dl, and once with kph=2 to get Pvap and Dv.
    :p double x(20) [out]: Liquid phase composition (array of mole fractions) 
    :p double y(20) [out]: Vapor phase composition  (array of mole fractions) 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``kph`` flags

        :1: Input z is liquid composition (bubble point)
        :-1: Force calculation in the liquid phase even if T<Ttrp
        :2: Input z is vapor composition (dew point)
        :-2: Force calculation in the vapor phase even if T<Ttrp
        :3: Input z is liquid composition along the freezing line (melting line)
        :4: Input z is vapor composition along the sublimation line

        ``ierr`` flags

        :0: Successful
        :121: T > Tcrit
        :124: Pure fluid iteration did not converge (See subroutine LIMITX for other possible error numbers.)


.. f:subroutine:: SETAGAdll (ierr, herr, herr_length)

    
    Set up working arrays for use with AGA8 equation of state.
    
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :108: Error (e.g. fluid not found)


.. f:subroutine:: SETFLUIDSdll (hFld, ierr, hFld_length)

    
    Call the SETUP routine without the need to pass ncomp, hrf, hFmix, or herr,
    or to declare the length of hfld as 255 or 10000 bytes long.  For a pure
    fluid, hfld simply contains the name of the fluid file (with a path if
    needed).  For a mixture, it contains the names of the constituents in the
    mixture separated by a ``|``, a semicolon, or an asterisk.  To load a
    predefined mixture, call the SETMIXTURE subroutine (which must return
    the composition array and thus cannot be included here).  If it is
    necessary to set the reference state, call SETUP instead.  If ierr
    comes back non-zero, call the ERRMSG routine to obtain it.
    
    Examples::
    
        call SETFLUIDS ('ARGON',ierr)    (load argon as a pure fluid)
        call SETFLUIDS ('FLUIDS/NITROGEN.FLD|FLUIDS/ARGON.FLD|FLUIDS/OXYGEN.FLD|',ierr)  (for the air mixture, but giving a path as well)
        call SETFLUIDS ('AIR.PPF',ierr)  (load the air mixture, but read from the pseudo-pure file; properties will be slightly different from the *.mix file since they are different models)
        call SETFLUIDS ('methane * ethane * propane * butane',ierr)
    
    :p char hFld [in]: String containing the fluid file names 
    :p int ierr [out]: Error flag
    :p int hFld_length: length of variable ``hFld`` (default: 10000)


    :Flags: 

        ``ierr`` flags

        :0: Successful (Values are identical to SETUP; a 109 is returned if the number of fluids in hfld is less than icomp.)


.. f:subroutine:: SETKTVdll (icomp, jcomp, hmodij, fij, hFmix, ierr, herr, hmodij_length, hFmix_length, herr_length)

    
    Set mixture model and/or parameters.
    
    This subroutine must be called after SETUP, but before any call to
    SETREF (for cases where energy, enthalpy, entropy, Gibbs energy, or
    the Helmholtz energy are required); it need not be called at all if
    the default mixture parameters (those read in by SETUP) are to be used.
    
    The component numbers icomp and jcomp must match the order that is found
    in the HMX.BNC file for each binary pair, or, in the case where
    no interaction parameters are available in the HMX.BNC file, icomp
    and jcomp must be in the same order as was used in the call to SETUP.
    If the numbers in these two integers are backwards, an error number
    and message will be returned, and nothing will be changed.  In this
    situation, switch the numbers and call this routine again.
    
    ========================   ==============================
    Kunz-Wagner model (KW0)    Lemmon-Jacobsen model (LJ6)
    ------------------------   ------------------------------
    fij(1) = betaT             fij(1) = zeta
    fij(2) = gammaT            fij(2) = xi
    fij(3) = betaV             fij(3) = Fij
    fij(4) = gammaV            fij(4) = beta
    fij(5) = Fij               fij(5) = gamma
    fij(6) = 'not used'        fij(6) = 'not used'
    ========================   ==============================
    
    :p int icomp [in]: Component i 
    :p int jcomp [in]: Component j 
    :p char hmodij [in]: Mixing rule for the binary pair i,j (e.g. LJ6, KW0, XR0, or LIN) (character*3) If hmodij is 'RST', reset all pairs to values from the original call to SETUP (all other inputs are ignored)
    :p double fij(6) [in]: Binary mixture parameters (array of dimension nmxpar; currently nmxpar is set to 6) The parameters will vary depending on hmodij (see above)
    :p char hFmix [in]: No longer used. Info from previous versions: File name (character*255) containing generalized parameters for the binary mixture model; this will usually be the same as the corresponding input to SETUP (e.g.,'HMX.BNC') 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int hmodij_length: length of variable ``hmodij`` (default: 3)
    :p int hFmix_length: length of variable ``hFmix`` (default: 255)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :111: Error in opening mixture file
        :603: Illegal i,j specification (i=j or i>nc or j>nc)
        :604: Order of fluids is backwards from that in HMX.BNC


.. f:subroutine:: SETMIXTUREdll (hMixNme, z, ierr, hMixNme_length)

    
    Call the SETMIX routine for a predefined mixture without the need to
    pass hFmix, hrf, ncc, hf, or herr.  It is not necessary to declare the
    length of hMixNme as 255 bytes long.  A path can be included if needed.
    The extension ".mix" is not required.  If it is necessary to set the
    reference state, call subroutine FLAGS first.  The composition of the
    mixture will be returned in the z array.  If ierr comes back non-zero,
    call the ERRMSG routine to obtain it.
    
    Examples::
    
        call SETMIXTURE ('AIR.MIX',z,ierr) ! load the air mixture from the AIR.MIX file
        call SETMIXTURE ('C:/REFPROP/MIXTURES/AIR.MIX',z,ierr)    read the AIR.MIX file from the C:/REFPROP/MIXTURES directory
        call SETMIXTURE ('R410A.MIX',z,ierr) ! load the R410A mixture, the composition will be returned on a mole percent basis in the z array.
        call SETMIXTURE ('R410A',z,ierr)  ! works the same as above for predefined refrigerant mixtures that start with R4 or R5.
    
    :p char hMixNme [in]: String of any character length containing the mixture file name 
    :p double z(20) [out]: Composition array (mole fractions) 
    :p int ierr [out]: Error flag
    :p int hMixNme_length: length of variable ``hMixNme`` (default: 10000)


    :Flags: 

        ``ierr`` flags

        :0: Successful (Values are identical to SETMIX)


.. f:subroutine:: SETMIXdll (hMixNme, hFmix, hrf, ncc, hFiles, z, ierr, herr, hMixNme_length, hFmix_length, hrf_length, hFiles_length, herr_length)

    
    Open a mixture file (e.g., R410A.mix) and read constituents and
    mole fractions.
    
    :p char hMixNme [in]: Mixture file name (character*255) 
    :p char hFmix [in]: File containing mixture coefficients (character*255) 
    :p char hrf [in]: Reference state (character*3); See subroutine SETUP for specifics. 
    :p int ncc [out]: Number of fluids in mixture 
    :p char hFiles [out]: Array of file names specifying mixture components that were used to call setup (character*255)
    :p double z(20) [out]: Array of mole fractions for the specified mixture 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int hMixNme_length: length of variable ``hMixNme`` (default: 255)
    :p int hFmix_length: length of variable ``hFmix`` (default: 255)
    :p int hrf_length: length of variable ``hrf`` (default: 3)
    :p int hFiles_length: length of variable ``hFiles`` (default: 10000)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :101: Error in opening file
        :-102: Mixture file contains mixing parameters
        :805: Sum of compositions not equal to one


.. f:subroutine:: SETMODdll (ncomp, htype, hmix, hcomp, ierr, herr, htype_length, hmix_length, hcomp_length, herr_length)

    
    Set model(s) other than the NIST-recommended ('NBS') ones.
    
    This subroutine must be called before SETUP; it need not be called
    at all if the default (NIST-recommended) models are desired.
    
    :p int ncomp [in]: Number of components (1 for pure fluid) (integer) 
    :p char htype [in]: Flag indicating which model to set (character*3)
    :p char hmix [in]: Mixture model for the property specified in htype (character*3) (ignored if number of components = 1)
    :p char hcomp [in]: Component model(s) for property specified in htype [array (1..ncomp) of character*3]
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int htype_length: length of variable ``htype`` (default: 3)
    :p int hmix_length: length of variable ``hmix`` (default: 3)
    :p int hcomp_length: length of variable ``hcomp`` (default: 60)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``htype`` flags

        :'EOS': Equation of state
        :'ETA': Viscosity
        :'TCX': Thermal conductivity
        :'STN': Surface tension
        :'NBS': Reset all of the above model types to 'NBS' (values of hmix and hcomp are ignored)

        ``hmix`` flags

        :'NBS': Use NIST recommendation for specified fluid/mixture
        :'HMX': Mixture Helmholtz model for thermodynamic properties
        :'ECS': Extended corresponding states for viscosity or therm. cond.
        :'STX': Surface tension mixture model

        ``hcomp`` flags

        :'NBS': NIST recommendation for specified fluid/mixture
        :'FEQ': Helmholtz energy model
        :'BWR': Pure fluid modified Benedict-Webb-Rubin (MBWR)
        :'ECS': Extended corresponding states (all fluids)
        :'VS1': The 'composite' model for R134a, R152a, NH3, etc.
        :'VS2': Younglove-Ely model for hydrocarbons
        :'VS4': Generalized friction theory of Quinones-Cisneros and Deiters
        :'VS5': Chung et al. (1988) predictive model
        :'VS6': Vesovic form of VS1 model
        :'VS7': Polynomial/exponential model
        :'TC1': The 'composite' model for R134a, R152a, etc.
        :'TC2': Younglove-Ely model for hydrocarbons
        :'TC5': Chung et al. (1988) predictive model
        :'ST1': Surface tension as f(tau); tau = 1 - T/Tc

        ``ierr`` flags

        :0: Successful
        :113: ncomp outside of bounds


.. f:subroutine:: SETNCdll (ncomp, )

    
    Allow the user to modify the value of nc (the number of components in
    a mixture) so that a subset of the loaded mixtures can be used.
    For example, a 4 component mixture could be set up, but nc could
    be set to 3 to calculate properties of the mixture of the first three
    components.  The last component can then be used as a pure fluid.
    For example, SETUP could be called to load four fluids, R32.fld,
    R125.fld, R134a.fld, and R407C.ppf, followed by a call to SETNC(3)
    so that the 4th component is not used in mixture calculations.
    The pseudo-pure fluid equation in R407C.ppf can be accessed by calling
    PUREFLD(4) to get single-phase thermodynamic properties, and VLE
    states or transport properties that require the first three components
    can be obtained by calling PUREFLD(0) and setting the composition
    array z with the appropriate values.
    
    :p int ncomp [in]: number of components in the mixture 



.. f:subroutine:: SETPATHdll (hpth, hpth_length)

    
    Set the path where the fluid files are located.
    
    :p char hpth [in]: Location of the fluid files (character*255) The path does not need to contain the ending "/" and it can point directly to the location where the DLL is stored if a fluids subdirectory (with the corresponding fluid files) is located there, for example, hpth='C:/Program Files (x86)/REFPROP' 
    :p int hpth_length: length of variable ``hpth`` (default: 255)



.. f:subroutine:: SETREFDIRdll (hpth, hpth_length)

    
    Set a path to the location of original fluid files so that a user
    can specify where their fluid file is located, but the reference
    files needed for transport properties, etc., such as nitrogen.fld,
    can be found.
    
    :p char hpth [in]: Location of the fluid files (character*255) The path does not need to contain the ending "\". For example:  hpth='C:\Program Files\Refprop\fluids' 
    :p int hpth_length: length of variable ``hpth`` (default: 255)



.. f:subroutine:: SETREFdll (hrf, ixflag, x0, h0, s0, T0, P0, ierr, herr, hrf_length, herr_length)

    
    Set reference state enthalpy and entropy.
    
    This subroutine must be called after SETUP; it need not be called at all
    if the reference state specified in the call to SETUP is to be used.
    
    :p char hrf [in]: Reference state for thermodynamic calculations (character*3)
    :p int ixflag [in]: Composition flag
    :p double x0(20) [in]: Composition for which h0 and s0 apply; array(1:nc) (array of mole fractions) This is useful for mixtures of a predefined composition, e.g., refrigerant blends such as R410A. Only has meaning if ixflag = 2
    :p double h0 [in]: Reference state enthalpy at T0, P0, and x0 [J/mol] (only has meaning if hrf = 'OTH' or 'OT0') 
    :p double s0 [in]: Reference state entropy at T0, P0, and x0 [J/mol-K] (only has meaning if hrf = 'OTH' or 'OT0') 
    :p double T0 [in]: Reference state temperature [K] (only has meaning if hrf = 'OTH' or 'OT0') T0 = -1 indicates saturated liquid at normal boiling point (bubble point for a mixture)
    :p double P0 [in]: Reference state pressure [kPa] (only has meaning if hrf = 'OTH' or 'OT0') P0 = -1 indicates saturated liquid at T0 (and x0) P0 = -2 indicates saturated vapor at T0 (and x0) 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int hrf_length: length of variable ``hrf`` (default: 3)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``hrf`` flags

        :'NBP': h,s = 0 at normal boiling point(s)
        :'ASH': h,s = 0 for saturated liquid at -40 C (ASHRAE convention)
        :'IIR': h = 200 kJ/kg, s = 1 kJ/kg-K for sat. liquid at 0 C (IIR convention)
        :'DEF': Default reference state as specified in fluid file
        :'OTH': Other, as specified by h0, s0, T0, P0 (real gas state)
        :'OT0': Other, as specified by h0, s0, T0, P0 (ideal-gas state)
        :'NA': Not applicable, do not set up the reference state. The values of e, h, and s will have a random reference state. Do not use except for EOS testing.
        :'???': Set hrf to the value of the current reference state and exit

        ``ixflag`` flags

        :1: Reference state applied to pure components
        :2: Reference state applied to mixture x0

        ``ierr`` flags

        :0: Successful
        :22: Tmin > Tref for IIR reference state
        :23: Tcrit < Tref for IIR reference state
        :24: Tmin > Tref for ASHRAE reference state
        :25: Tcrit < Tref for ASHRAE reference state
        :26: Tmin > Tnbp for NBP reference state
        :-28: Can't apply 'DEF' to mixture; will apply to pure components
        :-29: Unknown reference state specified; will use 'DEF'
        :119: Convergence failure in calculating reference state


.. f:subroutine:: SETUPdll (ncomp, hFiles, hFmix, hrf, ierr, herr, hFiles_length, hFmix_length, hrf_length, herr_length)

    
    Define models and initialize arrays.
    
    :p int ncomp [in]: Number of components (1 for pure fluid) (integer) If called with ncomp=-1, the version number*10000 will be returned in ierr.
    :p char hFiles [in]: Array of file names specifying the fluid or the mixture components (character*255); e.g., 'fluids\r134a.fld' (DOS) ':fluids:r134a.fld' (Mac) '[full_path]/fluids/r134a.fld' (UNIX)
    :p char hFmix [in]: Name of file containing mixture coefficients (character*255); e.g., 'fluids\HMX.BNC'
    :p char hrf [in]: Reference state for thermodynamic calculations (character*3). Other choices are possible, see SETREF
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int hFiles_length: length of variable ``hFiles`` (default: 10000)
    :p int hFmix_length: length of variable ``hFmix`` (default: 255)
    :p int hrf_length: length of variable ``hrf`` (default: 3)
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``hrf`` flags

        :'DEF': default reference state as specified in fluid file
        :'NBP': h,s = 0 at pure component normal boiling point
        :'ASH': h,s = 0 for sat. liquid at -40 C (ASHRAE convention)
        :'IIR': h = 200 kJ/kg and s = 1 kJ/kg-K for sat. liquid at 0 C (IIR convention)

        ``ierr`` flags

        :0: Successful
        :101: Error in opening file
        :102: Error in file or premature end of file
        :-107: Unknown model encountered in file
        :105: Specified model not found
        :-105: Must use routine SETREF for (OTH) reference state choice
        :111: Error in opening mixture file
        :112: Mixture file of wrong type
        :114: nc not equal to the nc sent to SETMOD
        :-117: Binary pair not found, all parameters will be estimated
        :117: Mixture parameters not available, mixture is outside the range of the model and calculations will not be made


.. f:subroutine:: SPLNROOTdll (isp, iderv, f, a, ierr, herr, herr_length)

    
    Calculates the root of a given value of a spline function
    
    :p int isp [in]: Indicator for which spline to use 1 to nc - Composition nc+1 - Temperature nc+2 - Pressure nc+3 - Density nc+4 - Enthalpy or Energy (depending on the value of ieflag). nc+5 - Entropy
    :p int iderv [in]: Values of -1 and -2 return lower and upper root values, a value of 0 returns the spline root, a value of 1 returns the root where the derivative of the spline with respect to D is equal to the the value of f (set f=0 to find maximum or minimum).
    :p double f [in]: Value of spline function 
    :p double a [out]: Root value (initial value required since some splines can be doubled valued) 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :151: Routine did not converge.'


.. f:subroutine:: SPLNVALdll (isp, iderv, a, f, ierr, herr, herr_length)

    
    Calculates the value of a spline or the derivative of the spline
    at the specified value.
    
    :p int isp [in]: Indicator for which spline to use
    :p int iderv [in]: Values of -1 and -2 return lowest and highest density values of the splines, a value of 0 returns spline function value, a value of 1 returns the derivative of the spline with respect to the input value, and a value of 2 returns the 2nd derivative.
    :p double a [in]: Input value (molar density of the known phase) 
    :p double f [out]: Desired output value 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``isp`` flags

        :0: Molar density of the known phase
        :1 to nc: Composition of the incipient phase
        :nc+1: Temperature
        :nc+2: Pressure
        :nc+3: Molar density of the equilibrium phase
        :nc+4: Enthalpy
        :nc+5: Entropy


.. f:subroutine:: SUBLPdll (P, z, T, ierr, herr, herr_length)

    
    Compute the sublimation line temperature as a function of pressure
    and composition.
    
    :p double P [in]: Sublimation line pressure [kPa] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double T [out]: Temperature [K] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :-4: Pressure above triple point pressure
        :501: No equation available


.. f:subroutine:: SUBLTdll (T, z, P, ierr, herr, herr_length)

    
    Compute the sublimation line pressure as a function of temperature
    and composition.
    
    :p double T [in]: Temperature [K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double P [out]: Sublimation line pressure [kPa] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :501: No equation available


.. f:subroutine:: SURFTdll (T, Dl, z, sigma, ierr, herr, herr_length)

    
    Compute surface tension as a function of T.  SATT is called to obtain
    the liquid density.  If this is already known then your calling
    routines should use subroutine STN to greatly reduce the time
    needed in the calculation of the surface tension.
    
    :p double T [in]: Temperature [K] 
    :p double Dl [out]: Molar density of liquid phase [mol/L] (only returned for mixtures) 
    :p double z(20) [in]: Composition of liquid phase (array of mole fractions) 
    :p double sigma [out]: Surface tension [N/m] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful Other error messages returned from SATT or STN


.. f:subroutine:: SURTENdll (T, Dl, Dv, x, y, sigma, ierr, herr, herr_length)

    
    Compute surface tension as a function of T.  The routine assumes that
    SATT has already been called and the saturation densities are known.
    If this is not the case, then call SURFT instead.
    
    With version 10 of Refprop, this routine is not necessary anymore,
    and STN can be called instead if desired.  The only difference is
    that this routines checks to see if the densities are not zero,
    and calls SATT if so.
    
    (See subroutine STN for the description of all variables.)
    
    :p double T: XXXXXXXXXX
    :p double Dl: XXXXXXXXXX
    :p double Dv: XXXXXXXXXX
    :p double x(20): XXXXXXXXXX
    :p double y(20): XXXXXXXXXX
    :p double sigma: XXXXXXXXXX
    :p int ierr: XXXXXXXXXX
    :p char herr: XXXXXXXXXX
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: TDFLSHdll (T, D, z, P, Dl, Dv, x, y, q, e, h, s, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given temperature, bulk density, and bulk composition.
    This routine accepts both single-phase and two-phase states as inputs;
    for single-phase calculations, the subroutine THERM is much faster.
    (See subroutines ABFLSH or TPDFLSH for the description of all variables.)
    
    :p double T [in]: Temperature [K]
    :p double D [in]: Density [mol/K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double P [out]: Pressure [kPa]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double e [out]: Internal energy [J/mol]
    :p double h [out]: Enthalpy [J/mol]
    :p double s [out]: Entropy [J/mol-K]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: TEFL1dll (T, e, z, Dmin, Dmax, D, ierr, herr, herr_length)

    
    Iterate for single-phase density as a function of temperature,
    energy, and composition.
    (See subroutine ABFL1 for the description of all variables.)
    
    :p double T [in]: Temperature [K]
    :p double e [in]: Internal energy [J/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double Dmin [in]: Lower bound on density [mol/L]
    :p double Dmax [in]: Upper bound on density [mol/L]
    :p double D [out]: Density [mol/K]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: TEFLSHdll (T, e, z, kr, P, D, Dl, Dv, x, y, q, h, s, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given temperature, bulk energy, and bulk composition.
    (See subroutines ABFLSH or TBFLSH for the description of all variables.)
    
    :p double T [in]: Temperature [K]
    :p double e [in]: Internal energy [J/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p int kr: XXXXXXXXXX
    :p double P [out]: Pressure [kPa]
    :p double D [out]: Density [mol/K]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double h [out]: Enthalpy [J/mol]
    :p double s [out]: Entropy [J/mol-K]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: THERM0dll (T, D, z, P0, e0, h0, s0, Cv0, Cp00, w0, a0, g0, )

    
    Compute ideal-gas thermal quantities as a function of temperature,
    density, and composition from core functions.
    
    This routine is the same as THERM, except it only calculates ideal
    gas properties (Z=1) at any temperature and density.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double P0 [out]: Pressure [kPa] 
    :p double e0 [out]: Internal energy [J/mol] 
    :p double h0 [out]: Enthalpy [J/mol] 
    :p double s0 [out]: Entropy [J/mol-K] 
    :p double Cv0 [out]: Isochoric heat capacity [J/mol-K] 
    :p double Cp00 [out]: Isobaric heat capacity [J/mol-K] 
    :p double w0 [out]: Speed of sound [m/s] 
    :p double a0 [out]: Helmholtz energy [J/mol] 
    :p double g0 [out]: Gibbs free energy [J/mol] 



.. f:subroutine:: THERM2dll (T, D, z, P, e, h, s, Cv, Cp, w, zz, hjt, a, g, xkappa, beta, dPdD, d2PdD2, dPdT, dDdT, dDdP, d2PdT2, d2PdTD, spare3, spare4, )

    
    Compute thermal quantities as a function of temperature, density,
    and composition.  This routine is the simply the combination of
    several others.  See warning in subroutines THERM or ALLPROPS.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double P: XXXXXXXXXX
    :p double e: XXXXXXXXXX
    :p double h: XXXXXXXXXX
    :p double s: XXXXXXXXXX
    :p double Cv: XXXXXXXXXX
    :p double Cp: XXXXXXXXXX
    :p double w: XXXXXXXXXX
    :p double zz [out]: Compressibility factor (= PV/RT) [-] (See subroutines THERM, THERM3, AG, and DERVPVT for the description of all variables.) 
    :p double hjt: XXXXXXXXXX
    :p double a [out]: Helmholtz energy [J/mol] 
    :p double g [out]: Gibbs free energy [J/mol] 
    :p double xkappa: XXXXXXXXXX
    :p double beta: XXXXXXXXXX
    :p double dPdD: XXXXXXXXXX
    :p double d2PdD2: XXXXXXXXXX
    :p double dPdT: XXXXXXXXXX
    :p double dDdT: XXXXXXXXXX
    :p double dDdP: XXXXXXXXXX
    :p double d2PdT2: XXXXXXXXXX
    :p double d2PdTD: XXXXXXXXXX
    :p double spare3: XXXXXXXXXX
    :p double spare4: XXXXXXXXXX



.. f:subroutine:: THERM3dll (T, D, z, xkappa, beta, xisenk, xkt, betas, bs, xkkt, thrott, pi, spht, )

    
    Compute miscellaneous thermodynamic properties.
    See warning in subroutines THERM or ALLPROPS.
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double xkappa [out]: Isothermal compressibility [1/kPa] 
    :p double beta [out]: Volume expansivity [1/K] 
    :p double xisenk [out]: Isentropic expansion coefficient [-] 
    :p double xkt [out]: Isothermal expansion coefficient [-] 
    :p double betas [out]: Adiabatic compressibility [1/kPa] 
    :p double bs [out]: Adiabatic bulk modulus [kPa] 
    :p double xkkt [out]: Isothermal bulk modulus [kPa] 
    :p double thrott [out]: Isothermal throttling coefficient [L/mol] 
    :p double pi [out]: Internal pressure [kPa] 
    :p double spht [out]: Specific heat input [J/mol] 



.. f:subroutine:: THERMdll (T, D, z, P, e, h, s, Cv, Cp, w, hjt, )

    
    Compute thermal quantities as a function of temperature, density,
    and composition from core functions (Helmholtz energy, ideal
    gas heat capacity, and various derivatives and integrals).
    
    .. warning::
    
        Do NOT call this routine for two-phase states,
        otherwise it will return a metastable state if near the phase
        boundary or complete nonsense at other conditions.  The value of q
        that is returned from the flash routines will indicate a two phase
        state by returning a value between 0 and 1.  In such a situation,
        properties can only be calculated for the saturated liquid
        and vapor states.  For example, when calling PHFLSH::
    
            call PHFLSH (P,h,z,T,D,Dl,Dv,x,y,q,e,s,Cv,Cp,w,ierr,herr)
    
        If q>0 and q<1, then values of the liquid compositions will
        be returned in the x and y arrays, and the properties of the
        liquid and vapor states can be calculated, for example, as::
    
            call ENTRO (T,Dl,x,sliq)
            call ENTRO (T,Dv,x,svap)
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double P [out]: Pressure [kPa] 
    :p double e [out]: Internal energy [J/mol] 
    :p double h [out]: Enthalpy [J/mol] 
    :p double s [out]: Entropy [J/mol-K] 
    :p double Cv [out]: Isochoric heat capacity [J/mol-K] 
    :p double Cp [out]: Isobaric heat capacity [J/mol-K] 
    :p double w [out]: Speed of sound [m/s] 
    :p double hjt [out]: Isenthalpic Joule-Thomson coefficient [K/kPa] 



.. f:subroutine:: THFL1dll (T, h, z, Dmin, Dmax, D, ierr, herr, herr_length)

    
    Iterate for single-phase density as a function of temperature,
    enthalpy, and composition.
    (See subroutine ABFL1 for the description of all variables.)
    
    :p double T [in]: Temperature [K]
    :p double h [in]: Enthalpy [J/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double Dmin [in]: Lower bound on density [mol/L]
    :p double Dmax [in]: Upper bound on density [mol/L]
    :p double D [out]: Density [mol/K]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: THFLSHdll (T, h, z, kr, P, D, Dl, Dv, x, y, q, e, s, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given temperature, bulk enthalpy, and bulk composition.
    Often in the liquid, two solutions exist, one of them in the two phase.
    If this is the case, call THFLSH with kr=2 to get the single-phase state.
    (See subroutines ABFLSH or TBFLSH for the description of all variables.)
    
    :p double T [in]: Temperature [K]
    :p double h [in]: Enthalpy [J/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p int kr: XXXXXXXXXX
    :p double P [out]: Pressure [kPa]
    :p double D [out]: Density [mol/K]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double e [out]: Internal energy [J/mol]
    :p double s [out]: Entropy [J/mol-K]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: TPFL2dll (T, P, z, Dl, Dv, x, y, q, ierr, herr, herr_length)

    
    Flash calculation given temperature, pressure, and bulk composition.
    This routine accepts only two-phase states as inputs; if the phase is
    not known use TPFLSH.  Use TPRHO for single-phase states.
    
    :p double T [in]: Temperature [K] 
    :p double P [in]: Pressure [kPa] 
    :p double z(20) [in]: Overall composition (array of mole fractions) 
    :p double Dl [out]: Molar density of the liquid phase [mol/L] 
    :p double Dv [out]: Molar density of the vapor phase [mol/L] 
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions) 
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions) 
    :p double q [out]: Vapor quality on a MOLAR basis (moles vapor/total moles) 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :213: TPRHO did not converge
        :226: Iteration did not converge


.. f:subroutine:: TPFLSHdll (T, P, z, D, Dl, Dv, x, y, q, e, h, s, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given temperature, pressure, and bulk composition.
    This routine accepts both single-phase and two-phase states as inputs;
    for single-phase calculations, the subroutine TPRHO is much faster.
    
    :p double T [in]: Temperature [K] 
    :p double P [in]: Pressure [kPa] 
    :p double z(20) [in]: Overall composition (array of mole fractions) 
    :p double D [out]: Density [mol/L] 
    :p double Dl [out]: Molar density of the liquid phase [mol/L] 
    :p double Dv [out]: Molar density of the vapor phase [mol/L] 
    :p double x(20) [out]: Composition of the liquid phase (array of mole or mass fractions) 
    :p double y(20) [out]: Composition of the vapor phase (array of mole or mass fractions) 
    :p double q [out]: Vapor quality [mol/mol]
    :p double e [out]: Internal energy [J/mol]
    :p double h [out]: Enthalpy [J/mol]
    :p double s [out]: Entropy [J/mol-K]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) (See subroutine ABFLSH for the description of all other output variables.) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :213: Density calculation did not converge
        :215: Supercritical density calculation did not converge
        :223: Bubble point did not converge
        :224: Dew point did not converge


.. f:subroutine:: TPRHOPRdll (T, P, z, D1, D2, )

    
    Compute density with a volume-translated modification of the
    Peng-Robinson equation of state::
    
        P=RT/(v+c+b)-a/((v+c)*(v+c+b)+b(v+c+b))
    
    c is a translation constant, as given in Peneloux and Rauzy,
    Fluid Phase Equilib. 8:7-23, 1982.
    
    :p double T [in]: Temperature [K] 
    :p double P [in]: Pressure [kPa] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double D1 [out]: Largest density root [mol/L] 
    :p double D2 [out]: Smallest density root [mol/L] 



.. f:subroutine:: TPRHOdll (T, P, z, kph, kguess, D, ierr, herr, herr_length)

    
    Iterate for density as a function of temperature, pressure, and
    composition of a specified phase.
    
    .. warning:
    
        Invalid densities will be returned for T and P outside the range of
        validity, e.g., P>Pmelt, P<Psat for kph=1, etc.
    
    :p double T [in]: Temperature [K] 
    :p double P [in]: Pressure [kPa] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p int kph [in]: Phase flag
    :p int kguess [in]: Guess flag
    :p double D [out]: Molar density [mol/L] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``kph`` flags

        :1: Liquid phase
        :2: Vapor phase
        :0: Stable phase - NOT ALLOWED (use TPFLSH) (Unless an initial guess is supplied for D)
        :-1: Force the search in the liquid phase (for metastable points)
        :-2: Force the search in the vapor phase (for metastable points)

        ``kguess`` flags

        :0: No first guess for D provided
        :1: First guess for D provided

        ``ierr`` flags

        :0: Successful
        :201: Illegal input (kph <= 0)
        :202: Liquid-phase iteration did not converge
        :203: Vapor-phase iteration did not converge


.. f:subroutine:: TQFLSHdll (T, q, z, kq, P, D, Dl, Dv, x, y, e, h, s, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given temperature, quality, and bulk composition.
    This routine accepts saturation or two-phase states as inputs.
    (See subroutines ABFLSH or AQFLSH for the description of all variables.)
    
    :p double T [in]: Temperature [K]
    :p double q [in]: Vapor quality [mol/mol]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p int kq: XXXXXXXXXX
    :p double P [out]: Pressure [kPa]
    :p double D [out]: Density [mol/K]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double e [out]: Internal energy [J/mol]
    :p double h [out]: Enthalpy [J/mol]
    :p double s [out]: Entropy [J/mol-K]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: TRNPRPdll (T, D, z, eta, tcx, ierr, herr, herr_length)

    
    Compute the transport properties thermal conductivity and
    viscosity as functions of temperature, density, and composition.
    
    .. warning::
    
        Do NOT call this routine for two-phase states,
        otherwise it will return a metastable state if near the phase boundary
        or complete nonsense at other conditions.  The value of q that is
        returned from the flash routines will indicate a two phase state
        by returning a value between 0 and 1.  In such a situation, the
        transport properties can only be calculated for the saturated liquid
        and vapor states.  For example, when calling PHFLSH::
    
            call PHFLSH (P,h,z,T,D,Dl,Dv,x,y,q,e,s,Cv,Cp,w,ierr,herr)
    
        If q>0 and q<1, then values of the liquid compositions will be returned
        in the x and y arrays, and the transport properties of the liquid and
        vapor states can be calculated as follows::
    
            call TRNPRP (T,Dl,x,etaliq,tcxliq,ierr,herr)
            call TRNPRP (T,Dv,y,etavap,tcxvap,ierr,herr)
    
    :p double T [in]: Temperature [K] 
    :p double D [in]: Molar density [mol/L] 
    :p double z(20) [in]: Composition array (array of mole fractions) 
    :p double eta [out]: Viscosity [uPa-s] 
    :p double tcx [out]: Thermal conductivity [W/m-K] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :502: Unknown viscosity or thermal conductivity model specified
        :73: One or more inputs are out of bounds for the ECS model
        :74: Inputs to the vis. and th. cond. correlations are out 2of range
        :540: Transport equations are not available for one or more of the fluids
        :541: Transport equations are not available for mixtures with water at molar concentrations greater than 5%
        :542: Transport equations are not available for mixtures with alcohols
        :543: Transport equations are not available for the ammonia/water mixture
        :-508: Invalid region for viscosity of reference fluid 1
        :-558: 2-D Newton-Raphson method for conformal temperature and density did not converge
        :-560: Pure fluid is exactly at the critical point; thermal conductivity is infinite
        :561: Pure fluid correlation produced an erroneous value for either viscosity or thermal conductivity
        :5##: Pure fluid correlation out of range; attempted to use ECS method


.. f:subroutine:: TSATDdll (D, z, T, ierr, herr, herr_length)

    
    Compute the saturated temperature as a function of saturated density
    and composition.
    
    :p double D [in]: Saturated density [mol/L] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double T [out]: Temperature [K] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :2: Density greater than triple point density
        :501: No equation available


.. f:subroutine:: TSATPdll (P, z, T, ierr, herr, herr_length)

    
    Compute the vapor temperature as a function of pressure
    and composition.
    
    If the input pressure is negative, compute the liquid temperature as a
    function of liquid pressure and composition (used only for
    pseudo-pure fluids).
    
    :p double P [in]: Vapor pressure [kPa] If negative, liquid pressure [kPa] (the negative sign is only used as a flag).
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double T [out]: Temperature [K] ierr, herr; See error codes in the ANCERR2 routine. 
    :p int ierr: XXXXXXXXXX
    :p char herr: XXXXXXXXXX
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: TSFL1dll (T, s, z, Dmin, Dmax, D, ierr, herr, herr_length)

    
    Iterate for single-phase density as a function of temperature,
    entropy, and composition.
    (See subroutine ABFL1 for the description of all variables.)
    
    :p double T [in]: Temperature [K]
    :p double s [in]: Entropy [J/mol-K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p double Dmin [in]: Lower bound on density [mol/L]
    :p double Dmax [in]: Upper bound on density [mol/L]
    :p double D [out]: Density [mol/K]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: TSFLSHdll (T, s, z, kr, P, D, Dl, Dv, x, y, q, e, h, Cv, Cp, w, ierr, herr, herr_length)

    
    Flash calculation given temperature, bulk entropy, and bulk composition.
    (See subroutines ABFLSH or TBFLSH for the description of all variables.)
    
    :p double T [in]: Temperature [K]
    :p double s [in]: Entropy [J/mol-K]
    :p double z(20) [in]: Bulk Composition (array of mole fractions)
    :p int kr: XXXXXXXXXX
    :p double P [out]: Pressure [kPa]
    :p double D [out]: Density [mol/K]
    :p double Dl [out]: Molar density of the liquid phase [mol/L]
    :p double Dv [out]: Molar density of the vapor phase [mol/L]
    :p double x(20) [out]: Composition of the liquid phase (array of mole fractions)
    :p double y(20) [out]: Composition of the vapor phase (array of mole fractions)
    :p double q [out]: Vapor quality [mol/mol]
    :p double e [out]: Internal energy [J/mol]
    :p double h [out]: Enthalpy [J/mol]
    :p double Cv [out]: Isochoric heat capacity [J/mol-K]
    :p double Cp [out]: Isobaric heat capacity [J/mol-K]
    :p double w [out]: Speed of sound [m/s]
    :p int ierr [out]: Error code (no error if ierr==0)
    :p char herr [out]: Error string (character*255)
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: UNSETAGAdll (, )

    
    Load original values into arrays changed in the call to SETAGA.  This
    routine resets the values back to those loaded when SETUP was called.
    



.. f:subroutine:: VAPSPNDLdll (T, z, D, ierr, herr, herr_length)

    
    Find the vapor spinodal density for a given temperature.  If no
    spinodal exists, return the point of zero curvature.  This only
    happens with a few of the older equations, these being D5, methanol,
    and nitrogen.
    
    :p double T [in]: Temperature [K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double D [out]: Density at vapor spinodal [mol/L] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)


    :Flags: 

        ``ierr`` flags

        :0: Successful
        :121: T>Tc
        :633: Failed to converge
        :-638: Spinodal not found, point of zero curvature returned


.. f:subroutine:: VIRBAdll (T, z, Ba, )

    
    Compute the second acoustic virial coefficient Ba (L/mol) as a function
    of temperature (K) and composition x (array of mole fractions).
    For further information, see
    Trusler and Zarari, J. Chem. Thermodyn., 28:329-335, 1996.
    Gillis and Moldover, Int. J. Theromphys., 17(6):1305-1324, 1996.
    This routine approximates Ba.  For pure fluids, the routine VIRBCD is exact.
    
    :p double T [in]: Temperature [K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double Ba [out]: Second acoustic virial coefficient [L/mol] 



.. f:subroutine:: VIRBCDdll (T, z, B, C, D, E, )

    
    Compute virial coefficients as a function of temperature and composition.
    The routine currently works only for pure fluids and for the Helmholtz equation.
    All values are computed exactly based on the terms in the EOS, not
    as was done in VIRB by calculating properties at a density of 1d-8.
    
    :p double T [in]: Temperature [K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double B [out]: Second virial coefficient [L/mol]       = a01 
    :p double C [out]:  Third virial coefficient [(L/mol)^2]   = a02 
    :p double D [out]: Fourth virial coefficient [(L/mol)^3]   = a03/2d0 
    :p double E [out]:  Fifth virial coefficient [(L/mol)^4]   = a04/6d0 assume nomenclature of a02=[partial^2(alphar)/partial(del)^2] above 



.. f:subroutine:: VIRBdll (T, z, B, )

    
    Compute the second virial coefficient B (L/mol) as a function of
    temperature T (K) and composition x (array of mole fractions).
    This routine approximates B.  For pure fluids, the routine VIRBCD is exact.
    
    :p double T [in]: Temperature [K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double B [out]: Second virial coefficient [L/mol] 



.. f:subroutine:: VIRCAdll (T, z, Ca, )

    
    Compute the third acoustic virial coefficient Ca (L/mol)^2 as a function
    of temperature (K) and composition x (array of mole fractions).
    For further information, see
    Estela-Uribe and Trusler, Int. J. Theromphys., 21(5):1033, 2000.
    Gillis and Moldover, Int. J. Theromphys., 17(6):1305-1324, 1996.
    This routine approximates Ca.  For pure fluids, the routine VIRBCD is exact.
    
    :p double T [in]: Temperature [K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double Ca [out]: Third acoustic virial coefficient [(L/mol)^2] 



.. f:subroutine:: VIRCdll (T, z, C, )

    
    Compute the third virial coefficient C (L/mol)^2 as a function of
    temperature T (K) and composition x (array of mole fractions).
    This routine approximates C.  For pure fluids, the routine VIRBCD is exact.
    
    :p double T [in]: Temperature [K] 
    :p double z(20) [in]: Composition (array of mole fractions) 
    :p double C [out]:  Third virial coefficient [(L/mol)^2]   = a02 



.. f:subroutine:: WMOLIdll (icomp, wmm, )

    
    Return the molar mass (molecular weight) of a component in a mixture.
    
    :p int icomp [in]: Component number in the mixture 
    :p double wmm: XXXXXXXXXX



.. f:subroutine:: WMOLdll (z, wmm, )

    
    Return the molar mass (molecular weight) for a mixture of
    a specified composition.
    
    :p double z(20) [in]: Composition array (array of mole fractions) 
    :p double wmm: XXXXXXXXXX



.. f:subroutine:: XMASSdll (xmol, xkg, wmix, )

    
    Converts composition on a mole fraction basis to mass fractions.
    
    :p double xmol(20) [in]: Composition array (array of mole fractions) 
    :p double xkg(20) [out]: Composition array (array of mass fractions) 
    :p double wmix [out]: Molar mass of the mixture [g/mol], a.k.a. molecular weight 



.. f:subroutine:: XMOLEdll (xkg, xmol, wmix, )

    
    Converts composition on a mass fraction basis to mole fraction.
    
    :p double xkg(20) [in]: Composition array (array of mass fractions) 
    :p double xmol(20) [out]: Composition array (array of mole fractions) 
    :p double wmix [out]: Molar mass of the mixture [g/mol], a.k.a. molecular weight 



