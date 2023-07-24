
from typing import Any, Dict, List, Optional, Type, Union


import os
import pandas


class Results:
    """
    Class for managing and storing experiment results.
    """

    def __init__(
        self,
        directory: str,
    ) -> None:
        """
        Initializes a Results instance.

        Args:
            directory (str): The directory where the results will be stored.
        """
        pass

    def update(
        self,
        model: Any,
        specification: Dict[str, Any],
        output: Any,
        plot: Any,
    ) -> None:
        """
        Updates the results with the given model, specification, output, and plot.

        Args:
            model (Model): The model used in the experiment.
            specification (Dict[str, Union[str, float, int]]): The specifications of the experiment.
            output (Output): The output of the experiment.
            plot (Plot): The plot object of the experiment.
        """
        pass

    def save(self) -> None:
        """
        Save the results to a CSV file at the specified path.
        """
        pass

    def _load(self) -> pandas.DataFrame:
        """
        Load the results from a CSV file at the specified path.

        Returns:
            pandas.DataFrame: The loaded results.
        """
        pass


class Ablation:
    """
    Class for conducting ablation study experiments.
    """

    def __init__(
        self,
        model_class: Type,
        specifications: Dict[str, List[Any]],
        data: Any,
        labels: Any,
        directory: str,
    ) -> None:
        """
        Initializes an Ablation instance.

        Args:
            model_class (Type[Model]): The class of the model to be used in the experiments.
            specifications (Dict[str, Union[str, float, int]]): The specifications of the experiments.
            data (Any): The data to be used in the experiments.
            labels (Any): The labels for the data.
            directory (str): The directory where the experiment results will be stored.
        """
        pass

    def run(self) -> None:
        """
        Run the ablation study.
        """
        pass

    def _training_iter(self) -> None:
        """
        Conducts a training iteration in the ablation study.
        """
        pass

    def _inference_iter(self) -> None:
        """
        Conducts an inference iteration in the ablation study.
        """
        pass

    def _plotting_iter(self) -> None:
        """
        Conducts a plotting iteration in the ablation study.
        """
        pass

    def _logging_iter(self) -> None:
        """
        Conducts a logging iteration in the ablation study.
        """
        pass

    def _update_best_iter(self) -> None:
        """
        Updates the best result in the ablation study.
        """
        pass
