cbf_detector_struct
*******************

.. py:class:: cbf_detector_struct

.. py:method:: cbf_detector_struct.free_detector()

   cbf_free_detector destroys the detector object specified by detector and frees all associated memory.



.. py:method:: cbf_detector_struct.get_beam_center(indexslow, indexfast, centerslow, centerfast)

   cbf_get_beam_center sets \*centerfast and \*centerslow to the displacements in mm
   along the detector axes from pixel (0, 0) to the point at which the beam intersects the
   detector and \*indexfast and \*indexslow to the corresponding indices.
   cbf_set_beam_center sets the offsets in the axis category for the detector element
   axis with precedence 1 to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  \*indexfast and
   \*indexslow.  cbf_set_reference_beam_center sets the displacments in the array_structure_list_axis
   category to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  by \*indexfast and
   \*indexslow.  In order to achieve consistent results, a reference detector should be used
   for detector to have all axes at their reference settings.

   Note that the precedence 1 axis is the fastest axis, so that \*centerfast and \*indexfast
   are the fast axis components of the center and \*centerslow and \*indexslow are the
   slow axis components of the center.

   The _fs calls give the displacments in a fast-to-slow order.  The calls with no suffix and the
   calls _sf calls give the displacements in slow-to-fast order

   Any of the destination pointers may be NULL for getting the beam center.  For setting the beam
   axis, either the indices of the center must not be NULL.

   The indices are non-negative for beam centers within the detector surface, but the center for an axis with
   a negative increment will be negative for a beam center within the detector surface.

   For cbf_set_beam_center if the diffrn_data_frame category exists with a row for the corresponding element id,
   the values will be set for _diffrn_data_frame.center_fast and _diffrn_data_frame.center_slow
   in millimetres and the value of _diffrn_data_frame.center_units will be set to 'mm'.

   For cbf_set_reference_beam_center if the diffrn_detector_element category exists with a row for the corresponding element id,
   the values will be set for _diffrn_detector_element.reference_center_fast and _diffrn_detector_element.reference_center_slow
   in millimetres and the value of _diffrn_detector_element.reference_units will be set to 'mm'.

   :param indexslow: Pointer to the destination slow index.
   :param indexfast: Pointer to the destination fast index.
   :param centerslow: Pointer to the destination displacement along the slow axis.
   :param centerfast: Pointer to the destination displacement along the fast axis.

.. py:method:: cbf_detector_struct.get_beam_center_fs(indexfast, indexslow, centerfast, centerslow)

   cbf_get_beam_center sets \*centerfast and \*centerslow to the displacements in mm
   along the detector axes from pixel (0, 0) to the point at which the beam intersects the
   detector and \*indexfast and \*indexslow to the corresponding indices.
   cbf_set_beam_center sets the offsets in the axis category for the detector element
   axis with precedence 1 to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  \*indexfast and
   \*indexslow.  cbf_set_reference_beam_center sets the displacments in the array_structure_list_axis
   category to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  by \*indexfast and
   \*indexslow.  In order to achieve consistent results, a reference detector should be used
   for detector to have all axes at their reference settings.

   Note that the precedence 1 axis is the fastest axis, so that \*centerfast and \*indexfast
   are the fast axis components of the center and \*centerslow and \*indexslow are the
   slow axis components of the center.

   The _fs calls give the displacments in a fast-to-slow order.  The calls with no suffix and the
   calls _sf calls give the displacements in slow-to-fast order

   Any of the destination pointers may be NULL for getting the beam center.  For setting the beam
   axis, either the indices of the center must not be NULL.

   The indices are non-negative for beam centers within the detector surface, but the center for an axis with
   a negative increment will be negative for a beam center within the detector surface.

   For cbf_set_beam_center if the diffrn_data_frame category exists with a row for the corresponding element id,
   the values will be set for _diffrn_data_frame.center_fast and _diffrn_data_frame.center_slow
   in millimetres and the value of _diffrn_data_frame.center_units will be set to 'mm'.

   For cbf_set_reference_beam_center if the diffrn_detector_element category exists with a row for the corresponding element id,
   the values will be set for _diffrn_detector_element.reference_center_fast and _diffrn_detector_element.reference_center_slow
   in millimetres and the value of _diffrn_detector_element.reference_units will be set to 'mm'.

   :param indexfast: Pointer to the destination fast index.
   :param indexslow: Pointer to the destination slow index.
   :param centerfast: Pointer to the destination displacement along the fast axis.
   :param centerslow: Pointer to the destination displacement along the slow axis.

.. py:method:: cbf_detector_struct.get_beam_center_sf(indexslow, indexfast, centerslow, centerfast)

   cbf_get_beam_center sets \*centerfast and \*centerslow to the displacements in mm
   along the detector axes from pixel (0, 0) to the point at which the beam intersects the
   detector and \*indexfast and \*indexslow to the corresponding indices.
   cbf_set_beam_center sets the offsets in the axis category for the detector element
   axis with precedence 1 to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  \*indexfast and
   \*indexslow.  cbf_set_reference_beam_center sets the displacments in the array_structure_list_axis
   category to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  by \*indexfast and
   \*indexslow.  In order to achieve consistent results, a reference detector should be used
   for detector to have all axes at their reference settings.

   Note that the precedence 1 axis is the fastest axis, so that \*centerfast and \*indexfast
   are the fast axis components of the center and \*centerslow and \*indexslow are the
   slow axis components of the center.

   The _fs calls give the displacments in a fast-to-slow order.  The calls with no suffix and the
   calls _sf calls give the displacements in slow-to-fast order

   Any of the destination pointers may be NULL for getting the beam center.  For setting the beam
   axis, either the indices of the center must not be NULL.

   The indices are non-negative for beam centers within the detector surface, but the center for an axis with
   a negative increment will be negative for a beam center within the detector surface.

   For cbf_set_beam_center if the diffrn_data_frame category exists with a row for the corresponding element id,
   the values will be set for _diffrn_data_frame.center_fast and _diffrn_data_frame.center_slow
   in millimetres and the value of _diffrn_data_frame.center_units will be set to 'mm'.

   For cbf_set_reference_beam_center if the diffrn_detector_element category exists with a row for the corresponding element id,
   the values will be set for _diffrn_detector_element.reference_center_fast and _diffrn_detector_element.reference_center_slow
   in millimetres and the value of _diffrn_detector_element.reference_units will be set to 'mm'.

   :param indexslow: Pointer to the destination slow index.
   :param indexfast: Pointer to the destination fast index.
   :param centerslow: Pointer to the destination displacement along the slow axis.
   :param centerfast: Pointer to the destination displacement along the fast axis.

.. py:method:: cbf_detector_struct.set_beam_center(indexslow, indexfast, centerslow, centerfast)

   cbf_get_beam_center sets \*centerfast and \*centerslow to the displacements in mm
   along the detector axes from pixel (0, 0) to the point at which the beam intersects the
   detector and \*indexfast and \*indexslow to the corresponding indices.
   cbf_set_beam_center sets the offsets in the axis category for the detector element
   axis with precedence 1 to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  \*indexfast and
   \*indexslow.  cbf_set_reference_beam_center sets the displacments in the array_structure_list_axis
   category to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  by \*indexfast and
   \*indexslow.  In order to achieve consistent results, a reference detector should be used
   for detector to have all axes at their reference settings.

   Note that the precedence 1 axis is the fastest axis, so that \*centerfast and \*indexfast
   are the fast axis components of the center and \*centerslow and \*indexslow are the
   slow axis components of the center.

   The _fs calls give the displacments in a fast-to-slow order.  The calls with no suffix and the
   calls _sf calls give the displacements in slow-to-fast order

   Any of the destination pointers may be NULL for getting the beam center.  For setting the beam
   axis, either the indices of the center must not be NULL.

   The indices are non-negative for beam centers within the detector surface, but the center for an axis with
   a negative increment will be negative for a beam center within the detector surface.

   For cbf_set_beam_center if the diffrn_data_frame category exists with a row for the corresponding element id,
   the values will be set for _diffrn_data_frame.center_fast and _diffrn_data_frame.center_slow
   in millimetres and the value of _diffrn_data_frame.center_units will be set to 'mm'.

   For cbf_set_reference_beam_center if the diffrn_detector_element category exists with a row for the corresponding element id,
   the values will be set for _diffrn_detector_element.reference_center_fast and _diffrn_detector_element.reference_center_slow
   in millimetres and the value of _diffrn_detector_element.reference_units will be set to 'mm'.

   :param indexslow: Pointer to the destination slow index.
   :param indexfast: Pointer to the destination fast index.
   :param centerslow: Pointer to the destination displacement along the slow axis.
   :param centerfast: Pointer to the destination displacement along the fast axis.

.. py:method:: cbf_detector_struct.set_beam_center_fs(indexfast, indexslow, centerfast, centerslow)

   cbf_get_beam_center sets \*centerfast and \*centerslow to the displacements in mm
   along the detector axes from pixel (0, 0) to the point at which the beam intersects the
   detector and \*indexfast and \*indexslow to the corresponding indices.
   cbf_set_beam_center sets the offsets in the axis category for the detector element
   axis with precedence 1 to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  \*indexfast and
   \*indexslow.  cbf_set_reference_beam_center sets the displacments in the array_structure_list_axis
   category to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  by \*indexfast and
   \*indexslow.  In order to achieve consistent results, a reference detector should be used
   for detector to have all axes at their reference settings.

   Note that the precedence 1 axis is the fastest axis, so that \*centerfast and \*indexfast
   are the fast axis components of the center and \*centerslow and \*indexslow are the
   slow axis components of the center.

   The _fs calls give the displacments in a fast-to-slow order.  The calls with no suffix and the
   calls _sf calls give the displacements in slow-to-fast order

   Any of the destination pointers may be NULL for getting the beam center.  For setting the beam
   axis, either the indices of the center must not be NULL.

   The indices are non-negative for beam centers within the detector surface, but the center for an axis with
   a negative increment will be negative for a beam center within the detector surface.

   For cbf_set_beam_center if the diffrn_data_frame category exists with a row for the corresponding element id,
   the values will be set for _diffrn_data_frame.center_fast and _diffrn_data_frame.center_slow
   in millimetres and the value of _diffrn_data_frame.center_units will be set to 'mm'.

   For cbf_set_reference_beam_center if the diffrn_detector_element category exists with a row for the corresponding element id,
   the values will be set for _diffrn_detector_element.reference_center_fast and _diffrn_detector_element.reference_center_slow
   in millimetres and the value of _diffrn_detector_element.reference_units will be set to 'mm'.

   :param indexfast: Pointer to the destination fast index.
   :param indexslow: Pointer to the destination slow index.
   :param centerfast: Pointer to the destination displacement along the fast axis.
   :param centerslow: Pointer to the destination displacement along the slow axis.

.. py:method:: cbf_detector_struct.set_beam_center_sf(indexslow, indexfast, centerslow, centerfast)

   cbf_get_beam_center sets \*centerfast and \*centerslow to the displacements in mm
   along the detector axes from pixel (0, 0) to the point at which the beam intersects the
   detector and \*indexfast and \*indexslow to the corresponding indices.
   cbf_set_beam_center sets the offsets in the axis category for the detector element
   axis with precedence 1 to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  \*indexfast and
   \*indexslow.  cbf_set_reference_beam_center sets the displacments in the array_structure_list_axis
   category to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  by \*indexfast and
   \*indexslow.  In order to achieve consistent results, a reference detector should be used
   for detector to have all axes at their reference settings.

   Note that the precedence 1 axis is the fastest axis, so that \*centerfast and \*indexfast
   are the fast axis components of the center and \*centerslow and \*indexslow are the
   slow axis components of the center.

   The _fs calls give the displacments in a fast-to-slow order.  The calls with no suffix and the
   calls _sf calls give the displacements in slow-to-fast order

   Any of the destination pointers may be NULL for getting the beam center.  For setting the beam
   axis, either the indices of the center must not be NULL.

   The indices are non-negative for beam centers within the detector surface, but the center for an axis with
   a negative increment will be negative for a beam center within the detector surface.

   For cbf_set_beam_center if the diffrn_data_frame category exists with a row for the corresponding element id,
   the values will be set for _diffrn_data_frame.center_fast and _diffrn_data_frame.center_slow
   in millimetres and the value of _diffrn_data_frame.center_units will be set to 'mm'.

   For cbf_set_reference_beam_center if the diffrn_detector_element category exists with a row for the corresponding element id,
   the values will be set for _diffrn_detector_element.reference_center_fast and _diffrn_detector_element.reference_center_slow
   in millimetres and the value of _diffrn_detector_element.reference_units will be set to 'mm'.

   :param indexslow: Pointer to the destination slow index.
   :param indexfast: Pointer to the destination fast index.
   :param centerslow: Pointer to the destination displacement along the slow axis.
   :param centerfast: Pointer to the destination displacement along the fast axis.

.. py:method:: cbf_detector_struct.set_reference_beam_center(indexslow, indexfast, centerslow, centerfast)

   cbf_get_beam_center sets \*centerfast and \*centerslow to the displacements in mm
   along the detector axes from pixel (0, 0) to the point at which the beam intersects the
   detector and \*indexfast and \*indexslow to the corresponding indices.
   cbf_set_beam_center sets the offsets in the axis category for the detector element
   axis with precedence 1 to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  \*indexfast and
   \*indexslow.  cbf_set_reference_beam_center sets the displacments in the array_structure_list_axis
   category to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  by \*indexfast and
   \*indexslow.  In order to achieve consistent results, a reference detector should be used
   for detector to have all axes at their reference settings.

   Note that the precedence 1 axis is the fastest axis, so that \*centerfast and \*indexfast
   are the fast axis components of the center and \*centerslow and \*indexslow are the
   slow axis components of the center.

   The _fs calls give the displacments in a fast-to-slow order.  The calls with no suffix and the
   calls _sf calls give the displacements in slow-to-fast order

   Any of the destination pointers may be NULL for getting the beam center.  For setting the beam
   axis, either the indices of the center must not be NULL.

   The indices are non-negative for beam centers within the detector surface, but the center for an axis with
   a negative increment will be negative for a beam center within the detector surface.

   For cbf_set_beam_center if the diffrn_data_frame category exists with a row for the corresponding element id,
   the values will be set for _diffrn_data_frame.center_fast and _diffrn_data_frame.center_slow
   in millimetres and the value of _diffrn_data_frame.center_units will be set to 'mm'.

   For cbf_set_reference_beam_center if the diffrn_detector_element category exists with a row for the corresponding element id,
   the values will be set for _diffrn_detector_element.reference_center_fast and _diffrn_detector_element.reference_center_slow
   in millimetres and the value of _diffrn_detector_element.reference_units will be set to 'mm'.

   :param indexslow: Pointer to the destination slow index.
   :param indexfast: Pointer to the destination fast index.
   :param centerslow: Pointer to the destination displacement along the slow axis.
   :param centerfast: Pointer to the destination displacement along the fast axis.

.. py:method:: cbf_detector_struct.set_reference_beam_center_fs(indexfast, indexslow, centerfast, centerslow)

   cbf_get_beam_center sets \*centerfast and \*centerslow to the displacements in mm
   along the detector axes from pixel (0, 0) to the point at which the beam intersects the
   detector and \*indexfast and \*indexslow to the corresponding indices.
   cbf_set_beam_center sets the offsets in the axis category for the detector element
   axis with precedence 1 to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  \*indexfast and
   \*indexslow.  cbf_set_reference_beam_center sets the displacments in the array_structure_list_axis
   category to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  by \*indexfast and
   \*indexslow.  In order to achieve consistent results, a reference detector should be used
   for detector to have all axes at their reference settings.

   Note that the precedence 1 axis is the fastest axis, so that \*centerfast and \*indexfast
   are the fast axis components of the center and \*centerslow and \*indexslow are the
   slow axis components of the center.

   The _fs calls give the displacments in a fast-to-slow order.  The calls with no suffix and the
   calls _sf calls give the displacements in slow-to-fast order

   Any of the destination pointers may be NULL for getting the beam center.  For setting the beam
   axis, either the indices of the center must not be NULL.

   The indices are non-negative for beam centers within the detector surface, but the center for an axis with
   a negative increment will be negative for a beam center within the detector surface.

   For cbf_set_beam_center if the diffrn_data_frame category exists with a row for the corresponding element id,
   the values will be set for _diffrn_data_frame.center_fast and _diffrn_data_frame.center_slow
   in millimetres and the value of _diffrn_data_frame.center_units will be set to 'mm'.

   For cbf_set_reference_beam_center if the diffrn_detector_element category exists with a row for the corresponding element id,
   the values will be set for _diffrn_detector_element.reference_center_fast and _diffrn_detector_element.reference_center_slow
   in millimetres and the value of _diffrn_detector_element.reference_units will be set to 'mm'.

   :param indexfast: Pointer to the destination fast index.
   :param indexslow: Pointer to the destination slow index.
   :param centerfast: Pointer to the destination displacement along the fast axis.
   :param centerslow: Pointer to the destination displacement along the slow axis.

.. py:method:: cbf_detector_struct.set_reference_beam_center_sf(indexslow, indexfast, centerslow, centerfast)

   cbf_get_beam_center sets \*centerfast and \*centerslow to the displacements in mm
   along the detector axes from pixel (0, 0) to the point at which the beam intersects the
   detector and \*indexfast and \*indexslow to the corresponding indices.
   cbf_set_beam_center sets the offsets in the axis category for the detector element
   axis with precedence 1 to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  \*indexfast and
   \*indexslow.  cbf_set_reference_beam_center sets the displacments in the array_structure_list_axis
   category to place the beam center at the position given in mm by \*centerfast
   and \*centerslow as the displacements in mm along the detector axes from pixel (0, 0)
   to the point at which the beam intersects the detector at the indices given  by \*indexfast and
   \*indexslow.  In order to achieve consistent results, a reference detector should be used
   for detector to have all axes at their reference settings.

   Note that the precedence 1 axis is the fastest axis, so that \*centerfast and \*indexfast
   are the fast axis components of the center and \*centerslow and \*indexslow are the
   slow axis components of the center.

   The _fs calls give the displacments in a fast-to-slow order.  The calls with no suffix and the
   calls _sf calls give the displacements in slow-to-fast order

   Any of the destination pointers may be NULL for getting the beam center.  For setting the beam
   axis, either the indices of the center must not be NULL.

   The indices are non-negative for beam centers within the detector surface, but the center for an axis with
   a negative increment will be negative for a beam center within the detector surface.

   For cbf_set_beam_center if the diffrn_data_frame category exists with a row for the corresponding element id,
   the values will be set for _diffrn_data_frame.center_fast and _diffrn_data_frame.center_slow
   in millimetres and the value of _diffrn_data_frame.center_units will be set to 'mm'.

   For cbf_set_reference_beam_center if the diffrn_detector_element category exists with a row for the corresponding element id,
   the values will be set for _diffrn_detector_element.reference_center_fast and _diffrn_detector_element.reference_center_slow
   in millimetres and the value of _diffrn_detector_element.reference_units will be set to 'mm'.

   :param indexslow: Pointer to the destination slow index.
   :param indexfast: Pointer to the destination fast index.
   :param centerslow: Pointer to the destination displacement along the slow axis.
   :param centerfast: Pointer to the destination displacement along the fast axis.

.. py:method:: cbf_detector_struct.get_detector_distance(distance)

   cbf_get_detector_distance sets \*distance to the nearest distance from the sample position to the detector plane.


   :param distance: Pointer to the destination distance.

.. py:method:: cbf_detector_struct.get_detector_normal(normal1, normal2, normal3)

   cbf_get_detector_normal sets \*normal1, \*normal2, and \*normal3 to the 3 components of the of the normal vector to the detector plane.  The vector is normalized.

   Any of the destination pointers may be NULL.

   :param normal1: Pointer to the destination x component of the normal vector.
   :param normal2: Pointer to the destination y component of the normal vector.
   :param normal3: Pointer to the destination z component of the normal vector.

.. py:method:: cbf_detector_struct.get_detector_axes(slowaxis1, slowaxis2, slowaxis3, fastaxis1, fastaxis2, fastaxis3)

   cbf_get_detector_axis_slow sets \*slowaxis1, \*slowaxis2, and \*slowaxis3 to the 3 components of
   the slow axis of the specified detector at the current settings of all axes.
   cbf_get_detector_axis_slow sets \*fastaxis1, \*fastaxis2, and \*fastaxis3 to the 3 components of
   the fast axis of the specified detector at the current settings of all axes.
   cbf_get_detector_axes, cbf_get_detector_axes_fs and int cbf_get_detector_axes_sf set  
   \*slowaxis1, \*slowaxis2, and \*slowaxis3 to the 3 components of
   the slow axis and \*fastaxis1, \*fastaxis2, and \*fastaxis3 to the 3 components of
   the fast axis of the specified detector at the current settings of all axes.
   cbf_get_detector_surface_axes sets \*axis_id1 and \*axis_id2
   to the names of the two surface axes of the detector or ".",

   Any of the destination pointers may be NULL.

   :param slowaxis1: Pointer to the destination x component of the slow axis vector.
   :param slowaxis2: Pointer to the destination y component of the slow axis vector.
   :param slowaxis3: Pointer to the destination z component of the slow axis vector.
   :param fastaxis1: Pointer to the destination x component of the fast axis vector.
   :param fastaxis2: Pointer to the destination y component of the fast axis vector.
   :param fastaxis3: Pointer to the destination z component of the fast axis vector.

.. py:method:: cbf_detector_struct.get_detector_axes_fs(fastaxis1, fastaxis2, fastaxis3, slowaxis1, slowaxis2, slowaxis3)

   cbf_get_detector_axis_slow sets \*slowaxis1, \*slowaxis2, and \*slowaxis3 to the 3 components of
   the slow axis of the specified detector at the current settings of all axes.
   cbf_get_detector_axis_slow sets \*fastaxis1, \*fastaxis2, and \*fastaxis3 to the 3 components of
   the fast axis of the specified detector at the current settings of all axes.
   cbf_get_detector_axes, cbf_get_detector_axes_fs and int cbf_get_detector_axes_sf set  
   \*slowaxis1, \*slowaxis2, and \*slowaxis3 to the 3 components of
   the slow axis and \*fastaxis1, \*fastaxis2, and \*fastaxis3 to the 3 components of
   the fast axis of the specified detector at the current settings of all axes.
   cbf_get_detector_surface_axes sets \*axis_id1 and \*axis_id2
   to the names of the two surface axes of the detector or ".",

   Any of the destination pointers may be NULL.

   :param fastaxis1: Pointer to the destination x component of the fast axis vector.
   :param fastaxis2: Pointer to the destination y component of the fast axis vector.
   :param fastaxis3: Pointer to the destination z component of the fast axis vector.
   :param slowaxis1: Pointer to the destination x component of the slow axis vector.
   :param slowaxis2: Pointer to the destination y component of the slow axis vector.
   :param slowaxis3: Pointer to the destination z component of the slow axis vector.

.. py:method:: cbf_detector_struct.get_detector_axes_sf(slowaxis1, slowaxis2, slowaxis3, fastaxis1, fastaxis2, fastaxis3)

   cbf_get_detector_axis_slow sets \*slowaxis1, \*slowaxis2, and \*slowaxis3 to the 3 components of
   the slow axis of the specified detector at the current settings of all axes.
   cbf_get_detector_axis_slow sets \*fastaxis1, \*fastaxis2, and \*fastaxis3 to the 3 components of
   the fast axis of the specified detector at the current settings of all axes.
   cbf_get_detector_axes, cbf_get_detector_axes_fs and int cbf_get_detector_axes_sf set  
   \*slowaxis1, \*slowaxis2, and \*slowaxis3 to the 3 components of
   the slow axis and \*fastaxis1, \*fastaxis2, and \*fastaxis3 to the 3 components of
   the fast axis of the specified detector at the current settings of all axes.
   cbf_get_detector_surface_axes sets \*axis_id1 and \*axis_id2
   to the names of the two surface axes of the detector or ".",

   Any of the destination pointers may be NULL.

   :param slowaxis1: Pointer to the destination x component of the slow axis vector.
   :param slowaxis2: Pointer to the destination y component of the slow axis vector.
   :param slowaxis3: Pointer to the destination z component of the slow axis vector.
   :param fastaxis1: Pointer to the destination x component of the fast axis vector.
   :param fastaxis2: Pointer to the destination y component of the fast axis vector.
   :param fastaxis3: Pointer to the destination z component of the fast axis vector.

.. py:method:: cbf_detector_struct.get_detector_axis_fast(fastaxis1, fastaxis2, fastaxis3)

   cbf_get_detector_axis_slow sets \*slowaxis1, \*slowaxis2, and \*slowaxis3 to the 3 components of
   the slow axis of the specified detector at the current settings of all axes.
   cbf_get_detector_axis_slow sets \*fastaxis1, \*fastaxis2, and \*fastaxis3 to the 3 components of
   the fast axis of the specified detector at the current settings of all axes.
   cbf_get_detector_axes, cbf_get_detector_axes_fs and int cbf_get_detector_axes_sf set  
   \*slowaxis1, \*slowaxis2, and \*slowaxis3 to the 3 components of
   the slow axis and \*fastaxis1, \*fastaxis2, and \*fastaxis3 to the 3 components of
   the fast axis of the specified detector at the current settings of all axes.
   cbf_get_detector_surface_axes sets \*axis_id1 and \*axis_id2
   to the names of the two surface axes of the detector or ".",

   Any of the destination pointers may be NULL.

   :param fastaxis1: Pointer to the destination x component of the fast axis vector.
   :param fastaxis2: Pointer to the destination y component of the fast axis vector.
   :param fastaxis3: Pointer to the destination z component of the fast axis vector.

.. py:method:: cbf_detector_struct.get_detector_axis_slow(slowaxis1, slowaxis2, slowaxis3)

   cbf_get_detector_axis_slow sets \*slowaxis1, \*slowaxis2, and \*slowaxis3 to the 3 components of
   the slow axis of the specified detector at the current settings of all axes.
   cbf_get_detector_axis_slow sets \*fastaxis1, \*fastaxis2, and \*fastaxis3 to the 3 components of
   the fast axis of the specified detector at the current settings of all axes.
   cbf_get_detector_axes, cbf_get_detector_axes_fs and int cbf_get_detector_axes_sf set  
   \*slowaxis1, \*slowaxis2, and \*slowaxis3 to the 3 components of
   the slow axis and \*fastaxis1, \*fastaxis2, and \*fastaxis3 to the 3 components of
   the fast axis of the specified detector at the current settings of all axes.
   cbf_get_detector_surface_axes sets \*axis_id1 and \*axis_id2
   to the names of the two surface axes of the detector or ".",

   Any of the destination pointers may be NULL.

   :param slowaxis1: Pointer to the destination x component of the slow axis vector.
   :param slowaxis2: Pointer to the destination y component of the slow axis vector.
   :param slowaxis3: Pointer to the destination z component of the slow axis vector.

.. py:method:: cbf_detector_struct.get_detector_surface_axes(axis_id1, axis_id2)

   cbf_get_detector_axis_slow sets \*slowaxis1, \*slowaxis2, and \*slowaxis3 to the 3 components of
   the slow axis of the specified detector at the current settings of all axes.
   cbf_get_detector_axis_slow sets \*fastaxis1, \*fastaxis2, and \*fastaxis3 to the 3 components of
   the fast axis of the specified detector at the current settings of all axes.
   cbf_get_detector_axes, cbf_get_detector_axes_fs and int cbf_get_detector_axes_sf set  
   \*slowaxis1, \*slowaxis2, and \*slowaxis3 to the 3 components of
   the slow axis and \*fastaxis1, \*fastaxis2, and \*fastaxis3 to the 3 components of
   the fast axis of the specified detector at the current settings of all axes.
   cbf_get_detector_surface_axes sets \*axis_id1 and \*axis_id2
   to the names of the two surface axes of the detector or ".",

   Any of the destination pointers may be NULL.

   :param axis_id1: Pointer to the destination first surface axis name.
   :param axis_id2: Pointer to the destination second surface axis name.

.. py:method:: cbf_detector_struct.get_pixel_coordinates(indexslow, indexfast, coordinate1, coordinate2, coordinate3)

   cbf_get_pixel_coordinates, cbf_get_pixel_coordinates_fs and cbf_get_pixel_coordinates_sf ses \*coordinate1, \*coordinate2, and \*coordinate3 
   to the vector position of pixel (indexfast, indexslow) on the detector surface.  If 
   indexslow and indexfast are integers then the coordinates
   correspond to the center of a pixel.

   Any of the destination pointers may be NULL.

   :param indexslow: Slow index.
   :param indexfast: Fast index.
   :param coordinate1: Pointer to the destination x component.
   :param coordinate2: Pointer to the destination y component.
   :param coordinate3: Pointer to the destination z component.

.. py:method:: cbf_detector_struct.get_pixel_coordinates_fs(indexfast, indexslow, coordinate1, coordinate2, coordinate3)

   cbf_get_pixel_coordinates, cbf_get_pixel_coordinates_fs and cbf_get_pixel_coordinates_sf ses \*coordinate1, \*coordinate2, and \*coordinate3 
   to the vector position of pixel (indexfast, indexslow) on the detector surface.  If 
   indexslow and indexfast are integers then the coordinates
   correspond to the center of a pixel.

   Any of the destination pointers may be NULL.

   :param indexfast: Fast index.
   :param indexslow: Slow index.
   :param coordinate1: Pointer to the destination x component.
   :param coordinate2: Pointer to the destination y component.
   :param coordinate3: Pointer to the destination z component.

.. py:method:: cbf_detector_struct.get_pixel_coordinates_sf(indexslow, indexfast, coordinate1, coordinate2, coordinate3)

   cbf_get_pixel_coordinates, cbf_get_pixel_coordinates_fs and cbf_get_pixel_coordinates_sf ses \*coordinate1, \*coordinate2, and \*coordinate3 
   to the vector position of pixel (indexfast, indexslow) on the detector surface.  If 
   indexslow and indexfast are integers then the coordinates
   correspond to the center of a pixel.

   Any of the destination pointers may be NULL.

   :param indexslow: Slow index.
   :param indexfast: Fast index.
   :param coordinate1: Pointer to the destination x component.
   :param coordinate2: Pointer to the destination y component.
   :param coordinate3: Pointer to the destination z component.

.. py:method:: cbf_detector_struct.get_pixel_normal(indexslow, indexfast, normal1, normal2, normal3)

   cbf_get_detector_normal, cbf_get_pixel_normal_fs and cbf_get_pixel_normal_sf set 
   \*normal1, \*normal2, and \*normal3 to the 3 components of the of the normal vector 
   to the pixel at (indexfast, indexslow).  The vector is normalized.

   Any of the destination pointers may be NULL.

   :param indexslow: Slow index.
   :param indexfast: Fast index.
   :param normal1: Pointer to the destination x component of the normal vector.
   :param normal2: Pointer to the destination y component of the normal vector.
   :param normal3: Pointer to the destination z component of the normal vector.

.. py:method:: cbf_detector_struct.get_pixel_normal_fs(indexfast, indexslow, normal1, normal2, normal3)

   cbf_get_detector_normal, cbf_get_pixel_normal_fs and cbf_get_pixel_normal_sf set 
   \*normal1, \*normal2, and \*normal3 to the 3 components of the of the normal vector 
   to the pixel at (indexfast, indexslow).  The vector is normalized.

   Any of the destination pointers may be NULL.

   :param indexfast: Fast index.
   :param indexslow: Slow index.
   :param normal1: Pointer to the destination x component of the normal vector.
   :param normal2: Pointer to the destination y component of the normal vector.
   :param normal3: Pointer to the destination z component of the normal vector.

.. py:method:: cbf_detector_struct.get_pixel_normal_sf(indexslow, indexfast, normal1, normal2, normal3)

   cbf_get_detector_normal, cbf_get_pixel_normal_fs and cbf_get_pixel_normal_sf set 
   \*normal1, \*normal2, and \*normal3 to the 3 components of the of the normal vector 
   to the pixel at (indexfast, indexslow).  The vector is normalized.

   Any of the destination pointers may be NULL.

   :param indexslow: Slow index.
   :param indexfast: Fast index.
   :param normal1: Pointer to the destination x component of the normal vector.
   :param normal2: Pointer to the destination y component of the normal vector.
   :param normal3: Pointer to the destination z component of the normal vector.

.. py:method:: cbf_detector_struct.get_pixel_area(indexslow, indexfast, area, projected_area)

   cbf_get_pixel_area, cbf_get_pixel_area_fs and cbf_get_pixel_area_sf set \*area to the area of the pixel at (indexfast, indexslow) 
   on the detector surface and \*projected_area to the apparent area of the pixel as viewed 
   from the sample position, with indexslow being the slow axis and indexfast being the fast axis.

   Either of the destination pointers may be NULL.

   :param indexslow: Slow index.
   :param indexfast: Fast index.
   :param area: Pointer to the destination area in mm2.
   :param projected_area: Pointer to the destination apparent area in mm2.

.. py:method:: cbf_detector_struct.get_pixel_area_fs(indexfast, indexslow, area, projected_area)

   cbf_get_pixel_area, cbf_get_pixel_area_fs and cbf_get_pixel_area_sf set \*area to the area of the pixel at (indexfast, indexslow) 
   on the detector surface and \*projected_area to the apparent area of the pixel as viewed 
   from the sample position, with indexslow being the slow axis and indexfast being the fast axis.

   Either of the destination pointers may be NULL.

   :param indexfast: Fast index.
   :param indexslow: Slow index.
   :param area: Pointer to the destination area in mm2.
   :param projected_area: Pointer to the destination apparent area in mm2.

.. py:method:: cbf_detector_struct.get_pixel_area_sf(indexslow, indexfast, area, projected_area)

   cbf_get_pixel_area, cbf_get_pixel_area_fs and cbf_get_pixel_area_sf set \*area to the area of the pixel at (indexfast, indexslow) 
   on the detector surface and \*projected_area to the apparent area of the pixel as viewed 
   from the sample position, with indexslow being the slow axis and indexfast being the fast axis.

   Either of the destination pointers may be NULL.

   :param indexslow: Slow index.
   :param indexfast: Fast index.
   :param area: Pointer to the destination area in mm2.
   :param projected_area: Pointer to the destination apparent area in mm2.

.. py:method:: cbf_detector_struct.get_inferred_pixel_size(axis_number, psize)

   cbf_get_inferred_pixel_size, cbf_get_inferred_pixel_size_sf set \*psize to point to 
   the double value in millimeters of the
   pixel size for the axis axis_number value.  The slow index is treated as axis 1 and the next faster index is treated
   as axis 2.  cbf_get_inferred_pixel_size_fs sets \*psize to point to the double value in 
   millimeters of the
   pixel size for the axis axis_number value.  The fast index is treated as axis 1  and the next slower index is treated
   as axis 2.
   If the axis number is negative, the axes are used in the reverse order so that an axis_number
   of -1 indicates the fast axes in a call to cbf_get_inferred_pixel_size or cbf_get_inferred_pixel_size_sf
   and indicates the fast axis in a call to cbf_get_inferred_pixel_size_fs.

   :param axis_number: The number of the axis.
   :param psize:

.. py:method:: cbf_detector_struct.get_inferred_pixel_size_fs(axis_number, psize)

   cbf_get_inferred_pixel_size, cbf_get_inferred_pixel_size_sf set \*psize to point to 
   the double value in millimeters of the
   pixel size for the axis axis_number value.  The slow index is treated as axis 1 and the next faster index is treated
   as axis 2.  cbf_get_inferred_pixel_size_fs sets \*psize to point to the double value in 
   millimeters of the
   pixel size for the axis axis_number value.  The fast index is treated as axis 1  and the next slower index is treated
   as axis 2.
   If the axis number is negative, the axes are used in the reverse order so that an axis_number
   of -1 indicates the fast axes in a call to cbf_get_inferred_pixel_size or cbf_get_inferred_pixel_size_sf
   and indicates the fast axis in a call to cbf_get_inferred_pixel_size_fs.

   :param axis_number: The number of the axis.
   :param psize:

.. py:method:: cbf_detector_struct.get_inferred_pixel_size_sf(axis_number, psize)

   cbf_get_inferred_pixel_size, cbf_get_inferred_pixel_size_sf set \*psize to point to 
   the double value in millimeters of the
   pixel size for the axis axis_number value.  The slow index is treated as axis 1 and the next faster index is treated
   as axis 2.  cbf_get_inferred_pixel_size_fs sets \*psize to point to the double value in 
   millimeters of the
   pixel size for the axis axis_number value.  The fast index is treated as axis 1  and the next slower index is treated
   as axis 2.
   If the axis number is negative, the axes are used in the reverse order so that an axis_number
   of -1 indicates the fast axes in a call to cbf_get_inferred_pixel_size or cbf_get_inferred_pixel_size_sf
   and indicates the fast axis in a call to cbf_get_inferred_pixel_size_fs.

   :param axis_number: The number of the axis.
   :param psize: