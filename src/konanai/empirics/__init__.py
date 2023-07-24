"""
This module is designed to offer robust tools for conducting
empirical analysis, an essential component of high-level language and speech
processing research.

It includes the following submodule:

- Ablation: Provides classes that facilitate comprehensive ablation studies,
            enabling detailed evaluation of different models and features.

Attributes:
    Results: Class to organize and process the results from various empirical analyses.
    Ablation: Class for performing ablation studies to understand the effect of
              removing certain elements or features from a model.
"""

from .ablation import (
    Results,
    Ablation,
)
