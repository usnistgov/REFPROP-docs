.. _aboutrefprop:

*************
About REFPROP
*************

REFPROP is an acronym for REFerence fluid PROPerties. This program, developed by the National Institute of Standards and Technology (NIST), calculates the thermodynamic and transport properties of industrially important fluids and their mixtures. These properties can be displayed in :ref:`Tables <isopropertytables>`  and :ref:`Plots <plotwindow>`  through the graphical user interface; they are also accessible through spreadsheets or user-written applications accessing the :ref:`REFPROP dll <dll_s>`.

REFPROP is based on the most accurate pure fluid and mixture models currently available. It implements three models for the thermodynamic properties of pure fluids: equations of state explicit in Helmholtz energy, the modified Benedict-Webb-Rubin equation of state, and an extended corresponding states (ECS) model. Mixture calculations employ a model that applies mixing rules to the Helmholtz energy of the mixture components; it uses a departure function to account for the departure from ideal mixing. Viscosity and thermal conductivity are modeled with either fluid-specific correlations, an ECS method, or in some cases the friction theory method.

The property formulations and fluid data files were programmed by:

| Eric W. Lemmon, Ian H. Bell, Marcia L. Huber, and Mark O. McLinden
| Applied Chemicals and Materials Division
| National Institute of Standards and Technology
| Boulder, CO 80305
|
| Eric.Lemmon@nist.gov
| Ian.Bell@nist.gov
| Marcia.Huber@nist.gov


REFPROP 10.0 is the culmination of several years of revisions and updates.  Work never stops on the development of thermophysical properties and equations, but the last two years have been especially intense and fully dedicated to this release.  Although there are only four authors of this work, we are very grateful to the many contributions of our NIST colleagues, including Gary Hardin, Allan Harvey, Chris Muzny, Vladimir Diky, Ala Bazyleva, and Janiel Reed who have provided support over the last several versions of REFPROP.  Also of NIST are Adam Morey, Cindy McKneely, and Sherena Johnson who distribute the product for us to industry.  A number of individuals from industry have contributed continuously over the last several years; we are indebted to them for their help, and we thank Tobias Loew, Nik Felbab, Nicolas James, Dan Williams, Jim Pollard, and Stuart Lawson.

We acknowledge our many colleagues whose property models we have taken from the literature, and without which this database would be much reduced in scope.  In particular, the Ruhr University in Bochum, Germany, has for many decades worked alongside us in the development of equations of state.  The contributions of Wolfgang Wagner, Roland Span, and Monika Thol can easily be seen by browsing through the fluid information.  We thank Marc Assael of Aristotle University of Thessaloniki (Greece) for his many contributions to the development of transport property formulations.  We also thank our colleagues within our division whose efforts have made possible the NIST/TRC SOURCE and TDE Databases, of which we have made extensive use for our data needs required to develop thermophysical property equations.

Although REFPROP is a program built on equations of state, its entire existence is built on a foundation of experimental data, some of which dates back to the late 1800s.  Through experimental measurements, especially the highly accurate values of Wolfgang Wagner, Reiner Kleinrahm, Martin Trusler, Mark McLinden, Markus Richter, their students and colleagues, and many others, equations are built that are then used throughout industry world-wide.  Many things that touch our lives have been influenced in one way or another by these measurements.  Power generation alone affects all, and the properties from these equations influence the efficiency and design of that infrastructure.  Likewise, heating, cooling, and transportation have all been influenced by the measurements and subsequent property equations.  We are greatly indebted to the enormous work of so many scientists and engineers that continues unseen by most.

The development of this software package was supported by the NIST Applied Chemicals and Materials Division and the NIST Standard Reference Data Program.  The development of the models and the measurement of the data on which REFPROP is based have been supported over a period of many years by numerous sponsors.

**IMPORTANT:** Please visit the `REFPROP FAQ <https://pages.nist.gov/REFPROP-docs/>`_ web site as your first resource when you encounter difficulties or have questions. Most email enquiries are answered by pointing to the FAQ. Using the FAQ will save valuable NIST resources that can be used to further develop REFPROP.

\*Certain trade names and other commercial designations are used in this work for the purpose of clarity. In no case does such identification imply endorsement by the National Institute of Standards and Technology, nor does it imply that the products or services so identified are necessarily the best available for the purpose.
