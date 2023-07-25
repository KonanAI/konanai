"""
This module provides intuitive, easy-to-use wrappers for several
external tools integral to high-level speech and language processing tasks.

It includes the following submodules:

- UMAP: NonparametricUmap and ParametricUmap classes for dimensionality
        reduction tasks.
- OpenSMILE: BaseOpensmile, EgemapsV2, and Compare2016 classes for extracting
             a wide range of audio features.
- Charsiu: ForcedAligner and PredictiveAligner classes for precise alignment
           tasks.

Attributes:
    NonparametricUmap: Non-parametric UMAP class for dimensionality reduction.
    ParametricUmap: Parametric UMAP class for dimensionality reduction.
    BaseOpensmile: Base class for opensmile features extraction.
    EgemapsV2: Class for extracting EGEMAPS v2 features using opensmile.
    Compare2016: Class for extracting COMPARE 2016 features using opensmile.
    ForcedAligner: Class for forced alignment tasks using Charsiu.
    PredictiveAligner: Class for predictive alignment tasks using Charsiu.
"""

# pylint: disable=wrong-import-position

import sys
from pathlib import Path

charsiu_path = Path(__file__).resolve().parent / "lib" / "charsiu" / "src"
(charsiu_path / "__init__.py").touch(exist_ok=True)
sys.path.append(str(charsiu_path))

import Charsiu

from .umap_wrapper import (
    NonparametricUmap,
    ParametricUmap,
)

from .opensmile_wrapper import (
    BaseOpensmile,
    EgemapsV2,
    Compare2016,
)

from .charsiu_wrapper import (
    ForcedAligner,
    PredictiveAligner,
)
