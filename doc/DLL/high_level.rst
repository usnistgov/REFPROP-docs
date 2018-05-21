

.. _high_level_api:

.. This file was auto-generated on 21 May 2018 12:36:03. DO NOT(!!!!) modify this file directly.  Modify the generator script in the scripts folder.

**************
High-Level API
**************

Function Listing
----------------

- :f:func:`ABFLSHdll`
- :f:func:`ALLPROPS0dll`
- :f:func:`ALLPROPS1dll`
- :f:func:`ALLPROPSdll`
- :f:func:`ERRMSGdll`
- :f:func:`FLAGSdll`
- :f:func:`GETENUMdll`
- :f:func:`REFPROP1dll`
- :f:func:`REFPROP2dll`
- :f:func:`REFPROPdll`
- :f:func:`SETFLUIDSdll`
- :f:func:`SETMIXTUREdll`
- :f:func:`SETPATHdll`


Function Documentation
----------------------
.. f:subroutine:: ABFLSHdll (ab, a, b, z, iFlag, T, P, D, Dl, Dv, x, y, q, e, h, s, Cv, Cp, w, ierr, herr, ab_length, herr_length)

    
    General flash calculation that handles all inputs of T, P, D, h, e, s, and q.
    
    Includes both blind flash calculations, and situations where
    the phase is known to be liquid, vapor, or 2-phase, and thus the
    calculation time will be much faster.
    
    Many of the 2-phase flash routines can accept initial estimates to
    decrease calculation time and improve convergence.  ABFLSH does
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
    * For saturation properties, use codes of 'TQ' or 'PQ' for ab, and send b=1.
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
        - 0 - Default
        - 1 - Quality on a molar basis (moles vapor/total moles) (default, the value of 1 is not necessarily needed).
        - 2 - Quality on a mass basis (mass vapor/total mass);
          for inputs of T and either h or e (kr flag)
        - 3 - Return lower density root.
        - 4 - Return higher density root.
    
    Examples:
    
    * 000 - Default - Phase of state is unknown, molar units will be used everywhere,
      higher density root will be returned.
    * 002 - Use mass based properties for everything except composition.
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
    :p double Dv [out]: Molar density of the vapor phase [mol/L or kg/m^3]; if only one phase is present, Dl = Dv = D.
    :p double x(20) [out]: Composition of the liquid phase (array of mole or mass fractions) 
    :p double y(20) [out]: Composition of the vapor phase (array of mole or mass fractions); if only one phase is present, x = y = z.
    :p double q [out]: Vapor quality on a MOLAR basis (moles of vapor/total moles)
    :p double e [out]: Overall internal energy [J/mol or kJ/kg] 
    :p double h [out]: Overall enthalpy [J/mol or kJ/kg] 
    :p double s [out]: Overall entropy [J/mol-K or kJ/kg-K] 
    :p double Cv [out]: Isochoric (constant D) heat capacity [J/mol-K or kJ/kg-K] 
    :p double Cp [out]: Isobaric (constant P) heat capacity [J/mol-K or kJ/kg-K] 
    :p double w [out]: Speed of sound [m/s] 
    :p int ierr [out]: Error flag
    :p char herr [out]: Error string (character*255) 
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


.. f:subroutine:: ALLPROPS0dll (iIn, iOut, iFlag, T, D, z, Output, ierr, herr, herr_length)

    
    Calculate any single phase property defined in the iOut array and
    return the values in the Output array.  This routine should NOT
    be called for two-phase states!
    
    The output array is not reset so that several passes can be made to
    fill in holes left by the previous pass (such as entries at different
    T, D, or z).  The caller can zero out this array if so desired.
    
    This routine is designed with the "superuser" in mind.  It removes all
    string comparisons to approach the speed that could be obtained by
    calling the dedicated functions (such as THERM), but making it easy
    by allowing all inputs to be calculated with one routine.  Since the
    units are not returned here, look in the ALLPROPS documentation under
    the molar column.
    
    These values of iOut are defined in the COMMONS.INC file
    and are obtained by a call to GETENUM, as such for the enthalpy::
    
        call GETENUM (0,'H',iEnum,ierr,herr)
    
    To obtain the pure fluid value for some of the inputs,
    add 10000*ic (where ic is the component number) to the value
    of the enumerated value.  The properties that can be used for this are
    given the bottom of the comments section in the ALLPROPS routine.
    
    
    :p int iIn [in]: Number of properties to calculate. 
    :p int iOut(200) [in]: Array of enumerated values that identify the property to be calculated (see above)
    :p int iFlag [in]: Not yet used. 
    :p double T [in]: Temperature [K] 
    :p double D [in]: Density [mol/L] 
    :p double z(20) [in]: Overall composition (array of mole fractions) 
    :p double Output(200) [out]: Values of the calculated properties. 
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
    :p double c [out]: Output value (array of size 200 dimensioned as double precision). The number -9999970 will be returned when errors occur or no input was requested.
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
        phase boundary, and complete nonsense at other conditions.  The
        value of q that is returned from the flash routines will indicate
        a two phase state by returning a value between 0 and 1.  In such
        a situation, properties can only be calculated for the saturated
        liquid and vapor states.  For example, when calling PHFLSH::
    
            call PHFLSH (P,h,z,T,D,Dl,Dv,x,y,q,e,s,Cv,Cp,w,ierr,herr)
    
        If q>0 and q<1, then values of the liquid and vapor compositions will
        be returned in the x and y arrays, and the properties of the
        liquid and vapor states can be calculated, for example::
    
            call ENTRO (T,Dl,x,sliq)
            call ENTRO (T,Dv,x,svap)
    
    ALLPROPS was the name of a program developed at the University of
    Idaho under the direction of R.B. Stewart and R.T Jacobsen at the
    Center for Applied Thermodynamic Studies (CATS), with
    S.G. Penoncello and S.W. Beyerlein as professors at this institution.
    The software was distributed for about 10 years until around 
    2000 when it was officially replaced by the Refprop program.
    Some of the techniques from ALLPROPS was used in the development of
    Version 6 of Refprop, and were in some ways its forerunner.  The
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
    
    The name ALLPROPS was revived at NIST in 2017 in memory of the old but
    not forgotten program whose roots still form the foundation of much
    that goes on behind the scenes in the development of equations of
    state and property software.
    
    **Calling from the DLL**
    
    Two routines are available in the DLL, these are ALLPROPSdll and
    ALLPRP200dll.  Both compress the ``hUnitsArray`` array so that it can be passed
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
    
    **Note about criticals**: The items TC,PC,DC will return the critical point of a pure fluid, or, when SATSPLN
    has been called, the critical point of the mixture (or a very close approximation).
    When the splines have not been set up, the values are the same as TCEST below.
    For the critical points of the pure fluids in a mixture, use TCRIT, etc., explained
    below, which is useful when multiple fluids have been loaded.
    Parameters in the HMX.BNC file, which, for a binary mixture, are close for Type I
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
    DPDD       dP/dD at constant T                            [kPa/(dm^3/mol)]         [kPa/(m^3/kg)]
    DPDT       dP/dT at constant D                            [kPa/K]                  [kPa/K]
    DDDP       dD/dP at constant T                            [(mol/dm^3)/kPa]         [(kg/m^3)/kPa]
    DDDT       dD/dT at constant P                            [(mol/dm^3)/K]           [(kg/m^3)/K]
    DTDP       dT/dP at constant D                            [K/kPa]                  [K/kPa]
    DTDD       dT/dD at constant P                            [(dm^3/mol)*K]           [(m^3/kg)*K]
    D2PDD2     d^2P/dD^2 at constant T                        [kPa/(dm^3/mol)^2]       [kPa/(m^3/kg)^2]
    D2PDT2     d^2P/dT^2 at constant D                        [kPa/K^2]                [kPa/K^2]
    D2PDTD     d^2P/dTdD                                      [kPa/(dm^3/mol)/K]       [kPa/(m^3/kg)/K]
    D2DDP2     d^2D/dP^2 at constant T                        [(mol/dm^3)/kPa^2]       [(kg/m^3)/kPa^2]
    D2DDT2     d^2D/dT^2 at constant P                        [(mol/dm^3)/K^2]         [(kg/m^3)/K^2]
    D2DDPT     d^2D/dPdT                                      [(mol/dm^3)/(kPa*K)]     [(kg/m^3)/[kPa*K]]
    D2TDP2     d^2T/dP^2 at constant D                        [K/kPa^2]                [K/kPa^2]
    D2TDD2     d^2T/dD^2 at constant P                        [(dm^3/mol)^2*K]         [(m^3/kg)^2*K]
    D2TDPD     d^2T/dPdD                                      [K/(dm^3/mol)/kPa]       [K/(m^3/kg)/kPa]
    
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
    VIS        Viscosity                                      [uPa*s]                  [uPa*s]
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
    
    :p char hOut [in]: Input string of properties to calculate. Inputs can be separated by spaces, commas, semicolons, or bars, but should not be mixed.  For example, a proper string would be hOut='T,P,D,H,E,S', whereas an improperly defined string would be hOut='T,P;D H|E,S'. Use of lower or upper case is not important. Some properties will return multiple values, for example, hOut='F,Fc,XMOLE' will return 12 properties for a four component system, these being F(1), F(2), F(3), F(4), Fc(1), Fc(2), etc. To retrieve the property of a single component, use, for example, hOut='XMOLE(2),XMOLE(3)'.
    :p int iUnits [in]: See subroutine REFPROP for a complete description of the iUnits input value. A negative value for iUnits indicates that the input temperature is given in K and density in mol/dm^3, (Refprop default units), otherwise T and D will be converted first to K and mol/dm^3.  Do not use the negative value for the iUnits parameter everywhere, only in this one situation.
    :p int iMass [in]: Specifies if the input composition is mole or mass based
    :p int iFlag [in]: Turn on or off writing of labels and units to hUnitsArray (eventually may be multiple flags combined into one variable, similar to ABFLSH)
    :p double T: XXXXXXXXXX
    :p double D: XXXXXXXXXX
    :p double z(20): XXXXXXXXXX
    :p double Output(200) [out]: Array of properties that were specified in the hOut string (array of size 200 dimensioned as double precision). The number -9999970 will be returned when errors occur or no input was requested.
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
    
    :p int ierr [in]: Error number from the last call to ERRNUM 
    :p char herr [out]: Associated error string (character*255) 
    :p int herr_length: length of variable ``herr`` (default: 255)



.. f:subroutine:: FLAGSdll (hFlag, jFlag, kFlag, ierr, herr, hFlag_length, herr_length)

    
    Set flags for desired behavior from the program.
    
    .. table:: Table of flags in FLAGS function
        :class: longtable
    
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``hFlag``           | ``jFlag``                                                                                           |
        +=====================+=====================================================================================================+
        | ``Return errors``   | *  0 - Return only final messages (default).                                                        |
        |                     | *  1 - Return all intermediate messages.                                                            |
        |                     | *  2 - Do not return messages.                                                                      |
        |                     |                                                                                                     |
        |                     | This flag is not reset with a new call to SETUP.                                                    |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Write errors``    | *  0 - Error strings not written to screen (default).                                               |
        |                     | * -1 - Error string written to screen.                                                              |
        |                     | *  1 - Error string written to screen only if ierr is positive.                                     |
        |                     | * 3,-3 - Same as 1 and -1, but program also pauses.                                                 |
        |                     |                                                                                                     |
        |                     | This flag is not reset with a new call to SETUP.                                                    |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Dir search``      | * 0 - Search for fluid files in alternate directories (as defined in OPENFL) (default).             |
        |                     | * 1 - Do not search in directories other than the one set by the call to SETPATH,                   |
        |                     |   except for a 'fluids' subdirectory within the folder given in SETPATH.                            |
        |                     |   If the fluid files for the reference fluid(s) are not in the SETPATH directory,                   |
        |                     |   then transport properties may not be calculated.                                                  |
        |                     | * 2 - Make no additional checks if the fluid file is not found after the first attempt to open      |
        |                     |   the file (for example, checking upper and lower case).                                            |
        |                     |                                                                                                     |
        |                     | This flag is never reset.                                                                           |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Cp0Ph0``          | * 1 - Change the ideal gas equation to Cp0.                                                         |
        |                     | * 2 - Change the ideal gas equation to PH0.                                                         |
        |                     |                                                                                                     |
        |                     | The default is set by the value in the fluid file.                                                  |
        |                     | Calling SETUP resets the equation to its default state as given in the fluid file.                  |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``PX0``             | * 0 - Use the fluid file as is for the ideal gas equation (default).                                |
        |                     | * 1 - Use the PX0 (or PH0 when no PX0 is available) for all calculations and turn off the call      |
        |                     |   to SETREF.  For mixtures, the reference state of "each pure component" will be used.              |
        |                     |                                                                                                     |
        |                     | This flag is never reset.  When setting up the fluids through a call to the REFPROP subroutine,     |
        |                     | the SETREF flag described below will override this flag if turned on.                               |
        |                     | Warning:  Don't use the Cp0Ph0 flag to attempt to switch back to Cp0 (h and s will be wrong)        |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``Skip SETREF``     | * 0 - Call the SETREF routine to setup the reference state (default).                               |
        |                     | * 1 - Skip the call to SETREF.  However, this means energy, enthalpy, and entropy will not be       |
        |                     |   correct (but only by an offset to their usual values).                                            |
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
        |                     |   a mixture or reducing nc.                                                                         |
        |                     |                                                                                                     |
        |                     | Subroutine RESETA is always called by SETUP, but does not reset many of the flags set by calls      |
        |                     | to this routine.                                                                                    |
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
        |                     | This option is reset during the call to SETUP.                                                      |
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
        |                     | If the AGA8 option is active, it overrides all other models.  Unlike the GERG 2008 option, this     |
        |                     | model is active (or deactivated) immediately upon calling this routine.                             |
        |                     | The AGA8 flag is never reset, thus recalling SETUP only changes the fluids, not the model.          |
        +---------------------+-----------------------------------------------------------------------------------------------------+
        | ``GERG 2008``       | * 0 - Set a flag to turn off GERG 2008 next time SETUP is called.                                   |
        |                     | * 1 - Turn on the flag that will cause the GERG 2008 equation to be loaded next time SETUP is called|
        |                     |                                                                                                     |
        | or ``GERG``         | This option MUST be called before SETUP.   When turning off the GERG, call the SETUP routine again  |
        |                     | after calling this routine.  Because the GERG model is not activated until SETUP is called,         |
        |                     | the value of kflag will be 1 until the next call to setup, at which time it will be set to 2 to     |
        |                     | indicate that it is fully active.    When turning off the GERG model, the value of kflag will be -1 |
        |                     | until the next call to setup, and then it will be reset to zero.  The -1 indicates that it is still |
        |                     | in use but waiting to be reset.  This flag is never reset.                                          |
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
        |                     |                                                                                                     |
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



.. f:subroutine:: GETENUMdll (iFlag, hEnum, iEnum, ierr, herr, hEnum_length, herr_length)

    
    Translate a string of letters into an integer value that can be used
    in calls to ALLPROPS0 to increase the speed of property calculations
    by eliminating string comparisons (which are time expensive in Fortran).
    This can be done once at the beginning of a program for all properties
    that will be used, and stored for later use as needed.
    
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
        :3: Check property strings only that are not functions of T and D (for example, the critical point, acentric factor, limits of the EOS, etc.).


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
    :p int iUnits [in]: The unit system to be used for the input and output properties (such as SI, English, etc.) See the details in the REFPROP subroutine for a complete description of the iUnits input value. **NOTE**: A mass based value for iUnits does not imply that the input and output compositions are on a mass basis, this is specified with the iMass variable.
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
    given in FLSH_SUB.FOR) and the non-iterative functions such as THERM and TRNPRP requires very few (or no)
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
    selected, the composition will be returned in the zm array (on a molar or mass basis depending on iMass).
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
    When q is >0 and <1, then the quality uses a molar basis when iMass=0, and a mass basis
    when iMass=1.  The value of iUnits has no effect on the value of q (as either an input or output).
    The shortcuts Tsat and Psat can be used to specify a saturation state for the liquid for a pure fluid.
    To return, for example, the saturated vapor density, Dvap would be used as an output variable.
    The order of the properties being sent to the routine in the variables a and b has to be the
    same as the letters sent to hIn; for example, if hIn is 'QT', then a=q and b=T.
    
    The ABFLSH routine is called to determine the phase of the inputs (liquid, vapor, or 2-phase), and
    then the appropriate iterative routine will be called to obtain the independent properties of the
    equations of state: temperature and density.  For subsequent calculations for
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
      TP>, PH>, HSL.
    
    - ``**<`` or ``**V``: The letter 'V' (or the sign '<') specifies that the input state for the properties listed
      in the first two letters is in the single phase vapor (including metastable states).  For
      example:  TP<, PH<, HSV.
    
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
    - ``DOI_###(#)``: Return the DOI of the equation given by the three letters following the underscore, where the valid letters
      are EOS for equation of state, VIS for viscosity, TCX for thermal conductivity, STN for surface tension,
      DIE for dielectic constant, MLT for melting line, and SBL for sublimation line.  For example, DOI_EOS would
      return the DOI for the equation of state.  For mixtures, the component must be specified at the end in the parenthesis,
      for example, DOI_VIS(3).
    - ``WEB_###(#)``: Return the web address for the equation given by the three letters following the underscore, as explained
      in the DOI section.
    - ``REFSTATE``: Return the reference state in use (NBP, IIR, ASH, OTH, etc.).
    - ``GWP``: Return the global warming potential (found in the fluid file header).
    - ``ODP``: Return the ozone depletion potential (found in the fluid file header).
    - ``FDIR``: Return the location (directory) of the fluid file.  The directory is returned in both the hUnits string and in
      herr if no other error occurred (paths that are more than 50 characters long are truncated in hUnits).
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
      hOut='UNITCONV_T' or hOut='UNITCONV_D'.
    - ``UNITUSER``, ``UNITUSER2``: Set a predefined set of units based on the user's need.
      Two different sets can be assigned depending on the input sent to the routine.  The variable hIn
      contains the numbers that are specified by the enumerations in the CONSTS.INC file, separated by semicolons.
      For example, hIn='0;157;0;0;0;403;0;0;0;0' would set the pressure to use units of atm and the
      speed of sound to use units of km/h. The numbers are listed in the order of T, P, D, H, S, W, I, E, K, and N
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
    - ``VAPORFLUIDSTRING``: Return a string that contains the fluid names and compositions for the vapor phase of a two-phase state.
      For example, "R32;R125|0.25;0.75".  The string is passed back in hUnits.
    - ``QMOLE``: Return the molar quality for 2-phase states.
    - ``QMASS``: Return the mass quality for 2-phase states.
    - ``XMASS``: Return the mass compositions in the Output array as with the X command.  See comment about ``Qmass``.
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
        Pressure         kPa         MPa         MPa           MPa
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
    
    :p char hFld [in]: String of any character length containing the fluid file names 
    :p int ierr [out]: Error flag
    :p int hFld_length: length of variable ``hFld`` (default: 10000)


    :Flags: 

        ``ierr`` flags

        :0: Successful (Values are identical to SETUP; a 109 is returned if the number of fluids in hfld is less than icomp.)


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


.. f:subroutine:: SETPATHdll (hpth, hpth_length)

    
    Set the path where the fluid files are located.
    
    :p char hpth [in]: Location of the fluid files (character*255) The path does not need to contain the ending "/" and it can point directly to the location where the DLL is stored if a fluids subdirectory (with the corresponding fluid files) is located there, for example, hpth='C:/Program Files (x86)/REFPROP' 
    :p int hpth_length: length of variable ``hpth`` (default: 255)



