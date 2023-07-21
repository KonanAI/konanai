from abc import ABC, abstractmethod
from typing import Type, Callable, Optional, Tuple, List, Dict, ClassVar, Set
from .time import Time


ARTICULATORY_CLASSIFICATION = {}  # replace with actual values


class LinguisticUnit(ABC):
    """
    Abstract base class representing a general linguistic unit.

    Attributes:
        active_vocabulary (ClassVar[Set[str]]): A set containing the active vocabulary.

    TODO: Replace this with a more specific class description.
    """

    active_vocabulary: ClassVar[Set[str]] = set()

    def __init__(self, start: Time, end: Time, data: str):
        """
        Initialize a LinguisticUnit.

        Args:
            start (Time): The start time of the linguistic unit.
            end (Time): The end time of the linguistic unit.
            data (str): The actual content of the linguistic unit.

        TODO: Replace this with a more specific method description.
        """
        pass

    @property
    @abstractmethod
    def duration(self) -> Time:
        """
        Calculate and return the duration of the linguistic unit.

        Returns:
            Time: The duration of the linguistic unit.

        TODO: Replace this with a more specific property description.
        """
        pass


class Phoneme(LinguisticUnit):
    """
    Class representing a Phoneme, inherits from LinguisticUnit.

    TODO: Replace this with a more specific class description.
    """

    articulatory_classification = ARTICULATORY_CLASSIFICATION

    @property
    def classification(self) -> str:
        """
        Returns the classification of the Phoneme.

        TODO: Replace this with a more specific property description.
        """
        pass

    @classmethod
    def _get_phonemes_by_group(
        cls,
        group: str,
    ) -> List[str]:
        """
        Get phonemes by group.

        Args:
            group (str): The group to get phonemes for.

        Returns:
            List[str]: List of phonemes in the specified group.

        TODO: Replace this with a more specific method description.
        """
        pass

    @classmethod
    def coronals(cls) -> List[str]:
        """
        Get phonemes in the coronal group.

        Returns:
            List[str]: List of phonemes in the coronal group.

        TODO: Replace this with a more specific method description.
        """
        pass

    @classmethod
    def dorsals(cls) -> List[str]:
        """
        Get phonemes in the dorsal group.

        Returns:
            List[str]: List of phonemes in the dorsal group.

        TODO: Replace this with a more specific method description.
        """
        pass

    @classmethod
    def labials(cls) -> List[str]:
        """
        Get phonemes in the labial group.

        Returns:
            List[str]: List of phonemes in the labial group.

        TODO: Replace this with a more specific method description.
        """
        pass

    @classmethod
    def laryngeals(cls) -> List[str]:
        """
        Get phonemes in the laryngeal group.

        Returns:
            List[str]: List of phonemes in the laryngeal group.

        TODO: Replace this with a more specific method description.
        """
        pass

    @classmethod
    def silent(cls) -> List[str]:
        """
        Get silent phonemes.

        Returns:
            List[str]: List of silent phonemes.

        TODO: Replace this with a more specific method description.
        """
        pass

    @classmethod
    def special(cls) -> List[str]:
        """
        Get special phonemes.

        Returns:
            List[str]: List of special phonemes.

        TODO: Replace this with a more specific method description.
        """
        pass

    @classmethod
    def vowels(cls) -> List[str]:
        """
        Get vowel phonemes.

        Returns:
            List[str]: List of vowel phonemes.

        TODO: Replace this with a more specific method description.
        """
        pass

    @property
    def duration(self) -> Time:
        """
        Calculate and return the duration of the Phoneme.

        Returns:
            Time: The duration of the Phoneme.

        TODO: Replace this with a more specific property description.
        """
        pass


class Word(LinguisticUnit):
    """
    Class representing a Word, inherits from LinguisticUnit.

    TODO: Replace this with a more specific class description.
    """

    @classmethod
    def syllabify(
        cls,
        phonemes: Optional[List[str]] = None,
    ) -> List[List[str]]:
        """
        Syllabify a list of phonemes.

        Args:
            phonemes (Optional[List[str]]): List of phonemes to syllabify.

        Returns:
            List[List[str]]: List of syllables with phonemes.

        TODO: Replace this with a more specific method description.
        """
        pass

    @property
    def duration(self) -> Time:
        """
        Calculate and return the duration of the Word.

        Returns:
            Time: The duration of the Word.

        TODO: Replace this with a more specific property description.
        """
        pass
