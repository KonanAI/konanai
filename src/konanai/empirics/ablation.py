from typing import Any, Dict, List, Optional, Type, Union


import os
import pandas


class Results:
    def __init__(
        self,
        directory: str,
    ) -> None:
        pass

    def update(
        self,
        model: Any,
        specification: Dict[str, Any],
        output: Any,
        plot: Any,
    ) -> None:
        pass

    def save(self) -> None:
        pass

    def _load(self) -> pandas.DataFrame:
        pass


class Ablation:
    def __init__(
        self,
        model_class: Type,
        specifications: Dict[str, List[Any]],
        data: Any,
        labels: Any,
        directory: str,
    ) -> None:
        pass

    def run(self) -> None:
        pass

    def _training_iter(self) -> None:
        pass

    def _inference_iter(self) -> None:
        pass

    def _plotting_iter(self) -> None:
        pass

    def _logging_iter(self) -> None:
        pass

    def _update_best_iter(self) -> None:
        pass
