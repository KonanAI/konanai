
from abc import ABC, abstractmethod
from typing import Type, Callable, Optional, Tuple, List, Dict, ClassVar, Set
from .time import Time


ARTICULATORY_CLASSIFICATION = {}  # replace with actual values


class LinguisticUnit(ABC):
    """
    Base class for representing linguistic units such as words or phonemes.
    It includes common attributes and methods relevant to these units.

    Attributes:
        active_vocabulary (ClassVar[Set[str]]): Stores unique linguistic
        units currently in use across all instances of subclasses.
    """

    active_vocabulary: ClassVar[Set[str]] = set()

    def __init__(self, start: Time, end: Time, data: str):
        """
        Construct a LinguisticUnit with start and end times, and content.

        Args:
            start (Time): Time object representing when the unit starts.
            end (Time): Time object representing when the unit ends.
            data (str): The content of the linguistic unit.
        """
        pass

    @property
    @abstractmethod
    def duration(self) -> Time:
        """
        Provides the duration of the linguistic unit by computing the
        difference between the end time and start time.

        Returns:
            Time: The duration of the linguistic unit.
        """
        pass


class Phoneme(LinguisticUnit):
    """
    Represents a Phoneme, a unit of sound in speech, subclassing
    LinguisticUnit. It includes properties related to the Phoneme's
    characteristics and duration.

    Attributes:
        articulatory_classification (ARTICULATORY_CLASSIFICATION):
        Classification based on phoneme's articulatory properties.
    """

    articulatory_classification = ARTICULATORY_CLASSIFICATION

    @property
    def classification(self) -> str:
        """
        Get the articulatory classification of the Phoneme based on
        its production properties.

        Returns:
            str: The classification of the Phoneme.
        """
        pass

    @classmethod
    def _get_phonemes_by_group(
        cls,
        group: str,
    ) -> List[str]:
        """
        Retrieve all phonemes belonging to a specific group defined
        by its articulatory characteristics.

        Args:
            group (str): The articulatory group for phoneme retrieval.

        Returns:
            List[str]: Phonemes corresponding to the specified group.
        """
        pass

    @classmethod
    def coronals(cls) -> List[str]:
        """
        Retrieves phonemes belonging to the coronal group,
        characterized by the blade of the tongue being used
        for articulation.

        Returns:
            List[str]: Phonemes in the coronal group.
        """
        pass

    @classmethod
    def dorsals(cls) -> List[str]:
        """
        Retrieves phonemes belonging to the dorsal group,
        characterized by the body of the tongue being used
        for articulation.

        Returns:
            List[str]: Phonemes in the dorsal group.
        """
        pass

    @classmethod
    def labials(cls) -> List[str]:
        """
        Retrieves phonemes belonging to the labial group,
        characterized by the lips being used for articulation.

        Returns:
            List[str]: Phonemes in the labial group.
        """
        pass

    @classmethod
    def laryngeals(cls) -> List[str]:
        """
        Retrieves phonemes belonging to the laryngeal group,
        characterized by the larynx being used for articulation.

        Returns:
            List[str]: Phonemes in the laryngeal group.
        """
        pass

    @classmethod
    def silent(cls) -> List[str]:
        """
        Retrieves silent phonemes, which do not produce audible
        sound but are part of the speech structure.

        Returns:
            List[str]: Silent phonemes.
        """
        pass

    @classmethod
    def special(cls) -> List[str]:
        """
        Retrieves special phonemes, that have unique articulatory
        properties or functions in the language system.

        Returns:
            List[str]: Special phonemes.
        """
        pass

    @property
    def duration(self) -> Time:
        """
        Provides the duration of the Phoneme, calculated as the
        difference between the end and start times of the Phoneme.

        Returns:
            Time: The duration of the Phoneme.
        """
        pass


class Word(LinguisticUnit):
    """
    Represents a Word, a fundamental unit of language, that inherits
    from the LinguisticUnit class.

    Each Word object encapsulates the start and end times, the actual
    word content, and methods to perform various operations such as
    syllabification and duration calculation.
    """

    @classmethod
    def syllabify(
        cls,
        phonemes: Optional[List[str]] = None,
    ) -> List[List[str]]:
        """
        Breaks a list of phonemes into constituent syllables according
        to linguistic rules.

        Args:
            phonemes (Optional[List[str]]): List of phonemes to be
                syllabified.

        Returns:
            List[List[str]]: Nested list where each inner list represents
                a syllable, composed of phonemes.
        """
        pass

    @property
    def duration(self) -> Time:
        """
        Computes the duration of the word by subtracting the start time
        from the end time.

        Returns:
            Time: The duration of the word.
        """
        pass
