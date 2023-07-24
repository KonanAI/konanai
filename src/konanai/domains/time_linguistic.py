from typing import Optional, List, Type, Tuple
from abc import ABC


import pandas
import numpy


from .linguistic import LinguisticUnit, Word, Phoneme
from .time import Time, Waveform
from ..externals import ForcedAligner, PredictiveAligner


class Alignment(ABC):
    """
    An abstract base class defining a blueprint for various types of
    linguistic alignment, which is the mapping between speech and text
    at the granularity of specific linguistic units.
    """

    def __init__(
        self,
        dataframe: pandas.DataFrame,
        unit_type: Type[LinguisticUnit],
    ) -> None:
        """
        Initializes an Alignment instance using a dataframe and the
        type of linguistic unit (e.g., phoneme, word) for the alignment.

        Args:
            dataframe (pandas.DataFrame): DataFrame representing the
                alignment between audio and linguistic units.
            unit_type (Type[LinguisticUnit]): Linguistic unit type that
                the alignment is based on.
        """
        pass

    @property
    def units(self) -> Optional[List[LinguisticUnit]]:
        """
        Retrieves the list of linguistic units involved in the alignment.
        The units are derived from the DataFrame used during initialization.

        Returns:
            Optional[List[LinguisticUnit]]: List of linguistic units
                involved in the alignment. If no units are available,
                returns None.
        """
        pass


class WordAlignment(Alignment):
    """
    A class representing alignment of linguistic content at the granularity
    of words. Inherits from the base class 'Alignment'.
    """

    def __init__(
        self,
        dataframe: pandas.DataFrame,
    ) -> None:
        """
        Constructs a WordAlignment instance using a dataframe that
        represents the word-level alignment of linguistic content.

        Args:
            dataframe (pandas.DataFrame): DataFrame representing the
                alignment between audio and word units.
        """
        pass


class PhonemeAlignment(Alignment):
    """
    A class representing alignment of linguistic content at the granularity
    of phonemes. Inherits from the base class 'Alignment'.
    """

    def __init__(
        self,
        dataframe: pandas.DataFrame,
    ) -> None:
        """
        Constructs a PhonemeAlignment instance using a dataframe that
        represents the phoneme-level alignment of linguistic content.

        Args:
            dataframe (pandas.DataFrame): DataFrame representing the
                alignment between audio and phoneme units.
        """
        pass


class Transcript:
    """
    Class representing a linguistic transcript which facilitates operations
    like alignment calculation and access to word and phoneme components.
    """

    def __init__(self, data: str) -> None:
        """
        Constructs a Transcript instance from a given string representation
        of linguistic data.

        Args:
            data (str): String representation of the transcript data.
        """
        pass

    @classmethod
    def from_file(
        cls: Type["Transcript"],
        file_path: str,
    ) -> "Transcript":
        """
        Creates a Transcript instance by loading linguistic data from a
        specified file.

        Args:
            file_path (str): Path to the file containing the transcript data.

        Returns:
            Transcript: A Transcript instance initialized with data from the file.
        """
        pass

    def calculate_alignment(
        self,
        waveform: Waveform,
    ) -> None:
        """
        Calculates the alignment of the transcript with a given waveform,
        facilitating synchronization of audio and linguistic data.

        Args:
            waveform (Waveform): The waveform associated with the transcript.
        """
        pass

    @property
    def word_alignment(self) -> Optional[WordAlignment]:
        """
        Provides access to the word-level alignment of the transcript.

        Returns:
            Optional[WordAlignment]: The word alignment data if available,
            otherwise None.
        """
        pass

    @property
    def phoneme_alignment(self) -> Optional[PhonemeAlignment]:
        """
        Provides access to the phoneme-level alignment of the transcript.

        Returns:
            Optional[PhonemeAlignment]: The phoneme alignment data if
            available, otherwise None.
        """
        pass

    @property
    def words(self) -> Optional[List[Word]]:
        """
        Retrieves all words in the transcript.

        Returns:
            Optional[List[Word]]: List of words in the transcript if available,
            otherwise None.
        """
        pass

    @property
    def phonemes(self) -> Optional[List[Phoneme]]:
        """
        Retrieves all phonemes in the transcript.

        Returns:
            Optional[List[Phoneme]]: List of phonemes in the transcript if
            available, otherwise None.
        """
        pass
