""" Methods for Interpolating Functions

Wrappers around FITPACK functions:

  splrep    -- find smoothing spline given (x,y) points on curve.
  splprep   -- find smoothing spline given parametrically defined curve.
  splev     -- evaluate the spline or its derivatives.
  splint    -- compute definite integral of a spline.
  sproot    -- find the roots of a cubic spline.
  spalde    -- compute all derivatives of a spline at given points.
  bisplep   -- find bivariate smoothing spline representation.
  bisplev   -- evaluate bivariate smoothing spline. 

Interpolation Class

  linear_1d -- Create a class whose instances can linearly interpolate
               to compute unknown values.
"""

from interpolate import linear_1d
from fitpack import splrep, splprep, splev, splint, sproot, \
                    spalde, bisplep, bisplev

