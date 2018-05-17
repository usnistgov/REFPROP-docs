.. _opensession: 

****
Open
****

The Open command reads a file previously saved with the :ref:`filesave`  command. The files are identified by a .RFP filename extension. The Open command restores the program to the state it was in when the :ref:`filesave` command was issued. Thus, the :ref:`units`, :ref:`reference`, :ref:`properties`, :ref:`substance`, and all :ref:`isopropertytables`  and :ref:`plotwindow`  are restored. Note that the Open command will replace all settings and windows of the current session with those from the previously saved file; REFPROP will prompt the user to :ref:`filesave`  the current session before opening the saved session.