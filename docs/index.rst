
Konanai API
===========

.. module:: konanai

This part of the documentation covers all the interfaces of konanai. For parts
where konanai depends on external libraries, we document the most important
right here and provide links to the canonical documentation.


Domains Module
--------------

.. module:: konanai.domains

This module provides diverse functionalities encompassing several critical
domains integral to speech and language processing.

.. automodule:: konanai.domains
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.time.Time
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.time.Waveform
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.linguistic.LinguisticUnit
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.linguistic.Phoneme
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.linguistic.Word
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.time_frequency.Spectrogram
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.time_frequency.PowerSpectrogram
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.time_linguistic.Alignment
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.time_linguistic.WordAlignment
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.time_linguistic.PhonemeAlignment
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.time_linguistic.Transcript
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.representation.DataHandler
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.representation.Embedding
   :members:
   :inherited-members:

.. autoclass:: konanai.domains.representation.DecisionBoundary
   :members:
   :inherited-members:


Externals Module
----------------

.. module:: konanai.externals

This module provides intuitive, easy-to-use wrappers for several external tools
integral to high-level speech and language processing tasks.

.. automodule:: konanai.externals
   :members:
   :inherited-members:

.. autoclass:: konanai.externals.umap_wrapper.NonparametricUmap
   :members:
   :inherited-members:

.. autoclass:: konanai.externals.umap_wrapper.ParametricUmap
   :members:
   :inherited-members:

.. autoclass:: konanai.externals.opensmile_wrapper.BaseOpensmile
   :members:
   :inherited-members:

.. autoclass:: konanai.externals.opensmile_wrapper.EgemapsV2
   :members:
   :inherited-members:

.. autoclass:: konanai.externals.opensmile_wrapper.Compare2016
   :members:
   :inherited-members:

.. autoclass:: konanai.externals.charsiu_wrapper.ForcedAligner
   :members:
   :inherited-members:

.. autoclass:: konanai.externals.charsiu_wrapper.PredictiveAligner
   :members:
   :inherited-members:


Models Module
-------------

.. module:: konanai.models

This module provides a suite of estimators, forming the backbone of the machine
learning capabilities within `konanai`.

.. automodule:: konanai.models
   :members:
   :inherited-members:

.. autoclass:: konanai.models.acoustic_phonetic.BaseEstimator
   :members:
   :inherited-members:

.. autoclass:: konanai.models.acoustic_phonetic.AcousticEstimator
   :members:
   :inherited-members:

.. autoclass:: konanai.models.acoustic_phonetic.PhoneticEstimator
   :members:
   :inherited-members:


Empirics Module
---------------

.. module:: konanai.empirics

This module is designed to offer robust tools for conducting empirical analysis,
an essential component of high-level language and speech processing research.

.. automodule:: konanai.empirics
   :members:
   :inherited-members:

.. autoclass:: konanai.empirics.ablation.Results
   :members:
   :inherited-members:

.. autoclass:: konanai.empirics.ablation.Ablation
   :members:
   :inherited-members:
