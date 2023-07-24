
from typing import Optional, Union


import sklearn.base
import numpy
import umap


class NonparametricUmap(
    sklearn.base.BaseEstimator,
    sklearn.base.TransformerMixin,
    sklearn.base.RegressorMixin,
):
    """
    A class to handle non-parametric UMAP models. It extends BaseEstimator,
    TransformerMixin, and RegressorMixin from sklearn.base.
    """

    def __init__(
        self,
        specification: dict,
        basepath: str,
        data: Optional[numpy.ndarray] = None,
        labels: Optional[numpy.ndarray] = None,
    ) -> None:
        """
        Initializes the NonparametricUmap object with the given specifications,
        basepath, data, and labels.

        Args:
            specification (dict): Specifications for the UMAP model.
            basepath (str): The path to save or load the model.
            data (numpy.ndarray, optional): The training data for the model.
            labels (numpy.ndarray, optional): The labels for the data.
        """
        pass

    def fit(
        self,
        X: numpy.ndarray,
        y: Optional[numpy.ndarray] = None,
    ) -> "NonparametricUmapModel":
        """
        Fits the UMAP model on the given data.

        Args:
            X (numpy.ndarray): The data to fit the model.
            y (numpy.ndarray, optional): The labels for the data.

        Returns:
            NonparametricUmapModel: The fitted UMAP model.
        """
        pass

    def predict(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        """
        Predicts the labels for the given data using the fitted UMAP model.

        Args:
            X (numpy.ndarray): The data to predict the labels for.

        Returns:
            numpy.ndarray: The predicted labels.
        """
        pass

    def fit_predict(
        self,
        X: numpy.ndarray,
        y: Optional[numpy.ndarray] = None,
    ) -> numpy.ndarray:
        """
        Fits the UMAP model on the given data and returns the predicted labels.

        Args:
            X (numpy.ndarray): The data to fit the model and predict the labels.
            y (numpy.ndarray, optional): The labels for the data.

        Returns:
            numpy.ndarray: The predicted labels.
        """
        pass

    def transform(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        """
        Transforms the given data using the fitted UMAP model.

        Args:
            X (numpy.ndarray): The data to transform.

        Returns:
            numpy.ndarray: The transformed data.
        """
        pass

    def save(self) -> None:
        """
        Saves the fitted UMAP model at the designated basepath.
        """
        pass

    def _load(self) -> umap.UMAP:
        """
        Loads the UMAP model from the designated basepath.

        Returns:
            umap.UMAP: The loaded UMAP model.
        """
        pass

    def _instantiate(self) -> umap.UMAP:
        """
        Instantiates a new UMAP model with the given specifications.

        Returns:
            umap.UMAP: The instantiated UMAP model.
        """
        pass


class ParametricUmap(
    sklearn.base.BaseEstimator,
    sklearn.base.TransformerMixin,
    sklearn.base.RegressorMixin,
):
    """
    A class to handle parametric UMAP models. It extends BaseEstimator,
    TransformerMixin, and RegressorMixin from sklearn.base.
    """

    def __init__(
        self,
        specification: dict,
        basepath: str,
        data: Optional[numpy.ndarray] = None,
        labels: Optional[numpy.ndarray] = None,
    ) -> None:
        """
        Initializes the ParametricUmap object with the given specifications,
        basepath, data, and labels.

        Args:
            specification (dict): Specifications for the parametric UMAP model.
            basepath (str): The path to save or load the model.
            data (numpy.ndarray, optional): The training data for the model.
            labels (numpy.ndarray, optional): The labels for the data.
        """
        pass

    def _instantiate(self) -> umap.parametric_umap.ParametricUMAP:
        """
        Instantiates a new parametric UMAP model with the given specifications.

        Returns:
            umap.parametric_umap.ParametricUMAP: The instantiated UMAP model.
        """
        pass

    def fit(
        self,
        X: numpy.ndarray,
        y: Optional[numpy.ndarray] = None,
    ) -> "ParametricUmapModel":
        """
        Fits the parametric UMAP model on the given data.

        Args:
            X (numpy.ndarray): The data to fit the model.
            y (numpy.ndarray, optional): The labels for the data.

        Returns:
            ParametricUmapModel: The fitted parametric UMAP model.
        """
        pass

    def predict(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        """
        Predicts the labels for the given data using the fitted parametric UMAP model.

        Args:
            X (numpy.ndarray): The data to predict the labels for.

        Returns:
            numpy.ndarray: The predicted labels.
        """
        pass

    def fit_predict(
        self,
        X: numpy.ndarray,
        y: Optional[numpy.ndarray] = None,
    ) -> numpy.ndarray:
        """
        Fits the parametric UMAP model on the given data and returns the predicted labels.

        Args:
            X (numpy.ndarray): The data to fit the model and predict the labels.
            y (numpy.ndarray, optional): The labels for the data.

        Returns:
            numpy.ndarray: The predicted labels.
        """
        pass

    def transform(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        """
        Transforms the given data using the fitted parametric UMAP model.

        Args:
            X (numpy.ndarray): The data to transform.

        Returns:
            numpy.ndarray: The transformed data.
        """
        pass

    def save(self) -> None:
        """
        Saves the fitted parametric UMAP model at the designated basepath.
        """
        pass

    def _load(self) -> umap.parametric_umap.ParametricUMAP:
        """
        Loads the parametric UMAP model from the designated basepath.

        Returns:
            umap.parametric_umap.ParametricUMAP: The loaded parametric UMAP model.
        """
        pass
