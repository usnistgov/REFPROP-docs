.. _readdata: 

*******************
Read Data from File
*******************

Values can be read from an ASCII file and placed in an open table. An Open file dialog appears in which you may specify the file containing the independent property values. The box at the top of the window displays the first 20 lines of the selected file so that you can see the format of the values in the file. Although only 20 lines are shown, all of the lines are read in when you press the OK button. Lines in the file that begin with a nonnumeric character, such as \*, are treated as comments and are ignored.

Data are read from the file and inserted into the table depending on the inputs under the 'Read column' and 'Insert data into field' options. The column specified under 'Read column' will be entered into the field specified under 'Insert data into field'. It is not necessary to read all of the input properties from the file. For example, you can read the temperature but not the pressure by selecting the blank line (at the top of the drop down box) in the second (and subsequent) rows.

Extra data from the file can be read and placed in a comment column in the :ref:`specifiedstatepoints`  table. The capability to read additional data from a file is useful in comparing experimental and calculated values of a property, for example. Before this can be done, the 'Add a comment column to tables' option must be specified in the :ref:`preferences`, and a new table containing the comment field must be created. The comment field can then be specified in one of the boxes under the 'Insert data into field' label. They can then be plotted along with calculated values.