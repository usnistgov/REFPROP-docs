.. _sample_visual_basic_code: 

************************
Sample Visual Basic Code
************************

**Sample Visual Basic Code**

Sample Visual Basic (VB6) code is provided that demonstrates the use of VB with REFPROP. The file is called Sample.bas and is located in the Examples directory where the REFPROP program was installed. It uses the dynamic link library REFPROP.DLL. Sample :ref:`FORTRAN <sample_fortran_code>`  and :ref:`Excel <excel_spreadsheets>`  files are also included.

VB subroutines analogous to all of the FORTRAN subroutines are available. The subroutine names have 'dll' appended to the FORTRAN names (for example, SETUPdll is the VB analog to the FORTRAN subroutine SETUP). The inputs and outputs are the same as the FORTRAN routines, except that additional arguments specifying the length of any string variables are required.

The file Sample.bas consists of subroutine and variable declarations in the first part of the file. These declarations would be necessary for any program. The latter part of the file provides examples of calling the various subroutines. No output is displayed when the program is run because it is intended only to show how the calling routines work. Comments are given throughout the code describing the various calls and procedures. Additional details on the subroutines and functions are given in the FORTRAN code included with REFPROP and in the file MANUAL.TXT.

For information on linking with VB.NET, see the :ref:`REFPROP FAQ <faq>`  `website <http://www.boulder.nist.gov/div838/theory/refprop/Frequently_asked_questions.htm#NETApplications>`_.


