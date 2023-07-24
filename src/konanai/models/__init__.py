"""
This module provides a suite of estimators, forming the backbone of
the machine learning capabilities within `konanai`.

It includes the following submodule:

- Acoustic Phonetic: Contains base estimator and specialized estimators
                       like AcousticEstimator and PhoneticEstimator for
                       handling both acoustic and phonetic data.

Attributes:
    BaseEstimator: A basic estimator providing common functionalities for the other specialized estimators.
    AcousticEstimator: A specialized estimator designed for handling acoustic data.
    PhoneticEstimator: A specialized estimator designed for handling phonetic data.
"""

from .acoustic_phonetic import (
    BaseEstimator,
    AcousticEstimator,
    PhoneticEstimator,
)
