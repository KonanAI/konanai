from typing import Optional, Union


import sklearn.base
import numpy
import umap


class NonparametricUmap(
    sklearn.base.BaseEstimator,
    sklearn.base.TransformerMixin,
    sklearn.base.RegressorMixin,
):
    def __init__(
        self,
        specification: dict,
        basepath: str,
        data: Optional[numpy.ndarray] = None,
        labels: Optional[numpy.ndarray] = None,
    ) -> None:
        pass

    def fit(
        self,
        X: numpy.ndarray,
        y: Optional[numpy.ndarray] = None,
    ) -> "NonparametricUmapModel":
        pass

    def predict(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        pass

    def fit_predict(
        self,
        X: numpy.ndarray,
        y: Optional[numpy.ndarray] = None,
    ) -> numpy.ndarray:
        pass

    def transform(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        pass

    def save(self) -> None:
        pass

    def _load(self) -> umap.UMAP:
        pass

    def _instantiate(self) -> umap.UMAP:
        pass


class ParametricUmap(
    sklearn.base.BaseEstimator,
    sklearn.base.TransformerMixin,
    sklearn.base.RegressorMixin,
):
    def __init__(
        self,
        specification: dict,
        basepath: str,
        data: Optional[numpy.ndarray] = None,
        labels: Optional[numpy.ndarray] = None,
    ) -> None:
        pass

    def _instantiate(self) -> umap.parametric_umap.ParametricUMAP:
        pass

    def fit(
        self,
        X: numpy.ndarray,
        y: Optional[numpy.ndarray] = None,
    ) -> "ParametricUmapModel":
        pass

    def predict(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        pass

    def fit_predict(
        self,
        X: numpy.ndarray,
        y: Optional[numpy.ndarray] = None,
    ) -> numpy.ndarray:
        pass

    def transform(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        pass

    def save(self) -> None:
        pass

    def _load(self) -> umap.parametric_umap.ParametricUMAP:
        pass
