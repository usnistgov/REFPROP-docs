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
| eric.lemmon@nist.gov
| ian.bell@nist.gov
| marcia.huber@nist.gov

The user interface was written by Eric W. Lemmon.

**IMPORTANT:** Please visit the `REFPROP FAQ <https://pages.nist.gov/REFPROP-docs/>`_ web site as your first resource when you encounter difficulties or have questions. Most email enquiries are answered by pointing to the FAQ. Using the FAQ will save valuable NIST resources that can be used to further develop REFPROP.

*Certain trade names and other commercial designations are used in this work for the purpose of clarity. In no case does such identification imply endorsement by the National Institute of Standards and Technology, nor does it imply that the products or services so identified are necessarily the best available for the purpose.
