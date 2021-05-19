cbf_h5handle_struct
*******************

.. py:class:: cbf_h5handle_struct

.. py:method:: cbf_h5handle_struct.h5handle_get_file(file)


   Get the current id of the file within the given handle.

   Check the handle for the presence of a file, optionally returning it.

   :param file: A place to store the file (if found), or null if the file isn't wanted.

.. py:method:: cbf_h5handle_struct.h5handle_get_beam(group, name)


   Get the current id and name of the beam group within the given
   handle.

   Check the handle for the presence of a beam group and its name,
   optionally returning any combination of them. The error code
   'CBF_NOTFOUND' will be returned if any of the requested items of data
   cannot be found.

   The handle retains ownership of the returned object and/or string,
   neither of them should be free'd by the caller.

   :param group: A place to store the group (if found), or null if the group isn't wanted.
   :param name: A place to store the name of the group (if found), or null if the name isn't wanted.

.. py:method:: cbf_h5handle_struct.h5handle_set_beam(group, name)


   Set the id and name of the beam group within the given handle.

   Sets the beam group and name within the handle to the given values.
   Doesn't check or modify the ``NX_class`` attribute in any way. The
   handle will take ownership of the group id iff this function
   succeeds.

   :param group: The group to be set as the current beam group
   :param name: The name which the group should be given.

.. py:method:: cbf_h5handle_struct.h5handle_require_beam(group, name)


   Ensure I have a beam in the hdf5 handle.

   This will check if the beam group within the handle matches any
   existing group of the same name within the current file. If they
   don't match a new group is opened or created and added to the handle.
   The ``NX_class`` attributes are not checked.

   :param group: An optional pointer to a place where the group should be stored.
   :param name: The group name, or null to use the default name of "beam".

.. py:method:: cbf_h5handle_struct.h5handle_get_instrument(group, name)


   Get the current id and name of the instrument group within the given
   handle.

   Check the handle for the presence of an instrument group and its
   name, optionally returning any combination of them. The error code
   'CBF_NOTFOUND' will be returned if any of the requested items of data
   cannot be found.

   The handle retains ownership of the returned object and/or string,
   neither of them should be free'd by the caller.

   :param group: A place to store the group (if found), or null if the group isn't wanted.
   :param name: A place to store the name of the group (if found), or null if the name isn't wanted.

.. py:method:: cbf_h5handle_struct.h5handle_set_instrument(group, name)


   Set the id and name of the instrument group within the given handle.

   Sets the instrument group and name within the handle to the given
   values. Doesn't check or modify the ``NX_class`` attribute in any
   way. The handle will take ownership of the group id iff this function
   succeeds.

   :param group: The group to be set as the current instrument group
   :param name: The name which the group should be given.

.. py:method:: cbf_h5handle_struct.h5handle_find_instrument(group, name)


   Find an existing instrument group within the given handle.

   :param group:
   :param name:

.. py:method:: cbf_h5handle_struct.h5handle_require_instrument(group, name)


   Ensure I have an instrument in the hdf5 handle.

   This will check if the instrument group within the handle matches any
   existing group of the same name within the current file. If they
   don't match a new group is opened or created and added to the handle.
   The ``NX_class`` attributes are not checked.

   :param group: An optional pointer to a place where the group should be stored.
   :param name: The group name, or null to use the default name of "instrument".

.. py:method:: cbf_h5handle_struct.h5handle_get_detector(group, name)


   Get the current id and name of the detector group within the given
   handle.

   Check the handle for the presence of an detector group and its name,
   optionally returning any combination of them. The error code
   'CBF_NOTFOUND' will be returned if any of the requested items of data
   cannot be found.

   The handle retains ownership of the returned object and/or string,
   neither of them should be free'd by the caller.

   :param group: A place to store the group (if found), or null if the group isn't wanted.
   :param name: A place to store the name of the group (if found), or null if the name isn't wanted.

.. py:method:: cbf_h5handle_struct.h5handle_set_detector(group, name)


   Set the id and name of the detector group within the given handle.

   Sets the detector group and name within the handle to the given
   values. Doesn't check or modify the ``NX_class`` attribute in any
   way. The handle will take ownership of the group id iff this function
   succeeds.

   :param group: The group to be set as the current detector group
   :param name: The name which the group should be given.

.. py:method:: cbf_h5handle_struct.h5handle_find_detector(group, name)


   Find an existing detector group within the given handle.

   :param group:
   :param name:

.. py:method:: cbf_h5handle_struct.h5handle_set_file(file)


   Set the id of the file within the given handle.

   Sets the file id within the handle to the given value. Doesn't check
   or modify any attributes in any way.

   :param file: The file to be set as the current file id.

.. py:method:: cbf_h5handle_struct.h5handle_require_detector(group, name)


   Ensure I have a detector in the hdf5 handle.

   This will check if the detector group within the handle matches any
   existing group of the same name within the current file. If they
   don't match a new group is opened or created and added to the handle.
   The ``NX_class`` attributes are not checked.

   :param group: An optional pointer to a place where the group should be stored.
   :param name: The group name, or null to use the default name of "detector".

.. py:method:: cbf_h5handle_struct.h5handle_get_goniometer(group, name)


   Get the current id and name of the goniometer group within the given
   handle.

   Check the handle for the presence of an goniometer group and its
   name, optionally returning any combination of them. The error code
   'CBF_NOTFOUND' will be returned if any of the requested items of data
   cannot be found.

   The handle retains ownership of the returned object and/or string,
   neither of them should be free'd by the caller.

   :param group: A place to store the group (if found), or null if the group isn't wanted.
   :param name: A place to store the name of the group (if found), or null if the name isn't wanted.

.. py:method:: cbf_h5handle_struct.h5handle_set_goniometer(group, name)


   Set the id and name of the goniometer group within the given handle.

   Sets the goniometer group and name within the handle to the given
   values. Doesn't check or modify the ``NX_class`` attribute in any
   way. The handle will take ownership of the group id iff this function
   succeeds.

   :param group: The group to be set as the current goniometer group
   :param name: The name which the group should be given.

.. py:method:: cbf_h5handle_struct.h5handle_require_goniometer(group, name)


   Ensure I have a goniometer in the hdf5 handle.

   This will check if the goniometer group within the handle matches any
   existing group of the same name within the current file. If they
   don't match a new group is opened or created and added to the handle.
   The ``NX_class`` attributes are not checked.

   :param group: An optional pointer to a place where the group should be stored.
   :param name: The group name, or null to use the default name of "goniometer".

.. py:method:: cbf_h5handle_struct.h5handle_get_monochromator(group, name)


   Get the current id and name of the monochromator group within the
   given handle.

   Check the handle for the presence of an monochromator group and its
   name, optionally returning any combination of them. The error code
   'CBF_NOTFOUND' will be returned if any of the requested items of data
   cannot be found.

   The handle retains ownership of the returned object and/or string,
   neither of them should be free'd by the caller.

   :param group: A place to store the group (if found), or null if the group isn't wanted.
   :param name: A place to store the name of the group (if found), or null if the name isn't wanted.

.. py:method:: cbf_h5handle_struct.h5handle_set_monochromator(group, name)


   Set the id and name of the monochromator group within the given
   handle.

   Sets the monochromator group and name within the handle to the given
   values. Doesn't check or modify the ``NX_class`` attribute in any
   way. The handle will take ownership of the group id iff this function
   succeeds.

   :param group: The group to be set as the current monochromator group
   :param name: The name which the group should be given.

.. py:method:: cbf_h5handle_struct.h5handle_require_monochromator(group, name)


   Ensure I have a monochromator in the hdf5 handle.

   This will check if the monochromator group within the handle matches
   any existing group of the same name within the current file. If they
   don't match a new group is opened or created and added to the handle.
   The ``NX_class`` attributes are not checked.

   :param group: An optional pointer to a place where the group should be stored.
   :param name: The group name, or null to use the default name of "monochromator".

.. py:method:: cbf_h5handle_struct.h5handle_get_source(group, name)


   Get the current id and name of the source group within the given
   handle.

   Check the handle for the presence of an source group and its name,
   optionally returning any combination of them. The error code
   'CBF_NOTFOUND' will be returned if any of the requested items of data
   cannot be found.

   The handle retains ownership of the returned object and/or string,
   neither of them should be free'd by the caller.

   :param group: A place to store the group (if found), or null if the group isn't wanted.
   :param name: A place to store the name of the group (if found), or null if the name isn't wanted.

.. py:method:: cbf_h5handle_struct.h5handle_set_source(group, name)


   Set the id and name of the source group within the given handle.

   Sets the source group and name within the handle to the given values.
   Doesn't check or modify the ``NX_class`` attribute in any way. The
   handle will take ownership of the group id iff this function
   succeeds.

   :param group: The group to be set as the current source group
   :param name: The name which the group should be given.

.. py:method:: cbf_h5handle_struct.h5handle_require_source(group, name)


   Ensure I have a source in the hdf5 handle.

   This will check if the source group within the handle matches any
   existing group of the same name within the current file. If they
   don't match a new group is opened or created and added to the handle.
   The ``NX_class`` attributes are not checked.

   :param group: An optional pointer to a place where the group should be stored.
   :param name: The group name, or null to use the default name of "source".

.. py:method:: cbf_h5handle_struct.h5handle_get_entry(group, name)


   Get the current id and name of the entry group within the given
   handle.

   Check the handle for the presence of an entry group and its name,
   optionally returning any combination of them. The error code
   'CBF_NOTFOUND' will be returned if any of the requested items of data
   cannot be found.

   The handle retains ownership of the returned object and/or string,
   neither of them should be free'd by the caller.

   :param group: A place to store the group (if found), or null if the group isn't wanted.
   :param name: A place to store the name of the group (if found), or null if the name isn't wanted.

.. py:method:: cbf_h5handle_struct.free_h5handle()


   Free a handle for an HDF5 file.

   Checks if the handle appears to be valid, the free's the handle and
   any data that the handle owns.


.. py:method:: cbf_h5handle_struct.create_h5handle3(file)


   Allocates space for a HDF5 file handle and associates it with the
   given file.

   This function expects the user to create or open a hdf5 file with the
   appropriate parameters for what they are trying to do, replacing
   older functions which would create a file with the ``H5F_ACC_TRUNC``
   flag and ``H5F_CLOSE_STRONG`` property.

   :param file: A HDF5 file to store within the newly created handle.

.. py:method:: cbf_h5handle_struct.write_nx2cbf(cbf)


   Extract data from a nexus file and store it in a CBF file.

   Reads NeXus-format data from the entry group defined in the ``nx``
   handle, extracting data related to the frame with index ``nx->slice``
   and in CBF-format within the the ``cbf`` handle.

   :param cbf: The handle in which to store the resulting CBF data.

.. py:method:: cbf_h5handle_struct.h5handle_set_entry(group, name)


   Set the id and name of the entry group within the given handle.

   Sets the entry group and name within the handle to the given values.
   Doesn't check or modify the ``NX_class`` attribute in any way. The
   handle will take ownership of the group id iff this function
   succeeds.

   :param group: The group to be set as the current entry group
   :param name: The name which the group should be given.

.. py:method:: cbf_h5handle_struct.h5handle_require_entry(group, name)


   Ensure I have an entry in the hdf5 handle.

   This will check if the entry group within the handle matches any
   existing group of the same name within the current file. If they
   don't match a new group is opened or created and added to the handle.
   The ``NX_class`` attributes are not checked.

   :param group: An optional pointer to a place where the group should be stored.
   :param name: The group name, or null to use the default name of "entry".

.. py:method:: cbf_h5handle_struct.h5handle_require_entry_definition(group, name, definition, version, URL)


   Ensure I have an entry in the hdf5 handle with definition.

   This will check if the entry group and definition within the handle
   matches any existing group of the same name within the current file
   and has a definition designation that agrees. If the group name
   doesn't match a new group is opened or created and added to the
   handle. If the ``definition`` does not match, it is replaced with the
   new one. If the ``version`` attribute does not match it is replaced
   with the new one. If the ``URL>`` attribute does not match it is
   replace with the new one. The ``NX_class`` attributes are not
   checked, but if a new entry is created it will be created with
   ``NX_class`` NXentry.

   :param group: An optional pointer to a place where the group ID should be stored.
   :param name: The group name, or null to use the default name of "entry".
   :param definition: The definition name, or null to not specify a definition name.
   :param version: The version string, or null to not specify a version string.
   :param URL: The URL at which the definition is stored, or null to not specify a URL

.. py:method:: cbf_h5handle_struct.h5handle_get_sample(group, name)


   Get the current id and name of the sample group within the given
   handle.

   Check the handle for the presence of an sample group and its name,
   optionally returning any combination of them.

   :param group: A place to store the group (if found), or null if the group isn't wanted.
   :param name: A place to store the name of the group (if found), or null if the name isn't wanted.

.. py:method:: cbf_h5handle_struct.h5handle_set_sample(group, name)


   Set the id and name of the sample group within the given handle.

   Sets the sample group and name within the handle to the given values.
   Doesn't check or modify the ``NX_class`` attribute in any way. The
   handle will take ownership of the group id iff this function
   succeeds.

   :param group: The group to be set as the current sample group
   :param name: The name which the group should be given.

.. py:method:: cbf_h5handle_struct.h5handle_require_sample(group, name)


   Ensure I have a sample in the hdf5 handle.

   This will check if the sample group within the handle matches any
   existing group of the same name within the current file. If they
   don't match a new group is opened or created and added to the handle.
   The ``NX_class`` attributes are not checked.

   :param group: An optional pointer to a place where the group should be stored.
   :param name: The group name, or null to use the default name of "sample".