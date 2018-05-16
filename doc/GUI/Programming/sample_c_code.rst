.. _sample_c_code: 

***************
Sample C++ Code
***************

**Sample C++ Code**

The example C code (located on the FAQ website) uses explicit (sometimes called late) linking for the functions in the DLL. All functions exported by the DLL have been provided in the header file, REFPROP2.h, for completeness. All functions exported by REFPROP are in the file PASS_FTN.FOR located in the REFPROP\FORTRAN directory. The main issues in mixed-language code compiling are function naming conventions, argument passing, and stack maintenance. Explicit calling of the FORTRAN functions in the DLL allows one to define a function pointer name explicitly. The _stdcall keyword on the function prototype lets the compiler know how arguments will be passed and which side is responsible for cleaning the stack after the function call.


