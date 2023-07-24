"""
This module provides diverse functionalities encompassing several
critical domains integral to speech and language processing.

It includes the following submodules:

- `time`: Time-series analyses are facilitated through classes such as Time
          and Waveform.
- `linguistic`: Fundamental linguistic units are encapsulated in classes such
                as Phoneme and Word.
- `time_linguistic`: The bridging of time and linguistic domains is
                     facilitated with classes like Alignment and Transcript.
- `time_frequency`: A Spectrogram class is provided for time-frequency
                    analyses.
- `representation`: High-level data representation and visualization tasks
                   are facilitated through classes like DataHandler and Plot.

Attributes:
    Time: Time-series analysis class.
    Waveform: Class for waveforms in time-series analysis.
    LinguisticUnit: Base class for linguistic units.
    Phoneme: Class representing phonemes.
    Word: Class representing words.
    Alignment: Class for aligning time and linguistic units.
    WordAlignment: Class for word alignments.
    PhonemeAlignment: Class for phoneme alignments.
    Transcript: Class for transcriptions.
    Spectrogram: Class for time-frequency analysis.
    DataHandler: Class for high-level data representation.
    Embedding: Class for embedding data.
    DecisionBoundary: Class for decision boundaries.
    Plot: Class for data visualization.
"""

from .time import (
    Time,
    Waveform,
)

from .linguistic import (
    LinguisticUnit,
    Phoneme,
    Word,
)

from .time_linguistic import (
    Alignment,
    WordAlignment,
    PhonemeAlignment,
    Transcript,
)

from .time_frequency import (
    Spectrogram,
)

from .representation import (
    DataHandler,
    Embedding,
    DecisionBoundary,
    Plot,
)
