from typing import Optional, List, Type, Tuple
from abc import ABC


import pandas
import numpy


from .linguistic import LinguisticUnit, Word, Phoneme
from .time import Time, Waveform
from ..externals import ForcedAligner, PredictiveAligner


class Alignment(ABC):
    """
    Abstract base class for different types of linguistic alignment.

    TODO: Replace this with a more specific class description.
    """

    def __init__(
        self,
        dataframe: pandas.DataFrame,
        unit_type: Type[LinguisticUnit],
    ) -> None:
        """
        Initializes an `Alignment` instance.

        Args:
            dataframe (pandas.DataFrame): The DataFrame representing the alignment.
            unit_type (Type[LinguisticUnit]): The type of linguistic unit the alignment is based on.

        TODO: Replace this with a more specific method description.
        """
        pass

    @property
    def units(self) -> Optional[List[LinguisticUnit]]:
        """
        Gets the linguistic units involved in the alignment.

        Returns:
            Optional[List[LinguisticUnit]]: The linguistic units, or `None` if no units are involved.

        TODO: Replace this with a more specific method description.
        """
        pass


class WordAlignment(Alignment):
    """
    Represents an alignment based on words.

    TODO: Replace this with a more specific class description.
    """

    def __init__(
        self,
        dataframe: pandas.DataFrame,
    ) -> None:
        """
        Initializes a `WordAlignment` instance.

        Args:
            dataframe (pandas.DataFrame): The DataFrame representing the alignment.

        TODO: Replace this with a more specific method description.
        """
        pass


class PhonemeAlignment(Alignment):
    """
    Represents an alignment based on phonemes.

    TODO: Replace this with a more specific class description.
    """

    def __init__(
        self,
        dataframe: pandas.DataFrame,
    ) -> None:
        """
        Initializes a `PhonemeAlignment` instance.

        Args:
            dataframe (pandas.DataFrame): The DataFrame representing the alignment.

        TODO: Replace this with a more specific method description.
        """
        pass


class Transcript:
    """
    Represents a linguistic transcript.

    TODO: Replace this with a more specific class description.
    """

    def __init__(self, data: str) -> None:
        """
        Initializes a `Transcript` instance.

        Args:
            data (str): The transcript data.

        TODO: Replace this with a more specific method description.
        """
        pass

    @classmethod
    def from_file(
        cls: Type["Transcript"],
        file_path: str,
    ) -> "Transcript":
        """
        Creates a `Transcript` instance from a file.

        Args:
            file_path (str): The path to the file.

        Returns:
            Transcript: The created `Transcript` instance.

        TODO: Replace this with a more specific method description.
        """
        pass

    def calculate_alignment(
        self,
        waveform: Waveform,
    ) -> None:
        """
        Calculates the alignment of the transcript with a waveform.

        Args:
            waveform (Waveform): The waveform.

        TODO: Replace this with a more specific method description.
        """
        pass

    @property
    def word_alignment(self) -> Optional[WordAlignment]:
        """
        Gets the word alignment of the transcript.

        Returns:
            Optional[WordAlignment]: The word alignment, or `None` if no word alignment exists.

        TODO: Replace this with a more specific method description.
        """
        pass

    @property
    def phoneme_alignment(self) -> Optional[PhonemeAlignment]:
        """
        Gets the phoneme alignment of the transcript.

        Returns:
            Optional[PhonemeAlignment]: The phoneme alignment, or `None` if no phoneme alignment exists.

        TODO: Replace this with a more specific method description.
        """
        pass

    @property
    def words(self) -> Optional[List[Word]]:
        """
        Gets the words in the transcript.

        Returns:
            Optional[List[Word]]: The words, or `None` if no words are in the transcript.

        TODO: Replace this with a more specific method description.
        """
        pass

    @property
    def phonemes(self) -> Optional[List[Phoneme]]:
        """
        Gets the phonemes in the transcript.

        Returns:
            Optional[List[Phoneme]]: The phonemes, or `None` if no phonemes are in the transcript.

        TODO: Replace this with a more specific method description.
        """
        pass
