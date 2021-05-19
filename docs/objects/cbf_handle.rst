cbf_handle_struct
*****************

.. py:class:: cbf_handle_struct

.. py:method:: cbf_handle_struct.new_row()


   cbf_new_row adds a new row to the current category and makes it the
   current row.


.. py:method:: cbf_handle_struct.insert_row(rownumber)


   cbf_insert_row adds a new row to the current category. The new row is
   inserted as row *rownumber* and existing rows starting from
   *rownumber* are moved up by 1. The new row becomes the current row.

   If the category has fewer than *rownumber* rows, the function returns
   CBF_NOTFOUND.

   The row numbers start from 0.

   :param rownumber: The row number of the new row.

.. py:method:: cbf_handle_struct.delete_row(rownumber)


   cbf_delete_row deletes a row from the current category. Rows starting
   from *rownumber* +1 are moved down by 1. If the current row was
   higher than *rownumber*, or if the current row is the last row, it
   will also move down by 1.

   The row numbers start from 0.

   :param rownumber: The number of the row to delete.

.. py:method:: cbf_handle_struct.set_datablockname(datablockname)


   cbf_set_datablockname changes the name of the current data block to
   *datablockname*. cbf_set_saveframename changes the name of the
   current save frame to *saveframename*.

   If a data block or save frame with this name already exists
   (comparison is case-insensitive), the function returns CBF_IDENTICAL.

   :param datablockname: The new save frame name.

.. py:method:: cbf_handle_struct.set_saveframename(saveframename)


   cbf_set_datablockname changes the name of the current data block to
   *datablockname*. cbf_set_saveframename changes the name of the
   current save frame to *saveframename*.

   If a data block or save frame with this name already exists
   (comparison is case-insensitive), the function returns CBF_IDENTICAL.

   :param saveframename:

.. py:method:: cbf_handle_struct.reset_datablocks()


   cbf_reset_datablocks deletes all categories from all data blocks.

   The current data block does not change.


.. py:method:: cbf_handle_struct.reset_datablock()


   cbf_reset_datablock deletes all categories from the current data
   block. cbf_reset_saveframe deletes all categories from the current
   save frame.


.. py:method:: cbf_handle_struct.reset_saveframe()


   cbf_reset_datablock deletes all categories from the current data
   block. cbf_reset_saveframe deletes all categories from the current
   save frame.


.. py:method:: cbf_handle_struct.reset_category()


   cbf_reset_category deletes all columns and rows from current
   category.


.. py:method:: cbf_handle_struct.remove_datablock()


   cbf_remove_datablock deletes the current data block.
   cbf_remove_saveframe deletes the current save frame.

   The current data block becomes undefined.


.. py:method:: cbf_handle_struct.remove_saveframe()


   cbf_remove_datablock deletes the current data block.
   cbf_remove_saveframe deletes the current save frame.

   The current data block becomes undefined.


.. py:method:: cbf_handle_struct.remove_category()


   cbf_remove_category deletes the current category.

   The current category becomes undefined.


.. py:method:: cbf_handle_struct.remove_column()


   cbf_remove_column deletes the current column.

   The current column becomes undefined.


.. py:method:: cbf_handle_struct.free_handle()


   cbf_free_handle destroys the CBF object specified by the *handle* and
   frees all associated memory.


.. py:method:: cbf_handle_struct.remove_row()


   cbf_remove_row deletes the current row in the current category.

   If the current row was the last row, it will move down by 1,
   otherwise, it will remain the same.


.. py:method:: cbf_handle_struct.rewind_datablock()


   cbf_rewind_datablock makes the first data block the current data
   block.

   If there are no data blocks, the function returns CBF_NOTFOUND.

   The current category becomes undefined.


.. py:method:: cbf_handle_struct.rewind_blockitem(type)


   cbf_rewind_category makes the first category in the current data
   block the current category. cbf_rewind_saveframe makes the first
   saveframe in the current data block the current saveframe.
   cbf_rewind_blockitem makes the first blockitem (category or
   saveframe) in the current data block the current blockitem. The type
   of the blockitem (CBF_CATEGORY or CBF_SAVEFRAME) is returned in
   *type*.

   If there are no categories, saveframes or blockitems the function
   returns CBF_NOTFOUND.

   The current column and row become undefined.

   :param type: CBF handle.

.. py:method:: cbf_handle_struct.rewind_category()


   cbf_rewind_category makes the first category in the current data
   block the current category. cbf_rewind_saveframe makes the first
   saveframe in the current data block the current saveframe.
   cbf_rewind_blockitem makes the first blockitem (category or
   saveframe) in the current data block the current blockitem. The type
   of the blockitem (CBF_CATEGORY or CBF_SAVEFRAME) is returned in
   *type*.

   If there are no categories, saveframes or blockitems the function
   returns CBF_NOTFOUND.

   The current column and row become undefined.


.. py:method:: cbf_handle_struct.rewind_saveframe()


   cbf_rewind_category makes the first category in the current data
   block the current category. cbf_rewind_saveframe makes the first
   saveframe in the current data block the current saveframe.
   cbf_rewind_blockitem makes the first blockitem (category or
   saveframe) in the current data block the current blockitem. The type
   of the blockitem (CBF_CATEGORY or CBF_SAVEFRAME) is returned in
   *type*.

   If there are no categories, saveframes or blockitems the function
   returns CBF_NOTFOUND.

   The current column and row become undefined.


.. py:method:: cbf_handle_struct.rewind_column()


   cbf_rewind_column makes the first column in the current category the
   current column.

   If there are no columns, the function returns CBF_NOTFOUND.

   The current row is not affected.


.. py:method:: cbf_handle_struct.rewind_row()


   cbf_rewind_row makes the first row in the current category the
   current row.

   If there are no rows, the function returns CBF_NOTFOUND.

   The current column is not affected.


.. py:method:: cbf_handle_struct.next_datablock()


   cbf_next_datablock makes the data block following the current data
   block the current data block.

   If there are no more data blocks, the function returns CBF_NOTFOUND.

   The current category becomes undefined.


.. py:method:: cbf_handle_struct.next_category()


   cbf_next_category makes the category following the current category
   in the current data block the current category.

   If there are no more categories, the function returns CBF_NOTFOUND.

   The current column and row become undefined.


.. py:method:: cbf_handle_struct.next_column()


   cbf_next_column makes the column following the current column in the
   current category the current column.

   If there are no more columns, the function returns CBF_NOTFOUND.

   The current row is not affected.


.. py:method:: cbf_handle_struct.next_row()


   cbf_next_row makes the row following the current row in the current
   category the current row.

   If there are no more rows, the function returns CBF_NOTFOUND.

   The current column is not affected.


.. py:method:: cbf_handle_struct.find_datablock(datablockname)


   cbf_find_datablock makes the data block with name *datablockname* the
   current data block.

   The comparison is case-insensitive.

   If the data block does not exist, the function returns CBF_NOTFOUND.

   The current category becomes undefined.

   :param datablockname: The name of the data block to find.

.. py:method:: cbf_handle_struct.read_file(file, flags)


   cbf_read_file reads the CBF or CIF file *file* into the CBF object
   specified by *handle*, using the CIF 1.0 convention of 80 character
   lines. cbf_read_widefile reads the CBF or CIF file *file* into the
   CBF object specified by *handle*, using the CIF 1.1 convention of
   2048 character lines. A warning is issued to stderr for ascii lines
   over the limit. No test is performed on binary sections.

   Validation is performed in three ways levels: during the lexical
   scan, during the parse, and, if a dictionary was converted, against
   the value types, value enumerations, categories and parent-child
   relationships specified in the dictionary.

   *flags* controls the interpretation of binary section headers, the
   parsing of brackets constructs and the parsing of treble-quoted
   strings.

   +-------------------------+-------------------------------------------+
   | MSG_DIGEST:             | Instructs CBFlib to check that the digest |
   |                         | of the binary section matches any header  |
   |                         | digest value. If the digests do not       |
   |                         | match, the call will return CBF_FORMAT.   |
   |                         | This evaluation and comparison is delayed |
   |                         | (a "lazy" evaluation) to ensure maximal   |
   |                         | processing efficiency. If an immediately  |
   |                         | evaluation is required, see               |
   |                         | MSG_DIGESTNOW, below.                     |
   +-------------------------+-------------------------------------------+
   | MSG_DIGESTNOW:          | Instructs CBFlib to check that the digest |
   |                         | of the binary section matches any header  |
   |                         | digeste value. If the digests do not      |
   |                         | match, the call will return CBF_FORMAT.   |
   |                         | This evaluation and comparison is         |
   |                         | performed during initial parsing of the   |
   |                         | section to ensure timely error reporting  |
   |                         | at the expense of processing efficiency.  |
   |                         | If a more efficient delayed ("lazy")      |
   |                         | evaluation is required, see MSG_DIGEST,   |
   |                         | above.                                    |
   +-------------------------+-------------------------------------------+
   | MSG_DIGESTWARN:         | Instructs CBFlib to check that the digest |
   |                         | of the binary section matches any header  |
   |                         | digeste value. If the digests do not      |
   |                         | match, a warning message will be sent to  |
   |                         | stderr, but processing will attempt to    |
   |                         | continue. This evaluation and comparison  |
   |                         | is first performed during initial parsing |
   |                         | of the section to ensure timely error     |
   |                         | reporting at the expense of processing    |
   |                         | efficiency. An mismatch of the message    |
   |                         | digest usually indicates a serious error, |
   |                         | but it is sometimes worth continuing      |
   |                         | processing to try to isolate the cause of |
   |                         | the error. **Use this option with         |
   |                         | caution.**                                |
   +-------------------------+-------------------------------------------+
   | MSG_NODIGEST:           | Do not check the digest (default).        |
   +-------------------------+-------------------------------------------+
   | PARSE_BRACKETS:         | Accept DDLm bracket-delimited             |
   |                         | **[item,item,...item]** or                |
   |                         | **{item,item,...item}** or                |
   |                         | **(item,item,...item)** constructs as     |
   |                         | valid, stripping non-quoted embedded      |
   |                         | whitespace and comments. These constructs |
   |                         | may span multiple lines.                  |
   +-------------------------+-------------------------------------------+
   | PARSE_LIBERAL_BRACKETS: | Accept DDLm bracket-delimited             |
   |                         | **[item,item,...item]** or                |
   |                         | **{item,item,...item}** or                |
   |                         | **(item,item,...item)** constructs as     |
   |                         | valid, stripping embedded non-quoted,     |
   |                         | non-separating whitespace and comments.   |
   |                         | These constructs may span multiple lines. |
   |                         | In this case, whitespace may be used as   |
   |                         | an alternative to the comma.              |
   +-------------------------+-------------------------------------------+
   | PARSE_TRIPLE_QUOTES:    | Accept DDLm triple-quoted                 |
   |                         | **"""item,item,...item"""** or            |
   |                         | **'''item,item,...item'''** constructs as |
   |                         | valid, stripping embedded whitespace and  |
   |                         | comments. These constructs may span       |
   |                         | multiple lines. If this flag is set, then |
   |                         | ''' will **not** be interpreted as a      |
   |                         | quoted apoptrophe and """ will **not** be |
   |                         | interpreted as a quoted double quote mark |
   |                         | and                                       |
   +-------------------------+-------------------------------------------+
   | PARSE_NOBRACKETS:       | Do not accept DDLm bracket-delimited      |
   |                         | **[item,item,...item]** or                |
   |                         | **{item,item,...item}** or                |
   |                         | **(item,item,...item)** constructs as     |
   |                         | valid, stripping non-quoted embedded      |
   |                         | whitespace and comments. These constructs |
   |                         | may span multiple lines.                  |
   +-------------------------+-------------------------------------------+
   | PARSE_NOTRIPLE_QUOTES:  | No not accept DDLm triple-quoted          |
   |                         | **"""item,item,...item"""** or            |
   |                         | **'''item,item,...item'''** constructs as |
   |                         | valid, stripping embedded whitespace and  |
   |                         | comments. These constructs may span       |
   |                         | multiple lines. If this flag is set, then |
   |                         | ''' will be interpreted as a quoted       |
   |                         | apostrophe and """ will be interpreted as |
   |                         | a quoted double quote mark.               |
   +-------------------------+-------------------------------------------+

   CBFlib defers reading binary sections as long as possible. In the
   current version of CBFlib, this means that:

   | 1. The file must be a random-access file opened in binary mode
     (fopen ( , "rb")).
   | 2. The program *must not* close the file. CBFlib will close the
     file using fclose ( ) when it is no longer needed.

   These restrictions may change in a future release.

   :param file: Pointer to a file descriptor.
   :param flags:

.. py:method:: cbf_handle_struct.read_widefile(file, flags)


   cbf_read_file reads the CBF or CIF file *file* into the CBF object
   specified by *handle*, using the CIF 1.0 convention of 80 character
   lines. cbf_read_widefile reads the CBF or CIF file *file* into the
   CBF object specified by *handle*, using the CIF 1.1 convention of
   2048 character lines. A warning is issued to stderr for ascii lines
   over the limit. No test is performed on binary sections.

   Validation is performed in three ways levels: during the lexical
   scan, during the parse, and, if a dictionary was converted, against
   the value types, value enumerations, categories and parent-child
   relationships specified in the dictionary.

   *flags* controls the interpretation of binary section headers, the
   parsing of brackets constructs and the parsing of treble-quoted
   strings.

   +-------------------------+-------------------------------------------+
   | MSG_DIGEST:             | Instructs CBFlib to check that the digest |
   |                         | of the binary section matches any header  |
   |                         | digest value. If the digests do not       |
   |                         | match, the call will return CBF_FORMAT.   |
   |                         | This evaluation and comparison is delayed |
   |                         | (a "lazy" evaluation) to ensure maximal   |
   |                         | processing efficiency. If an immediately  |
   |                         | evaluation is required, see               |
   |                         | MSG_DIGESTNOW, below.                     |
   +-------------------------+-------------------------------------------+
   | MSG_DIGESTNOW:          | Instructs CBFlib to check that the digest |
   |                         | of the binary section matches any header  |
   |                         | digeste value. If the digests do not      |
   |                         | match, the call will return CBF_FORMAT.   |
   |                         | This evaluation and comparison is         |
   |                         | performed during initial parsing of the   |
   |                         | section to ensure timely error reporting  |
   |                         | at the expense of processing efficiency.  |
   |                         | If a more efficient delayed ("lazy")      |
   |                         | evaluation is required, see MSG_DIGEST,   |
   |                         | above.                                    |
   +-------------------------+-------------------------------------------+
   | MSG_DIGESTWARN:         | Instructs CBFlib to check that the digest |
   |                         | of the binary section matches any header  |
   |                         | digeste value. If the digests do not      |
   |                         | match, a warning message will be sent to  |
   |                         | stderr, but processing will attempt to    |
   |                         | continue. This evaluation and comparison  |
   |                         | is first performed during initial parsing |
   |                         | of the section to ensure timely error     |
   |                         | reporting at the expense of processing    |
   |                         | efficiency. An mismatch of the message    |
   |                         | digest usually indicates a serious error, |
   |                         | but it is sometimes worth continuing      |
   |                         | processing to try to isolate the cause of |
   |                         | the error. **Use this option with         |
   |                         | caution.**                                |
   +-------------------------+-------------------------------------------+
   | MSG_NODIGEST:           | Do not check the digest (default).        |
   +-------------------------+-------------------------------------------+
   | PARSE_BRACKETS:         | Accept DDLm bracket-delimited             |
   |                         | **[item,item,...item]** or                |
   |                         | **{item,item,...item}** or                |
   |                         | **(item,item,...item)** constructs as     |
   |                         | valid, stripping non-quoted embedded      |
   |                         | whitespace and comments. These constructs |
   |                         | may span multiple lines.                  |
   +-------------------------+-------------------------------------------+
   | PARSE_LIBERAL_BRACKETS: | Accept DDLm bracket-delimited             |
   |                         | **[item,item,...item]** or                |
   |                         | **{item,item,...item}** or                |
   |                         | **(item,item,...item)** constructs as     |
   |                         | valid, stripping embedded non-quoted,     |
   |                         | non-separating whitespace and comments.   |
   |                         | These constructs may span multiple lines. |
   |                         | In this case, whitespace may be used as   |
   |                         | an alternative to the comma.              |
   +-------------------------+-------------------------------------------+
   | PARSE_TRIPLE_QUOTES:    | Accept DDLm triple-quoted                 |
   |                         | **"""item,item,...item"""** or            |
   |                         | **'''item,item,...item'''** constructs as |
   |                         | valid, stripping embedded whitespace and  |
   |                         | comments. These constructs may span       |
   |                         | multiple lines. If this flag is set, then |
   |                         | ''' will **not** be interpreted as a      |
   |                         | quoted apoptrophe and """ will **not** be |
   |                         | interpreted as a quoted double quote mark |
   |                         | and                                       |
   +-------------------------+-------------------------------------------+
   | PARSE_NOBRACKETS:       | Do not accept DDLm bracket-delimited      |
   |                         | **[item,item,...item]** or                |
   |                         | **{item,item,...item}** or                |
   |                         | **(item,item,...item)** constructs as     |
   |                         | valid, stripping non-quoted embedded      |
   |                         | whitespace and comments. These constructs |
   |                         | may span multiple lines.                  |
   +-------------------------+-------------------------------------------+
   | PARSE_NOTRIPLE_QUOTES:  | No not accept DDLm triple-quoted          |
   |                         | **"""item,item,...item"""** or            |
   |                         | **'''item,item,...item'''** constructs as |
   |                         | valid, stripping embedded whitespace and  |
   |                         | comments. These constructs may span       |
   |                         | multiple lines. If this flag is set, then |
   |                         | ''' will be interpreted as a quoted       |
   |                         | apostrophe and """ will be interpreted as |
   |                         | a quoted double quote mark.               |
   +-------------------------+-------------------------------------------+

   CBFlib defers reading binary sections as long as possible. In the
   current version of CBFlib, this means that:

   | 1. The file must be a random-access file opened in binary mode
     (fopen ( , "rb")).
   | 2. The program *must not* close the file. CBFlib will close the
     file using fclose ( ) when it is no longer needed.

   These restrictions may change in a future release.

   :param file: Pointer to a file descriptor.
   :param flags:

.. py:method:: cbf_handle_struct.find_category(categoryname)


   cbf_find_category makes the category in the current data block with
   name *categoryname* the current category.

   The comparison is case-insensitive.

   If the category does not exist, the function returns CBF_NOTFOUND.

   The current column and row become undefined.

   :param categoryname: The name of the category to find.

.. py:method:: cbf_handle_struct.find_column(columnname)


   cbf_find_column makes the columns in the current category with name
   *columnname* the current column.

   The comparison is case-insensitive.

   If the column does not exist, the function returns CBF_NOTFOUND.

   The current row is not affected.

   :param columnname: The name of column to find.

.. py:method:: cbf_handle_struct.find_row(value)


   cbf_find_row makes the first row in the current column with value
   *value* the current row.

   The comparison is case-sensitive.

   If a matching row does not exist, the function returns CBF_NOTFOUND.

   The current column is not affected.

   :param value: The value of the row to find.

.. py:method:: cbf_handle_struct.find_nextrow(value)


   cbf_find_nextrow makes the makes the next row in the current column
   with value *value* the current row. The search starts from the row
   following the last row found with cbf_find_row or cbf_find_nextrow,
   or from the current row if the current row was defined using any
   other function.

   The comparison is case-sensitive.

   If no more matching rows exist, the function returns CBF_NOTFOUND.

   The current column is not affected.

   :param value: the value to search for.

.. py:method:: cbf_handle_struct.count_datablocks(datablocks)


   cbf_count_datablocks puts the number of data blocks in
   \*\ *datablocks* .

   :param datablocks: Pointer to the destination data block count.

.. py:method:: cbf_handle_struct.count_categories(categories)


   cbf_count_categories puts the number of categories in the current
   data block in \*\ *categories*.

   :param categories: Pointer to the destination category count.

.. py:method:: cbf_handle_struct.count_columns(columns)


   cbf_count_columns puts the number of columns in the current category
   in \*\ *columns*.

   :param columns: Pointer to the destination column count.

.. py:method:: cbf_handle_struct.count_rows(rows)


   cbf_count_rows puts the number of rows in the current category in
   \*\ *rows* .

   :param rows: Pointer to the destination row count.

.. py:method:: cbf_handle_struct.select_datablock(datablock)


   cbf_select_datablock selects data block number *datablock* as the
   current data block.

   The first data block is number 0.

   If the data block does not exist, the function returns CBF_NOTFOUND.

   :param datablock: Number of the data block to select.

.. py:method:: cbf_handle_struct.select_category(category)


   cbf_select_category selects category number *category* in the current
   data block as the current category.

   The first category is number 0.

   The current column and row become undefined.

   If the category does not exist, the function returns CBF_NOTFOUND.

   :param category: Number of the category to select.

.. py:method:: cbf_handle_struct.write_file(file, readable, ciforcbf, flags, encoding)


   cbf_write_file writes the CBF object specified by *handle* into the
   file *file*, following CIF 1.0 conventions of 80 character lines.
   cbf_write_widefile writes the CBF object specified by *handle* into
   the file *file*, following CIF 1.1 conventions of 2048 character
   lines. A warning is issued to stderr for ascii lines over the limit,
   and an attempt is made to fold lines to fit. No test is performed on
   binary sections.

   If a dictionary has been provided, aliases will be applied on output.

   Unlike cbf_read_file, the *file* does not have to be random-access.

   If the file is random-access and readable, *readable* can be set to
   non-0 to indicate to CBFlib that the file can be used as a buffer to
   conserve disk space. If the file is not random-access or not
   readable, *readable* must be 0.

   If *readable* is non-0, CBFlib will close the file when it is no
   longer required, otherwise this is the responsibility of the program.

   *ciforcbf* selects the format in which the binary sections are
   written:

   === ===========================
   CIF Write an imgCIF file.
   CBF Write a CBF file (default).
   === ===========================

   *flags* selects the type of header used in CBF binary sections,
   selects whether message digests are generated, and controls the style
   of output. The value of *flags* can be a logical OR of any of:

   +------------------------+--------------------------------------------+
   | MIME_HEADERS           | Use MIME-type headers (default).           |
   +------------------------+--------------------------------------------+
   | MIME_NOHEADERS         | Use a simple ASCII headers.                |
   +------------------------+--------------------------------------------+
   | MSG_DIGEST             | Generate message digests for binary data   |
   |                        | validation.                                |
   +------------------------+--------------------------------------------+
   | MSG_NODIGEST           | Do not generate message digests (default). |
   +------------------------+--------------------------------------------+
   | PARSE_BRACKETS         | Do not convert bracketed strings to text   |
   |                        | fields (default).                          |
   +------------------------+--------------------------------------------+
   | PARSE_LIBERAL_BRACKETS | Do not convert bracketed strings to text   |
   |                        | fields (default).                          |
   +------------------------+--------------------------------------------+
   | PARSE_NOBRACKETS       | Convert bracketed strings to text fields   |
   |                        | (default).                                 |
   +------------------------+--------------------------------------------+
   | PARSE_TRIPLE_QUOTES    | Do not convert triple-quoted strings to    |
   |                        | text fields (default).                     |
   +------------------------+--------------------------------------------+
   | PARSE_NOTRIPLE_QUOTES  | Convert triple-quoted strings to text      |
   |                        | fields (default).                          |
   +------------------------+--------------------------------------------+
   | PAD_1K                 | Pad binary sections with 1023 nulls.       |
   +------------------------+--------------------------------------------+
   | PAD_2K                 | Pad binary sections with 2047 nulls.       |
   +------------------------+--------------------------------------------+
   | PAD_4K                 | Pad binary sections with 4095 nulls.       |
   +------------------------+--------------------------------------------+

   Note that on output, the types "prns&, "brcs" and "bkts" will be
   converted to "text" fields if PARSE_NOBRACKETS has been set *flags*,
   and that the types "tsqs" and "tdqs" will be converted to "text"
   fields if the flag PARSE_NOTRIPLE_QUOTES has been set in the *flags*.
   It is an error to set PARSE_NOBRACKETS and to set either
   PARSE_BRACKETS or PARSE_LIBERAL_BRACKETS. It is an error to set both
   PARSE_NOTRIPLE_QUOTES and PARSE_TRIPLE_QUOTES.

   *encoding* selects the type of encoding used for binary sections and
   the type of line-termination in imgCIF files. The value can be a
   logical OR of any of:

   +--------------+------------------------------------------------------+
   | ENC_BASE64   | Use BASE64 encoding (default).                       |
   +--------------+------------------------------------------------------+
   | ENC_QP       | Use QUOTED-PRINTABLE encoding.                       |
   +--------------+------------------------------------------------------+
   | ENC_BASE8    | Use BASE8 (octal) encoding.                          |
   +--------------+------------------------------------------------------+
   | ENC_BASE10   | Use BASE10 (decimal) encoding.                       |
   +--------------+------------------------------------------------------+
   | ENC_BASE16   | Use BASE16 (hexadecimal) encoding.                   |
   +--------------+------------------------------------------------------+
   | ENC_FORWARD  | For BASE8, BASE10 or BASE16 encoding, map bytes to   |
   |              | words forward (1234) (default on little-endian       |
   |              | machines).                                           |
   +--------------+------------------------------------------------------+
   | ENC_BACKWARD | Map bytes to words backward (4321) (default on       |
   |              | big-endian machines).                                |
   +--------------+------------------------------------------------------+
   | ENC_CRTERM   | Terminate lines with CR.                             |
   +--------------+------------------------------------------------------+
   | ENC_LFTERM   | Terminate lines with LF (default).                   |
   +--------------+------------------------------------------------------+

   :param file: Pointer to a file descriptor.
   :param readable: If non-0: this file is random-access and readable and can be used as a buffer.
   :param ciforcbf: Selects the format in which the binary sections are written (CIF/CBF).
   :param flags:
   :param encoding: Selects the type of encoding used for binary sections and the type of line-termination in imgCIF files.

.. py:method:: cbf_handle_struct.write_widefile(file, readable, ciforcbf, flags, encoding)


   cbf_write_file writes the CBF object specified by *handle* into the
   file *file*, following CIF 1.0 conventions of 80 character lines.
   cbf_write_widefile writes the CBF object specified by *handle* into
   the file *file*, following CIF 1.1 conventions of 2048 character
   lines. A warning is issued to stderr for ascii lines over the limit,
   and an attempt is made to fold lines to fit. No test is performed on
   binary sections.

   If a dictionary has been provided, aliases will be applied on output.

   Unlike cbf_read_file, the *file* does not have to be random-access.

   If the file is random-access and readable, *readable* can be set to
   non-0 to indicate to CBFlib that the file can be used as a buffer to
   conserve disk space. If the file is not random-access or not
   readable, *readable* must be 0.

   If *readable* is non-0, CBFlib will close the file when it is no
   longer required, otherwise this is the responsibility of the program.

   *ciforcbf* selects the format in which the binary sections are
   written:

   === ===========================
   CIF Write an imgCIF file.
   CBF Write a CBF file (default).
   === ===========================

   *flags* selects the type of header used in CBF binary sections,
   selects whether message digests are generated, and controls the style
   of output. The value of *flags* can be a logical OR of any of:

   +------------------------+--------------------------------------------+
   | MIME_HEADERS           | Use MIME-type headers (default).           |
   +------------------------+--------------------------------------------+
   | MIME_NOHEADERS         | Use a simple ASCII headers.                |
   +------------------------+--------------------------------------------+
   | MSG_DIGEST             | Generate message digests for binary data   |
   |                        | validation.                                |
   +------------------------+--------------------------------------------+
   | MSG_NODIGEST           | Do not generate message digests (default). |
   +------------------------+--------------------------------------------+
   | PARSE_BRACKETS         | Do not convert bracketed strings to text   |
   |                        | fields (default).                          |
   +------------------------+--------------------------------------------+
   | PARSE_LIBERAL_BRACKETS | Do not convert bracketed strings to text   |
   |                        | fields (default).                          |
   +------------------------+--------------------------------------------+
   | PARSE_NOBRACKETS       | Convert bracketed strings to text fields   |
   |                        | (default).                                 |
   +------------------------+--------------------------------------------+
   | PARSE_TRIPLE_QUOTES    | Do not convert triple-quoted strings to    |
   |                        | text fields (default).                     |
   +------------------------+--------------------------------------------+
   | PARSE_NOTRIPLE_QUOTES  | Convert triple-quoted strings to text      |
   |                        | fields (default).                          |
   +------------------------+--------------------------------------------+
   | PAD_1K                 | Pad binary sections with 1023 nulls.       |
   +------------------------+--------------------------------------------+
   | PAD_2K                 | Pad binary sections with 2047 nulls.       |
   +------------------------+--------------------------------------------+
   | PAD_4K                 | Pad binary sections with 4095 nulls.       |
   +------------------------+--------------------------------------------+

   Note that on output, the types "prns&, "brcs" and "bkts" will be
   converted to "text" fields if PARSE_NOBRACKETS has been set *flags*,
   and that the types "tsqs" and "tdqs" will be converted to "text"
   fields if the flag PARSE_NOTRIPLE_QUOTES has been set in the *flags*.
   It is an error to set PARSE_NOBRACKETS and to set either
   PARSE_BRACKETS or PARSE_LIBERAL_BRACKETS. It is an error to set both
   PARSE_NOTRIPLE_QUOTES and PARSE_TRIPLE_QUOTES.

   *encoding* selects the type of encoding used for binary sections and
   the type of line-termination in imgCIF files. The value can be a
   logical OR of any of:

   +--------------+------------------------------------------------------+
   | ENC_BASE64   | Use BASE64 encoding (default).                       |
   +--------------+------------------------------------------------------+
   | ENC_QP       | Use QUOTED-PRINTABLE encoding.                       |
   +--------------+------------------------------------------------------+
   | ENC_BASE8    | Use BASE8 (octal) encoding.                          |
   +--------------+------------------------------------------------------+
   | ENC_BASE10   | Use BASE10 (decimal) encoding.                       |
   +--------------+------------------------------------------------------+
   | ENC_BASE16   | Use BASE16 (hexadecimal) encoding.                   |
   +--------------+------------------------------------------------------+
   | ENC_FORWARD  | For BASE8, BASE10 or BASE16 encoding, map bytes to   |
   |              | words forward (1234) (default on little-endian       |
   |              | machines).                                           |
   +--------------+------------------------------------------------------+
   | ENC_BACKWARD | Map bytes to words backward (4321) (default on       |
   |              | big-endian machines).                                |
   +--------------+------------------------------------------------------+
   | ENC_CRTERM   | Terminate lines with CR.                             |
   +--------------+------------------------------------------------------+
   | ENC_LFTERM   | Terminate lines with LF (default).                   |
   +--------------+------------------------------------------------------+

   :param file: Pointer to a file descriptor.
   :param readable: If non-0: this file is random-access and readable and can be used as a buffer.
   :param ciforcbf: Selects the format in which the binary sections are written (CIF/CBF).
   :param flags:
   :param encoding: Selects the type of encoding used for binary sections and the type of line-termination in imgCIF files.

.. py:method:: cbf_handle_struct.select_column(column)


   cbf_select_column selects column number *column* in the current
   category as the current column.

   The first column is number 0.

   The current row is not affected

   If the column does not exist, the function returns CBF_NOTFOUND.

   :param column: Number of the column to select.

.. py:method:: cbf_handle_struct.select_row(row)


   cbf_select_row selects row number *row* in the current category as
   the current row.

   The first row is number 0.

   The current column is not affected

   If the row does not exist, the function returns CBF_NOTFOUND.

   :param row: Number of the row to select.

.. py:method:: cbf_handle_struct.datablock_name(datablockname)


   cbf_datablock_name sets \*\ *datablockname* to point to the name of
   the current data block.

   The data block name will be valid as long as the data block exists
   and has not been renamed.

   The name must not be modified by the program in any way.

   :param datablockname: Pointer to the destination data block name pointer.

.. py:method:: cbf_handle_struct.category_name(categoryname)


   cbf_category_name sets \*\ *categoryname* to point to the name of the
   current category of the current data block.

   The category name will be valid as long as the category exists.

   The name must not be modified by the program in any way.

   :param categoryname: Pointer to the destination category name pointer.

.. py:method:: cbf_handle_struct.column_name(columnname)


   cbf_column_name sets \*\ *columnname* to point to the name of the
   current column of the current category.

   The column name will be valid as long as the column exists.

   The name must not be modified by the program in any way.

   cbf_set_column_name sets the name of the current column to
   *newcolumnname*

   :param columnname: Pointer to the destination column name pointer.

.. py:method:: cbf_handle_struct.set_column_name(newcolumnname)


   cbf_column_name sets \*\ *columnname* to point to the name of the
   current column of the current category.

   The column name will be valid as long as the column exists.

   The name must not be modified by the program in any way.

   cbf_set_column_name sets the name of the current column to
   *newcolumnname*

   :param newcolumnname: New column name pointer.

.. py:method:: cbf_handle_struct.row_number(row)


   cbf_row_number sets \*\ *row* to the number of the current row of the
   current category.

   :param row: Pointer to the destination row number.

.. py:method:: cbf_handle_struct.get_value(value)


   cbf_get_value sets \*\ *value* to point to the ASCII value of the
   item at the current column and row. cbf_require_value sets
   \*\ *value* to point to the ASCII value of the item at the current
   column and row, creating the data item if necessary and initializing
   it to a copy of *defaultvalue*.

   If the value is not ASCII, the function returns CBF_BINARY.

   The value will be valid as long as the item exists and has not been
   set to a new value.

   The value must not be modified by the program in any way.

   :param value: Pointer to the destination value pointer.

.. py:method:: cbf_handle_struct.require_value(value, defaultvalue)


   cbf_get_value sets \*\ *value* to point to the ASCII value of the
   item at the current column and row. cbf_require_value sets
   \*\ *value* to point to the ASCII value of the item at the current
   column and row, creating the data item if necessary and initializing
   it to a copy of *defaultvalue*.

   If the value is not ASCII, the function returns CBF_BINARY.

   The value will be valid as long as the item exists and has not been
   set to a new value.

   The value must not be modified by the program in any way.

   :param value: Pointer to the destination value pointer.
   :param defaultvalue: Default value character string.

.. py:method:: cbf_handle_struct.set_value(value)


   cbf_set_value sets the item at the current column and row to the
   ASCII value *value*.

   :param value: ASCII value.

.. py:method:: cbf_handle_struct.get_typeofvalue(typeofvalue)


   cbf_get_value sets \*\ *typeofvalue* to point an ASCII descriptor of
   the value of the item at the current column and row. The strings that
   may be returned are:

   ====== ==============================================================
   "null" for a null value indicated by a "." or a "?"
   "bnry" for a binary value
   "word" for an unquoted string
   "dblq" for a double-quoted string
   "sglq" for a single-quoted string
   "text" for a semicolon-quoted string (multiline text field)
   "prns" for a parenthesis-bracketed string (multiline text field)
   "brcs" for a brace-bracketed string (multiline text field)
   "bkts" for a square-bracket-bracketed string (multiline text field)
   "tsqs" for a treble-single-quote quoted string (multiline text field)
   "tdqs" for a treble-double-quote quoted string (multiline text field)
   ====== ==============================================================

   Not all types are valid for all type of CIF files. In partcular the
   types "prns", "brcs", "bkts" were introduced with DDLm and are not
   valid in DDL1 or DDL2 CIFS. The types "tsqs" and "tdqs" are not
   formally part of the CIF syntax. A field for which no value has been
   set sets \*\ *typeofvalue* to NULL rather than to the string "null".

   The *typeofvalue* must not be modified by the program in any way.

   :param typeofvalue: Pointer to the destination type-of-value string pointer.

.. py:method:: cbf_handle_struct.set_typeofvalue(typeofvalue)


   cbf_set_typeofvalue sets the type of the item at the current column
   and row to the type specified by the ASCII character string given by
   *typeofvalue*. The strings that may be used are:

   ====== ==============================================================
   "null" for a null value indicated by a "." or a "?"
   "bnry" for a binary value
   "word" for an unquoted string
   "dblq" for a double-quoted string
   "sglq" for a single-quoted string
   "text" for a semicolon-quoted string (multiline text field)
   "prns" for a parenthesis-bracketed string (multiline text field)
   "brcs" for a brace-bracketed string (multiline text field)
   "bkts" for a square-bracket-bracketed string (multiline text field)
   "tsqs" for a treble-single-quote quoted string (multiline text field)
   "tdqs" for a treble-double-quote quoted string (multiline text field)
   ====== ==============================================================

   Not all types may be used for all values. Not all types are valid for
   all type of CIF files. In partcular the types "prns", "brcs", "bkts"
   were introduced with DDLm and are not valid in DDL1 or DDL2 CIFS. The
   types "tsqs" and "tdqs" are not formally part of the CIF syntax. No
   changes may be made to the type of binary values. You may not set the
   type of a string that contains a single quote followed by a blank or
   a tab or which contains multiple lines to "sglq". You may not set the
   type of a string that contains a double quote followed by a blank or
   a tab or which contains multiple lines to "dblq".

   :param typeofvalue: ASCII string for desired type of value.

.. py:method:: cbf_handle_struct.new_datablock(datablockname)


   cbf_new_datablock creates a new data block with name *datablockname*
   and makes it the current data block. cbf_new_saveframe creates a new
   save frame with name *saveframename* within the current data block
   and makes the new save frame the current save frame.

   If a data block or save frame with this name already exists, the
   existing data block or save frame becomes the current data block or
   save frame.

   :param datablockname: The name of the new data block.

.. py:method:: cbf_handle_struct.new_saveframe(saveframename)


   cbf_new_datablock creates a new data block with name *datablockname*
   and makes it the current data block. cbf_new_saveframe creates a new
   save frame with name *saveframename* within the current data block
   and makes the new save frame the current save frame.

   If a data block or save frame with this name already exists, the
   existing data block or save frame becomes the current data block or
   save frame.

   :param saveframename: The name of the new save frame.

.. py:method:: cbf_handle_struct.get_integervalue(number)


   cbf_get_integervalue sets \*\ *number* to the value of the ASCII item
   at the current column and row interpreted as a decimal integer.
   cbf_require_integervalue sets \*\ *number* to the value of the ASCII
   item at the current column and row interpreted as a decimal integer,
   setting it to *defaultvalue* if necessary.

   If the value is not ASCII, the function returns CBF_BINARY.

   :param number: pointer to the number.

.. py:method:: cbf_handle_struct.require_integervalue(number, defaultvalue)


   cbf_get_integervalue sets \*\ *number* to the value of the ASCII item
   at the current column and row interpreted as a decimal integer.
   cbf_require_integervalue sets \*\ *number* to the value of the ASCII
   item at the current column and row interpreted as a decimal integer,
   setting it to *defaultvalue* if necessary.

   If the value is not ASCII, the function returns CBF_BINARY.

   :param number: pointer to the number.
   :param defaultvalue: default number value.

.. py:method:: cbf_handle_struct.set_integervalue(number)


   cbf_set_integervalue sets the item at the current column and row to
   the integer value *number* written as a decimal ASCII string.

   :param number: Integer value.

.. py:method:: cbf_handle_struct.get_doublevalue(number)


   cbf_get_doublevalue sets \*\ *number* to the value of the ASCII item
   at the current column and row interpreted as a decimal floating-point
   number. cbf_require_doublevalue sets \*\ *number* to the value of the
   ASCII item at the current column and row interpreted as a decimal
   floating-point number, setting it to *defaultvalue* if necessary.

   If the value is not ASCII, the function returns CBF_BINARY.

   :param number: Pointer to the destination number.

.. py:method:: cbf_handle_struct.require_doublevalue(number, defaultvalue)


   cbf_get_doublevalue sets \*\ *number* to the value of the ASCII item
   at the current column and row interpreted as a decimal floating-point
   number. cbf_require_doublevalue sets \*\ *number* to the value of the
   ASCII item at the current column and row interpreted as a decimal
   floating-point number, setting it to *defaultvalue* if necessary.

   If the value is not ASCII, the function returns CBF_BINARY.

   :param number: Pointer to the destination number.
   :param defaultvalue: default number value.

.. py:method:: cbf_handle_struct.set_doublevalue(format, number)


   cbf_set_doublevalue sets the item at the current column and row to
   the floating-point value *number* written as an ASCII string with the
   format specified by *format* as appropriate for the printf function.

   :param format: Format for the number.
   :param number: Floating-point value.

.. py:method:: cbf_handle_struct.get_integerarrayparameters(compression, binary_id, elsize, elsigned, elunsigned, elements, minelement, maxelement)


   cbf_get_integerarrayparameters sets \*\ *compression*,
   \*\ *binary_id*, \*\ *elsize*, \*\ *elsigned*, \*\ *elunsigned*,
   \*\ *elements*, \*\ *minelement* and \*\ *maxelement* to values read
   from the binary value of the item at the current column and row. This
   provides all the arguments needed for a subsequent call to
   cbf_set_integerarray, if a copy of the array is to be made into
   another CIF or CBF. cbf_get_realarrayparameters sets
   \*\ *compression*, \*\ *binary_id*, \*\ *elsize*, \*\ *elements* to
   values read from the binary value of the item at the current column
   and row. This provides all the arguments needed for a subsequent call
   to cbf_set_realarray, if a copy of the arry is to be made into
   another CIF or CBF.

   The variants cbf_get_integerarrayparameters_wdims,
   cbf_get_integerarrayparameters_wdims_fs,
   cbf_get_integerarrayparameters_wdims_sf,
   cbf_get_realarrayparameters_wdims,
   cbf_get_realarrayparameters_wdims_fs,
   cbf_get_realarrayparameters_wdims_sf set \*\*\ *byteorder*,
   \*\ *dimfast*, \*\ *dimmid*, \*\ *dimslow*, and \*\ *padding* as
   well, providing the additional parameters needed for a subsequent
   call to cbf_set_integerarray_wdims or cbf_set_realarray_wdims.

   The value returned in \*\ *byteorder* is a pointer either to the
   string "little_endian" or to the string "big_endian". This should be
   the byte order of the data, not necessarily of the host machine. No
   attempt should be made to modify this string. At this time only
   "little_endian" will be returned.

   The values returned in \*\ *dimfast*, \*\ *dimmid* and \*\ *dimslow*
   are the sizes of the fastest changing, second fastest changing and
   third fastest changing dimensions of the array, if specified, or
   zero, if not specified.

   The value returned in \*\ *padding* is the size of the post-data
   padding, if any and if specified in the data header. The value is
   given as a count of octets.

   If the value is not binary, the function returns CBF_ASCII.

   :param compression: Compression method used.
   :param binary_id: Pointer to the destination integer binary identifier.
   :param elsize: Size in bytes of each array element.
   :param elsigned: Pointer to an integer.  Set to 1 if the elements can be read as signed integers.
   :param elunsigned: Pointer to an integer.  Set to 1 if the elements can be read as unsigned integers.
   :param elements: Pointer to the destination number of elements.
   :param minelement: Pointer to the destination smallest element.
   :param maxelement: Pointer to the destination largest element.

.. py:method:: cbf_handle_struct.get_integerarrayparameters_wdims(compression, binary_id, elsize, elsigned, elunsigned, elements, minelement, maxelement, byteorder, dimfast, dimmid, dimslow, padding)


   cbf_get_integerarrayparameters sets \*\ *compression*,
   \*\ *binary_id*, \*\ *elsize*, \*\ *elsigned*, \*\ *elunsigned*,
   \*\ *elements*, \*\ *minelement* and \*\ *maxelement* to values read
   from the binary value of the item at the current column and row. This
   provides all the arguments needed for a subsequent call to
   cbf_set_integerarray, if a copy of the array is to be made into
   another CIF or CBF. cbf_get_realarrayparameters sets
   \*\ *compression*, \*\ *binary_id*, \*\ *elsize*, \*\ *elements* to
   values read from the binary value of the item at the current column
   and row. This provides all the arguments needed for a subsequent call
   to cbf_set_realarray, if a copy of the arry is to be made into
   another CIF or CBF.

   The variants cbf_get_integerarrayparameters_wdims,
   cbf_get_integerarrayparameters_wdims_fs,
   cbf_get_integerarrayparameters_wdims_sf,
   cbf_get_realarrayparameters_wdims,
   cbf_get_realarrayparameters_wdims_fs,
   cbf_get_realarrayparameters_wdims_sf set \*\*\ *byteorder*,
   \*\ *dimfast*, \*\ *dimmid*, \*\ *dimslow*, and \*\ *padding* as
   well, providing the additional parameters needed for a subsequent
   call to cbf_set_integerarray_wdims or cbf_set_realarray_wdims.

   The value returned in \*\ *byteorder* is a pointer either to the
   string "little_endian" or to the string "big_endian". This should be
   the byte order of the data, not necessarily of the host machine. No
   attempt should be made to modify this string. At this time only
   "little_endian" will be returned.

   The values returned in \*\ *dimfast*, \*\ *dimmid* and \*\ *dimslow*
   are the sizes of the fastest changing, second fastest changing and
   third fastest changing dimensions of the array, if specified, or
   zero, if not specified.

   The value returned in \*\ *padding* is the size of the post-data
   padding, if any and if specified in the data header. The value is
   given as a count of octets.

   If the value is not binary, the function returns CBF_ASCII.

   :param compression: Compression method used.
   :param binary_id: Pointer to the destination integer binary identifier.
   :param elsize: Size in bytes of each array element.
   :param elsigned: Pointer to an integer.  Set to 1 if the elements can be read as signed integers.
   :param elunsigned: Pointer to an integer.  Set to 1 if the elements can be read as unsigned integers.
   :param elements: Pointer to the destination number of elements.
   :param minelement: Pointer to the destination smallest element.
   :param maxelement: Pointer to the destination largest element.
   :param byteorder: Pointer to the destination byte order.
   :param dimfast: Pointer to the destination fastest dimension.
   :param dimmid: Pointer to the destination second fastest dimension.
   :param dimslow: Pointer to the destination third fastest dimension.
   :param padding: Pointer to the destination padding size.

.. py:method:: cbf_handle_struct.get_integerarrayparameters_wdims_fs(compression, binary_id, elsize, elsigned, elunsigned, elements, minelement, maxelement, byteorder, dimfast, dimmid, dimslow, padding)


   cbf_get_integerarrayparameters sets \*\ *compression*,
   \*\ *binary_id*, \*\ *elsize*, \*\ *elsigned*, \*\ *elunsigned*,
   \*\ *elements*, \*\ *minelement* and \*\ *maxelement* to values read
   from the binary value of the item at the current column and row. This
   provides all the arguments needed for a subsequent call to
   cbf_set_integerarray, if a copy of the array is to be made into
   another CIF or CBF. cbf_get_realarrayparameters sets
   \*\ *compression*, \*\ *binary_id*, \*\ *elsize*, \*\ *elements* to
   values read from the binary value of the item at the current column
   and row. This provides all the arguments needed for a subsequent call
   to cbf_set_realarray, if a copy of the arry is to be made into
   another CIF or CBF.

   The variants cbf_get_integerarrayparameters_wdims,
   cbf_get_integerarrayparameters_wdims_fs,
   cbf_get_integerarrayparameters_wdims_sf,
   cbf_get_realarrayparameters_wdims,
   cbf_get_realarrayparameters_wdims_fs,
   cbf_get_realarrayparameters_wdims_sf set \*\*\ *byteorder*,
   \*\ *dimfast*, \*\ *dimmid*, \*\ *dimslow*, and \*\ *padding* as
   well, providing the additional parameters needed for a subsequent
   call to cbf_set_integerarray_wdims or cbf_set_realarray_wdims.

   The value returned in \*\ *byteorder* is a pointer either to the
   string "little_endian" or to the string "big_endian". This should be
   the byte order of the data, not necessarily of the host machine. No
   attempt should be made to modify this string. At this time only
   "little_endian" will be returned.

   The values returned in \*\ *dimfast*, \*\ *dimmid* and \*\ *dimslow*
   are the sizes of the fastest changing, second fastest changing and
   third fastest changing dimensions of the array, if specified, or
   zero, if not specified.

   The value returned in \*\ *padding* is the size of the post-data
   padding, if any and if specified in the data header. The value is
   given as a count of octets.

   If the value is not binary, the function returns CBF_ASCII.

   :param compression: Compression method used.
   :param binary_id: Pointer to the destination integer binary identifier.
   :param elsize: Size in bytes of each array element.
   :param elsigned: Pointer to an integer.  Set to 1 if the elements can be read as signed integers.
   :param elunsigned: Pointer to an integer.  Set to 1 if the elements can be read as unsigned integers.
   :param elements: Pointer to the destination number of elements.
   :param minelement: Pointer to the destination smallest element.
   :param maxelement: Pointer to the destination largest element.
   :param byteorder: Pointer to the destination byte order.
   :param dimfast: Pointer to the destination fastest dimension.
   :param dimmid: Pointer to the destination second fastest dimension.
   :param dimslow: Pointer to the destination third fastest dimension.
   :param padding: Pointer to the destination padding size.

.. py:method:: cbf_handle_struct.get_integerarrayparameters_wdims_sf(compression, binary_id, elsize, elsigned, elunsigned, elements, minelement, maxelement, byteorder, dimslow, dimmid, dimfast, padding)


   cbf_get_integerarrayparameters sets \*\ *compression*,
   \*\ *binary_id*, \*\ *elsize*, \*\ *elsigned*, \*\ *elunsigned*,
   \*\ *elements*, \*\ *minelement* and \*\ *maxelement* to values read
   from the binary value of the item at the current column and row. This
   provides all the arguments needed for a subsequent call to
   cbf_set_integerarray, if a copy of the array is to be made into
   another CIF or CBF. cbf_get_realarrayparameters sets
   \*\ *compression*, \*\ *binary_id*, \*\ *elsize*, \*\ *elements* to
   values read from the binary value of the item at the current column
   and row. This provides all the arguments needed for a subsequent call
   to cbf_set_realarray, if a copy of the arry is to be made into
   another CIF or CBF.

   The variants cbf_get_integerarrayparameters_wdims,
   cbf_get_integerarrayparameters_wdims_fs,
   cbf_get_integerarrayparameters_wdims_sf,
   cbf_get_realarrayparameters_wdims,
   cbf_get_realarrayparameters_wdims_fs,
   cbf_get_realarrayparameters_wdims_sf set \*\*\ *byteorder*,
   \*\ *dimfast*, \*\ *dimmid*, \*\ *dimslow*, and \*\ *padding* as
   well, providing the additional parameters needed for a subsequent
   call to cbf_set_integerarray_wdims or cbf_set_realarray_wdims.

   The value returned in \*\ *byteorder* is a pointer either to the
   string "little_endian" or to the string "big_endian". This should be
   the byte order of the data, not necessarily of the host machine. No
   attempt should be made to modify this string. At this time only
   "little_endian" will be returned.

   The values returned in \*\ *dimfast*, \*\ *dimmid* and \*\ *dimslow*
   are the sizes of the fastest changing, second fastest changing and
   third fastest changing dimensions of the array, if specified, or
   zero, if not specified.

   The value returned in \*\ *padding* is the size of the post-data
   padding, if any and if specified in the data header. The value is
   given as a count of octets.

   If the value is not binary, the function returns CBF_ASCII.

   :param compression: Compression method used.
   :param binary_id: Pointer to the destination integer binary identifier.
   :param elsize: Size in bytes of each array element.
   :param elsigned: Pointer to an integer.  Set to 1 if the elements can be read as signed integers.
   :param elunsigned: Pointer to an integer.  Set to 1 if the elements can be read as unsigned integers.
   :param elements: Pointer to the destination number of elements.
   :param minelement: Pointer to the destination smallest element.
   :param maxelement: Pointer to the destination largest element.
   :param byteorder: Pointer to the destination byte order.
   :param dimslow: Pointer to the destination third fastest dimension.
   :param dimmid: Pointer to the destination second fastest dimension.
   :param dimfast: Pointer to the destination fastest dimension.
   :param padding: Pointer to the destination padding size.

.. py:method:: cbf_handle_struct.get_realarrayparameters(compression, binary_id, elsize, elements)


   cbf_get_integerarrayparameters sets \*\ *compression*,
   \*\ *binary_id*, \*\ *elsize*, \*\ *elsigned*, \*\ *elunsigned*,
   \*\ *elements*, \*\ *minelement* and \*\ *maxelement* to values read
   from the binary value of the item at the current column and row. This
   provides all the arguments needed for a subsequent call to
   cbf_set_integerarray, if a copy of the array is to be made into
   another CIF or CBF. cbf_get_realarrayparameters sets
   \*\ *compression*, \*\ *binary_id*, \*\ *elsize*, \*\ *elements* to
   values read from the binary value of the item at the current column
   and row. This provides all the arguments needed for a subsequent call
   to cbf_set_realarray, if a copy of the arry is to be made into
   another CIF or CBF.

   The variants cbf_get_integerarrayparameters_wdims,
   cbf_get_integerarrayparameters_wdims_fs,
   cbf_get_integerarrayparameters_wdims_sf,
   cbf_get_realarrayparameters_wdims,
   cbf_get_realarrayparameters_wdims_fs,
   cbf_get_realarrayparameters_wdims_sf set \*\*\ *byteorder*,
   \*\ *dimfast*, \*\ *dimmid*, \*\ *dimslow*, and \*\ *padding* as
   well, providing the additional parameters needed for a subsequent
   call to cbf_set_integerarray_wdims or cbf_set_realarray_wdims.

   The value returned in \*\ *byteorder* is a pointer either to the
   string "little_endian" or to the string "big_endian". This should be
   the byte order of the data, not necessarily of the host machine. No
   attempt should be made to modify this string. At this time only
   "little_endian" will be returned.

   The values returned in \*\ *dimfast*, \*\ *dimmid* and \*\ *dimslow*
   are the sizes of the fastest changing, second fastest changing and
   third fastest changing dimensions of the array, if specified, or
   zero, if not specified.

   The value returned in \*\ *padding* is the size of the post-data
   padding, if any and if specified in the data header. The value is
   given as a count of octets.

   If the value is not binary, the function returns CBF_ASCII.

   :param compression: Compression method used.
   :param binary_id: Pointer to the destination integer binary identifier.
   :param elsize: Size in bytes of each array element.
   :param elements: Pointer to the destination number of elements.

.. py:method:: cbf_handle_struct.get_realarrayparameters_wdims(compression, binary_id, elsize, elements, byteorder, dimfast, dimmid, dimslow, padding)


   cbf_get_integerarrayparameters sets \*\ *compression*,
   \*\ *binary_id*, \*\ *elsize*, \*\ *elsigned*, \*\ *elunsigned*,
   \*\ *elements*, \*\ *minelement* and \*\ *maxelement* to values read
   from the binary value of the item at the current column and row. This
   provides all the arguments needed for a subsequent call to
   cbf_set_integerarray, if a copy of the array is to be made into
   another CIF or CBF. cbf_get_realarrayparameters sets
   \*\ *compression*, \*\ *binary_id*, \*\ *elsize*, \*\ *elements* to
   values read from the binary value of the item at the current column
   and row. This provides all the arguments needed for a subsequent call
   to cbf_set_realarray, if a copy of the arry is to be made into
   another CIF or CBF.

   The variants cbf_get_integerarrayparameters_wdims,
   cbf_get_integerarrayparameters_wdims_fs,
   cbf_get_integerarrayparameters_wdims_sf,
   cbf_get_realarrayparameters_wdims,
   cbf_get_realarrayparameters_wdims_fs,
   cbf_get_realarrayparameters_wdims_sf set \*\*\ *byteorder*,
   \*\ *dimfast*, \*\ *dimmid*, \*\ *dimslow*, and \*\ *padding* as
   well, providing the additional parameters needed for a subsequent
   call to cbf_set_integerarray_wdims or cbf_set_realarray_wdims.

   The value returned in \*\ *byteorder* is a pointer either to the
   string "little_endian" or to the string "big_endian". This should be
   the byte order of the data, not necessarily of the host machine. No
   attempt should be made to modify this string. At this time only
   "little_endian" will be returned.

   The values returned in \*\ *dimfast*, \*\ *dimmid* and \*\ *dimslow*
   are the sizes of the fastest changing, second fastest changing and
   third fastest changing dimensions of the array, if specified, or
   zero, if not specified.

   The value returned in \*\ *padding* is the size of the post-data
   padding, if any and if specified in the data header. The value is
   given as a count of octets.

   If the value is not binary, the function returns CBF_ASCII.

   :param compression: Compression method used.
   :param binary_id: Pointer to the destination integer binary identifier.
   :param elsize: Size in bytes of each array element.
   :param elements: Pointer to the destination number of elements.
   :param byteorder: Pointer to the destination byte order.
   :param dimfast: Pointer to the destination fastest dimension.
   :param dimmid: Pointer to the destination second fastest dimension.
   :param dimslow: Pointer to the destination third fastest dimension.
   :param padding: Pointer to the destination padding size.

.. py:method:: cbf_handle_struct.get_realarrayparameters_wdims_fs(compression, binary_id, elsize, elements, byteorder, dimfast, dimmid, dimslow, padding)


   cbf_get_integerarrayparameters sets \*\ *compression*,
   \*\ *binary_id*, \*\ *elsize*, \*\ *elsigned*, \*\ *elunsigned*,
   \*\ *elements*, \*\ *minelement* and \*\ *maxelement* to values read
   from the binary value of the item at the current column and row. This
   provides all the arguments needed for a subsequent call to
   cbf_set_integerarray, if a copy of the array is to be made into
   another CIF or CBF. cbf_get_realarrayparameters sets
   \*\ *compression*, \*\ *binary_id*, \*\ *elsize*, \*\ *elements* to
   values read from the binary value of the item at the current column
   and row. This provides all the arguments needed for a subsequent call
   to cbf_set_realarray, if a copy of the arry is to be made into
   another CIF or CBF.

   The variants cbf_get_integerarrayparameters_wdims,
   cbf_get_integerarrayparameters_wdims_fs,
   cbf_get_integerarrayparameters_wdims_sf,
   cbf_get_realarrayparameters_wdims,
   cbf_get_realarrayparameters_wdims_fs,
   cbf_get_realarrayparameters_wdims_sf set \*\*\ *byteorder*,
   \*\ *dimfast*, \*\ *dimmid*, \*\ *dimslow*, and \*\ *padding* as
   well, providing the additional parameters needed for a subsequent
   call to cbf_set_integerarray_wdims or cbf_set_realarray_wdims.

   The value returned in \*\ *byteorder* is a pointer either to the
   string "little_endian" or to the string "big_endian". This should be
   the byte order of the data, not necessarily of the host machine. No
   attempt should be made to modify this string. At this time only
   "little_endian" will be returned.

   The values returned in \*\ *dimfast*, \*\ *dimmid* and \*\ *dimslow*
   are the sizes of the fastest changing, second fastest changing and
   third fastest changing dimensions of the array, if specified, or
   zero, if not specified.

   The value returned in \*\ *padding* is the size of the post-data
   padding, if any and if specified in the data header. The value is
   given as a count of octets.

   If the value is not binary, the function returns CBF_ASCII.

   :param compression: Compression method used.
   :param binary_id: Pointer to the destination integer binary identifier.
   :param elsize: Size in bytes of each array element.
   :param elements: Pointer to the destination number of elements.
   :param byteorder: Pointer to the destination byte order.
   :param dimfast: Pointer to the destination fastest dimension.
   :param dimmid: Pointer to the destination second fastest dimension.
   :param dimslow: Pointer to the destination third fastest dimension.
   :param padding: Pointer to the destination padding size.

.. py:method:: cbf_handle_struct.get_realarrayparameters_wdims_sf(compression, binary_id, elsize, elements, byteorder, dimslow, dimmid, dimfast, padding)


   cbf_get_integerarrayparameters sets \*\ *compression*,
   \*\ *binary_id*, \*\ *elsize*, \*\ *elsigned*, \*\ *elunsigned*,
   \*\ *elements*, \*\ *minelement* and \*\ *maxelement* to values read
   from the binary value of the item at the current column and row. This
   provides all the arguments needed for a subsequent call to
   cbf_set_integerarray, if a copy of the array is to be made into
   another CIF or CBF. cbf_get_realarrayparameters sets
   \*\ *compression*, \*\ *binary_id*, \*\ *elsize*, \*\ *elements* to
   values read from the binary value of the item at the current column
   and row. This provides all the arguments needed for a subsequent call
   to cbf_set_realarray, if a copy of the arry is to be made into
   another CIF or CBF.

   The variants cbf_get_integerarrayparameters_wdims,
   cbf_get_integerarrayparameters_wdims_fs,
   cbf_get_integerarrayparameters_wdims_sf,
   cbf_get_realarrayparameters_wdims,
   cbf_get_realarrayparameters_wdims_fs,
   cbf_get_realarrayparameters_wdims_sf set \*\*\ *byteorder*,
   \*\ *dimfast*, \*\ *dimmid*, \*\ *dimslow*, and \*\ *padding* as
   well, providing the additional parameters needed for a subsequent
   call to cbf_set_integerarray_wdims or cbf_set_realarray_wdims.

   The value returned in \*\ *byteorder* is a pointer either to the
   string "little_endian" or to the string "big_endian". This should be
   the byte order of the data, not necessarily of the host machine. No
   attempt should be made to modify this string. At this time only
   "little_endian" will be returned.

   The values returned in \*\ *dimfast*, \*\ *dimmid* and \*\ *dimslow*
   are the sizes of the fastest changing, second fastest changing and
   third fastest changing dimensions of the array, if specified, or
   zero, if not specified.

   The value returned in \*\ *padding* is the size of the post-data
   padding, if any and if specified in the data header. The value is
   given as a count of octets.

   If the value is not binary, the function returns CBF_ASCII.

   :param compression: Compression method used.
   :param binary_id: Pointer to the destination integer binary identifier.
   :param elsize: Size in bytes of each array element.
   :param elements: Pointer to the destination number of elements.
   :param byteorder: Pointer to the destination byte order.
   :param dimslow: Pointer to the destination third fastest dimension.
   :param dimmid: Pointer to the destination second fastest dimension.
   :param dimfast: Pointer to the destination fastest dimension.
   :param padding: Pointer to the destination padding size.

.. py:method:: cbf_handle_struct.get_integerarray(binary_id, array, elsize, elsigned, elements, elements_read)


   cbf_get_integerarray reads the binary value of the item at the
   current column and row into an integer array. The array consists of
   *elements* elements of *elsize* bytes each, starting at *array*. The
   elements are signed if *elsigned* is non-0 and unsigned otherwise.
   \*\ *binary_id* is set to the binary section identifier and
   \*\ *elements_read* to the number of elements actually read.
   cbf_get_realarray reads the binary value of the item at the current
   column and row into a real array. The array consists of *elements*
   elements of *elsize* bytes each, starting at *array*. \*\ *binary_id*
   is set to the binary section identifier and \*\ *elements_read* to
   the number of elements actually read.

   If any element in the integer binary data cant fit into the
   destination element, the destination is set the nearest possible
   value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination array must consist of chars, shorts or
   ints (signed or unsigned). If *elsize* is not equal to sizeof (char),
   sizeof (short) or sizeof (int), for cbf_get_integerarray, or
   sizeof(double) or sizeof(float), for cbf_get_realarray the function
   returns CBF_ARGUMENT.

   An additional restriction in the current version of CBFlib is that
   values too large to fit in an int are not correctly decompressed. As
   an example, if the machine with 32-bit ints is reading an array
   containing a value outside the range 0 .. 2^\ :sup:`32`-1 (unsigned)
   or -2^\ :sup:`31` .. 2^\ :sup:`31`-1 (signed), the array will not be
   correctly decompressed. This restriction will be removed in a future
   release. For cbf_get_realarray, only IEEE format is supported. No
   conversion to other floating point formats is done at this time.

   :param binary_id: Pointer to the destination integer binary identifier.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param elsigned: Set to non-0 if the destination array elements are signed.
   :param elements: The number of elements to read.
   :param elements_read: Pointer to the destination number of elements actually read.

.. py:method:: cbf_handle_struct.get_realarray(binary_id, array, elsize, elements, elements_read)


   cbf_get_integerarray reads the binary value of the item at the
   current column and row into an integer array. The array consists of
   *elements* elements of *elsize* bytes each, starting at *array*. The
   elements are signed if *elsigned* is non-0 and unsigned otherwise.
   \*\ *binary_id* is set to the binary section identifier and
   \*\ *elements_read* to the number of elements actually read.
   cbf_get_realarray reads the binary value of the item at the current
   column and row into a real array. The array consists of *elements*
   elements of *elsize* bytes each, starting at *array*. \*\ *binary_id*
   is set to the binary section identifier and \*\ *elements_read* to
   the number of elements actually read.

   If any element in the integer binary data cant fit into the
   destination element, the destination is set the nearest possible
   value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination array must consist of chars, shorts or
   ints (signed or unsigned). If *elsize* is not equal to sizeof (char),
   sizeof (short) or sizeof (int), for cbf_get_integerarray, or
   sizeof(double) or sizeof(float), for cbf_get_realarray the function
   returns CBF_ARGUMENT.

   An additional restriction in the current version of CBFlib is that
   values too large to fit in an int are not correctly decompressed. As
   an example, if the machine with 32-bit ints is reading an array
   containing a value outside the range 0 .. 2^\ :sup:`32`-1 (unsigned)
   or -2^\ :sup:`31` .. 2^\ :sup:`31`-1 (signed), the array will not be
   correctly decompressed. This restriction will be removed in a future
   release. For cbf_get_realarray, only IEEE format is supported. No
   conversion to other floating point formats is done at this time.

   :param binary_id: Pointer to the destination integer binary identifier.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param elements: The number of elements to read.
   :param elements_read: Pointer to the destination number of elements actually read.

.. py:method:: cbf_handle_struct.set_integerarray(compression, binary_id, array, elsize, elsigned, elements)


   cbf_set_integerarray sets the binary value of the item at the current
   column and row to an integer *array*. The array consists of
   *elements* elements of *elsize* bytes each, starting at *array*. The
   elements are signed if *elsigned* is non-0 and unsigned otherwise.
   *binary_id* is the binary section identifier. cbf_set_realarray sets
   the binary value of the item at the current column and row to an
   integer *array*. The array consists of *elements* elements of
   *elsize* bytes each, starting at *array*. *binary_id* is the binary
   section identifier.

   The cbf_set_integerarray_wdims, cbf_set_integerarray_wdims_fs,
   cbf_set_integerarray_wdims_sf, cbf_set_realarray_wdims,
   cbf_set_realarray_wdims_fs and cbf_set_realarray_wdims_sf variants
   allow the data header values of *byteorder*, *dimfast*, *dimmid*,
   *dimslow* and *padding* to be set to the data byte order, the
   fastest, second fastest and third fastest array dimensions and the
   size in byte of the post data padding to be used.

   The array will be compressed using the compression scheme specifed by
   *compression*. Currently, the available schemes are:

   +-----------------------------------+-----------------------------------+
   | CBF_CANONICAL                     | Canonical-code compression        |
   |                                   | (section 3.3.1)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED                        | CCP4-style packing (section       |
   |                                   | 3.3.2)                            |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED_V2                     | CCP4-style packing, version 2     |
   |                                   | (section 3.3.2)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_BYTE_OFFSET                   | Simple "byte_offset" compression. |
   +-----------------------------------+-----------------------------------+
   | CBF_NIBBLE_OFFSET                 | Simple "nibble_offset"            |
   |                                   | compression.                      |
   +-----------------------------------+-----------------------------------+
   | CBF_NONE                          | No compression. NOTE: This scheme |
   |                                   | is by far the slowest of the four |
   |                                   | and uses much more disk space. It |
   |                                   | is intended for routine use with  |
   |                                   | small arrays only. With large     |
   |                                   | arrays (like images) it should be |
   |                                   | used only for debugging.          |
   +-----------------------------------+-----------------------------------+

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source array must consist of chars, shorts or ints
   (signed or unsigned), for cbf_set_integerarray, or IEEE doubles or
   floats for cbf_set_realarray. If *elsize* is not equal to sizeof
   (char), sizeof (short) or sizeof (int), the function returns
   CBF_ARGUMENT.

   :param compression: Compression method to use.
   :param binary_id: Integer binary identifier.
   :param array: Pointer to the source array.
   :param elsize: Size in bytes of each source array element.
   :param elsigned: Set to non-0 if the source array elements are signed. elements: The number of elements in the array.
   :param elements:

.. py:method:: cbf_handle_struct.set_integerarray_wdims(compression, binary_id, array, elsize, elsigned, elements, byteorder, dimfast, dimmid, dimslow, padding)


   cbf_set_integerarray sets the binary value of the item at the current
   column and row to an integer *array*. The array consists of
   *elements* elements of *elsize* bytes each, starting at *array*. The
   elements are signed if *elsigned* is non-0 and unsigned otherwise.
   *binary_id* is the binary section identifier. cbf_set_realarray sets
   the binary value of the item at the current column and row to an
   integer *array*. The array consists of *elements* elements of
   *elsize* bytes each, starting at *array*. *binary_id* is the binary
   section identifier.

   The cbf_set_integerarray_wdims, cbf_set_integerarray_wdims_fs,
   cbf_set_integerarray_wdims_sf, cbf_set_realarray_wdims,
   cbf_set_realarray_wdims_fs and cbf_set_realarray_wdims_sf variants
   allow the data header values of *byteorder*, *dimfast*, *dimmid*,
   *dimslow* and *padding* to be set to the data byte order, the
   fastest, second fastest and third fastest array dimensions and the
   size in byte of the post data padding to be used.

   The array will be compressed using the compression scheme specifed by
   *compression*. Currently, the available schemes are:

   +-----------------------------------+-----------------------------------+
   | CBF_CANONICAL                     | Canonical-code compression        |
   |                                   | (section 3.3.1)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED                        | CCP4-style packing (section       |
   |                                   | 3.3.2)                            |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED_V2                     | CCP4-style packing, version 2     |
   |                                   | (section 3.3.2)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_BYTE_OFFSET                   | Simple "byte_offset" compression. |
   +-----------------------------------+-----------------------------------+
   | CBF_NIBBLE_OFFSET                 | Simple "nibble_offset"            |
   |                                   | compression.                      |
   +-----------------------------------+-----------------------------------+
   | CBF_NONE                          | No compression. NOTE: This scheme |
   |                                   | is by far the slowest of the four |
   |                                   | and uses much more disk space. It |
   |                                   | is intended for routine use with  |
   |                                   | small arrays only. With large     |
   |                                   | arrays (like images) it should be |
   |                                   | used only for debugging.          |
   +-----------------------------------+-----------------------------------+

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source array must consist of chars, shorts or ints
   (signed or unsigned), for cbf_set_integerarray, or IEEE doubles or
   floats for cbf_set_realarray. If *elsize* is not equal to sizeof
   (char), sizeof (short) or sizeof (int), the function returns
   CBF_ARGUMENT.

   :param compression: Compression method to use.
   :param binary_id: Integer binary identifier.
   :param array: Pointer to the source array.
   :param elsize: Size in bytes of each source array element.
   :param elsigned: Set to non-0 if the source array elements are signed. elements: The number of elements in the array.
   :param elements:
   :param byteorder:
   :param dimfast:
   :param dimmid:
   :param dimslow:
   :param padding:

.. py:method:: cbf_handle_struct.set_integerarray_wdims_fs(compression, binary_id, array, elsize, elsigned, elements, byteorder, dimfast, dimmid, dimslow, padding)


   cbf_set_integerarray sets the binary value of the item at the current
   column and row to an integer *array*. The array consists of
   *elements* elements of *elsize* bytes each, starting at *array*. The
   elements are signed if *elsigned* is non-0 and unsigned otherwise.
   *binary_id* is the binary section identifier. cbf_set_realarray sets
   the binary value of the item at the current column and row to an
   integer *array*. The array consists of *elements* elements of
   *elsize* bytes each, starting at *array*. *binary_id* is the binary
   section identifier.

   The cbf_set_integerarray_wdims, cbf_set_integerarray_wdims_fs,
   cbf_set_integerarray_wdims_sf, cbf_set_realarray_wdims,
   cbf_set_realarray_wdims_fs and cbf_set_realarray_wdims_sf variants
   allow the data header values of *byteorder*, *dimfast*, *dimmid*,
   *dimslow* and *padding* to be set to the data byte order, the
   fastest, second fastest and third fastest array dimensions and the
   size in byte of the post data padding to be used.

   The array will be compressed using the compression scheme specifed by
   *compression*. Currently, the available schemes are:

   +-----------------------------------+-----------------------------------+
   | CBF_CANONICAL                     | Canonical-code compression        |
   |                                   | (section 3.3.1)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED                        | CCP4-style packing (section       |
   |                                   | 3.3.2)                            |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED_V2                     | CCP4-style packing, version 2     |
   |                                   | (section 3.3.2)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_BYTE_OFFSET                   | Simple "byte_offset" compression. |
   +-----------------------------------+-----------------------------------+
   | CBF_NIBBLE_OFFSET                 | Simple "nibble_offset"            |
   |                                   | compression.                      |
   +-----------------------------------+-----------------------------------+
   | CBF_NONE                          | No compression. NOTE: This scheme |
   |                                   | is by far the slowest of the four |
   |                                   | and uses much more disk space. It |
   |                                   | is intended for routine use with  |
   |                                   | small arrays only. With large     |
   |                                   | arrays (like images) it should be |
   |                                   | used only for debugging.          |
   +-----------------------------------+-----------------------------------+

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source array must consist of chars, shorts or ints
   (signed or unsigned), for cbf_set_integerarray, or IEEE doubles or
   floats for cbf_set_realarray. If *elsize* is not equal to sizeof
   (char), sizeof (short) or sizeof (int), the function returns
   CBF_ARGUMENT.

   :param compression: Compression method to use.
   :param binary_id: Integer binary identifier.
   :param array: Pointer to the source array.
   :param elsize: Size in bytes of each source array element.
   :param elsigned: Set to non-0 if the source array elements are signed. elements: The number of elements in the array.
   :param elements:
   :param byteorder:
   :param dimfast:
   :param dimmid:
   :param dimslow:
   :param padding:

.. py:method:: cbf_handle_struct.set_integerarray_wdims_sf(compression, binary_id, array, elsize, elsigned, elements, byteorder, dimslow, dimmid, dimfast, padding)


   cbf_set_integerarray sets the binary value of the item at the current
   column and row to an integer *array*. The array consists of
   *elements* elements of *elsize* bytes each, starting at *array*. The
   elements are signed if *elsigned* is non-0 and unsigned otherwise.
   *binary_id* is the binary section identifier. cbf_set_realarray sets
   the binary value of the item at the current column and row to an
   integer *array*. The array consists of *elements* elements of
   *elsize* bytes each, starting at *array*. *binary_id* is the binary
   section identifier.

   The cbf_set_integerarray_wdims, cbf_set_integerarray_wdims_fs,
   cbf_set_integerarray_wdims_sf, cbf_set_realarray_wdims,
   cbf_set_realarray_wdims_fs and cbf_set_realarray_wdims_sf variants
   allow the data header values of *byteorder*, *dimfast*, *dimmid*,
   *dimslow* and *padding* to be set to the data byte order, the
   fastest, second fastest and third fastest array dimensions and the
   size in byte of the post data padding to be used.

   The array will be compressed using the compression scheme specifed by
   *compression*. Currently, the available schemes are:

   +-----------------------------------+-----------------------------------+
   | CBF_CANONICAL                     | Canonical-code compression        |
   |                                   | (section 3.3.1)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED                        | CCP4-style packing (section       |
   |                                   | 3.3.2)                            |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED_V2                     | CCP4-style packing, version 2     |
   |                                   | (section 3.3.2)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_BYTE_OFFSET                   | Simple "byte_offset" compression. |
   +-----------------------------------+-----------------------------------+
   | CBF_NIBBLE_OFFSET                 | Simple "nibble_offset"            |
   |                                   | compression.                      |
   +-----------------------------------+-----------------------------------+
   | CBF_NONE                          | No compression. NOTE: This scheme |
   |                                   | is by far the slowest of the four |
   |                                   | and uses much more disk space. It |
   |                                   | is intended for routine use with  |
   |                                   | small arrays only. With large     |
   |                                   | arrays (like images) it should be |
   |                                   | used only for debugging.          |
   +-----------------------------------+-----------------------------------+

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source array must consist of chars, shorts or ints
   (signed or unsigned), for cbf_set_integerarray, or IEEE doubles or
   floats for cbf_set_realarray. If *elsize* is not equal to sizeof
   (char), sizeof (short) or sizeof (int), the function returns
   CBF_ARGUMENT.

   :param compression: Compression method to use.
   :param binary_id: Integer binary identifier.
   :param array: Pointer to the source array.
   :param elsize: Size in bytes of each source array element.
   :param elsigned: Set to non-0 if the source array elements are signed. elements: The number of elements in the array.
   :param elements:
   :param byteorder:
   :param dimslow:
   :param dimmid:
   :param dimfast:
   :param padding:

.. py:method:: cbf_handle_struct.set_realarray(compression, binary_id, array, elsize, elements)


   cbf_set_integerarray sets the binary value of the item at the current
   column and row to an integer *array*. The array consists of
   *elements* elements of *elsize* bytes each, starting at *array*. The
   elements are signed if *elsigned* is non-0 and unsigned otherwise.
   *binary_id* is the binary section identifier. cbf_set_realarray sets
   the binary value of the item at the current column and row to an
   integer *array*. The array consists of *elements* elements of
   *elsize* bytes each, starting at *array*. *binary_id* is the binary
   section identifier.

   The cbf_set_integerarray_wdims, cbf_set_integerarray_wdims_fs,
   cbf_set_integerarray_wdims_sf, cbf_set_realarray_wdims,
   cbf_set_realarray_wdims_fs and cbf_set_realarray_wdims_sf variants
   allow the data header values of *byteorder*, *dimfast*, *dimmid*,
   *dimslow* and *padding* to be set to the data byte order, the
   fastest, second fastest and third fastest array dimensions and the
   size in byte of the post data padding to be used.

   The array will be compressed using the compression scheme specifed by
   *compression*. Currently, the available schemes are:

   +-----------------------------------+-----------------------------------+
   | CBF_CANONICAL                     | Canonical-code compression        |
   |                                   | (section 3.3.1)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED                        | CCP4-style packing (section       |
   |                                   | 3.3.2)                            |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED_V2                     | CCP4-style packing, version 2     |
   |                                   | (section 3.3.2)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_BYTE_OFFSET                   | Simple "byte_offset" compression. |
   +-----------------------------------+-----------------------------------+
   | CBF_NIBBLE_OFFSET                 | Simple "nibble_offset"            |
   |                                   | compression.                      |
   +-----------------------------------+-----------------------------------+
   | CBF_NONE                          | No compression. NOTE: This scheme |
   |                                   | is by far the slowest of the four |
   |                                   | and uses much more disk space. It |
   |                                   | is intended for routine use with  |
   |                                   | small arrays only. With large     |
   |                                   | arrays (like images) it should be |
   |                                   | used only for debugging.          |
   +-----------------------------------+-----------------------------------+

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source array must consist of chars, shorts or ints
   (signed or unsigned), for cbf_set_integerarray, or IEEE doubles or
   floats for cbf_set_realarray. If *elsize* is not equal to sizeof
   (char), sizeof (short) or sizeof (int), the function returns
   CBF_ARGUMENT.

   :param compression: Compression method to use.
   :param binary_id: Integer binary identifier.
   :param array: Pointer to the source array.
   :param elsize: Size in bytes of each source array element.
   :param elements:

.. py:method:: cbf_handle_struct.set_realarray_wdims(compression, binary_id, array, elsize, elements, byteorder, dimfast, dimmid, dimslow, padding)


   cbf_set_integerarray sets the binary value of the item at the current
   column and row to an integer *array*. The array consists of
   *elements* elements of *elsize* bytes each, starting at *array*. The
   elements are signed if *elsigned* is non-0 and unsigned otherwise.
   *binary_id* is the binary section identifier. cbf_set_realarray sets
   the binary value of the item at the current column and row to an
   integer *array*. The array consists of *elements* elements of
   *elsize* bytes each, starting at *array*. *binary_id* is the binary
   section identifier.

   The cbf_set_integerarray_wdims, cbf_set_integerarray_wdims_fs,
   cbf_set_integerarray_wdims_sf, cbf_set_realarray_wdims,
   cbf_set_realarray_wdims_fs and cbf_set_realarray_wdims_sf variants
   allow the data header values of *byteorder*, *dimfast*, *dimmid*,
   *dimslow* and *padding* to be set to the data byte order, the
   fastest, second fastest and third fastest array dimensions and the
   size in byte of the post data padding to be used.

   The array will be compressed using the compression scheme specifed by
   *compression*. Currently, the available schemes are:

   +-----------------------------------+-----------------------------------+
   | CBF_CANONICAL                     | Canonical-code compression        |
   |                                   | (section 3.3.1)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED                        | CCP4-style packing (section       |
   |                                   | 3.3.2)                            |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED_V2                     | CCP4-style packing, version 2     |
   |                                   | (section 3.3.2)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_BYTE_OFFSET                   | Simple "byte_offset" compression. |
   +-----------------------------------+-----------------------------------+
   | CBF_NIBBLE_OFFSET                 | Simple "nibble_offset"            |
   |                                   | compression.                      |
   +-----------------------------------+-----------------------------------+
   | CBF_NONE                          | No compression. NOTE: This scheme |
   |                                   | is by far the slowest of the four |
   |                                   | and uses much more disk space. It |
   |                                   | is intended for routine use with  |
   |                                   | small arrays only. With large     |
   |                                   | arrays (like images) it should be |
   |                                   | used only for debugging.          |
   +-----------------------------------+-----------------------------------+

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source array must consist of chars, shorts or ints
   (signed or unsigned), for cbf_set_integerarray, or IEEE doubles or
   floats for cbf_set_realarray. If *elsize* is not equal to sizeof
   (char), sizeof (short) or sizeof (int), the function returns
   CBF_ARGUMENT.

   :param compression: Compression method to use.
   :param binary_id: Integer binary identifier.
   :param array: Pointer to the source array.
   :param elsize: Size in bytes of each source array element.
   :param elements:
   :param byteorder:
   :param dimfast:
   :param dimmid:
   :param dimslow:
   :param padding:

.. py:method:: cbf_handle_struct.set_realarray_wdims_fs(compression, binary_id, array, elsize, elements, byteorder, dimfast, dimmid, dimslow, padding)


   cbf_set_integerarray sets the binary value of the item at the current
   column and row to an integer *array*. The array consists of
   *elements* elements of *elsize* bytes each, starting at *array*. The
   elements are signed if *elsigned* is non-0 and unsigned otherwise.
   *binary_id* is the binary section identifier. cbf_set_realarray sets
   the binary value of the item at the current column and row to an
   integer *array*. The array consists of *elements* elements of
   *elsize* bytes each, starting at *array*. *binary_id* is the binary
   section identifier.

   The cbf_set_integerarray_wdims, cbf_set_integerarray_wdims_fs,
   cbf_set_integerarray_wdims_sf, cbf_set_realarray_wdims,
   cbf_set_realarray_wdims_fs and cbf_set_realarray_wdims_sf variants
   allow the data header values of *byteorder*, *dimfast*, *dimmid*,
   *dimslow* and *padding* to be set to the data byte order, the
   fastest, second fastest and third fastest array dimensions and the
   size in byte of the post data padding to be used.

   The array will be compressed using the compression scheme specifed by
   *compression*. Currently, the available schemes are:

   +-----------------------------------+-----------------------------------+
   | CBF_CANONICAL                     | Canonical-code compression        |
   |                                   | (section 3.3.1)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED                        | CCP4-style packing (section       |
   |                                   | 3.3.2)                            |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED_V2                     | CCP4-style packing, version 2     |
   |                                   | (section 3.3.2)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_BYTE_OFFSET                   | Simple "byte_offset" compression. |
   +-----------------------------------+-----------------------------------+
   | CBF_NIBBLE_OFFSET                 | Simple "nibble_offset"            |
   |                                   | compression.                      |
   +-----------------------------------+-----------------------------------+
   | CBF_NONE                          | No compression. NOTE: This scheme |
   |                                   | is by far the slowest of the four |
   |                                   | and uses much more disk space. It |
   |                                   | is intended for routine use with  |
   |                                   | small arrays only. With large     |
   |                                   | arrays (like images) it should be |
   |                                   | used only for debugging.          |
   +-----------------------------------+-----------------------------------+

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source array must consist of chars, shorts or ints
   (signed or unsigned), for cbf_set_integerarray, or IEEE doubles or
   floats for cbf_set_realarray. If *elsize* is not equal to sizeof
   (char), sizeof (short) or sizeof (int), the function returns
   CBF_ARGUMENT.

   :param compression: Compression method to use.
   :param binary_id: Integer binary identifier.
   :param array: Pointer to the source array.
   :param elsize: Size in bytes of each source array element.
   :param elements:
   :param byteorder:
   :param dimfast:
   :param dimmid:
   :param dimslow:
   :param padding:

.. py:method:: cbf_handle_struct.set_realarray_wdims_sf(compression, binary_id, array, elsize, elements, byteorder, dimslow, dimmid, dimfast, padding)


   cbf_set_integerarray sets the binary value of the item at the current
   column and row to an integer *array*. The array consists of
   *elements* elements of *elsize* bytes each, starting at *array*. The
   elements are signed if *elsigned* is non-0 and unsigned otherwise.
   *binary_id* is the binary section identifier. cbf_set_realarray sets
   the binary value of the item at the current column and row to an
   integer *array*. The array consists of *elements* elements of
   *elsize* bytes each, starting at *array*. *binary_id* is the binary
   section identifier.

   The cbf_set_integerarray_wdims, cbf_set_integerarray_wdims_fs,
   cbf_set_integerarray_wdims_sf, cbf_set_realarray_wdims,
   cbf_set_realarray_wdims_fs and cbf_set_realarray_wdims_sf variants
   allow the data header values of *byteorder*, *dimfast*, *dimmid*,
   *dimslow* and *padding* to be set to the data byte order, the
   fastest, second fastest and third fastest array dimensions and the
   size in byte of the post data padding to be used.

   The array will be compressed using the compression scheme specifed by
   *compression*. Currently, the available schemes are:

   +-----------------------------------+-----------------------------------+
   | CBF_CANONICAL                     | Canonical-code compression        |
   |                                   | (section 3.3.1)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED                        | CCP4-style packing (section       |
   |                                   | 3.3.2)                            |
   +-----------------------------------+-----------------------------------+
   | CBF_PACKED_V2                     | CCP4-style packing, version 2     |
   |                                   | (section 3.3.2)                   |
   +-----------------------------------+-----------------------------------+
   | CBF_BYTE_OFFSET                   | Simple "byte_offset" compression. |
   +-----------------------------------+-----------------------------------+
   | CBF_NIBBLE_OFFSET                 | Simple "nibble_offset"            |
   |                                   | compression.                      |
   +-----------------------------------+-----------------------------------+
   | CBF_NONE                          | No compression. NOTE: This scheme |
   |                                   | is by far the slowest of the four |
   |                                   | and uses much more disk space. It |
   |                                   | is intended for routine use with  |
   |                                   | small arrays only. With large     |
   |                                   | arrays (like images) it should be |
   |                                   | used only for debugging.          |
   +-----------------------------------+-----------------------------------+

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source array must consist of chars, shorts or ints
   (signed or unsigned), for cbf_set_integerarray, or IEEE doubles or
   floats for cbf_set_realarray. If *elsize* is not equal to sizeof
   (char), sizeof (short) or sizeof (int), the function returns
   CBF_ARGUMENT.

   :param compression: Compression method to use.
   :param binary_id: Integer binary identifier.
   :param array: Pointer to the source array.
   :param elsize: Size in bytes of each source array element.
   :param elements:
   :param byteorder:
   :param dimslow:
   :param dimmid:
   :param dimfast:
   :param padding:

.. py:method:: cbf_handle_struct.require_datablock(datablockname)


   cbf_require_datablock makes the data block with name *datablockname*
   the current data block, if it exists, or creates it if it does not.

   The comparison is case-insensitive.

   The current category becomes undefined.

   :param datablockname: The name of the data block to find or create.

.. py:method:: cbf_handle_struct.force_new_datablock(datablockname)


   cbf_force_new_datablock creates a new data block with name
   *datablockname* and makes it the current data block. Duplicate data
   block names are allowed. cbf_force_new_saveframe creates a new savew
   frame with name *saveframename* and makes it the current save frame.
   Duplicate save frame names are allowed.

   Even if a save frame with this name already exists, a new save frame
   is created and becomes the current save frame.

   :param datablockname: The name of the new data block.

.. py:method:: cbf_handle_struct.force_new_saveframe(saveframename)


   cbf_force_new_datablock creates a new data block with name
   *datablockname* and makes it the current data block. Duplicate data
   block names are allowed. cbf_force_new_saveframe creates a new savew
   frame with name *saveframename* and makes it the current save frame.
   Duplicate save frame names are allowed.

   Even if a save frame with this name already exists, a new save frame
   is created and becomes the current save frame.

   :param saveframename: The name of the new save frame.

.. py:method:: cbf_handle_struct.require_category(categoryname)


   cbf_rewuire_category makes the category in the current data block
   with name *categoryname* the current category, if it exists, or
   creates the catagory if it does not exist.

   The comparison is case-insensitive.

   The current column and row become undefined.

   :param categoryname: The name of the category to find.

.. py:method:: cbf_handle_struct.require_column(columnname)


   cbf_require_column makes the columns in the current category with
   name *columnname* the current column, if it exists, or creates it if
   it does not.

   The comparison is case-insensitive.

   The current row is not affected.

   :param columnname: The name of column to find.

.. py:method:: cbf_handle_struct.require_column_value(columnname, value, defaultvalue)


   cbf_require_column_doublevalue sets \*\ *value* to the ASCII item at
   the current row for the column given with the name given by
   \*\ *columnname*, or to the string given by *defaultvalue* if the
   item cannot be found.

   :param columnname: Name of the column containing the number.
   :param value: pointer to the location to receive the value.
   :param defaultvalue: Value to use if the requested column and value cannot be found.

.. py:method:: cbf_handle_struct.require_column_integervalue(columnname, number, defaultvalue)


   cbf_require_column_doublevalue sets \*\ *number* to the value of the
   ASCII item at the current row for the column given with the name
   given by \*\ *columnname*, with the value interpreted as an integer
   number, or to the number given by *defaultvalue* if the item cannot
   be found.

   :param columnname: Name of the column containing the number.
   :param number: pointer to the location to receive the integer value.
   :param defaultvalue: Value to use if the requested column and value cannot be found.

.. py:method:: cbf_handle_struct.require_column_doublevalue(columnname, number, defaultvalue)


   cbf_require_column_doublevalue sets \*\ *number* to the value of the
   ASCII item at the current row for the column given with the name
   given by \*\ *columnname*, with the value interpreted as a decimal
   floating-point number, or to the number given by *defaultvalue* if
   the item cannot be found.

   :param columnname: Name of the column containing the number.
   :param number: pointer to the location to receive the floating-point value.
   :param defaultvalue: Value to use if the requested column and value cannot be found.

.. py:method:: cbf_handle_struct.get_dictionary(dictionary)


   cbf_get_dictionary sets \*\ *dictionary* to the handle of a CBF which
   has been associated with the CBF *handle* by cbf_set_dictionary.
   cbf_set_dictionary associates the CBF handle *dictionary_in* with
   *handle* as its dictionary. cbf_require_dictionary sets
   \*\ *dictionary* to the handle of a CBF which has been associated
   with the CBF *handle* by cbf_set_dictionary or creates a new empty
   CBF and associates it with *handle*, returning the new handle in
   \*\ *dictionary*.

   :param dictionary: Pointer to CBF handle of dictionary.

.. py:method:: cbf_handle_struct.require_dictionary(dictionary)


   cbf_get_dictionary sets \*\ *dictionary* to the handle of a CBF which
   has been associated with the CBF *handle* by cbf_set_dictionary.
   cbf_set_dictionary associates the CBF handle *dictionary_in* with
   *handle* as its dictionary. cbf_require_dictionary sets
   \*\ *dictionary* to the handle of a CBF which has been associated
   with the CBF *handle* by cbf_set_dictionary or creates a new empty
   CBF and associates it with *handle*, returning the new handle in
   \*\ *dictionary*.

   :param dictionary: Pointer to CBF handle of dictionary.

.. py:method:: cbf_handle_struct.set_dictionary(dictionary_in)


   cbf_get_dictionary sets \*\ *dictionary* to the handle of a CBF which
   has been associated with the CBF *handle* by cbf_set_dictionary.
   cbf_set_dictionary associates the CBF handle *dictionary_in* with
   *handle* as its dictionary. cbf_require_dictionary sets
   \*\ *dictionary* to the handle of a CBF which has been associated
   with the CBF *handle* by cbf_set_dictionary or creates a new empty
   CBF and associates it with *handle*, returning the new handle in
   \*\ *dictionary*.

   :param dictionary_in: CBF handle of dcitionary.

.. py:method:: cbf_handle_struct.convert_dictionary(dictionary)


   cbf_convert_dictionary converts *dictionary* as a DDL1 or DDL2
   dictionary to a CBF dictionary of category and item properties for
   *handle*, creating a new dictionary if none exists or layering the
   definitions in *dictionary* onto the existing dictionary of *handle*
   if one exists.

   If a CBF is read into *handle* after calling cbf_convert_dictionary,
   then the dictionary will be used for validation of the CBF as it is
   read.

   :param dictionary: CBF handle of dictionary.

.. py:method:: cbf_handle_struct.find_local_tag(tag)


   cbf_find_tag searches all of the CBF *handle* for the CIF tag given
   by the string *tag* and makes it the current tag. The search does not
   include the dictionary, but does include save frames as well as
   categories.

   The string *tag* is the complete tag in either DDL1 or DDL2 format,
   starting with the leading underscore, not just a category or column.

   :param tag: CIF tag.

.. py:method:: cbf_handle_struct.find_tag(tag)


   cbf_find_tag searches all of the CBF *handle* for the CIF tag given
   by the string *tag* and makes it the current tag. The search does not
   include the dictionary, but does include save frames as well as
   categories.

   The string *tag* is the complete tag in either DDL1 or DDL2 format,
   starting with the leading underscore, not just a category or column.

   :param tag: CIF tag.

.. py:method:: cbf_handle_struct.find_category_root(categoryname, categoryroot)


   cbf_find_category_root sets \*\ *categoryroot* to the root category
   of which *categoryname* is an alias. cbf_set_category_root sets
   *categoryname_in* as an alias of *categoryroot* in the dictionary
   associated with *handle*, creating the dictionary if necessary.
   cbf_require_category_root sets \*\ *categoryroot* to the root
   category of which *categoryname* is an alias, if there is one, or to
   the value of *categoryname*, if *categoryname* is not an alias.

   A returned *categoryroot* string must not be modified in any way.

   :param categoryname: category name which may be an alias.
   :param categoryroot: pointer to a returned category root name.

.. py:method:: cbf_handle_struct.require_category_root(categoryname, categoryroot)


   cbf_find_category_root sets \*\ *categoryroot* to the root category
   of which *categoryname* is an alias. cbf_set_category_root sets
   *categoryname_in* as an alias of *categoryroot* in the dictionary
   associated with *handle*, creating the dictionary if necessary.
   cbf_require_category_root sets \*\ *categoryroot* to the root
   category of which *categoryname* is an alias, if there is one, or to
   the value of *categoryname*, if *categoryname* is not an alias.

   A returned *categoryroot* string must not be modified in any way.

   :param categoryname: category name which may be an alias.
   :param categoryroot: pointer to a returned category root name.

.. py:method:: cbf_handle_struct.set_category_root(categoryname_in, categoryroot)


   cbf_find_category_root sets \*\ *categoryroot* to the root category
   of which *categoryname* is an alias. cbf_set_category_root sets
   *categoryname_in* as an alias of *categoryroot* in the dictionary
   associated with *handle*, creating the dictionary if necessary.
   cbf_require_category_root sets \*\ *categoryroot* to the root
   category of which *categoryname* is an alias, if there is one, or to
   the value of *categoryname*, if *categoryname* is not an alias.

   A returned *categoryroot* string must not be modified in any way.

   :param categoryname_in:
   :param categoryroot: pointer to a returned category root name.

.. py:method:: cbf_handle_struct.new_category(categoryname)


   cbf_new_category creates a new category in the current data block
   with name *categoryname* and makes it the current category.

   If a category with this name already exists, the existing category
   becomes the current category.

   :param categoryname: The name of the new category.

.. py:method:: cbf_handle_struct.find_tag_root(tagname, tagroot)


   cbf_find_tag_root sets \*\ *tagroot* to the root tag of which
   *tagname* is an alias. cbf_set_tag_root sets *tagname* as an alias of
   *tagroot_in* in the dictionary associated with *handle*, creating the
   dictionary if necessary. cbf_require_tag_root sets \*\ *tagroot* to
   the root tag of which *tagname* is an alias, if there is one, or to
   the value of *tagname*, if *tagname* is not an alias.

   A returned *tagroot* string must not be modified in any way.

   :param tagname: tag name which may be an alias.
   :param tagroot: pointer to a returned tag root name.

.. py:method:: cbf_handle_struct.require_tag_root(tagname, tagroot)


   cbf_find_tag_root sets \*\ *tagroot* to the root tag of which
   *tagname* is an alias. cbf_set_tag_root sets *tagname* as an alias of
   *tagroot_in* in the dictionary associated with *handle*, creating the
   dictionary if necessary. cbf_require_tag_root sets \*\ *tagroot* to
   the root tag of which *tagname* is an alias, if there is one, or to
   the value of *tagname*, if *tagname* is not an alias.

   A returned *tagroot* string must not be modified in any way.

   :param tagname: tag name which may be an alias.
   :param tagroot: pointer to a returned tag root name.

.. py:method:: cbf_handle_struct.set_tag_root(tagname, tagroot_in)


   cbf_find_tag_root sets \*\ *tagroot* to the root tag of which
   *tagname* is an alias. cbf_set_tag_root sets *tagname* as an alias of
   *tagroot_in* in the dictionary associated with *handle*, creating the
   dictionary if necessary. cbf_require_tag_root sets \*\ *tagroot* to
   the root tag of which *tagname* is an alias, if there is one, or to
   the value of *tagname*, if *tagname* is not an alias.

   A returned *tagroot* string must not be modified in any way.

   :param tagname: tag name which may be an alias.
   :param tagroot_in: input tag root name.

.. py:method:: cbf_handle_struct.find_tag_category(tagname, categoryname)


   cbf_find_tag_category sets *categoryname* to the category associated
   with *tagname* in the dictionary associated with *handle*.
   cbf_set_tag_category upddates the dictionary associated with *handle*
   to indicated that *tagname* is in category *categoryname_in*.

   :param tagname: tag name.
   :param categoryname: pointer to a returned category name.

.. py:method:: cbf_handle_struct.set_tag_category(tagname, categoryname_in)


   cbf_find_tag_category sets *categoryname* to the category associated
   with *tagname* in the dictionary associated with *handle*.
   cbf_set_tag_category upddates the dictionary associated with *handle*
   to indicated that *tagname* is in category *categoryname_in*.

   :param tagname: tag name.
   :param categoryname_in: input category name.

.. py:method:: cbf_handle_struct.force_new_category(categoryname)


   cbf_force_new_category creates a new category in the current data
   block with name *categoryname* and makes it the current category.
   Duplicate category names are allowed.

   Even if a category with this name already exists, a new category of
   the same name is created and becomes the current category. The allows
   for the creation of unlooped tag/value lists drawn from the same
   category.

   :param categoryname: The name of the new category.

.. py:method:: cbf_handle_struct.new_column(columnname)


   cbf_new_column creates a new column in the current category with name
   *columnname* and makes it the current column.

   If a column with this name already exists, the existing column
   becomes the current category.

   :param columnname: The name of the new column.

.. py:method:: cbf_handle_struct.read_template(file)


   cbf_read_template reads the CBF or CIF file *file* into the CBF
   object specified by *handle* and selects the first datablock as the
   current datablock.

   :param file: Pointer to a file descriptor.

.. py:method:: cbf_handle_struct.get_divergence(div_x_source, div_y_source, div_x_y_source)


   cbf_get_divergence sets \*\ *div_x_source*, \*\ *div_y_source* and
   \*\ *div_x_y_source* to the corresponding source divergence
   parameters.

   Any of the destination pointers may be NULL.

   :param div_x_source: Pointer to the destination div_x_source.
   :param div_y_source: Pointer to the destination div_y_source.
   :param div_x_y_source: Pointer to the destination div_x_y_source.

.. py:method:: cbf_handle_struct.set_divergence(div_x_source, div_y_source, div_x_y_source)


   cbf_set_divergence sets the source divergence parameters to the
   values specified by *div_x_source*, *div_y_source* and
   *div_x_y_source*.

   :param div_x_source: New value of div_x_source.
   :param div_y_source: New value of div_y_source.
   :param div_x_y_source: New value of div_x_y_source.

.. py:method:: cbf_handle_struct.count_elements(elements)


   cbf_count_elements sets \*\ *elements* to the number of detector
   elements.

   :param elements: Pointer to the destination count.

.. py:method:: cbf_handle_struct.get_element_id(element_number, element_id)


   cbf_get_element_number sets *element_number* to a number that can be
   used in other cbf_simple calls to identify the detector element
   *element_id* and optionally the specific *array_id> and
   array_section_id. cbf_get_element_id sets \*\ element_id to point to
   the ASCII value of the element_number'th
   "diffrn_data_frame.detector_element_id" entry, counting from 0. The
   element_number is the ordinal of the detector element in the
   DIFFRN_DETECTOR_ELEMENT category. If an array_section_id is specified
   (i.e. is not NULL), the element_number is the sum of the ordinal of
   the detector element plus the number of detector elements multiplied
   by the ordinal of array_section_id for the specified array_id> in the
   ARRAY_STRUCTURE_LIST_SECTION category.*

   *If the detector element does not exist, the function returns
   CBF_NOTFOUND.*

   *The element_id will be valid as long as the item exists and has not
   been set to a new value.*

   *The element_id must not be modified by the program in any way.*

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param element_id: Pointer to the destination string for cbf_get_element_id, but the string itself for cbf_get_element_number.

.. py:method:: cbf_handle_struct.get_element_number(element_id, array_id, array_section_id, element_number)


   cbf_get_element_number sets *element_number* to a number that can be
   used in other cbf_simple calls to identify the detector element
   *element_id* and optionally the specific *array_id> and
   array_section_id. cbf_get_element_id sets \*\ element_id to point to
   the ASCII value of the element_number'th
   "diffrn_data_frame.detector_element_id" entry, counting from 0. The
   element_number is the ordinal of the detector element in the
   DIFFRN_DETECTOR_ELEMENT category. If an array_section_id is specified
   (i.e. is not NULL), the element_number is the sum of the ordinal of
   the detector element plus the number of detector elements multiplied
   by the ordinal of array_section_id for the specified array_id> in the
   ARRAY_STRUCTURE_LIST_SECTION category.*

   *If the detector element does not exist, the function returns
   CBF_NOTFOUND.*

   *The element_id will be valid as long as the item exists and has not
   been set to a new value.*

   *The element_id must not be modified by the program in any way.*

   :param element_id: Pointer to the destination string for cbf_get_element_id, but the string itself for cbf_get_element_number.
   :param array_id: The optional array id or NULL.
   :param array_section_id: The optional array_section_id or NULL.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.

.. py:method:: cbf_handle_struct.get_gain(element_number, gain, gain_esd)


   cbf_get_gain sets \*\ *gain* and \*\ *gain_esd* to the corresponding
   gain parameters for element number *element_number*.

   Either of the destination pointers may be NULL.

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param gain: Pointer to the destination gain.
   :param gain_esd: Pointer to the destination gain_esd.

.. py:method:: cbf_handle_struct.set_gain(element_number, gain, gain_esd)


   cbf_set_gain sets the gain of element number *element_number* to the
   values specified by *gain* and *gain_esd*.

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param gain: New gain value.
   :param gain_esd: New gain_esd value.

.. py:method:: cbf_handle_struct.get_overload(element_number, overload)


   cbf_get_overload sets \*\ *overload* to the overload value for
   element number *element_number*.

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param overload: Pointer to the destination overload.

.. py:method:: cbf_handle_struct.set_overload(element_number, overload)


   cbf_set_overload sets the overload value of element number
   *element_number* to *overload*.

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param overload: New overload value.

.. py:method:: cbf_handle_struct.get_integration_time(reserved, time)


   cbf_get_integration_time sets \*\ *time* to the integration time in
   seconds. The parameter *reserved* is presently unused and should be
   set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param time: Pointer to the destination time.

.. py:method:: cbf_handle_struct.set_integration_time(reserved, time)


   cbf_set_integration_time sets the integration time in seconds to the
   value specified by *time*. The parameter *reserved* is presently
   unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param time:

.. py:method:: cbf_handle_struct.get_diffrn_id(diffrn_id)


   cbf_get_diffrn_id sets \*\ *diffrn_id* to point to the ASCII value of
   the "diffrn.id" entry. cbf_require_diffrn_id also sets
   \*\ *diffrn_id* to point to the ASCII value of the "diffrn.id" entry,
   but, if the "diffrn.id" entry does not exist, it sets the value in
   the CBF and in\*\ *diffrn_id* to the character string given by
   *default_id*, creating the category and column is necessary.

   The *diffrn_id* will be valid as long as the item exists and has not
   been set to a new value.

   The *diffrn_id* must not be modified by the program in any way.

   :param diffrn_id: Pointer to the destination value pointer.

.. py:method:: cbf_handle_struct.require_diffrn_id(diffrn_id, default_id)


   cbf_get_diffrn_id sets \*\ *diffrn_id* to point to the ASCII value of
   the "diffrn.id" entry. cbf_require_diffrn_id also sets
   \*\ *diffrn_id* to point to the ASCII value of the "diffrn.id" entry,
   but, if the "diffrn.id" entry does not exist, it sets the value in
   the CBF and in\*\ *diffrn_id* to the character string given by
   *default_id*, creating the category and column is necessary.

   The *diffrn_id* will be valid as long as the item exists and has not
   been set to a new value.

   The *diffrn_id* must not be modified by the program in any way.

   :param diffrn_id: Pointer to the destination value pointer.
   :param default_id: Character string default value.

.. py:method:: cbf_handle_struct.get_timestamp(reserved, time, timezone)


   cbf_get_timestamp sets \*\ *time* to the collection timestamp in
   seconds since January 1 1970. \*\ *timezone* is set to timezone
   difference from UTC in minutes. The parameter *reserved* is presently
   unused and should be set to 0.

   Either of the destination pointers may be NULL.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param time: Pointer to the destination collection timestamp.
   :param timezone: Pointer to the destination timezone difference.

.. py:method:: cbf_handle_struct.set_timestamp(reserved, time, timezone, precision)


   cbf_set_timestamp sets the collection timestamp in seconds since
   January 1 1970 to the value specified by *time*. The timezone
   difference from UTC in minutes is set to *timezone*. If no timezone
   is desired, *timezone* should be CBF_NOTIM EZONE. The parameter
   *reserved* is presently unused and should be set to 0.

   The precision of the new timestamp is specified by the value
   *precision* in seconds. If *precision* is 0, the saved timestamp is
   assumed accurate to 1 second.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param time: Timestamp in seconds since January 1 1970.
   :param timezone: Timezone difference from UTC in minutes or CBF_NOTIMEZONE.
   :param precision: Timestamp precision in seconds.

.. py:method:: cbf_handle_struct.get_datestamp(reserved, year, month, day, hour, minute, second, timezone)


   *cbf_get_datestamp sets \*\ year, \*\ month, \*\ day, \*\ hour,
   \*\ minute and \*\ second to the corresponding values of the
   collection timestamp. \*\ timezone is set to timezone difference from
   UTC in minutes. The parameter < i>reserved* is presently unused and
   should be set to 0.

   Any of the destination pointers may be NULL.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param year: Pointer to the destination timestamp year.
   :param month: Pointer to the destination timestamp month (1-12).
   :param day: Pointer to the destination timestamp day (1-31).
   :param hour: Pointer to the destination timestamp hour (0-23).
   :param minute: Pointer to the destination timestamp minute (0-59).
   :param second: Pointer to the destination timestamp second (0-60.0).
   :param timezone: Pointer to the destination timezone difference from UTC in minutes.

.. py:method:: cbf_handle_struct.set_datestamp(reserved, year, month, day, hour, minute, second, timezone, precision)


   cbf_set_datestamp sets the collection timestamp in seconds since
   January 1 1970 to the value specified by *time*. The timezone
   difference from UTC in minutes is set to *timezone*. If no timezone
   is desired, *timezone* should be CBF_NOTIM EZONE. The parameter
   *reserved* is presently unused and should be set to 0.

   The precision of the new timestamp is specified by the value
   *precision* in seconds. If *precision* is 0, the saved timestamp is
   assumed accurate to 1 second.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param year:
   :param month:
   :param day:
   :param hour:
   :param minute:
   :param second:
   :param timezone: Timezone difference from UTC in minutes or CBF_NOTIMEZONE.
   :param precision: Timestamp precision in seconds.

.. py:method:: cbf_handle_struct.set_current_timestamp(reserved, timezone)


   cbf_set_current_timestamp sets the collection timestamp to the
   current time. The timezone difference from UTC in minutes is set to
   *timezone*. If no timezone is desired, *timezone* should be
   CBF_NOTIMEZONE. If no timezone is used, the timest amp will be UTC.
   The parameter *reserved* is presently unused and should be set to 0.

   The new timestamp will have a precision of 1 second.

   :param reserved: Unused.   Any value other than 0 is invalid.
   :param timezone: Timezone difference from UTC in minutes or CBF_NOTIMEZONE.

.. py:method:: cbf_handle_struct.get_3d_image_size(reserved, element_number, ndimslow, ndimmid, ndimfast)


   cbf_get_image_size, cbf_get_image_size_fs and cbf_get_image_size_sf
   set \*\ *ndimslow* and \*\ *ndimfast* to the slow and fast dimensions
   of the image array for element number *element_number*. If the array
   is 1-dimensional, \*\ *ndimslow* will be set to the array size and
   \*\ *ndimfast* will be set to 1. If the array is 3-dimensional an
   error code will be returned. cbf_get_3d_image_size,
   cbf_get_3d_image_size_fs and cbf_get_3d_image_size_sf set
   \*\ *ndimslow*, \*\ *ndimmid* and \*\ *ndimfast* to the slowest, next
   fastest and fastest dimensions, respectively, of the 3D image array
   for element number *element_number*. If the array is 1-dimensional,
   \*\ *ndimslow* will be set to the array size and \*\ *ndimmid* and
   \*\ *ndimfast* will be set to 1. If the array is 2-dimensional
   \*\ *ndimslow* and \*\ *ndimmid* will be set as for a call to
   cbf_get_image_size and \*\ *ndimfast* will be set to 1.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   Note that the ordering of dimensions is specified by values of the
   tag \_array_structure_list.precedence with a precedence of 1 for the
   fastest dimension, 2 for the next slower, etc., which is opposite to
   the ordering of the dimension arguments for these functions, except
   for the ones with the \_fs suffix..

   Any of the destination pointers may be NULL.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param ndimslow: Pointer to the destination slowest dimension.
   :param ndimmid: Pointer to the destination next faster dimension.
   :param ndimfast: Pointer to the destination fastest dimension.

.. py:method:: cbf_handle_struct.get_3d_image_size_fs(reserved, element_number, ndimfast, ndimmid, ndimslow)


   cbf_get_image_size, cbf_get_image_size_fs and cbf_get_image_size_sf
   set \*\ *ndimslow* and \*\ *ndimfast* to the slow and fast dimensions
   of the image array for element number *element_number*. If the array
   is 1-dimensional, \*\ *ndimslow* will be set to the array size and
   \*\ *ndimfast* will be set to 1. If the array is 3-dimensional an
   error code will be returned. cbf_get_3d_image_size,
   cbf_get_3d_image_size_fs and cbf_get_3d_image_size_sf set
   \*\ *ndimslow*, \*\ *ndimmid* and \*\ *ndimfast* to the slowest, next
   fastest and fastest dimensions, respectively, of the 3D image array
   for element number *element_number*. If the array is 1-dimensional,
   \*\ *ndimslow* will be set to the array size and \*\ *ndimmid* and
   \*\ *ndimfast* will be set to 1. If the array is 2-dimensional
   \*\ *ndimslow* and \*\ *ndimmid* will be set as for a call to
   cbf_get_image_size and \*\ *ndimfast* will be set to 1.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   Note that the ordering of dimensions is specified by values of the
   tag \_array_structure_list.precedence with a precedence of 1 for the
   fastest dimension, 2 for the next slower, etc., which is opposite to
   the ordering of the dimension arguments for these functions, except
   for the ones with the \_fs suffix..

   Any of the destination pointers may be NULL.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param ndimfast: Pointer to the destination fastest dimension.
   :param ndimmid: Pointer to the destination next faster dimension.
   :param ndimslow: Pointer to the destination slowest dimension.

.. py:method:: cbf_handle_struct.get_3d_image_size_sf(reserved, element_number, ndimslow, ndimmid, ndimfast)


   cbf_get_image_size, cbf_get_image_size_fs and cbf_get_image_size_sf
   set \*\ *ndimslow* and \*\ *ndimfast* to the slow and fast dimensions
   of the image array for element number *element_number*. If the array
   is 1-dimensional, \*\ *ndimslow* will be set to the array size and
   \*\ *ndimfast* will be set to 1. If the array is 3-dimensional an
   error code will be returned. cbf_get_3d_image_size,
   cbf_get_3d_image_size_fs and cbf_get_3d_image_size_sf set
   \*\ *ndimslow*, \*\ *ndimmid* and \*\ *ndimfast* to the slowest, next
   fastest and fastest dimensions, respectively, of the 3D image array
   for element number *element_number*. If the array is 1-dimensional,
   \*\ *ndimslow* will be set to the array size and \*\ *ndimmid* and
   \*\ *ndimfast* will be set to 1. If the array is 2-dimensional
   \*\ *ndimslow* and \*\ *ndimmid* will be set as for a call to
   cbf_get_image_size and \*\ *ndimfast* will be set to 1.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   Note that the ordering of dimensions is specified by values of the
   tag \_array_structure_list.precedence with a precedence of 1 for the
   fastest dimension, 2 for the next slower, etc., which is opposite to
   the ordering of the dimension arguments for these functions, except
   for the ones with the \_fs suffix..

   Any of the destination pointers may be NULL.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param ndimslow: Pointer to the destination slowest dimension.
   :param ndimmid: Pointer to the destination next faster dimension.
   :param ndimfast: Pointer to the destination fastest dimension.

.. py:method:: cbf_handle_struct.get_image_size(reserved, element_number, ndimslow, ndimfast)


   cbf_get_image_size, cbf_get_image_size_fs and cbf_get_image_size_sf
   set \*\ *ndimslow* and \*\ *ndimfast* to the slow and fast dimensions
   of the image array for element number *element_number*. If the array
   is 1-dimensional, \*\ *ndimslow* will be set to the array size and
   \*\ *ndimfast* will be set to 1. If the array is 3-dimensional an
   error code will be returned. cbf_get_3d_image_size,
   cbf_get_3d_image_size_fs and cbf_get_3d_image_size_sf set
   \*\ *ndimslow*, \*\ *ndimmid* and \*\ *ndimfast* to the slowest, next
   fastest and fastest dimensions, respectively, of the 3D image array
   for element number *element_number*. If the array is 1-dimensional,
   \*\ *ndimslow* will be set to the array size and \*\ *ndimmid* and
   \*\ *ndimfast* will be set to 1. If the array is 2-dimensional
   \*\ *ndimslow* and \*\ *ndimmid* will be set as for a call to
   cbf_get_image_size and \*\ *ndimfast* will be set to 1.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   Note that the ordering of dimensions is specified by values of the
   tag \_array_structure_list.precedence with a precedence of 1 for the
   fastest dimension, 2 for the next slower, etc., which is opposite to
   the ordering of the dimension arguments for these functions, except
   for the ones with the \_fs suffix..

   Any of the destination pointers may be NULL.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param ndimslow: Pointer to the destination slowest dimension.
   :param ndimfast: Pointer to the destination fastest dimension.

.. py:method:: cbf_handle_struct.get_image_size_fs(reserved, element_number, ndimfast, ndimslow)


   cbf_get_image_size, cbf_get_image_size_fs and cbf_get_image_size_sf
   set \*\ *ndimslow* and \*\ *ndimfast* to the slow and fast dimensions
   of the image array for element number *element_number*. If the array
   is 1-dimensional, \*\ *ndimslow* will be set to the array size and
   \*\ *ndimfast* will be set to 1. If the array is 3-dimensional an
   error code will be returned. cbf_get_3d_image_size,
   cbf_get_3d_image_size_fs and cbf_get_3d_image_size_sf set
   \*\ *ndimslow*, \*\ *ndimmid* and \*\ *ndimfast* to the slowest, next
   fastest and fastest dimensions, respectively, of the 3D image array
   for element number *element_number*. If the array is 1-dimensional,
   \*\ *ndimslow* will be set to the array size and \*\ *ndimmid* and
   \*\ *ndimfast* will be set to 1. If the array is 2-dimensional
   \*\ *ndimslow* and \*\ *ndimmid* will be set as for a call to
   cbf_get_image_size and \*\ *ndimfast* will be set to 1.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   Note that the ordering of dimensions is specified by values of the
   tag \_array_structure_list.precedence with a precedence of 1 for the
   fastest dimension, 2 for the next slower, etc., which is opposite to
   the ordering of the dimension arguments for these functions, except
   for the ones with the \_fs suffix..

   Any of the destination pointers may be NULL.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param ndimfast: Pointer to the destination fastest dimension.
   :param ndimslow: Pointer to the destination slowest dimension.

.. py:method:: cbf_handle_struct.get_image_size_sf(reserved, element_number, ndimslow, ndimfast)


   cbf_get_image_size, cbf_get_image_size_fs and cbf_get_image_size_sf
   set \*\ *ndimslow* and \*\ *ndimfast* to the slow and fast dimensions
   of the image array for element number *element_number*. If the array
   is 1-dimensional, \*\ *ndimslow* will be set to the array size and
   \*\ *ndimfast* will be set to 1. If the array is 3-dimensional an
   error code will be returned. cbf_get_3d_image_size,
   cbf_get_3d_image_size_fs and cbf_get_3d_image_size_sf set
   \*\ *ndimslow*, \*\ *ndimmid* and \*\ *ndimfast* to the slowest, next
   fastest and fastest dimensions, respectively, of the 3D image array
   for element number *element_number*. If the array is 1-dimensional,
   \*\ *ndimslow* will be set to the array size and \*\ *ndimmid* and
   \*\ *ndimfast* will be set to 1. If the array is 2-dimensional
   \*\ *ndimslow* and \*\ *ndimmid* will be set as for a call to
   cbf_get_image_size and \*\ *ndimfast* will be set to 1.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   Note that the ordering of dimensions is specified by values of the
   tag \_array_structure_list.precedence with a precedence of 1 for the
   fastest dimension, 2 for the next slower, etc., which is opposite to
   the ordering of the dimension arguments for these functions, except
   for the ones with the \_fs suffix..

   Any of the destination pointers may be NULL.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param ndimslow: Pointer to the destination slowest dimension.
   :param ndimfast: Pointer to the destination fastest dimension.

.. py:method:: cbf_handle_struct.get_3d_image(reserved, element_number, array, elsize, elsign, ndimslow, ndimmid, ndimfast)


   cbf_get_image, cbf_get_image_fs and cbf_get_image_sf read the image
   array for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimfast* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_get_real_image,
   cbf_get_real_image_fs and cbf_get_real_image_sf read the image array
   of IEEE doubles or floats for element number *element_number* into an
   *array*. A real array is always signed. cbf_get_3d_image,
   cbf_get_3d_image_fs and cbf_get_3d_image_sf read the 3D image array
   for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimmid*\ ×\ *ndimfast* elements of
   *elsize* bytes each, starting at *array*. The elements are signed if
   *elsign* is non-0 and unsigned otherwise. cbf_get_real_3d_image,
   cbf_get_real_3d_image_fs, cbf_get_real_3d_image_sf reads the 3D image
   array of IEEE doubles or floats for element number *element_number*
   into an *array*. A real array is always signed.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   The structure of the array as a 1-, 2- or 3-dimensional array should
   agree with the structure of the array given in the
   ARRAY_STRUCTURE_LIST category. If the array is 1-dimensional,
   *ndimslow* should be the array size and *ndimfast* and, for the 3D
   calls, *ndimmid*, should be set to 1 both in the call and in the
   imgCIF data being processed. If the array is 2-dimensional and a 3D
   call is used, *ndimslow* and *ndimmid* should be the array dimensions
   and *ndimfast* should be set to 1 both in the call and in the imgCIF
   data being processed.

   If any element in the binary data cant fit into the destination
   element, the destination is set the nearest possible value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination *array* must consist of chars, shorts or
   ints (signed or unsigned) for cbf_get_image, or IEEE doubles or
   floats for cbf_get_real_image. If *elsize* is not equal to sizeof
   (char), sizeof (short), sizeof (int), sizeof(double) or
   sizeof(float), the function returns CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param elsign:
   :param ndimslow: Slowest array dimension.
   :param ndimmid: Next faster array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.get_3d_image_fs(reserved, element_number, array, elsize, elsign, ndimfast, ndimmid, ndimslow)


   cbf_get_image, cbf_get_image_fs and cbf_get_image_sf read the image
   array for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimfast* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_get_real_image,
   cbf_get_real_image_fs and cbf_get_real_image_sf read the image array
   of IEEE doubles or floats for element number *element_number* into an
   *array*. A real array is always signed. cbf_get_3d_image,
   cbf_get_3d_image_fs and cbf_get_3d_image_sf read the 3D image array
   for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimmid*\ ×\ *ndimfast* elements of
   *elsize* bytes each, starting at *array*. The elements are signed if
   *elsign* is non-0 and unsigned otherwise. cbf_get_real_3d_image,
   cbf_get_real_3d_image_fs, cbf_get_real_3d_image_sf reads the 3D image
   array of IEEE doubles or floats for element number *element_number*
   into an *array*. A real array is always signed.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   The structure of the array as a 1-, 2- or 3-dimensional array should
   agree with the structure of the array given in the
   ARRAY_STRUCTURE_LIST category. If the array is 1-dimensional,
   *ndimslow* should be the array size and *ndimfast* and, for the 3D
   calls, *ndimmid*, should be set to 1 both in the call and in the
   imgCIF data being processed. If the array is 2-dimensional and a 3D
   call is used, *ndimslow* and *ndimmid* should be the array dimensions
   and *ndimfast* should be set to 1 both in the call and in the imgCIF
   data being processed.

   If any element in the binary data cant fit into the destination
   element, the destination is set the nearest possible value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination *array* must consist of chars, shorts or
   ints (signed or unsigned) for cbf_get_image, or IEEE doubles or
   floats for cbf_get_real_image. If *elsize* is not equal to sizeof
   (char), sizeof (short), sizeof (int), sizeof(double) or
   sizeof(float), the function returns CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param elsign:
   :param ndimfast: Fastest array dimension.
   :param ndimmid: Next faster array dimension.
   :param ndimslow: Slowest array dimension.

.. py:method:: cbf_handle_struct.get_3d_image_sf(reserved, element_number, array, elsize, elsign, ndimslow, ndimmid, ndimfast)


   cbf_get_image, cbf_get_image_fs and cbf_get_image_sf read the image
   array for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimfast* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_get_real_image,
   cbf_get_real_image_fs and cbf_get_real_image_sf read the image array
   of IEEE doubles or floats for element number *element_number* into an
   *array*. A real array is always signed. cbf_get_3d_image,
   cbf_get_3d_image_fs and cbf_get_3d_image_sf read the 3D image array
   for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimmid*\ ×\ *ndimfast* elements of
   *elsize* bytes each, starting at *array*. The elements are signed if
   *elsign* is non-0 and unsigned otherwise. cbf_get_real_3d_image,
   cbf_get_real_3d_image_fs, cbf_get_real_3d_image_sf reads the 3D image
   array of IEEE doubles or floats for element number *element_number*
   into an *array*. A real array is always signed.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   The structure of the array as a 1-, 2- or 3-dimensional array should
   agree with the structure of the array given in the
   ARRAY_STRUCTURE_LIST category. If the array is 1-dimensional,
   *ndimslow* should be the array size and *ndimfast* and, for the 3D
   calls, *ndimmid*, should be set to 1 both in the call and in the
   imgCIF data being processed. If the array is 2-dimensional and a 3D
   call is used, *ndimslow* and *ndimmid* should be the array dimensions
   and *ndimfast* should be set to 1 both in the call and in the imgCIF
   data being processed.

   If any element in the binary data cant fit into the destination
   element, the destination is set the nearest possible value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination *array* must consist of chars, shorts or
   ints (signed or unsigned) for cbf_get_image, or IEEE doubles or
   floats for cbf_get_real_image. If *elsize* is not equal to sizeof
   (char), sizeof (short), sizeof (int), sizeof(double) or
   sizeof(float), the function returns CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param elsign:
   :param ndimslow: Slowest array dimension.
   :param ndimmid: Next faster array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.get_image(reserved, element_number, array, elsize, elsign, ndimslow, ndimfast)


   cbf_get_image, cbf_get_image_fs and cbf_get_image_sf read the image
   array for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimfast* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_get_real_image,
   cbf_get_real_image_fs and cbf_get_real_image_sf read the image array
   of IEEE doubles or floats for element number *element_number* into an
   *array*. A real array is always signed. cbf_get_3d_image,
   cbf_get_3d_image_fs and cbf_get_3d_image_sf read the 3D image array
   for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimmid*\ ×\ *ndimfast* elements of
   *elsize* bytes each, starting at *array*. The elements are signed if
   *elsign* is non-0 and unsigned otherwise. cbf_get_real_3d_image,
   cbf_get_real_3d_image_fs, cbf_get_real_3d_image_sf reads the 3D image
   array of IEEE doubles or floats for element number *element_number*
   into an *array*. A real array is always signed.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   The structure of the array as a 1-, 2- or 3-dimensional array should
   agree with the structure of the array given in the
   ARRAY_STRUCTURE_LIST category. If the array is 1-dimensional,
   *ndimslow* should be the array size and *ndimfast* and, for the 3D
   calls, *ndimmid*, should be set to 1 both in the call and in the
   imgCIF data being processed. If the array is 2-dimensional and a 3D
   call is used, *ndimslow* and *ndimmid* should be the array dimensions
   and *ndimfast* should be set to 1 both in the call and in the imgCIF
   data being processed.

   If any element in the binary data cant fit into the destination
   element, the destination is set the nearest possible value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination *array* must consist of chars, shorts or
   ints (signed or unsigned) for cbf_get_image, or IEEE doubles or
   floats for cbf_get_real_image. If *elsize* is not equal to sizeof
   (char), sizeof (short), sizeof (int), sizeof(double) or
   sizeof(float), the function returns CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param elsign:
   :param ndimslow: Slowest array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.get_image_fs(reserved, element_number, array, elsize, elsign, ndimfast, ndimslow)


   cbf_get_image, cbf_get_image_fs and cbf_get_image_sf read the image
   array for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimfast* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_get_real_image,
   cbf_get_real_image_fs and cbf_get_real_image_sf read the image array
   of IEEE doubles or floats for element number *element_number* into an
   *array*. A real array is always signed. cbf_get_3d_image,
   cbf_get_3d_image_fs and cbf_get_3d_image_sf read the 3D image array
   for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimmid*\ ×\ *ndimfast* elements of
   *elsize* bytes each, starting at *array*. The elements are signed if
   *elsign* is non-0 and unsigned otherwise. cbf_get_real_3d_image,
   cbf_get_real_3d_image_fs, cbf_get_real_3d_image_sf reads the 3D image
   array of IEEE doubles or floats for element number *element_number*
   into an *array*. A real array is always signed.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   The structure of the array as a 1-, 2- or 3-dimensional array should
   agree with the structure of the array given in the
   ARRAY_STRUCTURE_LIST category. If the array is 1-dimensional,
   *ndimslow* should be the array size and *ndimfast* and, for the 3D
   calls, *ndimmid*, should be set to 1 both in the call and in the
   imgCIF data being processed. If the array is 2-dimensional and a 3D
   call is used, *ndimslow* and *ndimmid* should be the array dimensions
   and *ndimfast* should be set to 1 both in the call and in the imgCIF
   data being processed.

   If any element in the binary data cant fit into the destination
   element, the destination is set the nearest possible value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination *array* must consist of chars, shorts or
   ints (signed or unsigned) for cbf_get_image, or IEEE doubles or
   floats for cbf_get_real_image. If *elsize* is not equal to sizeof
   (char), sizeof (short), sizeof (int), sizeof(double) or
   sizeof(float), the function returns CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param elsign:
   :param ndimfast: Fastest array dimension.
   :param ndimslow: Slowest array dimension.

.. py:method:: cbf_handle_struct.get_image_sf(reserved, element_number, array, elsize, elsign, ndimslow, ndimfast)


   cbf_get_image, cbf_get_image_fs and cbf_get_image_sf read the image
   array for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimfast* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_get_real_image,
   cbf_get_real_image_fs and cbf_get_real_image_sf read the image array
   of IEEE doubles or floats for element number *element_number* into an
   *array*. A real array is always signed. cbf_get_3d_image,
   cbf_get_3d_image_fs and cbf_get_3d_image_sf read the 3D image array
   for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimmid*\ ×\ *ndimfast* elements of
   *elsize* bytes each, starting at *array*. The elements are signed if
   *elsign* is non-0 and unsigned otherwise. cbf_get_real_3d_image,
   cbf_get_real_3d_image_fs, cbf_get_real_3d_image_sf reads the 3D image
   array of IEEE doubles or floats for element number *element_number*
   into an *array*. A real array is always signed.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   The structure of the array as a 1-, 2- or 3-dimensional array should
   agree with the structure of the array given in the
   ARRAY_STRUCTURE_LIST category. If the array is 1-dimensional,
   *ndimslow* should be the array size and *ndimfast* and, for the 3D
   calls, *ndimmid*, should be set to 1 both in the call and in the
   imgCIF data being processed. If the array is 2-dimensional and a 3D
   call is used, *ndimslow* and *ndimmid* should be the array dimensions
   and *ndimfast* should be set to 1 both in the call and in the imgCIF
   data being processed.

   If any element in the binary data cant fit into the destination
   element, the destination is set the nearest possible value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination *array* must consist of chars, shorts or
   ints (signed or unsigned) for cbf_get_image, or IEEE doubles or
   floats for cbf_get_real_image. If *elsize* is not equal to sizeof
   (char), sizeof (short), sizeof (int), sizeof(double) or
   sizeof(float), the function returns CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param elsign:
   :param ndimslow: Slowest array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.get_real_3d_image(reserved, element_number, array, elsize, ndimslow, ndimmid, ndimfast)


   cbf_get_image, cbf_get_image_fs and cbf_get_image_sf read the image
   array for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimfast* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_get_real_image,
   cbf_get_real_image_fs and cbf_get_real_image_sf read the image array
   of IEEE doubles or floats for element number *element_number* into an
   *array*. A real array is always signed. cbf_get_3d_image,
   cbf_get_3d_image_fs and cbf_get_3d_image_sf read the 3D image array
   for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimmid*\ ×\ *ndimfast* elements of
   *elsize* bytes each, starting at *array*. The elements are signed if
   *elsign* is non-0 and unsigned otherwise. cbf_get_real_3d_image,
   cbf_get_real_3d_image_fs, cbf_get_real_3d_image_sf reads the 3D image
   array of IEEE doubles or floats for element number *element_number*
   into an *array*. A real array is always signed.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   The structure of the array as a 1-, 2- or 3-dimensional array should
   agree with the structure of the array given in the
   ARRAY_STRUCTURE_LIST category. If the array is 1-dimensional,
   *ndimslow* should be the array size and *ndimfast* and, for the 3D
   calls, *ndimmid*, should be set to 1 both in the call and in the
   imgCIF data being processed. If the array is 2-dimensional and a 3D
   call is used, *ndimslow* and *ndimmid* should be the array dimensions
   and *ndimfast* should be set to 1 both in the call and in the imgCIF
   data being processed.

   If any element in the binary data cant fit into the destination
   element, the destination is set the nearest possible value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination *array* must consist of chars, shorts or
   ints (signed or unsigned) for cbf_get_image, or IEEE doubles or
   floats for cbf_get_real_image. If *elsize* is not equal to sizeof
   (char), sizeof (short), sizeof (int), sizeof(double) or
   sizeof(float), the function returns CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param ndimslow: Slowest array dimension.
   :param ndimmid: Next faster array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.get_real_3d_image_fs(reserved, element_number, array, elsize, ndimfast, ndimmid, ndimslow)


   cbf_get_image, cbf_get_image_fs and cbf_get_image_sf read the image
   array for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimfast* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_get_real_image,
   cbf_get_real_image_fs and cbf_get_real_image_sf read the image array
   of IEEE doubles or floats for element number *element_number* into an
   *array*. A real array is always signed. cbf_get_3d_image,
   cbf_get_3d_image_fs and cbf_get_3d_image_sf read the 3D image array
   for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimmid*\ ×\ *ndimfast* elements of
   *elsize* bytes each, starting at *array*. The elements are signed if
   *elsign* is non-0 and unsigned otherwise. cbf_get_real_3d_image,
   cbf_get_real_3d_image_fs, cbf_get_real_3d_image_sf reads the 3D image
   array of IEEE doubles or floats for element number *element_number*
   into an *array*. A real array is always signed.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   The structure of the array as a 1-, 2- or 3-dimensional array should
   agree with the structure of the array given in the
   ARRAY_STRUCTURE_LIST category. If the array is 1-dimensional,
   *ndimslow* should be the array size and *ndimfast* and, for the 3D
   calls, *ndimmid*, should be set to 1 both in the call and in the
   imgCIF data being processed. If the array is 2-dimensional and a 3D
   call is used, *ndimslow* and *ndimmid* should be the array dimensions
   and *ndimfast* should be set to 1 both in the call and in the imgCIF
   data being processed.

   If any element in the binary data cant fit into the destination
   element, the destination is set the nearest possible value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination *array* must consist of chars, shorts or
   ints (signed or unsigned) for cbf_get_image, or IEEE doubles or
   floats for cbf_get_real_image. If *elsize* is not equal to sizeof
   (char), sizeof (short), sizeof (int), sizeof(double) or
   sizeof(float), the function returns CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param ndimfast: Fastest array dimension.
   :param ndimmid: Next faster array dimension.
   :param ndimslow: Slowest array dimension.

.. py:method:: cbf_handle_struct.get_real_3d_image_sf(reserved, element_number, array, elsize, ndimslow, ndimmid, ndimfast)


   cbf_get_image, cbf_get_image_fs and cbf_get_image_sf read the image
   array for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimfast* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_get_real_image,
   cbf_get_real_image_fs and cbf_get_real_image_sf read the image array
   of IEEE doubles or floats for element number *element_number* into an
   *array*. A real array is always signed. cbf_get_3d_image,
   cbf_get_3d_image_fs and cbf_get_3d_image_sf read the 3D image array
   for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimmid*\ ×\ *ndimfast* elements of
   *elsize* bytes each, starting at *array*. The elements are signed if
   *elsign* is non-0 and unsigned otherwise. cbf_get_real_3d_image,
   cbf_get_real_3d_image_fs, cbf_get_real_3d_image_sf reads the 3D image
   array of IEEE doubles or floats for element number *element_number*
   into an *array*. A real array is always signed.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   The structure of the array as a 1-, 2- or 3-dimensional array should
   agree with the structure of the array given in the
   ARRAY_STRUCTURE_LIST category. If the array is 1-dimensional,
   *ndimslow* should be the array size and *ndimfast* and, for the 3D
   calls, *ndimmid*, should be set to 1 both in the call and in the
   imgCIF data being processed. If the array is 2-dimensional and a 3D
   call is used, *ndimslow* and *ndimmid* should be the array dimensions
   and *ndimfast* should be set to 1 both in the call and in the imgCIF
   data being processed.

   If any element in the binary data cant fit into the destination
   element, the destination is set the nearest possible value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination *array* must consist of chars, shorts or
   ints (signed or unsigned) for cbf_get_image, or IEEE doubles or
   floats for cbf_get_real_image. If *elsize* is not equal to sizeof
   (char), sizeof (short), sizeof (int), sizeof(double) or
   sizeof(float), the function returns CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param ndimslow: Slowest array dimension.
   :param ndimmid: Next faster array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.get_real_image(reserved, element_number, array, elsize, ndimslow, ndimfast)


   cbf_get_image, cbf_get_image_fs and cbf_get_image_sf read the image
   array for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimfast* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_get_real_image,
   cbf_get_real_image_fs and cbf_get_real_image_sf read the image array
   of IEEE doubles or floats for element number *element_number* into an
   *array*. A real array is always signed. cbf_get_3d_image,
   cbf_get_3d_image_fs and cbf_get_3d_image_sf read the 3D image array
   for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimmid*\ ×\ *ndimfast* elements of
   *elsize* bytes each, starting at *array*. The elements are signed if
   *elsign* is non-0 and unsigned otherwise. cbf_get_real_3d_image,
   cbf_get_real_3d_image_fs, cbf_get_real_3d_image_sf reads the 3D image
   array of IEEE doubles or floats for element number *element_number*
   into an *array*. A real array is always signed.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   The structure of the array as a 1-, 2- or 3-dimensional array should
   agree with the structure of the array given in the
   ARRAY_STRUCTURE_LIST category. If the array is 1-dimensional,
   *ndimslow* should be the array size and *ndimfast* and, for the 3D
   calls, *ndimmid*, should be set to 1 both in the call and in the
   imgCIF data being processed. If the array is 2-dimensional and a 3D
   call is used, *ndimslow* and *ndimmid* should be the array dimensions
   and *ndimfast* should be set to 1 both in the call and in the imgCIF
   data being processed.

   If any element in the binary data cant fit into the destination
   element, the destination is set the nearest possible value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination *array* must consist of chars, shorts or
   ints (signed or unsigned) for cbf_get_image, or IEEE doubles or
   floats for cbf_get_real_image. If *elsize* is not equal to sizeof
   (char), sizeof (short), sizeof (int), sizeof(double) or
   sizeof(float), the function returns CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param ndimslow: Slowest array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.get_real_image_fs(reserved, element_number, array, elsize, ndimfast, ndimslow)


   cbf_get_image, cbf_get_image_fs and cbf_get_image_sf read the image
   array for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimfast* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_get_real_image,
   cbf_get_real_image_fs and cbf_get_real_image_sf read the image array
   of IEEE doubles or floats for element number *element_number* into an
   *array*. A real array is always signed. cbf_get_3d_image,
   cbf_get_3d_image_fs and cbf_get_3d_image_sf read the 3D image array
   for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimmid*\ ×\ *ndimfast* elements of
   *elsize* bytes each, starting at *array*. The elements are signed if
   *elsign* is non-0 and unsigned otherwise. cbf_get_real_3d_image,
   cbf_get_real_3d_image_fs, cbf_get_real_3d_image_sf reads the 3D image
   array of IEEE doubles or floats for element number *element_number*
   into an *array*. A real array is always signed.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   The structure of the array as a 1-, 2- or 3-dimensional array should
   agree with the structure of the array given in the
   ARRAY_STRUCTURE_LIST category. If the array is 1-dimensional,
   *ndimslow* should be the array size and *ndimfast* and, for the 3D
   calls, *ndimmid*, should be set to 1 both in the call and in the
   imgCIF data being processed. If the array is 2-dimensional and a 3D
   call is used, *ndimslow* and *ndimmid* should be the array dimensions
   and *ndimfast* should be set to 1 both in the call and in the imgCIF
   data being processed.

   If any element in the binary data cant fit into the destination
   element, the destination is set the nearest possible value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination *array* must consist of chars, shorts or
   ints (signed or unsigned) for cbf_get_image, or IEEE doubles or
   floats for cbf_get_real_image. If *elsize* is not equal to sizeof
   (char), sizeof (short), sizeof (int), sizeof(double) or
   sizeof(float), the function returns CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param ndimfast: Fastest array dimension.
   :param ndimslow: Slowest array dimension.

.. py:method:: cbf_handle_struct.get_real_image_sf(reserved, element_number, array, elsize, ndimslow, ndimfast)


   cbf_get_image, cbf_get_image_fs and cbf_get_image_sf read the image
   array for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimfast* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_get_real_image,
   cbf_get_real_image_fs and cbf_get_real_image_sf read the image array
   of IEEE doubles or floats for element number *element_number* into an
   *array*. A real array is always signed. cbf_get_3d_image,
   cbf_get_3d_image_fs and cbf_get_3d_image_sf read the 3D image array
   for element number *element_number* into an *array*. The array
   consists of *ndimslow*\ ×\ *ndimmid*\ ×\ *ndimfast* elements of
   *elsize* bytes each, starting at *array*. The elements are signed if
   *elsign* is non-0 and unsigned otherwise. cbf_get_real_3d_image,
   cbf_get_real_3d_image_fs, cbf_get_real_3d_image_sf reads the 3D image
   array of IEEE doubles or floats for element number *element_number*
   into an *array*. A real array is always signed.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   The structure of the array as a 1-, 2- or 3-dimensional array should
   agree with the structure of the array given in the
   ARRAY_STRUCTURE_LIST category. If the array is 1-dimensional,
   *ndimslow* should be the array size and *ndimfast* and, for the 3D
   calls, *ndimmid*, should be set to 1 both in the call and in the
   imgCIF data being processed. If the array is 2-dimensional and a 3D
   call is used, *ndimslow* and *ndimmid* should be the array dimensions
   and *ndimfast* should be set to 1 both in the call and in the imgCIF
   data being processed.

   If any element in the binary data cant fit into the destination
   element, the destination is set the nearest possible value.

   If the value is not binary, the function returns CBF_ASCII.

   If the requested number of elements cant be read, the function will
   read as many as it can and then return CBF_ENDOFDATA.

   Currently, the destination *array* must consist of chars, shorts or
   ints (signed or unsigned) for cbf_get_image, or IEEE doubles or
   floats for cbf_get_real_image. If *elsize* is not equal to sizeof
   (char), sizeof (short), sizeof (int), sizeof(double) or
   sizeof(float), the function returns CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param array: Pointer to the destination array.
   :param elsize: Size in bytes of each destination array element.
   :param ndimslow: Slowest array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.set_3d_image(reserved, element_number, compression, array, elsize, elsign, ndimslow, ndimmid, ndimfast)


   cbf_set_image, cbf_set_image_fs and cbf_set_image_sf write the image
   array for element number *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimslow* elements of *elsize* bytes each, starting
   at *array*. The elements are signed if *elsign* is non-zero and
   unsigned otherwise. cbf_set_real_image, cbf_set_real_image_fs and
   cbf_set_real_image_sf write the image array for element number
   *element_number*. The *array* consists of *ndimfast*\ ×\ *ndimslow*
   IEEE double or float elements of *elsize* bytes each, starting at
   *array*. cbf_set_3d_image, cbf_set_3d_image_fs and
   cbf_set_3d_image_sf write the 3D image array for element number
   *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_set_real_3d_image,
   cbf_set_real_3d_image_fs and cbf_set_real_3d_image_sf writes the 3D
   image array for element number *element_number*. The *array* consists
   of *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* IEEE double or float
   elements of *elsize* bytes each, starting at *array*.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   If the array is 1-dimensional, *ndimslow* should be the array size
   and *ndimfast* and, for the 3D calls, *ndimmid*, should be set to 1.
   If the array is 2-dimensional and the 3D calls are used, *ndimslow*
   and *ndimmid* should be used for the array dimensions and *ndimfast*
   should be set to 1.

   The array will be compressed using the compression scheme specifed by
   compression. Currently, the available schemes are:

   ================= =============================================
   CBF_CANONICAL     Canonical-code compression (section 3.3.1)
   CBF_PACKED        CCP4-style packing (section 3.3.2)
   CBF_PACKED_V2     CCP4-style packing, version 2 (section 3.3.2)
   CBF_BYTE_OFFSET   Simple "byte_offset" compression.
   CBF_NIBBLE_OFFSET Simple "nibble_offset" compression.
   CBF_NONE          No compression.
   ================= =============================================

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source *array* must consist of chars, shorts or ints
   (signed or unsigned)for cbf_set_image, or IEEE doubles or floats for
   cbf_set_real_image. If *elsize* is not equal to sizeof (short),
   sizeof (int), sizeof(double) or sizeof(float), the function returns
   CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param compression: Compression type.
   :param array: Pointer to the image array.
   :param elsize: Size in bytes of each image array element.
   :param elsign:
   :param ndimslow: Slowest array dimension.
   :param ndimmid: Second slowest array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.set_3d_image_fs(reserved, element_number, compression, array, elsize, elsign, ndimfast, ndimmid, ndimslow)


   cbf_set_image, cbf_set_image_fs and cbf_set_image_sf write the image
   array for element number *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimslow* elements of *elsize* bytes each, starting
   at *array*. The elements are signed if *elsign* is non-zero and
   unsigned otherwise. cbf_set_real_image, cbf_set_real_image_fs and
   cbf_set_real_image_sf write the image array for element number
   *element_number*. The *array* consists of *ndimfast*\ ×\ *ndimslow*
   IEEE double or float elements of *elsize* bytes each, starting at
   *array*. cbf_set_3d_image, cbf_set_3d_image_fs and
   cbf_set_3d_image_sf write the 3D image array for element number
   *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_set_real_3d_image,
   cbf_set_real_3d_image_fs and cbf_set_real_3d_image_sf writes the 3D
   image array for element number *element_number*. The *array* consists
   of *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* IEEE double or float
   elements of *elsize* bytes each, starting at *array*.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   If the array is 1-dimensional, *ndimslow* should be the array size
   and *ndimfast* and, for the 3D calls, *ndimmid*, should be set to 1.
   If the array is 2-dimensional and the 3D calls are used, *ndimslow*
   and *ndimmid* should be used for the array dimensions and *ndimfast*
   should be set to 1.

   The array will be compressed using the compression scheme specifed by
   compression. Currently, the available schemes are:

   ================= =============================================
   CBF_CANONICAL     Canonical-code compression (section 3.3.1)
   CBF_PACKED        CCP4-style packing (section 3.3.2)
   CBF_PACKED_V2     CCP4-style packing, version 2 (section 3.3.2)
   CBF_BYTE_OFFSET   Simple "byte_offset" compression.
   CBF_NIBBLE_OFFSET Simple "nibble_offset" compression.
   CBF_NONE          No compression.
   ================= =============================================

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source *array* must consist of chars, shorts or ints
   (signed or unsigned)for cbf_set_image, or IEEE doubles or floats for
   cbf_set_real_image. If *elsize* is not equal to sizeof (short),
   sizeof (int), sizeof(double) or sizeof(float), the function returns
   CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param compression: Compression type.
   :param array: Pointer to the image array.
   :param elsize: Size in bytes of each image array element.
   :param elsign:
   :param ndimfast: Fastest array dimension.
   :param ndimmid: Second slowest array dimension.
   :param ndimslow: Slowest array dimension.

.. py:method:: cbf_handle_struct.set_3d_image_sf(reserved, element_number, compression, array, elsize, elsign, ndimslow, ndimmid, ndimfast)


   cbf_set_image, cbf_set_image_fs and cbf_set_image_sf write the image
   array for element number *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimslow* elements of *elsize* bytes each, starting
   at *array*. The elements are signed if *elsign* is non-zero and
   unsigned otherwise. cbf_set_real_image, cbf_set_real_image_fs and
   cbf_set_real_image_sf write the image array for element number
   *element_number*. The *array* consists of *ndimfast*\ ×\ *ndimslow*
   IEEE double or float elements of *elsize* bytes each, starting at
   *array*. cbf_set_3d_image, cbf_set_3d_image_fs and
   cbf_set_3d_image_sf write the 3D image array for element number
   *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_set_real_3d_image,
   cbf_set_real_3d_image_fs and cbf_set_real_3d_image_sf writes the 3D
   image array for element number *element_number*. The *array* consists
   of *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* IEEE double or float
   elements of *elsize* bytes each, starting at *array*.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   If the array is 1-dimensional, *ndimslow* should be the array size
   and *ndimfast* and, for the 3D calls, *ndimmid*, should be set to 1.
   If the array is 2-dimensional and the 3D calls are used, *ndimslow*
   and *ndimmid* should be used for the array dimensions and *ndimfast*
   should be set to 1.

   The array will be compressed using the compression scheme specifed by
   compression. Currently, the available schemes are:

   ================= =============================================
   CBF_CANONICAL     Canonical-code compression (section 3.3.1)
   CBF_PACKED        CCP4-style packing (section 3.3.2)
   CBF_PACKED_V2     CCP4-style packing, version 2 (section 3.3.2)
   CBF_BYTE_OFFSET   Simple "byte_offset" compression.
   CBF_NIBBLE_OFFSET Simple "nibble_offset" compression.
   CBF_NONE          No compression.
   ================= =============================================

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source *array* must consist of chars, shorts or ints
   (signed or unsigned)for cbf_set_image, or IEEE doubles or floats for
   cbf_set_real_image. If *elsize* is not equal to sizeof (short),
   sizeof (int), sizeof(double) or sizeof(float), the function returns
   CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param compression: Compression type.
   :param array: Pointer to the image array.
   :param elsize: Size in bytes of each image array element.
   :param elsign:
   :param ndimslow: Slowest array dimension.
   :param ndimmid: Second slowest array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.set_image(reserved, element_number, compression, array, elsize, elsign, ndimslow, ndimfast)


   cbf_set_image, cbf_set_image_fs and cbf_set_image_sf write the image
   array for element number *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimslow* elements of *elsize* bytes each, starting
   at *array*. The elements are signed if *elsign* is non-zero and
   unsigned otherwise. cbf_set_real_image, cbf_set_real_image_fs and
   cbf_set_real_image_sf write the image array for element number
   *element_number*. The *array* consists of *ndimfast*\ ×\ *ndimslow*
   IEEE double or float elements of *elsize* bytes each, starting at
   *array*. cbf_set_3d_image, cbf_set_3d_image_fs and
   cbf_set_3d_image_sf write the 3D image array for element number
   *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_set_real_3d_image,
   cbf_set_real_3d_image_fs and cbf_set_real_3d_image_sf writes the 3D
   image array for element number *element_number*. The *array* consists
   of *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* IEEE double or float
   elements of *elsize* bytes each, starting at *array*.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   If the array is 1-dimensional, *ndimslow* should be the array size
   and *ndimfast* and, for the 3D calls, *ndimmid*, should be set to 1.
   If the array is 2-dimensional and the 3D calls are used, *ndimslow*
   and *ndimmid* should be used for the array dimensions and *ndimfast*
   should be set to 1.

   The array will be compressed using the compression scheme specifed by
   compression. Currently, the available schemes are:

   ================= =============================================
   CBF_CANONICAL     Canonical-code compression (section 3.3.1)
   CBF_PACKED        CCP4-style packing (section 3.3.2)
   CBF_PACKED_V2     CCP4-style packing, version 2 (section 3.3.2)
   CBF_BYTE_OFFSET   Simple "byte_offset" compression.
   CBF_NIBBLE_OFFSET Simple "nibble_offset" compression.
   CBF_NONE          No compression.
   ================= =============================================

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source *array* must consist of chars, shorts or ints
   (signed or unsigned)for cbf_set_image, or IEEE doubles or floats for
   cbf_set_real_image. If *elsize* is not equal to sizeof (short),
   sizeof (int), sizeof(double) or sizeof(float), the function returns
   CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param compression: Compression type.
   :param array: Pointer to the image array.
   :param elsize: Size in bytes of each image array element.
   :param elsign:
   :param ndimslow: Slowest array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.set_image_fs(reserved, element_number, compression, array, elsize, elsign, ndimfast, ndimslow)


   cbf_set_image, cbf_set_image_fs and cbf_set_image_sf write the image
   array for element number *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimslow* elements of *elsize* bytes each, starting
   at *array*. The elements are signed if *elsign* is non-zero and
   unsigned otherwise. cbf_set_real_image, cbf_set_real_image_fs and
   cbf_set_real_image_sf write the image array for element number
   *element_number*. The *array* consists of *ndimfast*\ ×\ *ndimslow*
   IEEE double or float elements of *elsize* bytes each, starting at
   *array*. cbf_set_3d_image, cbf_set_3d_image_fs and
   cbf_set_3d_image_sf write the 3D image array for element number
   *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_set_real_3d_image,
   cbf_set_real_3d_image_fs and cbf_set_real_3d_image_sf writes the 3D
   image array for element number *element_number*. The *array* consists
   of *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* IEEE double or float
   elements of *elsize* bytes each, starting at *array*.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   If the array is 1-dimensional, *ndimslow* should be the array size
   and *ndimfast* and, for the 3D calls, *ndimmid*, should be set to 1.
   If the array is 2-dimensional and the 3D calls are used, *ndimslow*
   and *ndimmid* should be used for the array dimensions and *ndimfast*
   should be set to 1.

   The array will be compressed using the compression scheme specifed by
   compression. Currently, the available schemes are:

   ================= =============================================
   CBF_CANONICAL     Canonical-code compression (section 3.3.1)
   CBF_PACKED        CCP4-style packing (section 3.3.2)
   CBF_PACKED_V2     CCP4-style packing, version 2 (section 3.3.2)
   CBF_BYTE_OFFSET   Simple "byte_offset" compression.
   CBF_NIBBLE_OFFSET Simple "nibble_offset" compression.
   CBF_NONE          No compression.
   ================= =============================================

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source *array* must consist of chars, shorts or ints
   (signed or unsigned)for cbf_set_image, or IEEE doubles or floats for
   cbf_set_real_image. If *elsize* is not equal to sizeof (short),
   sizeof (int), sizeof(double) or sizeof(float), the function returns
   CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param compression: Compression type.
   :param array: Pointer to the image array.
   :param elsize: Size in bytes of each image array element.
   :param elsign:
   :param ndimfast: Fastest array dimension.
   :param ndimslow: Slowest array dimension.

.. py:method:: cbf_handle_struct.set_image_sf(reserved, element_number, compression, array, elsize, elsign, ndimslow, ndimfast)


   cbf_set_image, cbf_set_image_fs and cbf_set_image_sf write the image
   array for element number *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimslow* elements of *elsize* bytes each, starting
   at *array*. The elements are signed if *elsign* is non-zero and
   unsigned otherwise. cbf_set_real_image, cbf_set_real_image_fs and
   cbf_set_real_image_sf write the image array for element number
   *element_number*. The *array* consists of *ndimfast*\ ×\ *ndimslow*
   IEEE double or float elements of *elsize* bytes each, starting at
   *array*. cbf_set_3d_image, cbf_set_3d_image_fs and
   cbf_set_3d_image_sf write the 3D image array for element number
   *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_set_real_3d_image,
   cbf_set_real_3d_image_fs and cbf_set_real_3d_image_sf writes the 3D
   image array for element number *element_number*. The *array* consists
   of *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* IEEE double or float
   elements of *elsize* bytes each, starting at *array*.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   If the array is 1-dimensional, *ndimslow* should be the array size
   and *ndimfast* and, for the 3D calls, *ndimmid*, should be set to 1.
   If the array is 2-dimensional and the 3D calls are used, *ndimslow*
   and *ndimmid* should be used for the array dimensions and *ndimfast*
   should be set to 1.

   The array will be compressed using the compression scheme specifed by
   compression. Currently, the available schemes are:

   ================= =============================================
   CBF_CANONICAL     Canonical-code compression (section 3.3.1)
   CBF_PACKED        CCP4-style packing (section 3.3.2)
   CBF_PACKED_V2     CCP4-style packing, version 2 (section 3.3.2)
   CBF_BYTE_OFFSET   Simple "byte_offset" compression.
   CBF_NIBBLE_OFFSET Simple "nibble_offset" compression.
   CBF_NONE          No compression.
   ================= =============================================

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source *array* must consist of chars, shorts or ints
   (signed or unsigned)for cbf_set_image, or IEEE doubles or floats for
   cbf_set_real_image. If *elsize* is not equal to sizeof (short),
   sizeof (int), sizeof(double) or sizeof(float), the function returns
   CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param compression: Compression type.
   :param array: Pointer to the image array.
   :param elsize: Size in bytes of each image array element.
   :param elsign:
   :param ndimslow: Slowest array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.set_real_3d_image(reserved, element_number, compression, array, elsize, ndimslow, ndimmid, ndimfast)


   cbf_set_image, cbf_set_image_fs and cbf_set_image_sf write the image
   array for element number *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimslow* elements of *elsize* bytes each, starting
   at *array*. The elements are signed if *elsign* is non-zero and
   unsigned otherwise. cbf_set_real_image, cbf_set_real_image_fs and
   cbf_set_real_image_sf write the image array for element number
   *element_number*. The *array* consists of *ndimfast*\ ×\ *ndimslow*
   IEEE double or float elements of *elsize* bytes each, starting at
   *array*. cbf_set_3d_image, cbf_set_3d_image_fs and
   cbf_set_3d_image_sf write the 3D image array for element number
   *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_set_real_3d_image,
   cbf_set_real_3d_image_fs and cbf_set_real_3d_image_sf writes the 3D
   image array for element number *element_number*. The *array* consists
   of *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* IEEE double or float
   elements of *elsize* bytes each, starting at *array*.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   If the array is 1-dimensional, *ndimslow* should be the array size
   and *ndimfast* and, for the 3D calls, *ndimmid*, should be set to 1.
   If the array is 2-dimensional and the 3D calls are used, *ndimslow*
   and *ndimmid* should be used for the array dimensions and *ndimfast*
   should be set to 1.

   The array will be compressed using the compression scheme specifed by
   compression. Currently, the available schemes are:

   ================= =============================================
   CBF_CANONICAL     Canonical-code compression (section 3.3.1)
   CBF_PACKED        CCP4-style packing (section 3.3.2)
   CBF_PACKED_V2     CCP4-style packing, version 2 (section 3.3.2)
   CBF_BYTE_OFFSET   Simple "byte_offset" compression.
   CBF_NIBBLE_OFFSET Simple "nibble_offset" compression.
   CBF_NONE          No compression.
   ================= =============================================

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source *array* must consist of chars, shorts or ints
   (signed or unsigned)for cbf_set_image, or IEEE doubles or floats for
   cbf_set_real_image. If *elsize* is not equal to sizeof (short),
   sizeof (int), sizeof(double) or sizeof(float), the function returns
   CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param compression: Compression type.
   :param array: Pointer to the image array.
   :param elsize: Size in bytes of each image array element.
   :param ndimslow: Slowest array dimension.
   :param ndimmid: Second slowest array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.set_real_3d_image_fs(reserved, element_number, compression, array, elsize, ndimfast, ndimmid, ndimslow)


   cbf_set_image, cbf_set_image_fs and cbf_set_image_sf write the image
   array for element number *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimslow* elements of *elsize* bytes each, starting
   at *array*. The elements are signed if *elsign* is non-zero and
   unsigned otherwise. cbf_set_real_image, cbf_set_real_image_fs and
   cbf_set_real_image_sf write the image array for element number
   *element_number*. The *array* consists of *ndimfast*\ ×\ *ndimslow*
   IEEE double or float elements of *elsize* bytes each, starting at
   *array*. cbf_set_3d_image, cbf_set_3d_image_fs and
   cbf_set_3d_image_sf write the 3D image array for element number
   *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_set_real_3d_image,
   cbf_set_real_3d_image_fs and cbf_set_real_3d_image_sf writes the 3D
   image array for element number *element_number*. The *array* consists
   of *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* IEEE double or float
   elements of *elsize* bytes each, starting at *array*.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   If the array is 1-dimensional, *ndimslow* should be the array size
   and *ndimfast* and, for the 3D calls, *ndimmid*, should be set to 1.
   If the array is 2-dimensional and the 3D calls are used, *ndimslow*
   and *ndimmid* should be used for the array dimensions and *ndimfast*
   should be set to 1.

   The array will be compressed using the compression scheme specifed by
   compression. Currently, the available schemes are:

   ================= =============================================
   CBF_CANONICAL     Canonical-code compression (section 3.3.1)
   CBF_PACKED        CCP4-style packing (section 3.3.2)
   CBF_PACKED_V2     CCP4-style packing, version 2 (section 3.3.2)
   CBF_BYTE_OFFSET   Simple "byte_offset" compression.
   CBF_NIBBLE_OFFSET Simple "nibble_offset" compression.
   CBF_NONE          No compression.
   ================= =============================================

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source *array* must consist of chars, shorts or ints
   (signed or unsigned)for cbf_set_image, or IEEE doubles or floats for
   cbf_set_real_image. If *elsize* is not equal to sizeof (short),
   sizeof (int), sizeof(double) or sizeof(float), the function returns
   CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param compression: Compression type.
   :param array: Pointer to the image array.
   :param elsize: Size in bytes of each image array element.
   :param ndimfast: Fastest array dimension.
   :param ndimmid: Second slowest array dimension.
   :param ndimslow: Slowest array dimension.

.. py:method:: cbf_handle_struct.set_real_3d_image_sf(reserved, element_number, compression, array, elsize, ndimslow, ndimmid, ndimfast)


   cbf_set_image, cbf_set_image_fs and cbf_set_image_sf write the image
   array for element number *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimslow* elements of *elsize* bytes each, starting
   at *array*. The elements are signed if *elsign* is non-zero and
   unsigned otherwise. cbf_set_real_image, cbf_set_real_image_fs and
   cbf_set_real_image_sf write the image array for element number
   *element_number*. The *array* consists of *ndimfast*\ ×\ *ndimslow*
   IEEE double or float elements of *elsize* bytes each, starting at
   *array*. cbf_set_3d_image, cbf_set_3d_image_fs and
   cbf_set_3d_image_sf write the 3D image array for element number
   *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_set_real_3d_image,
   cbf_set_real_3d_image_fs and cbf_set_real_3d_image_sf writes the 3D
   image array for element number *element_number*. The *array* consists
   of *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* IEEE double or float
   elements of *elsize* bytes each, starting at *array*.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   If the array is 1-dimensional, *ndimslow* should be the array size
   and *ndimfast* and, for the 3D calls, *ndimmid*, should be set to 1.
   If the array is 2-dimensional and the 3D calls are used, *ndimslow*
   and *ndimmid* should be used for the array dimensions and *ndimfast*
   should be set to 1.

   The array will be compressed using the compression scheme specifed by
   compression. Currently, the available schemes are:

   ================= =============================================
   CBF_CANONICAL     Canonical-code compression (section 3.3.1)
   CBF_PACKED        CCP4-style packing (section 3.3.2)
   CBF_PACKED_V2     CCP4-style packing, version 2 (section 3.3.2)
   CBF_BYTE_OFFSET   Simple "byte_offset" compression.
   CBF_NIBBLE_OFFSET Simple "nibble_offset" compression.
   CBF_NONE          No compression.
   ================= =============================================

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source *array* must consist of chars, shorts or ints
   (signed or unsigned)for cbf_set_image, or IEEE doubles or floats for
   cbf_set_real_image. If *elsize* is not equal to sizeof (short),
   sizeof (int), sizeof(double) or sizeof(float), the function returns
   CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param compression: Compression type.
   :param array: Pointer to the image array.
   :param elsize: Size in bytes of each image array element.
   :param ndimslow: Slowest array dimension.
   :param ndimmid: Second slowest array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.set_real_image(reserved, element_number, compression, array, elsize, ndimslow, ndimfast)


   cbf_set_image, cbf_set_image_fs and cbf_set_image_sf write the image
   array for element number *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimslow* elements of *elsize* bytes each, starting
   at *array*. The elements are signed if *elsign* is non-zero and
   unsigned otherwise. cbf_set_real_image, cbf_set_real_image_fs and
   cbf_set_real_image_sf write the image array for element number
   *element_number*. The *array* consists of *ndimfast*\ ×\ *ndimslow*
   IEEE double or float elements of *elsize* bytes each, starting at
   *array*. cbf_set_3d_image, cbf_set_3d_image_fs and
   cbf_set_3d_image_sf write the 3D image array for element number
   *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_set_real_3d_image,
   cbf_set_real_3d_image_fs and cbf_set_real_3d_image_sf writes the 3D
   image array for element number *element_number*. The *array* consists
   of *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* IEEE double or float
   elements of *elsize* bytes each, starting at *array*.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   If the array is 1-dimensional, *ndimslow* should be the array size
   and *ndimfast* and, for the 3D calls, *ndimmid*, should be set to 1.
   If the array is 2-dimensional and the 3D calls are used, *ndimslow*
   and *ndimmid* should be used for the array dimensions and *ndimfast*
   should be set to 1.

   The array will be compressed using the compression scheme specifed by
   compression. Currently, the available schemes are:

   ================= =============================================
   CBF_CANONICAL     Canonical-code compression (section 3.3.1)
   CBF_PACKED        CCP4-style packing (section 3.3.2)
   CBF_PACKED_V2     CCP4-style packing, version 2 (section 3.3.2)
   CBF_BYTE_OFFSET   Simple "byte_offset" compression.
   CBF_NIBBLE_OFFSET Simple "nibble_offset" compression.
   CBF_NONE          No compression.
   ================= =============================================

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source *array* must consist of chars, shorts or ints
   (signed or unsigned)for cbf_set_image, or IEEE doubles or floats for
   cbf_set_real_image. If *elsize* is not equal to sizeof (short),
   sizeof (int), sizeof(double) or sizeof(float), the function returns
   CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param compression: Compression type.
   :param array: Pointer to the image array.
   :param elsize: Size in bytes of each image array element.
   :param ndimslow: Slowest array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.set_real_image_fs(reserved, element_number, compression, array, elsize, ndimfast, ndimslow)


   cbf_set_image, cbf_set_image_fs and cbf_set_image_sf write the image
   array for element number *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimslow* elements of *elsize* bytes each, starting
   at *array*. The elements are signed if *elsign* is non-zero and
   unsigned otherwise. cbf_set_real_image, cbf_set_real_image_fs and
   cbf_set_real_image_sf write the image array for element number
   *element_number*. The *array* consists of *ndimfast*\ ×\ *ndimslow*
   IEEE double or float elements of *elsize* bytes each, starting at
   *array*. cbf_set_3d_image, cbf_set_3d_image_fs and
   cbf_set_3d_image_sf write the 3D image array for element number
   *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_set_real_3d_image,
   cbf_set_real_3d_image_fs and cbf_set_real_3d_image_sf writes the 3D
   image array for element number *element_number*. The *array* consists
   of *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* IEEE double or float
   elements of *elsize* bytes each, starting at *array*.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   If the array is 1-dimensional, *ndimslow* should be the array size
   and *ndimfast* and, for the 3D calls, *ndimmid*, should be set to 1.
   If the array is 2-dimensional and the 3D calls are used, *ndimslow*
   and *ndimmid* should be used for the array dimensions and *ndimfast*
   should be set to 1.

   The array will be compressed using the compression scheme specifed by
   compression. Currently, the available schemes are:

   ================= =============================================
   CBF_CANONICAL     Canonical-code compression (section 3.3.1)
   CBF_PACKED        CCP4-style packing (section 3.3.2)
   CBF_PACKED_V2     CCP4-style packing, version 2 (section 3.3.2)
   CBF_BYTE_OFFSET   Simple "byte_offset" compression.
   CBF_NIBBLE_OFFSET Simple "nibble_offset" compression.
   CBF_NONE          No compression.
   ================= =============================================

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source *array* must consist of chars, shorts or ints
   (signed or unsigned)for cbf_set_image, or IEEE doubles or floats for
   cbf_set_real_image. If *elsize* is not equal to sizeof (short),
   sizeof (int), sizeof(double) or sizeof(float), the function returns
   CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param compression: Compression type.
   :param array: Pointer to the image array.
   :param elsize: Size in bytes of each image array element.
   :param ndimfast: Fastest array dimension.
   :param ndimslow: Slowest array dimension.

.. py:method:: cbf_handle_struct.set_real_image_sf(reserved, element_number, compression, array, elsize, ndimslow, ndimfast)


   cbf_set_image, cbf_set_image_fs and cbf_set_image_sf write the image
   array for element number *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimslow* elements of *elsize* bytes each, starting
   at *array*. The elements are signed if *elsign* is non-zero and
   unsigned otherwise. cbf_set_real_image, cbf_set_real_image_fs and
   cbf_set_real_image_sf write the image array for element number
   *element_number*. The *array* consists of *ndimfast*\ ×\ *ndimslow*
   IEEE double or float elements of *elsize* bytes each, starting at
   *array*. cbf_set_3d_image, cbf_set_3d_image_fs and
   cbf_set_3d_image_sf write the 3D image array for element number
   *element_number*. The *array* consists of
   *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* elements of *elsize* bytes
   each, starting at *array*. The elements are signed if *elsign* is
   non-0 and unsigned otherwise. cbf_set_real_3d_image,
   cbf_set_real_3d_image_fs and cbf_set_real_3d_image_sf writes the 3D
   image array for element number *element_number*. The *array* consists
   of *ndimfast*\ ×\ *ndimmid*\ ×\ *ndimslow* IEEE double or float
   elements of *elsize* bytes each, starting at *array*.

   The \_fs calls give the dimensions in a fast-to-slow order. The calls
   with no suffix and the calls \_sf calls give the dimensions in
   slow-to-fast order

   If the array is 1-dimensional, *ndimslow* should be the array size
   and *ndimfast* and, for the 3D calls, *ndimmid*, should be set to 1.
   If the array is 2-dimensional and the 3D calls are used, *ndimslow*
   and *ndimmid* should be used for the array dimensions and *ndimfast*
   should be set to 1.

   The array will be compressed using the compression scheme specifed by
   compression. Currently, the available schemes are:

   ================= =============================================
   CBF_CANONICAL     Canonical-code compression (section 3.3.1)
   CBF_PACKED        CCP4-style packing (section 3.3.2)
   CBF_PACKED_V2     CCP4-style packing, version 2 (section 3.3.2)
   CBF_BYTE_OFFSET   Simple "byte_offset" compression.
   CBF_NIBBLE_OFFSET Simple "nibble_offset" compression.
   CBF_NONE          No compression.
   ================= =============================================

   The values compressed are limited to 64 bits. If any element in the
   array is larger than 64 bits, the value compressed is the nearest
   64-bit value.

   Currently, the source *array* must consist of chars, shorts or ints
   (signed or unsigned)for cbf_set_image, or IEEE doubles or floats for
   cbf_set_real_image. If *elsize* is not equal to sizeof (short),
   sizeof (int), sizeof(double) or sizeof(float), the function returns
   CBF_ARGUMENT.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param compression: Compression type.
   :param array: Pointer to the image array.
   :param elsize: Size in bytes of each image array element.
   :param ndimslow: Slowest array dimension.
   :param ndimfast: Fastest array dimension.

.. py:method:: cbf_handle_struct.count_axis_ancestors(axis_id, ancestors)


   cbf_count_axis_ancestors sets *ancestors* to the number of ancestors
   of axis *axis_id*. cbf_get_axis_ancestor sets \*\ *ancestor* to the
   ancestor axis of index *ancestor_index* of axis *axis_id*, starting
   with *axis_id* for *ancestor_index* 0.

   cbf_get_axis_depends_on sets \*\ *depends_on* to the immediate
   ancestor of *axis_id* or to "." if there is no such ancestor.
   cbf_get_axis_equipment sets \*\ *equipment* to the equipment of
   *axis_id* or to "." if there is no such equipment.
   cbf_get_axis_equipment_component sets \*\ *equipment_component* to
   the equipment_component of *axis_id* or to "." if there is no such
   equipment_component.

   cbf_get_axis_offset sets \*\ *offset1*, \*\ *offset2* and
   \*\ *offset3* to the components of the ofset of *axis_id*.

   cbf_get_axis_rotation sets *rotation* to the rotation of *axis_id* or
   to 0 if there is no such rotation. cbf_get_axis_rotation_axis sets
   \*\ *rotation_axis* to the rotation_axis of *axis_id* or to "." if
   there is no such rotation_axis.

   cbf_get_axis_setting sets \*\ *start* and \*\ *increment* to the
   corresponding values of the axis *axis_id*. Any of the destination
   pointers may be NULL.

   cbf_get_axis_type sets *axis_type* to the type of *axis_id*.

   cbf_get_axis_vector sets \*\ *vector1*, \*\ *vector2* and
   \*\ *vector3* to the components of the vector of *axis_id*.

   The parameter *reserved* is presently unused and should be set to 0.

   :param axis_id: Axis id.
   :param ancestors:

.. py:method:: cbf_handle_struct.get_axis_ancestor(axis_id, ancestor_index, ancestor)


   cbf_count_axis_ancestors sets *ancestors* to the number of ancestors
   of axis *axis_id*. cbf_get_axis_ancestor sets \*\ *ancestor* to the
   ancestor axis of index *ancestor_index* of axis *axis_id*, starting
   with *axis_id* for *ancestor_index* 0.

   cbf_get_axis_depends_on sets \*\ *depends_on* to the immediate
   ancestor of *axis_id* or to "." if there is no such ancestor.
   cbf_get_axis_equipment sets \*\ *equipment* to the equipment of
   *axis_id* or to "." if there is no such equipment.
   cbf_get_axis_equipment_component sets \*\ *equipment_component* to
   the equipment_component of *axis_id* or to "." if there is no such
   equipment_component.

   cbf_get_axis_offset sets \*\ *offset1*, \*\ *offset2* and
   \*\ *offset3* to the components of the ofset of *axis_id*.

   cbf_get_axis_rotation sets *rotation* to the rotation of *axis_id* or
   to 0 if there is no such rotation. cbf_get_axis_rotation_axis sets
   \*\ *rotation_axis* to the rotation_axis of *axis_id* or to "." if
   there is no such rotation_axis.

   cbf_get_axis_setting sets \*\ *start* and \*\ *increment* to the
   corresponding values of the axis *axis_id*. Any of the destination
   pointers may be NULL.

   cbf_get_axis_type sets *axis_type* to the type of *axis_id*.

   cbf_get_axis_vector sets \*\ *vector1*, \*\ *vector2* and
   \*\ *vector3* to the components of the vector of *axis_id*.

   The parameter *reserved* is presently unused and should be set to 0.

   :param axis_id: Axis id.
   :param ancestor_index: Integer index of the desired ancestor, starting with 0 for the current axis_id.
   :param ancestor: Pointer to destination ancestor name pointer.

.. py:method:: cbf_handle_struct.get_axis_depends_on(axis_id, depends_on)


   cbf_count_axis_ancestors sets *ancestors* to the number of ancestors
   of axis *axis_id*. cbf_get_axis_ancestor sets \*\ *ancestor* to the
   ancestor axis of index *ancestor_index* of axis *axis_id*, starting
   with *axis_id* for *ancestor_index* 0.

   cbf_get_axis_depends_on sets \*\ *depends_on* to the immediate
   ancestor of *axis_id* or to "." if there is no such ancestor.
   cbf_get_axis_equipment sets \*\ *equipment* to the equipment of
   *axis_id* or to "." if there is no such equipment.
   cbf_get_axis_equipment_component sets \*\ *equipment_component* to
   the equipment_component of *axis_id* or to "." if there is no such
   equipment_component.

   cbf_get_axis_offset sets \*\ *offset1*, \*\ *offset2* and
   \*\ *offset3* to the components of the ofset of *axis_id*.

   cbf_get_axis_rotation sets *rotation* to the rotation of *axis_id* or
   to 0 if there is no such rotation. cbf_get_axis_rotation_axis sets
   \*\ *rotation_axis* to the rotation_axis of *axis_id* or to "." if
   there is no such rotation_axis.

   cbf_get_axis_setting sets \*\ *start* and \*\ *increment* to the
   corresponding values of the axis *axis_id*. Any of the destination
   pointers may be NULL.

   cbf_get_axis_type sets *axis_type* to the type of *axis_id*.

   cbf_get_axis_vector sets \*\ *vector1*, \*\ *vector2* and
   \*\ *vector3* to the components of the vector of *axis_id*.

   The parameter *reserved* is presently unused and should be set to 0.

   :param axis_id: Axis id.
   :param depends_on: Pointer to destination depends_on name pointer.

.. py:method:: cbf_handle_struct.get_axis_equipment(axis_id, equipment)


   cbf_count_axis_ancestors sets *ancestors* to the number of ancestors
   of axis *axis_id*. cbf_get_axis_ancestor sets \*\ *ancestor* to the
   ancestor axis of index *ancestor_index* of axis *axis_id*, starting
   with *axis_id* for *ancestor_index* 0.

   cbf_get_axis_depends_on sets \*\ *depends_on* to the immediate
   ancestor of *axis_id* or to "." if there is no such ancestor.
   cbf_get_axis_equipment sets \*\ *equipment* to the equipment of
   *axis_id* or to "." if there is no such equipment.
   cbf_get_axis_equipment_component sets \*\ *equipment_component* to
   the equipment_component of *axis_id* or to "." if there is no such
   equipment_component.

   cbf_get_axis_offset sets \*\ *offset1*, \*\ *offset2* and
   \*\ *offset3* to the components of the ofset of *axis_id*.

   cbf_get_axis_rotation sets *rotation* to the rotation of *axis_id* or
   to 0 if there is no such rotation. cbf_get_axis_rotation_axis sets
   \*\ *rotation_axis* to the rotation_axis of *axis_id* or to "." if
   there is no such rotation_axis.

   cbf_get_axis_setting sets \*\ *start* and \*\ *increment* to the
   corresponding values of the axis *axis_id*. Any of the destination
   pointers may be NULL.

   cbf_get_axis_type sets *axis_type* to the type of *axis_id*.

   cbf_get_axis_vector sets \*\ *vector1*, \*\ *vector2* and
   \*\ *vector3* to the components of the vector of *axis_id*.

   The parameter *reserved* is presently unused and should be set to 0.

   :param axis_id: Axis id.
   :param equipment: Pointer to destination equipment name pointer.

.. py:method:: cbf_handle_struct.get_axis_equipment_component(axis_id, equipment_component)


   cbf_count_axis_ancestors sets *ancestors* to the number of ancestors
   of axis *axis_id*. cbf_get_axis_ancestor sets \*\ *ancestor* to the
   ancestor axis of index *ancestor_index* of axis *axis_id*, starting
   with *axis_id* for *ancestor_index* 0.

   cbf_get_axis_depends_on sets \*\ *depends_on* to the immediate
   ancestor of *axis_id* or to "." if there is no such ancestor.
   cbf_get_axis_equipment sets \*\ *equipment* to the equipment of
   *axis_id* or to "." if there is no such equipment.
   cbf_get_axis_equipment_component sets \*\ *equipment_component* to
   the equipment_component of *axis_id* or to "." if there is no such
   equipment_component.

   cbf_get_axis_offset sets \*\ *offset1*, \*\ *offset2* and
   \*\ *offset3* to the components of the ofset of *axis_id*.

   cbf_get_axis_rotation sets *rotation* to the rotation of *axis_id* or
   to 0 if there is no such rotation. cbf_get_axis_rotation_axis sets
   \*\ *rotation_axis* to the rotation_axis of *axis_id* or to "." if
   there is no such rotation_axis.

   cbf_get_axis_setting sets \*\ *start* and \*\ *increment* to the
   corresponding values of the axis *axis_id*. Any of the destination
   pointers may be NULL.

   cbf_get_axis_type sets *axis_type* to the type of *axis_id*.

   cbf_get_axis_vector sets \*\ *vector1*, \*\ *vector2* and
   \*\ *vector3* to the components of the vector of *axis_id*.

   The parameter *reserved* is presently unused and should be set to 0.

   :param axis_id: Axis id.
   :param equipment_component: Pointer to destination equipment_component name pointer.

.. py:method:: cbf_handle_struct.get_axis_offset(axis_id, offset1, offset2, offset3)


   cbf_count_axis_ancestors sets *ancestors* to the number of ancestors
   of axis *axis_id*. cbf_get_axis_ancestor sets \*\ *ancestor* to the
   ancestor axis of index *ancestor_index* of axis *axis_id*, starting
   with *axis_id* for *ancestor_index* 0.

   cbf_get_axis_depends_on sets \*\ *depends_on* to the immediate
   ancestor of *axis_id* or to "." if there is no such ancestor.
   cbf_get_axis_equipment sets \*\ *equipment* to the equipment of
   *axis_id* or to "." if there is no such equipment.
   cbf_get_axis_equipment_component sets \*\ *equipment_component* to
   the equipment_component of *axis_id* or to "." if there is no such
   equipment_component.

   cbf_get_axis_offset sets \*\ *offset1*, \*\ *offset2* and
   \*\ *offset3* to the components of the ofset of *axis_id*.

   cbf_get_axis_rotation sets *rotation* to the rotation of *axis_id* or
   to 0 if there is no such rotation. cbf_get_axis_rotation_axis sets
   \*\ *rotation_axis* to the rotation_axis of *axis_id* or to "." if
   there is no such rotation_axis.

   cbf_get_axis_setting sets \*\ *start* and \*\ *increment* to the
   corresponding values of the axis *axis_id*. Any of the destination
   pointers may be NULL.

   cbf_get_axis_type sets *axis_type* to the type of *axis_id*.

   cbf_get_axis_vector sets \*\ *vector1*, \*\ *vector2* and
   \*\ *vector3* to the components of the vector of *axis_id*.

   The parameter *reserved* is presently unused and should be set to 0.

   :param axis_id: Axis id.
   :param offset1: Pointer to destination first offset component value.
   :param offset2: Pointer to destination second offset component value.
   :param offset3: Pointer to destination third offset component value.

.. py:method:: cbf_handle_struct.get_axis_rotation(axis_id, rotation)


   cbf_count_axis_ancestors sets *ancestors* to the number of ancestors
   of axis *axis_id*. cbf_get_axis_ancestor sets \*\ *ancestor* to the
   ancestor axis of index *ancestor_index* of axis *axis_id*, starting
   with *axis_id* for *ancestor_index* 0.

   cbf_get_axis_depends_on sets \*\ *depends_on* to the immediate
   ancestor of *axis_id* or to "." if there is no such ancestor.
   cbf_get_axis_equipment sets \*\ *equipment* to the equipment of
   *axis_id* or to "." if there is no such equipment.
   cbf_get_axis_equipment_component sets \*\ *equipment_component* to
   the equipment_component of *axis_id* or to "." if there is no such
   equipment_component.

   cbf_get_axis_offset sets \*\ *offset1*, \*\ *offset2* and
   \*\ *offset3* to the components of the ofset of *axis_id*.

   cbf_get_axis_rotation sets *rotation* to the rotation of *axis_id* or
   to 0 if there is no such rotation. cbf_get_axis_rotation_axis sets
   \*\ *rotation_axis* to the rotation_axis of *axis_id* or to "." if
   there is no such rotation_axis.

   cbf_get_axis_setting sets \*\ *start* and \*\ *increment* to the
   corresponding values of the axis *axis_id*. Any of the destination
   pointers may be NULL.

   cbf_get_axis_type sets *axis_type* to the type of *axis_id*.

   cbf_get_axis_vector sets \*\ *vector1*, \*\ *vector2* and
   \*\ *vector3* to the components of the vector of *axis_id*.

   The parameter *reserved* is presently unused and should be set to 0.

   :param axis_id: Axis id.
   :param rotation: Pointer to destination rotation value.

.. py:method:: cbf_handle_struct.get_axis_rotation_axis(axis_id, rotation_axis)


   cbf_count_axis_ancestors sets *ancestors* to the number of ancestors
   of axis *axis_id*. cbf_get_axis_ancestor sets \*\ *ancestor* to the
   ancestor axis of index *ancestor_index* of axis *axis_id*, starting
   with *axis_id* for *ancestor_index* 0.

   cbf_get_axis_depends_on sets \*\ *depends_on* to the immediate
   ancestor of *axis_id* or to "." if there is no such ancestor.
   cbf_get_axis_equipment sets \*\ *equipment* to the equipment of
   *axis_id* or to "." if there is no such equipment.
   cbf_get_axis_equipment_component sets \*\ *equipment_component* to
   the equipment_component of *axis_id* or to "." if there is no such
   equipment_component.

   cbf_get_axis_offset sets \*\ *offset1*, \*\ *offset2* and
   \*\ *offset3* to the components of the ofset of *axis_id*.

   cbf_get_axis_rotation sets *rotation* to the rotation of *axis_id* or
   to 0 if there is no such rotation. cbf_get_axis_rotation_axis sets
   \*\ *rotation_axis* to the rotation_axis of *axis_id* or to "." if
   there is no such rotation_axis.

   cbf_get_axis_setting sets \*\ *start* and \*\ *increment* to the
   corresponding values of the axis *axis_id*. Any of the destination
   pointers may be NULL.

   cbf_get_axis_type sets *axis_type* to the type of *axis_id*.

   cbf_get_axis_vector sets \*\ *vector1*, \*\ *vector2* and
   \*\ *vector3* to the components of the vector of *axis_id*.

   The parameter *reserved* is presently unused and should be set to 0.

   :param axis_id: Axis id.
   :param rotation_axis: Pointer to destination rotation_axisn name pointer.

.. py:method:: cbf_handle_struct.get_axis_setting(reserved, axis_id, start, increment)


   cbf_count_axis_ancestors sets *ancestors* to the number of ancestors
   of axis *axis_id*. cbf_get_axis_ancestor sets \*\ *ancestor* to the
   ancestor axis of index *ancestor_index* of axis *axis_id*, starting
   with *axis_id* for *ancestor_index* 0.

   cbf_get_axis_depends_on sets \*\ *depends_on* to the immediate
   ancestor of *axis_id* or to "." if there is no such ancestor.
   cbf_get_axis_equipment sets \*\ *equipment* to the equipment of
   *axis_id* or to "." if there is no such equipment.
   cbf_get_axis_equipment_component sets \*\ *equipment_component* to
   the equipment_component of *axis_id* or to "." if there is no such
   equipment_component.

   cbf_get_axis_offset sets \*\ *offset1*, \*\ *offset2* and
   \*\ *offset3* to the components of the ofset of *axis_id*.

   cbf_get_axis_rotation sets *rotation* to the rotation of *axis_id* or
   to 0 if there is no such rotation. cbf_get_axis_rotation_axis sets
   \*\ *rotation_axis* to the rotation_axis of *axis_id* or to "." if
   there is no such rotation_axis.

   cbf_get_axis_setting sets \*\ *start* and \*\ *increment* to the
   corresponding values of the axis *axis_id*. Any of the destination
   pointers may be NULL.

   cbf_get_axis_type sets *axis_type* to the type of *axis_id*.

   cbf_get_axis_vector sets \*\ *vector1*, \*\ *vector2* and
   \*\ *vector3* to the components of the vector of *axis_id*.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param axis_id: Axis id.
   :param start: Pointer to the destination start value.
   :param increment: Pointer to the destination increment value.

.. py:method:: cbf_handle_struct.get_axis_type(axis_id, axis_type)


   cbf_count_axis_ancestors sets *ancestors* to the number of ancestors
   of axis *axis_id*. cbf_get_axis_ancestor sets \*\ *ancestor* to the
   ancestor axis of index *ancestor_index* of axis *axis_id*, starting
   with *axis_id* for *ancestor_index* 0.

   cbf_get_axis_depends_on sets \*\ *depends_on* to the immediate
   ancestor of *axis_id* or to "." if there is no such ancestor.
   cbf_get_axis_equipment sets \*\ *equipment* to the equipment of
   *axis_id* or to "." if there is no such equipment.
   cbf_get_axis_equipment_component sets \*\ *equipment_component* to
   the equipment_component of *axis_id* or to "." if there is no such
   equipment_component.

   cbf_get_axis_offset sets \*\ *offset1*, \*\ *offset2* and
   \*\ *offset3* to the components of the ofset of *axis_id*.

   cbf_get_axis_rotation sets *rotation* to the rotation of *axis_id* or
   to 0 if there is no such rotation. cbf_get_axis_rotation_axis sets
   \*\ *rotation_axis* to the rotation_axis of *axis_id* or to "." if
   there is no such rotation_axis.

   cbf_get_axis_setting sets \*\ *start* and \*\ *increment* to the
   corresponding values of the axis *axis_id*. Any of the destination
   pointers may be NULL.

   cbf_get_axis_type sets *axis_type* to the type of *axis_id*.

   cbf_get_axis_vector sets \*\ *vector1*, \*\ *vector2* and
   \*\ *vector3* to the components of the vector of *axis_id*.

   The parameter *reserved* is presently unused and should be set to 0.

   :param axis_id: Axis id.
   :param axis_type:

.. py:method:: cbf_handle_struct.get_axis_vector(axis_id, vector1, vector2, vector3)


   cbf_count_axis_ancestors sets *ancestors* to the number of ancestors
   of axis *axis_id*. cbf_get_axis_ancestor sets \*\ *ancestor* to the
   ancestor axis of index *ancestor_index* of axis *axis_id*, starting
   with *axis_id* for *ancestor_index* 0.

   cbf_get_axis_depends_on sets \*\ *depends_on* to the immediate
   ancestor of *axis_id* or to "." if there is no such ancestor.
   cbf_get_axis_equipment sets \*\ *equipment* to the equipment of
   *axis_id* or to "." if there is no such equipment.
   cbf_get_axis_equipment_component sets \*\ *equipment_component* to
   the equipment_component of *axis_id* or to "." if there is no such
   equipment_component.

   cbf_get_axis_offset sets \*\ *offset1*, \*\ *offset2* and
   \*\ *offset3* to the components of the ofset of *axis_id*.

   cbf_get_axis_rotation sets *rotation* to the rotation of *axis_id* or
   to 0 if there is no such rotation. cbf_get_axis_rotation_axis sets
   \*\ *rotation_axis* to the rotation_axis of *axis_id* or to "." if
   there is no such rotation_axis.

   cbf_get_axis_setting sets \*\ *start* and \*\ *increment* to the
   corresponding values of the axis *axis_id*. Any of the destination
   pointers may be NULL.

   cbf_get_axis_type sets *axis_type* to the type of *axis_id*.

   cbf_get_axis_vector sets \*\ *vector1*, \*\ *vector2* and
   \*\ *vector3* to the components of the vector of *axis_id*.

   The parameter *reserved* is presently unused and should be set to 0.

   :param axis_id: Axis id.
   :param vector1: Pointer to destination first vector component value.
   :param vector2: Pointer to destination second vector component value.
   :param vector3: Pointer to destination third vector component value.

.. py:method:: cbf_handle_struct.set_axis_setting(reserved, axis_id, start, increment)


   cbf_set_axis_setting sets the starting and increment values of the
   axis *axis_id* to *start* and *increment*.

   The parameter *reserved* is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param axis_id: Axis id.
   :param start: Start value.
   :param increment: Increment value.

.. py:method:: cbf_handle_struct.set_diffrn_id(diffrn_id)


   cbf_set_diffrn_id sets the "diffrn.id" entry of the current datablock
   to the ASCII value *diffrn_id*.

   This function also changes corresponding "diffrn_id" entries in the
   "diffrn_source", "diffrn_radiation", "diffrn_detector" and
   "diffrn_measurement" categories.

   :param diffrn_id: ASCII value.

.. py:method:: cbf_handle_struct.construct_goniometer(goniometer)


   cbf_construct_goniometer constructs a goniometer object using the
   description in the CBF object handle and initialises the goniometer
   handle \*\ *goniometer*.

   :param goniometer: Pointer to the destination goniometer handle.

.. py:method:: cbf_handle_struct.construct_detector(detector, element_number)


   cbf_construct_detector constructs a detector object for detector
   element number *element_number* using the description in the CBF
   object handle and initialises the detector handle \*\ *detector*.

   cbf_construct_reference_detector constructs a detector object for
   detector element number *element_number* using the description in the
   CBF object handle and initialises the detector handle \*\ *detector*
   using the reference settings of the axes.
   cbf_require_reference_detector is similar, but try to force the
   creations of missing intermediate categories needed to construct a
   detector object.

   :param detector: Pointer to the destination detector handle.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.

.. py:method:: cbf_handle_struct.construct_reference_detector(detector, element_number)


   cbf_construct_detector constructs a detector object for detector
   element number *element_number* using the description in the CBF
   object handle and initialises the detector handle \*\ *detector*.

   cbf_construct_reference_detector constructs a detector object for
   detector element number *element_number* using the description in the
   CBF object handle and initialises the detector handle \*\ *detector*
   using the reference settings of the axes.
   cbf_require_reference_detector is similar, but try to force the
   creations of missing intermediate categories needed to construct a
   detector object.

   :param detector: Pointer to the destination detector handle.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.

.. py:method:: cbf_handle_struct.require_reference_detector(detector, element_number)


   cbf_construct_detector constructs a detector object for detector
   element number *element_number* using the description in the CBF
   object handle and initialises the detector handle \*\ *detector*.

   cbf_construct_reference_detector constructs a detector object for
   detector element number *element_number* using the description in the
   CBF object handle and initialises the detector handle \*\ *detector*
   using the reference settings of the axes.
   cbf_require_reference_detector is similar, but try to force the
   creations of missing intermediate categories needed to construct a
   detector object.

   :param detector: Pointer to the destination detector handle.
   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.

.. py:method:: cbf_handle_struct.construct_positioner(positioner, axis_id)


   cbf_construct_positioner constructs a positioner object for the axis
   given by *axis_id* using the description in the CBF object handle and
   initialises the positioner handle \*\ *positioner*.

   cbf_construct_reference positioner constructs a positioner object for
   the axis given by *axis_id* using the description in the CBF object
   handle and initialises the detector handle \*\ *detector* using the
   reference settings of the axes.

   :param positioner:
   :param axis_id: The identifier of the axis in the "axis" category.

.. py:method:: cbf_handle_struct.construct_reference_positioner(positioner, axis_id)


   cbf_construct_positioner constructs a positioner object for the axis
   given by *axis_id* using the description in the CBF object handle and
   initialises the positioner handle \*\ *positioner*.

   cbf_construct_reference positioner constructs a positioner object for
   the axis given by *axis_id* using the description in the CBF object
   handle and initialises the detector handle \*\ *detector* using the
   reference settings of the axes.

   :param positioner:
   :param axis_id: The identifier of the axis in the "axis" category.

.. py:method:: cbf_handle_struct.get_crystal_id(crystal_id)


   cbf_get_crystal_id sets \*\ *crystal_id* to point to the ASCII value
   of the "diffrn.crystal_id" entry.

   If the value is not ASCII, the function returns CBF_BINARY.

   The value will be valid as long as the item exists and has not been
   set to a new value.

   The value must not be modified by the program in any way.

   :param crystal_id: Pointer to the destination value pointer.

.. py:method:: cbf_handle_struct.get_pixel_size(element_number, axis_number, psize)


   cbf_get_pixel_size and cbf_get_pixel_size_sf set \*\ *psize* to point
   to the double value in millimeters of the axis *axis_number* of the
   detector element *element_number*. The *axis_number* is numbered from
   1, starting with the slowest axis. cbf_get_pixel_size_fs sets
   \*\ *psize* to point to the double value in millimeters of the axis
   *axis_number* of the detector element *element_number*. The
   *axis_number* is numbered from 1, starting with the fastest axis.

   If a negative axis number is given, the order of axes is reversed, so
   that -1 specifies the slowest axis for cbf_get_pixel_size_fs and the
   fastest axis for cbf_get_pixel_size_sf.

   If the pixel size is not given explcitly in the "array_element_size"
   category, the function returns CBF_NOTFOUND.

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param axis_number: The number of the axis, starting from 1 for the fastest for cbf_get_pixel_size and cbf_get_pixel_size_fs and the slowest for cbf_get_pixel_size_sf.
   :param psize: Pointer to the destination pixel size.

.. py:method:: cbf_handle_struct.get_pixel_size_fs(element_number, axis_number, psize)


   cbf_get_pixel_size and cbf_get_pixel_size_sf set \*\ *psize* to point
   to the double value in millimeters of the axis *axis_number* of the
   detector element *element_number*. The *axis_number* is numbered from
   1, starting with the slowest axis. cbf_get_pixel_size_fs sets
   \*\ *psize* to point to the double value in millimeters of the axis
   *axis_number* of the detector element *element_number*. The
   *axis_number* is numbered from 1, starting with the fastest axis.

   If a negative axis number is given, the order of axes is reversed, so
   that -1 specifies the slowest axis for cbf_get_pixel_size_fs and the
   fastest axis for cbf_get_pixel_size_sf.

   If the pixel size is not given explcitly in the "array_element_size"
   category, the function returns CBF_NOTFOUND.

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param axis_number: The number of the axis, starting from 1 for the fastest for cbf_get_pixel_size and cbf_get_pixel_size_fs and the slowest for cbf_get_pixel_size_sf.
   :param psize: Pointer to the destination pixel size.

.. py:method:: cbf_handle_struct.get_pixel_size_sf(element_number, axis_number, psize)


   cbf_get_pixel_size and cbf_get_pixel_size_sf set \*\ *psize* to point
   to the double value in millimeters of the axis *axis_number* of the
   detector element *element_number*. The *axis_number* is numbered from
   1, starting with the slowest axis. cbf_get_pixel_size_fs sets
   \*\ *psize* to point to the double value in millimeters of the axis
   *axis_number* of the detector element *element_number*. The
   *axis_number* is numbered from 1, starting with the fastest axis.

   If a negative axis number is given, the order of axes is reversed, so
   that -1 specifies the slowest axis for cbf_get_pixel_size_fs and the
   fastest axis for cbf_get_pixel_size_sf.

   If the pixel size is not given explcitly in the "array_element_size"
   category, the function returns CBF_NOTFOUND.

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param axis_number: The number of the axis, starting from 1 for the fastest for cbf_get_pixel_size and cbf_get_pixel_size_fs and the slowest for cbf_get_pixel_size_sf.
   :param psize: Pointer to the destination pixel size.

.. py:method:: cbf_handle_struct.set_pixel_size(element_number, axis_number, psize)


   cbf_set_pixel_size and cbf_set_pixel_size_sf set the item in the
   "e;size"e; column of the "array_structure_list" category at the row
   which matches axis *axis_number* of the detector element
   *element_number* converting the double pixel size *psize* from meters
   to millimeters in storing it in the "size" column for the axis
   *axis_number* of the detector element *element_number*. The
   *axis_number* is numbered from 1, starting with the slowest axis.
   cbf_set_pixel_size_fs sets the item in the "e;size"e; column of the
   "array_structure_list" category at the row which matches axis
   *axis_number* of the detector element *element_number* converting the
   double pixel size *psize* from meters to millimeters in storing it in
   the "size" column for the axis *axis_number* of the detector element
   *element_number*. The *axis_number* is numbered from 1, starting with
   the fastest axis.

   If a negative axis number is given, the order of axes is reversed, so
   that -1 specifies the slowest axis for cbf_get_pixel_size_fs and the
   fastest axis for cbf_get_pixel_size_sf.

   If the "array_structure_list" category does not already exist, it is
   created.

   If the appropriate row in the "array_structure_list" catgeory does
   not already exist, it is created.

   If the pixel size is not given explcitly in the "array_element_size
   category", the function returns CBF_NOTFOUND.

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param axis_number: The number of the axis, fastest first, starting from 1.
   :param psize: The pixel size in millimeters.

.. py:method:: cbf_handle_struct.set_pixel_size_fs(element_number, axis_number, psize)


   cbf_set_pixel_size and cbf_set_pixel_size_sf set the item in the
   "e;size"e; column of the "array_structure_list" category at the row
   which matches axis *axis_number* of the detector element
   *element_number* converting the double pixel size *psize* from meters
   to millimeters in storing it in the "size" column for the axis
   *axis_number* of the detector element *element_number*. The
   *axis_number* is numbered from 1, starting with the slowest axis.
   cbf_set_pixel_size_fs sets the item in the "e;size"e; column of the
   "array_structure_list" category at the row which matches axis
   *axis_number* of the detector element *element_number* converting the
   double pixel size *psize* from meters to millimeters in storing it in
   the "size" column for the axis *axis_number* of the detector element
   *element_number*. The *axis_number* is numbered from 1, starting with
   the fastest axis.

   If a negative axis number is given, the order of axes is reversed, so
   that -1 specifies the slowest axis for cbf_get_pixel_size_fs and the
   fastest axis for cbf_get_pixel_size_sf.

   If the "array_structure_list" category does not already exist, it is
   created.

   If the appropriate row in the "array_structure_list" catgeory does
   not already exist, it is created.

   If the pixel size is not given explcitly in the "array_element_size
   category", the function returns CBF_NOTFOUND.

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param axis_number: The number of the axis, fastest first, starting from 1.
   :param psize: The pixel size in millimeters.

.. py:method:: cbf_handle_struct.set_pixel_size_sf(element_number, axis_number, psize)


   cbf_set_pixel_size and cbf_set_pixel_size_sf set the item in the
   "e;size"e; column of the "array_structure_list" category at the row
   which matches axis *axis_number* of the detector element
   *element_number* converting the double pixel size *psize* from meters
   to millimeters in storing it in the "size" column for the axis
   *axis_number* of the detector element *element_number*. The
   *axis_number* is numbered from 1, starting with the slowest axis.
   cbf_set_pixel_size_fs sets the item in the "e;size"e; column of the
   "array_structure_list" category at the row which matches axis
   *axis_number* of the detector element *element_number* converting the
   double pixel size *psize* from meters to millimeters in storing it in
   the "size" column for the axis *axis_number* of the detector element
   *element_number*. The *axis_number* is numbered from 1, starting with
   the fastest axis.

   If a negative axis number is given, the order of axes is reversed, so
   that -1 specifies the slowest axis for cbf_get_pixel_size_fs and the
   fastest axis for cbf_get_pixel_size_sf.

   If the "array_structure_list" category does not already exist, it is
   created.

   If the appropriate row in the "array_structure_list" catgeory does
   not already exist, it is created.

   If the pixel size is not given explcitly in the "array_element_size
   category", the function returns CBF_NOTFOUND.

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param axis_number: The number of the axis, fastest first, starting from 1.
   :param psize: The pixel size in millimeters.

.. py:method:: cbf_handle_struct.set_crystal_id(crystal_id)


   cbf_set_crystal_id sets the "diffrn.crystal_id" entry to the ASCII
   value *crystal_id*.

   :param crystal_id: ASCII value.

.. py:method:: cbf_handle_struct.get_unit_cell(cell[6], cell_esd[6])


   cbf_get_unit_cell sets *cell*\ [0:2] to the double values of the cell
   edge lengths a, b and c in Ångstroms, *cell*\ [3:5] to the double
   values of the cell angles α, β and γ in degrees, *cell_esd*\ [0:2] to
   the double values of the estimated strandard deviations of the cell
   edge lengths a, b and c in Ångstroms, *cell_esd*\ [3:5] to the double
   values of the estimated standard deviations of the the cell angles α,
   β and γ in degrees.

   The values returned are retrieved from the first row of the "cell"
   category. The value of "_cell.entry_id" is ignored.

   *cell* or *cell_esd* may be NULL.

   If *cell* is NULL, the cell parameters are not retrieved.

   If *cell_esd* is NULL, the cell parameter esds are not retrieved.

   If the "cell" category is present, but some of the values are
   missing, zeros are returned for the missing values.

   :param cell[6]:
   :param cell_esd[6]:

.. py:method:: cbf_handle_struct.set_unit_cell(cell[6], cell_esd[6])


   cbf_set_unit_cell sets the cell parameters to the double values given
   in *cell*\ [0:2] for the cell edge lengths a, b and c in Ångstroms,
   the double values given in *cell*\ [3:5] for the cell angles α, β and
   γ in degrees, the double values given in *cell_esd*\ [0:2] for the
   estimated strandard deviations of the cell edge lengths a, b and c in
   Ångstroms, and the double values given in *cell_esd*\ [3:5] for the
   estimated standard deviations of the the cell angles α, β and γ in
   degrees.

   The values are placed in the first row of the "cell" category. If no
   value has been given for "_cell.entry_id", it is set to the value of
   the "diffrn.id" entry of the current data block.

   *cell* or *cell_esd* may be NULL.

   If *cell* is NULL, the cell parameters are not set.

   If *cell_esd* is NULL, the cell parameter esds are not set.

   If the "cell" category is not present, it is created. If any of the
   necessary columns are not present, they are created.

   :param cell[6]:
   :param cell_esd[6]:

.. py:method:: cbf_handle_struct.get_reciprocal_cell(cell[6], cell_esd[6])


   cbf_get_reciprocal_cell sets *cell*\ [0:2] to the double values of
   the reciprocal cell edge lengths a\ :sup:`\*`, b\ :sup:`\*` and
   c\ :sup:`\*` in Ångstroms\ :sup:`-1`, *cell*\ [3:5] to the double
   values of the reciprocal cell angles α\ :sup:`\*`, β\ :sup:`\*` and
   γ\ :sup:`\*` in degrees, *cell_esd*\ [0:2] to the double values of
   the estimated strandard deviations of the reciprocal cell edge
   lengths a\ :sup:`\*`, b\ :sup:`\*` and c\ :sup:`\*` in
   Ångstroms\ :sup:`-1`, *cell_esd*\ [3:5] to the double values of the
   estimated standard deviations of the the reciprocal cell angles
   α\ :sup:`\*`, β\ :sup:`\*` and γ\ :sup:`\*` in degrees.

   The values returned are retrieved from the first row of the "cell"
   category. The value of "_cell.entry_id" is ignored.

   *cell* or *cell_esd* may be NULL.

   If *cell* is NULL, the reciprocal cell parameters are not retrieved.

   If *cell_esd* is NULL, the reciprocal cell parameter esds are not
   retrieved.

   If the "cell" category is present, but some of the values are
   missing, zeros are returned for the missing values.

   :param cell[6]:
   :param cell_esd[6]:

.. py:method:: cbf_handle_struct.set_reciprocal_cell(cell[6], cell_esd[6])


   cbf_set_reciprocal_cell sets the reciprocal cell parameters to the
   double values given in *cell*\ [0:2] for the reciprocal cell edge
   lengths a\ :sup:`\*`, b\ :sup:`\*` and c\ :sup:`\*` in
   Ångstroms\ :sup:`-1`, the double values given in *cell*\ [3:5] for
   the reciprocal cell angles α\ :sup:`\*`, β\ :sup:`\*` and
   γ\ :sup:`\*` in degrees, the double values given in *cell_esd*\ [0:2]
   for the estimated strandard deviations of the reciprocal cell edge
   lengths a\ :sup:`\*`, b\ :sup:`\*` and c\ :sup:`\*` in Ångstroms, and
   the double values given in *cell_esd*\ [3:5] for the estimated
   standard deviations of the reciprocal cell angles α\ :sup:`\*`,
   β\ :sup:`\*` and γ\ :sup:`\*` in degrees.

   The values are placed in the first row of the "cell" category. If no
   value has been given for "_cell.entry_id", it is set to the value of
   the "diffrn.id" entry of the current data block.

   *cell* or *cell_esd* may be NULL.

   If *cell* is NULL, the reciprocal cell parameters are not set.

   If *cell_esd* is NULL, the reciprocal cell parameter esds are not
   set.

   If the "cell" category is not present, it is created. If any of the
   necessary columns are not present, they are created.

   :param cell[6]:
   :param cell_esd[6]:

.. py:method:: cbf_handle_struct.get_orientation_matrix(ub_matrix[9])


   cbf_get_orientation_matrix sets *ub_matrix* to point to the array of
   orientation matrix entries in the "diffrn" category in the order of
   columns:

   "UB[1][1]" "UB[1][2]" "UB[1][3]"
   "UB[2][1]" "UB[2][2]" "UB[2][3]"
   "UB[3][1]" "UB[3][2]" "UB[3][3]"
   cbf_set_orientation_matrix sets the values in the "diffrn" category
   to the values pointed to by *ub_matrix*.

   :param ub_matrix[9]:

.. py:method:: cbf_handle_struct.set_orientation_matrix(ub_matrix[9])


   cbf_get_orientation_matrix sets *ub_matrix* to point to the array of
   orientation matrix entries in the "diffrn" category in the order of
   columns:

   "UB[1][1]" "UB[1][2]" "UB[1][3]"
   "UB[2][1]" "UB[2][2]" "UB[2][3]"
   "UB[3][1]" "UB[3][2]" "UB[3][3]"
   cbf_set_orientation_matrix sets the values in the "diffrn" category
   to the values pointed to by *ub_matrix*.

   :param ub_matrix[9]:

.. py:method:: cbf_handle_struct.get_bin_sizes(element_number, slowbinsize, fastbinsize)


   cbf_get_bin_sizes sets *slowbinsize* to point to the value of the
   number of pixels composing one array element in the dimension that
   changes at the second-fastest rate and *fastbinsize* to point to the
   value of the number of pixels composing one array element in the
   dimension that changes at the fastest rate for the dectector element
   with the ordinal *element_number*. cbf_set_bin_sizes sets the the
   pixel bin sizes in the "array_intensities" category to the values of
   *slowbinsize_in* for the number of pixels composing one array element
   in the dimension that changes at the second-fastest rate and
   *fastbinsize_in* for the number of pixels composing one array element
   in the dimension that changes at the fastest rate for the dectector
   element with the ordinal *element_number*.

   In order to allow for software binning involving fractions of pixels,
   the bin sizes are doubles rather than ints.

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param slowbinsize: Pointer to the returned number of pixels composing one array element in the dimension that changes at the second-fastest rate.
   :param fastbinsize: Pointer to the returned number of pixels composing one array element in the dimension that changes at the fastest rate.

.. py:method:: cbf_handle_struct.set_bin_sizes(element_number, slowbinsize_in, fastbinsize_in)


   cbf_get_bin_sizes sets *slowbinsize* to point to the value of the
   number of pixels composing one array element in the dimension that
   changes at the second-fastest rate and *fastbinsize* to point to the
   value of the number of pixels composing one array element in the
   dimension that changes at the fastest rate for the dectector element
   with the ordinal *element_number*. cbf_set_bin_sizes sets the the
   pixel bin sizes in the "array_intensities" category to the values of
   *slowbinsize_in* for the number of pixels composing one array element
   in the dimension that changes at the second-fastest rate and
   *fastbinsize_in* for the number of pixels composing one array element
   in the dimension that changes at the fastest rate for the dectector
   element with the ordinal *element_number*.

   In order to allow for software binning involving fractions of pixels,
   the bin sizes are doubles rather than ints.

   :param element_number: The number of the detector element counting from 0 by order of appearance in the "diffrn_data_frame" category.
   :param slowbinsize_in: The number of pixels composing one array element in the dimension that changes at the second-fastest rate.
   :param fastbinsize_in: The number of pixels composing one array element in the dimension that changes at the fastest rate.

.. py:method:: cbf_handle_struct.get_axis_poise(ratio, vector1, vector2, vector3, offset1, offset2, offset3, angle, axis_id, frame_id)


   cbf_get_axis_poise sets *vector1*, *vector2*, *vector3* to point to
   the components of the axis vector for axis *axis_id*, *offset1*,
   *offset2*, *offset3* to point to the components of the axis base
   offset vector for axis *axis_id*, and *angle* to point to the angle
   of rotation of axis *axis_id* after application of the axis settings
   for frame *frame_id*, using *ratio*, a value between 0 and 1,
   indicating how far into the internal motion in the frame to go. If
   *frame_id* is the string ".", the first frame found is used. If there
   is more than one frame, which frame will be found is indeterminate.
   If *frame_id* is NULL, the overall setting for the scan are used,
   rather than those for any particular frame. The vector and offset
   reported are the reference vector and offset of the axis *axis_id*
   transformed by application of all motions of the axes on which
   *axis_id* depends.

   cbf_get_goniometer_poise *vector1*, *vector2*, *vector3* to point to
   the components of the axis vector for the goniometer axis, *offset1*,
   *offset2*, *offset3* to point to the components of the axis base
   offset vector for the goniometer axis, and *angle* to point to the
   angle of rotation of the goniometer axis after application of **all**
   axis settings in the *goniometer* deriving the vector, offset and
   angle from the resulting matrix. Calculation of the vector is
   indeterminate if the angle is zero.

   cbf_get_axis_reference_poise sets *vector1*, *vector2*, *vector3* to
   point to the components of the axis vector for axis *axis_id*,
   *offset1*, *offset2*, *offset3* to point to the components of the
   axis base offset vector for axis *axis_id* unmodified by axis
   rotations. Any of the pointers may be specified as NULL.

   :param ratio: A number between 0 and 1 indication how far into the frame to go
   :param vector1: Pointer to the first component of the axis vector
   :param vector2: Pointer to the second component of the axis vector
   :param vector3: Pointer to the third component of the axis vector
   :param offset1: Pointer to the first component of the axis offset
   :param offset2: Pointer to the second component of the axis offset
   :param offset3: Pointer to the third component of the axis offset
   :param angle: Pointer to the rotation angle
   :param axis_id: The specified axis
   :param frame_id: The specified frame

.. py:method:: cbf_handle_struct.get_axis_reference_poise(vector1, vector2, vector3, offset1, offset2, offset3, axis_id)


   cbf_get_axis_poise sets *vector1*, *vector2*, *vector3* to point to
   the components of the axis vector for axis *axis_id*, *offset1*,
   *offset2*, *offset3* to point to the components of the axis base
   offset vector for axis *axis_id*, and *angle* to point to the angle
   of rotation of axis *axis_id* after application of the axis settings
   for frame *frame_id*, using *ratio*, a value between 0 and 1,
   indicating how far into the internal motion in the frame to go. If
   *frame_id* is the string ".", the first frame found is used. If there
   is more than one frame, which frame will be found is indeterminate.
   If *frame_id* is NULL, the overall setting for the scan are used,
   rather than those for any particular frame. The vector and offset
   reported are the reference vector and offset of the axis *axis_id*
   transformed by application of all motions of the axes on which
   *axis_id* depends.

   cbf_get_goniometer_poise *vector1*, *vector2*, *vector3* to point to
   the components of the axis vector for the goniometer axis, *offset1*,
   *offset2*, *offset3* to point to the components of the axis base
   offset vector for the goniometer axis, and *angle* to point to the
   angle of rotation of the goniometer axis after application of **all**
   axis settings in the *goniometer* deriving the vector, offset and
   angle from the resulting matrix. Calculation of the vector is
   indeterminate if the angle is zero.

   cbf_get_axis_reference_poise sets *vector1*, *vector2*, *vector3* to
   point to the components of the axis vector for axis *axis_id*,
   *offset1*, *offset2*, *offset3* to point to the components of the
   axis base offset vector for axis *axis_id* unmodified by axis
   rotations. Any of the pointers may be specified as NULL.

   :param vector1: Pointer to the first component of the axis vector
   :param vector2: Pointer to the second component of the axis vector
   :param vector3: Pointer to the third component of the axis vector
   :param offset1: Pointer to the first component of the axis offset
   :param offset2: Pointer to the second component of the axis offset
   :param offset3: Pointer to the third component of the axis offset
   :param axis_id: The specified axis

.. py:method:: cbf_handle_struct.get_goniometer_poise(ratio, vector1, vector2, vector3, offset1, offset2, offset3, angle)


   cbf_get_axis_poise sets *vector1*, *vector2*, *vector3* to point to
   the components of the axis vector for axis *axis_id*, *offset1*,
   *offset2*, *offset3* to point to the components of the axis base
   offset vector for axis *axis_id*, and *angle* to point to the angle
   of rotation of axis *axis_id* after application of the axis settings
   for frame *frame_id*, using *ratio*, a value between 0 and 1,
   indicating how far into the internal motion in the frame to go. If
   *frame_id* is the string ".", the first frame found is used. If there
   is more than one frame, which frame will be found is indeterminate.
   If *frame_id* is NULL, the overall setting for the scan are used,
   rather than those for any particular frame. The vector and offset
   reported are the reference vector and offset of the axis *axis_id*
   transformed by application of all motions of the axes on which
   *axis_id* depends.

   cbf_get_goniometer_poise *vector1*, *vector2*, *vector3* to point to
   the components of the axis vector for the goniometer axis, *offset1*,
   *offset2*, *offset3* to point to the components of the axis base
   offset vector for the goniometer axis, and *angle* to point to the
   angle of rotation of the goniometer axis after application of **all**
   axis settings in the *goniometer* deriving the vector, offset and
   angle from the resulting matrix. Calculation of the vector is
   indeterminate if the angle is zero.

   cbf_get_axis_reference_poise sets *vector1*, *vector2*, *vector3* to
   point to the components of the axis vector for axis *axis_id*,
   *offset1*, *offset2*, *offset3* to point to the components of the
   axis base offset vector for axis *axis_id* unmodified by axis
   rotations. Any of the pointers may be specified as NULL.

   :param ratio: A number between 0 and 1 indication how far into the frame to go
   :param vector1: Pointer to the first component of the axis vector
   :param vector2: Pointer to the second component of the axis vector
   :param vector3: Pointer to the third component of the axis vector
   :param offset1: Pointer to the first component of the axis offset
   :param offset2: Pointer to the second component of the axis offset
   :param offset3: Pointer to the third component of the axis offset
   :param angle: Pointer to the rotation angle

.. py:method:: cbf_handle_struct.get_wavelength(wavelength)


   cbf_get_wavelength sets \*\ *wavelength* to the current wavelength in
   Å.

   :param wavelength: Pointer to the destination.

.. py:method:: cbf_handle_struct.set_wavelength(wavelength)


   cbf_set_wavelength sets the current wavelength in Å to *wavelength*.

   :param wavelength: Wavelength in Å.

.. py:method:: cbf_handle_struct.get_polarization(polarizn_source_ratio, polarizn_source_norm)


   cbf_get_polarization sets \*\ *polarizn_source_ratio* and
   \*\ *polarizn_source_norm* to the corresponding source polarization
   parameters.

   Either destination pointer may be NULL.

   :param polarizn_source_ratio: Pointer to the destination polarizn_source_ratio.
   :param polarizn_source_norm: Pointer to the destination polarizn_source_norm.

.. py:method:: cbf_handle_struct.set_polarization(polarizn_source_ratio, polarizn_source_norm)


   cbf_set_polarization sets the source polarization to the values
   specified by *polarizn_source_ratio* and *polarizn_source_norm*.

   :param polarizn_source_ratio: New value of polarizn_source_ratio.
   :param polarizn_source_norm: New value of polarizn_source_norm.

.. py:method:: cbf_handle_struct.write_h5file(h5handle)


   Extract the data from a CBF file & put it into a NeXus file.

   Equivalent to ``cbf_write_cbf2nx(handle,h5handle,0,0,0)``.

   :param h5handle: The NeXuS file to write data to.

.. py:method:: cbf_handle_struct.write_cbf2nx(h5handle, datablock, scan, list)


   Extract the data from a CBF file & put it into a NeXus file.

   Extracts data from ``handle`` and generates a NeXus file in
   ``h5handle``. This will attempt to extract metadata and image data
   from each scan (or the named scan) within each datablock (or the the
   named datablock) and insert it into a given index into the NXentry
   group specified in ``h5handle``.

   Each scan in the CBF file corresponds to one NXentry in NeXus, so a
   CBF datablock with multiple scans must be converted by calling this
   function with the appropriate value of ``scan`` once for each scan in
   the datablock.

   The flags (within ``h5handle``) determine:

   -  Compression algorithm: zlib/CBF/none
   -  Plugin registration method: automatic/manual

   The strings given by ``h5handle->scan_id`` and
   ``h5handle->sample_id`` define:

   -  The presence and value of an identifier for the scan, stored in
      ``/*:NXentry/entry_identifier``.
   -  The presence and value of an identifier for the sample, stored in
      ``/*:NXentry/*:NXsample/sample_identifier``.

   :param h5handle: The NeXuS file to write data to.
   :param datablock: The name of the datablock to convert, or NULL to convert all datablocks.
   :param scan: The name of the scan to convert, or NULL if there is only one scan in the datablock.
   :param list: Boolean flag to determine if a list of processed items is printed.

.. py:method:: cbf_handle_struct.write_minih5file(h5handle, axisConfig)


   Extract the data from a miniCBF file & put it into a NeXus file.

   Extracts the miniCBF data directly - by parsing the header - and uses
   that plus the configuration options from ``axisConfig`` to generate a
   NeXus file in ``h5handle``. This can extract metadata and image data
   from miniCBF files containing multiple datablocks which each contain
   a single image and insert it into a given index into the NXentry
   group specified in ``h5handle``.

   Currently, only ``Pilatus 1.2`` format headers are supported.

   The flags determine:

   -  Compression algorithm: zlib/CBF/none
   -  Plugin registration method: automatic/manual

   :param h5handle: The NeXus file to write data to.
   :param axisConfig: The configuration settings desribing the axes and their relation to the sample and to each other.