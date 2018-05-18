.. _welcometorefprop: 

**********************************
Welcome to REFPROP's Documentation
**********************************

.. image:: _static/REFPROP.png

REFPROP is an acronym for REFerence fluid PROPerties. This program, developed by the National Institute of Standards and Technology (NIST), calculates the thermodynamic and transport properties of industrially important fluids and their mixtures. These properties can be displayed in :ref:`Tables <isopropertytables>`  and :ref:`Plots <plotwindow>`  through the graphical user interface; they are also accessible through spreadsheets or user-written applications accessing the :ref:`REFPROP dll <dll_s>`.

REFPROP is based on the most accurate pure fluid and mixture models currently available. It implements three models for the thermodynamic properties of pure fluids: equations of state explicit in Helmholtz energy, the modified Benedict-Webb-Rubin equation of state, and an extended corresponding states (ECS) model. Mixture calculations employ a model that applies mixing rules to the Helmholtz energy of the mixture components; it uses a departure function to account for the departure from ideal mixing. Viscosity and thermal conductivity are modeled with either fluid-specific correlations, an ECS method, or in some cases the friction theory method.

.. toctree::
   :maxdepth: 2

   GUI/index.rst
   DLL/index.rst