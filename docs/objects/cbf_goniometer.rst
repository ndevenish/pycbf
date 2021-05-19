cbf_goniometer_struct
*********************

.. py:class:: cbf_goniometer_struct

.. py:method:: cbf_goniometer_struct.free_goniometer()

   cbf_free_goniometer destroys the goniometer object specified by goniometer and frees all associated memory.



.. py:method:: cbf_goniometer_struct.get_rotation_axis(reserved, vector1, vector2, vector3)

   cbf_get_rotation_axis sets \*vector1, \*vector2, and \*vector3 to the 3 components of the goniometer rotation axis used for the exposure.

   Any of the destination pointers may be NULL.

   The parameter reserved is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param vector1: Pointer to the destination x component of the rotation axis.
   :param vector2: Pointer to the destination y component of the rotation axis.
   :param vector3: Pointer to the destination z component of the rotation axis.

.. py:method:: cbf_goniometer_struct.get_rotation_range(reserved, start, increment)

   cbf_get_rotation_range sets \*start and \*increment to the corresponding values of the goniometer rotation axis used for the exposure.

   Either of the destination pointers may be NULL.

   The parameter reserved is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param start: Pointer to the destination start value.
   :param increment: Pointer to the destination increment value.

.. py:method:: cbf_goniometer_struct.rotate_vector(reserved, ratio, initial1, initial2, initial3, final1, final2, final3)

   cbf_rotate_vector sets \*final1, \*final2, and \*final3 to the 3 components of the of the vector (initial1, initial2, initial3) after reorientation by applying the goniometer rotations.  The value ratio specif

   ies the goniometer setting and varies from 0.0 at the beginning of the exposure to 1.0 at the end, irrespective of the actual rotation range.

   Any of the destination pointers may be NULL.

   The parameter reserved is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param ratio: Goniometer setting.  0 = beginning of exposure, 1 = end.
   :param initial1: x component of the initial vector.
   :param initial2: y component of the initial vector.
   :param initial3: z component of the initial vector.
   :param final1:
   :param final2:
   :param final3:

.. py:method:: cbf_goniometer_struct.get_reciprocal(reserved, ratio, wavelength, real1, real2, real3, reciprocal1, reciprocal2, reciprocal3)

   cbf_get_reciprocal sets \*reciprocal1, \* reciprocal2, and \* reciprocal3 to the 3 components of the of the reciprocal-space vector corresponding to the real-space vector (real1, real2, real3).  The reciprocal-space
   vector is oriented to correspond to the goniometer setting with all axes at 0.  The value wavelength is the wavlength in Å and the value ratio specifies the current goniometer setting and varies from 0.0 at the beginning of the exposur

   e to 1.0 at the end, irrespective of the actual rotation range.

   Any of the destination pointers may be NULL.

   The parameter reserved is presently unused and should be set to 0.

   :param reserved: Unused.  Any value other than 0 is invalid.
   :param ratio: Goniometer setting.  0 = beginning of exposure, 1 = end.
   :param wavelength: Wavelength in Å.
   :param real1: x component of the real-space vector.
   :param real2: y component of the real-space vector.
   :param real3: z component of the real-space vector.
   :param reciprocal1: Pointer to the destination x component of the reciprocal-space vector.
   :param reciprocal2: Pointer to the destination y component of the reciprocal-space vector.
   :param reciprocal3: Pointer to the destination z component of the reciprocal-space vector.