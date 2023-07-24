
from typing import Optional


import sklearn.base
import numpy
import opensmile


class BaseOpensmile(
    sklearn.base.BaseEstimator,
    sklearn.base.TransformerMixin,
    sklearn.base.RegressorMixin,
):
    """
    A base class for OpenSMILE feature extraction.

    Attributes:
        feature_set (opensmile.FeatureSet): OpenSMILE feature set.
        population_mu (float): Population mean for standardization.
        population_sigma (float): Population standard deviation for
                                  standardization.
    """

    def __init__(
        self,
        feature_set: opensmile.FeatureSet,
        population_mu: float,
        population_sigma: float,
    ) -> None:
        """
        Initializes BaseOpensmile with the provided attributes.

        Args:
            feature_set (opensmile.FeatureSet): OpenSMILE feature set.
            population_mu (float): Population mean for standardization.
            population_sigma (float): Population standard deviation for
                                      standardization.
        """
        pass

    def fit(
        self,
        X: Optional[numpy.ndarray] = None,
        y: Optional[numpy.ndarray] = None,
    ) -> "BaseOpensmile":
        """
        Fits the transformer on the input data.

        Args:
            X (numpy.ndarray, optional): Input data.
            y (numpy.ndarray, optional): Target data.

        Returns:
            BaseOpensmile: The fitted instance.
        """
        pass

    def transform(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        """
        Transforms the input data based on the fitted transformer.

        Args:
            X (numpy.ndarray): Input data.

        Returns:
            numpy.ndarray: Transformed data.
        """
        pass

    def predict(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        """
        Predicts target data based on the fitted model.

        Args:
            X (numpy.ndarray): Input data.

        Returns:
            numpy.ndarray: Predicted data.
        """
        pass

    def _get_standardized(
        self,
        x: numpy.ndarray,
    ) -> numpy.ndarray:
        """
        Standardizes the input data.

        Args:
            x (numpy.ndarray): Input data.

        Returns:
            numpy.ndarray: Standardized data.
        """
        pass


class EgemapsV2(BaseOpensmile):
    """
    A class for eGeMAPSv02 feature extraction using OpenSMILE.

    Inherits from BaseOpensmile.

    Attributes:
        population_mu (float): Population mean for standardization.
        population_sigma (float): Population standard deviation for
                                  standardization.
    """

    def __init__(
        self,
        population_mu: float,
        population_sigma: float,
    ) -> None:
        """
        Initializes EgemapsV2 with the provided attributes.

        Args:
            population_mu (float): Population mean for standardization.
            population_sigma (float): Population standard deviation for
                                      standardization.
        """
        super().__init__(
            opensmile.FeatureSet.eGeMAPSv02,
            population_mu,
            population_sigma,
        )


class Compare2016(BaseOpensmile):
    """
    A class for ComParE_2016 feature extraction using OpenSMILE.

    Inherits from BaseOpensmile.

    Attributes:
        population_mu (float): Population mean for standardization.
        population_sigma (float): Population standard deviation for
                                  standardization.
    """

    def __init__(
        self,
        population_mu: float,
        population_sigma: float,
    ) -> None:
        """
        Initializes Compare2016 with the provided attributes.

        Args:
            population_mu (float): Population mean for standardization.
            population_sigma (float): Population standard deviation for
                                      standardization.
        """
        super().__init__(
            opensmile.FeatureSet.ComParE_2016,
            population_mu,
            population_sigma,
        )
