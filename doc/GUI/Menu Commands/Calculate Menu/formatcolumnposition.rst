.. _formatcolumnposition: 

*************************************************
Format, Column Position, and Automatic Data Entry
*************************************************

**Format, Column Position, and Automatic Data Entry**

The format of the data in each column is set to a default style. You can change the format of the data in the column by right clicking the mouse in the column header. This action will bring up a window in which the format of the data in the column and the column position can be changed.

To change the format of the values in the column, click on the arrow to the right of the 'Style' field. A list of 'Default', 'Fixed digits', 'Fixed decimal', and 'Scientific notation' is shown. The 'Fixed digits' option allows a fixed number of total digits, including those before and after the decimal point. The 'Fixed decimal' option allows a fixed number of digits to be specified to the right of the decimal point. The 'Scientific notation' option allows the number to be displayed in that format. An example illustrating the display format appears to the right of the word 'Format'. The number of digits to be displayed can be changed globally with the :ref:`preferences <preferences>`  command.

To change the column position, click the up or down arrows until the desired column position is shown. The positions of all other columns shift accordingly. To change the column position permanently, use the option in the :ref:`Substance <substance>`  menu called :ref:`Property Order <propertyorder>` . The units of the column can be changed using the 'Convert units' option. For mixtures, unit conversions requiring the molar mass of the fluid are not available. Note that you may not convert units when using specified state tables; however, the option to clear an entire column is available.

To fill a table with a range of numbers, enter a combination of values into the cells under the 'Specify values' section. The value to be placed in the first row of the selected row must be specified in the 'First value' field. Beneath this field are additional input boxes in which the last value in the range, the increment (or a multiplier), or last row can be specified. If 'Increment' is selected, the value of successive rows in the table is determined by adding the value in the increment field to the previous value. Similarly, if 'Multiply' is selected, successive values are determined by multiplying the previous value by the value indicated in the field. If 'Final value' is selected, the variable is varied in uniform increments from the specified initial value to the final value. In the special case where you wish to fill a certain number of rows with a constant, enter the starting row, the ending row, and the constant in the 'First value' field. The independent values entered must be in the unit system selected with the :ref:`Units <units>`  command. You can also specify that the values are saturated liquid or vapor states. This simply adds an 'l' or 'v' to the number as it places it in the field, as described in the :ref:`Specified State Points <specifiedstatepoints>`  dialog.


