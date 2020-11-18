from hetdesrun.component.registration import register
from hetdesrun.datatypes import DataType

import pandas as pd
import numpy as np

# ***** DO NOT EDIT LINES BELOW *****
# These lines may be overwritten if input/output changes.
@register(inputs={"data": DataType.Any}, outputs={"signum": DataType.Any})
def main(*, data):
    """entrypoint function for this component

    Usage example:
    >>> main(
    ...     data = pd.Series(
    ...        {
    ...            "2019-08-01T15:20:12": -25.0,
    ...            "2019-08-01T15:44:12": None,
    ...            "2019-08-03T16:20:15": 0,
    ...            "2019-08-05T12:00:34": 9.0
    ...        }
    ...     )
    ... )["signum"]
    2019-08-01T15:20:12   -1.0
    2019-08-01T15:44:12    NaN
    2019-08-03T16:20:15    0.0
    2019-08-05T12:00:34    1.0
    dtype: float64
    """
    # ***** DO NOT EDIT LINES ABOVE *****
    # write your function code here.

    return {"signum": np.sign(data)}
