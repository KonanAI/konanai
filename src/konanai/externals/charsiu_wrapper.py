
from typing import Any, Optional, Tuple

import sklearn.base
import numpy
import Charsiu


class ForcedAligner(
    sklearn.base.BaseEstimator,
    sklearn.base.TransformerMixin,
    sklearn.base.RegressorMixin,
):
    """
    Forced Aligner for aligning audio data with textual data.

    This class integrates the Charsiu forced aligner into the scikit-learn
    interface for seamless integration in ML pipelines.

    Attributes:
        aligner (str): The specification for the Charsiu aligner.

    Args:
        aligner (str, optional): The specification for the Charsiu aligner.
                                 Default is "charsiu/en_w2v2_fc_10ms".
    """

    def __init__(
        self,
        aligner: str = "charsiu/en_w2v2_fc_10ms",
    ) -> None:
        pass

    def fit(
        self,
        X: Optional[numpy.ndarray] = None,
        y: Optional[numpy.ndarray] = None,
    ) -> "ForcedAligner":
        """
        Fit the model to the data.

        Args:
            X (numpy.ndarray, optional): Feature data.
            y (numpy.ndarray, optional): Target labels.

        Returns:
            ForcedAligner: The instance of the aligner.
        """
        pass

    def transform(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        """
        Apply transformations to the data.

        Args:
            X (numpy.ndarray): Feature data.

        Returns:
            numpy.ndarray: Transformed data.
        """
        pass

    def predict(
        self,
        X: numpy.ndarray,
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """
        Predict alignment for the provided data.

        Args:
            X (numpy.ndarray): Feature data.

        Returns:
            Tuple[numpy.ndarray, numpy.ndarray]: Predicted phoneme and word
                                                 alignments.
        """
        pass


class PredictiveAligner(
    sklearn.base.BaseEstimator,
    sklearn.base.TransformerMixin,
    sklearn.base.RegressorMixin,
):
    """
    Predictive Aligner for predicting alignments from audio data.

    This class integrates the Charsiu predictive aligner into the scikit-learn
    interface for seamless integration in ML pipelines.

    Attributes:
        aligner (str): The specification for the Charsiu aligner.

    Args:
        aligner (str, optional): The specification for the Charsiu aligner.
                                 Default is "charsiu/en_w2v2_fc_10ms".
    """

    def __init__(
        self,
        aligner: str = "charsiu/en_w2v2_fc_10ms",
    ) -> None:
        pass

    def fit(
        self,
        X: Optional[numpy.ndarray] = None,
        y: Optional[numpy.ndarray] = None,
    ) -> "PredictiveAligner":
        """
        Fit the model to the data.

        Args:
            X (numpy.ndarray, optional): Feature data.
            y (numpy.ndarray, optional): Target labels.

        Returns:
            PredictiveAligner: The instance of the aligner.
        """
        pass

    def transform(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        """
        Apply transformations to the data.

        Args:
            X (numpy.ndarray): Feature data.

        Returns:
            numpy.ndarray: Transformed data.
        """
        pass

    def predict(
        self,
        X: numpy.ndarray,
    ) -> numpy.ndarray:
        """
        Predict alignment for the provided data.

        Args:
            X (numpy.ndarray): Feature data.

        Returns:
            numpy.ndarray: Predicted alignments.
        """
        pass
