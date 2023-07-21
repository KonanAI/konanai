from typing import Any, Optional, Tuple


import sklearn.base
import numpy
import Charsiu


class ForcedAligner(
    sklearn.base.BaseEstimator,
    sklearn.base.TransformerMixin,
    sklearn.base.RegressorMixin,
):
    def __init__(
        self,
        aligner="charsiu/en_w2v2_fc_10ms",
    ) -> None:
        pass

    def fit(
        self,
        X: Optional[numpy.ndarray] = None,
        y: Optional[numpy.ndarray] = None,
    ) -> "ForcedAligner":
        pass

    def transform(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        pass

    def predict(
        self,
        X: numpy.ndarray,
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        pass


class PredictiveAligner(
    sklearn.base.BaseEstimator,
    sklearn.base.TransformerMixin,
    sklearn.base.RegressorMixin,
):
    def __init__(
        self,
        aligner="charsiu/en_w2v2_fc_10ms",
    ) -> None:
        pass

    def fit(
        self,
        X: Optional[numpy.ndarray] = None,
        y: Optional[numpy.ndarray] = None,
    ) -> "PredictiveAligner":
        pass

    def transform(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        pass

    def predict(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        pass
