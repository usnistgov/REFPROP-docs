.. _aboutrefprop: 

*************
About REFPROP
*************

**About REFPROP**

REFPROP is an acronym for REFerence fluid PROPerties. This program, developed by the National Institute of Standards and Technology (NIST), calculates the thermodynamic and transport properties of industrially important fluids and their mixtures. These properties can be displayed in :ref:`tables <isopropertytables>`  and :ref:`plots <plotwindow>`  through the graphical user interface; they are also accessible through spreadsheets or user-written applications accessing the :ref:`REFPROP dll <dll_s>` .

REFPROP is based on the most accurate pure fluid and mixture models currently available. It implements three models for the thermodynamic properties of pure fluids: equations of state explicit in Helmholtz energy, the modified Benedict-Webb-Rubin equation of state, and an extended corresponding states (ECS) model. Mixture calculations employ a model that applies mixing rules to the Helmholtz energy of the mixture components; it uses a departure function to account for the departure from ideal mixing. Viscosity and thermal conductivity are modeled with either fluid-specific correlations, an ECS method, or in some cases the friction theory method.

The property formulations and fluid data files were programmed by:

Eric W. Lemmon, Marcia L. Huber, and Mark O. McLinden
Applied Chemicals and Materials Division
National Institute of Standards and Technology
Boulder, CO 80305
Eric.Lemmon@NIST.gov
Marcia.Huber@NIST.gov

The user interface was written by Eric W. Lemmon.

**IMPORTANT:** Please visit the `REFPROP FAQ <http://www.boulder.nist.gov/div838/theory/refprop/Frequently_asked_questions.htm>`_ web site as your first resource when you encounter difficulties or have questions. Most email enquiries are answered by pointing to the FAQ. Using the FAQ will save valuable resources that can be used to further develop REFPROP.


We gratefully acknowledge the many contributions of our colleagues and associates. Gary Hardin (of NIST) provided support with the help file and the installation package. Allan Harvey (of NIST) provided very thorough and greatly appreciated debugging of REFPROP. Frank Doyle developed the UserInformation sheet in the Excel file. G. Venkatarathnam (of the Indian Institute of Technology Madras) and Matthias Kunick (of the Zittau/Goerlitz University of Applied Sciences, Germany) provided routines and much help in the development of new algorithms for the calculation of VLE states in 9.1, particularly in the critical region. Diego Ortiz (of Texas A&amp;M University), Andreas Jaeger, and Johannes Gernert (both from the Ruhr University, Germany) helped with the analytical VLE routine added in version 9.0. Arno Laesecke (of NIST) provided an extensive collection of viscosity data. Lennart Vamling (of the Chalmers University of Technology in Sweden), Johannes Lux (of the German Aerospace Center), and Paul Brown (of Ramgen Power Systems) aided in the MATLAB link. Chris Muzny (of NIST) aided with the link to C++, and with the MATLAB link.

Previous versions of the REFPROP database were developed by Graham Morrison and John Gallagher. Jim Ely, Dan Friend, and Marcia Huber wrote the early versions of the related databases NIST12 and NIST14 from which we have extracted algorithms. We thank Sanford Klein and Adele Peskin, the programmers of the original graphical interface implemented in version 6. We had many helpful discussions with Dan Friend, Allan Harvey, Roland Span, Wolfgang Wagner, Richard Jacobsen, Vincent Arp, Arno Laesecke, Richard Perkins, and Reiner Tillner-Roth.

We also made extensive use of the CATS Database for Pure Fluids and Mixtures of the Center for Applied Thermodynamic Studies of the University of Idaho, Moscow, Idaho, the NIST/TRC SOURCE and TDE Databases, the AIChE DIPPR database, and the Dortmund Data Bank for Pure Component Properties (DDB-Pure), Oldenburg, Germany, in fitting the models implemented in REFPROP. Finally, we acknowledge our many colleagues whose property measurements and models we have taken from the literature, and without which this database would be much reduced in scope.

Development of this software package was supported by the NIST Thermophysical Properties Division and the NIST Standard Reference Data Program. The development of previous versions was supported by the Air-Conditioning and Refrigeration Technology Institute and the U.S. Department of Energy. Model development and measurements at NIST have been supported over a period of many years by numerous sponsors including the Air-Conditioning and Refrigeration Technology Institute, the U.S. Department of Energy, the Electric Power Research Institute, the Environmental Protection Agency, Oak Ridge National Laboratory, the American Society of Heating, Refrigerating and Air-Conditioning Engineers, and the Building Environment and Thermophysical Properties Divisions of NIST.


*Certain trade names and other commercial designations are used in this work for the purpose of clarity. In no case does such identification imply endorsement by the National Institute of Standards and Technology, nor does it imply that the products or services so identified are necessarily the best available for the purpose.


