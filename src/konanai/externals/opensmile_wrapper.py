#from typing import Optional
#
#
#import sklearn.base
#import numpy
#import opensmile
#
#
#class BaseOpensmile(
#    sklearn.base.BaseEstimator,
#    sklearn.base.TransformerMixin,
#    sklearn.base.RegressorMixin,
#):
#    def __init__(
#        self,
#        feature_set: opensmile.FeatureSet,
#        population_mu: float,
#        population_sigma: float,
#    ) -> None:
#        pass
#
#    def fit(
#        self,
#        X: Optional[numpy.ndarray] = None,
#        y: Optional[numpy.ndarray] = None,
#    ) -> "BaseOpensmile":
#        pass
#
#    def transform(
#        self,
#        X: numpy.ndarray,
#    ) -> numpy.ndarray:
#        pass
#
#    def predict(
#        self,
#        X: numpy.ndarray,
#    ) -> numpy.ndarray:
#        pass
#
#    def _get_standardized(
#        self,
#        x: numpy.ndarray,
#    ) -> numpy.ndarray:
#        pass
#
#
#class EgemapsV2(BaseOpensmile):
#    def __init__(
#        self,
#        population_mu: float,
#        population_sigma: float,
#    ) -> None:
#        super().__init__(
#            opensmile.FeatureSet.eGeMAPSv02,
#            population_mu,
#            population_sigma,
#        )
#
#
#class Compare2016(BaseOpensmile):
#    def __init__(
#        self,
#        population_mu: float,
#        population_sigma: float,
#    ) -> None:
#        super().__init__(
#            opensmile.FeatureSet.ComParE_2016,
#            population_mu,
#            population_sigma,
#        )
