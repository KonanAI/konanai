
from typing import Callable, Optional, Type, TypeVar


import torch


from .time import Waveform


T = TypeVar("T", bound="Spectrogram")


class Spectrogram:
    """
    Represents a Spectrogram, a visual representation of the spectrum
    of frequencies of sound as they vary with time.

    Encapsulates spectrogram data and provides methods for initialization
    from raw data or waveform files and objects, with optional custom
    transformations.
    """

    def __init__(self, data: torch.Tensor) -> None:
        """
        Initializes a Spectrogram instance with given data.

        Args:
            data (torch.Tensor): Tensor representing the spectrogram data.
        """
        pass

    @classmethod
    def from_waveform_file(
        cls: Type[T],
        filename: str,
        custom_transform: Optional[Callable[..., torch.Tensor]] = None,
    ) -> T:
        """
        Creates a Spectrogram instance from a waveform file.

        Args:
            filename (str): Path to the waveform file.
            custom_transform (Callable[..., torch.Tensor], optional): Custom
                transform function to apply to the waveform data.

        Returns:
            T: A Spectrogram instance.
        """
        pass

    @classmethod
    def from_waveform(
        cls: Type[T],
        waveform: Waveform,
        transform: Optional[Callable[..., torch.Tensor]] = None,
    ) -> T:
        """
        Creates a Spectrogram instance from a Waveform object.

        Args:
            waveform (Waveform): The waveform object to create the
                spectrogram from.
            transform (Callable[..., torch.Tensor], optional): Transform
                function to apply to the waveform data.

        Returns:
            T: A Spectrogram instance.
        """
        pass

    @staticmethod
    def _default_transform(waveform_data: torch.Tensor) -> torch.Tensor:
        """
        Applies a default transform to waveform data. This function can be
        overridden with custom transformations.

        Args:
            waveform_data (torch.Tensor): Input waveform data.

        Returns:
            torch.Tensor: Transformed waveform data.
        """
        pass

    @staticmethod
    def _default_stft(
        waveform_data: torch.Tensor,
        pad: int = 0,
        custom_window_fn: Optional[Callable[..., torch.Tensor]] = None,
        n_fft: int = 640,
        hop_length: int = 160,
        win_length: int = 640,
        power: Optional[float] = None,
        normalized: bool = False,
        center: bool = False,
        pad_mode: str = "reflect",
        onesided: bool = True,
    ) -> torch.Tensor:
        """
        Computes the short-time Fourier transform (STFT) of the waveform data.

        Args:
            waveform_data (torch.Tensor): Input waveform data.
            pad (int, optional): Amount of padding applied to the signal.
                Defaults to 0.
            custom_window_fn (Optional[Callable[..., torch.Tensor]], optional):
                Custom function used to generate window frames.
                Defaults to None.
            n_fft (int, optional): Size of FFT. Defaults to 640.
            hop_length (int, optional): Length of hop between STFT windows.
                Defaults to 160.
            win_length (int, optional): Window size. Defaults to 640.
            power (Optional[float], optional): Exponent for the magnitude
                spectrogram. Defaults to None.
            normalized (bool, optional): Whether the resulting spectrogram is
                normalized. Defaults to False.
            center (bool, optional): Whether to pad input signal for centered
                frames. Defaults to False.
            pad_mode (str, optional): Padding mode. Defaults to "reflect".
            onesided (bool, optional): Whether to return a one-sided
                spectrogram. Defaults to True.

        Returns:
            torch.Tensor: Spectrogram of input waveform.
        """
        pass

    @staticmethod
    def _default_window_fn(
        window_length: int,
        periodic: bool = True,
        dtype=None,
        device=None,
        requires_grad=False,
    ) -> torch.Tensor:
        """
        Creates a Hann window of a given length.

        Args:
            window_length (int): The length of the window.
            periodic (bool, optional): Whether the window is periodic.
                Defaults to True.
            dtype (optional): Desired data type of returned tensor. If
                specified, the input tensor is casted to dtype before the
                operation is performed. Defaults to None.
            device (optional): Desired device of returned tensor. If specified,
                the input tensor is casted to device before the operation is
                performed. Defaults to None.
            requires_grad (bool, optional): If autograd should record
                operations on the returned tensor. Defaults to False.

        Returns:
            torch.Tensor: The Hann window.
        """
        pass


class PowerSpectrogram(Spectrogram):
    """
    Class that encapsulates power spectrogram data, inheriting from
    the Spectrogram class. The power spectrogram is derived from the
    spectrogram of a signal, which has been squared element-wise.
    """

    @staticmethod
    def _default_transform(waveform_data: torch.Tensor) -> torch.Tensor:
        """
        Applies a default transform to waveform data, suitable for power
        spectrogram calculations. This function can be overridden with
        custom transformations.

        Args:
            waveform_data (torch.Tensor): Input waveform data.

        Returns:
            torch.Tensor: Transformed waveform data.
        """
        pass

    @staticmethod
    def _default_window_fn(
        window_length: int,
        periodic: bool = True,
        alpha: float = 25 / 46,
        beta: float = 21 / 46,
        dtype=None,
        device=None,
        requires_grad: bool = False,
    ) -> torch.Tensor:
        """
        Creates a Hamming window of a given length. The Hamming window is
        a window function that helps manage spectral leakage when
        performing a Fourier transform on a discrete signal.

        Args:
            window_length (int): The length of the window.
            periodic (bool, optional): Whether the window is periodic.
                Defaults to True.
            alpha (float, optional): Alpha parameter of the Hamming window.
                Defaults to 25/46.
            beta (float, optional): Beta parameter of the Hamming window.
                Defaults to 21/46.
            dtype (optional): Desired data type of returned tensor. If
                specified, the input tensor is casted to dtype before the
                operation is performed. Defaults to None.
            device (optional): Desired device of returned tensor. If
                specified, the input tensor is casted to device before the
                operation is performed. Defaults to None.
            requires_grad (bool, optional): If autograd should record
                operations on the returned tensor. Defaults to False.

        Returns:
            torch.Tensor: The Hamming window.
        """
        pass

    @staticmethod
    def _default_stft(
        waveform_data: torch.Tensor,
        pad: int = 0,
        custom_window_fn: Optional[Callable[..., torch.Tensor]] = None,
        n_fft: int = 640,
        hop_length: int = 160,
        win_length: int = 640,
        power: float = 2.0,
        normalized: bool = False,
        center: bool = False,
        pad_mode: str = "reflect",
        onesided: bool = True,
    ) -> torch.Tensor:
        """
        Computes the short-time Fourier transform (STFT) of the waveform data.
        In the case of the PowerSpectrogram, the computed spectrogram is
        raised to the given power to provide a magnitude power spectrogram.

        Args:
            waveform_data (torch.Tensor): Input waveform data.
            pad (int, optional): Amount of padding applied to the signal.
                Defaults to 0.
            custom_window_fn (Optional[Callable[..., torch.Tensor]], optional):
                Custom function used to generate window frames.
                Defaults to None.
            n_fft (int, optional): Size of FFT. Defaults to 640.
            hop_length (int, optional): Length of hop between STFT windows.
                Defaults to 160.
            win_length (int, optional): Window size. Defaults to 640.
            power (float, optional): Exponent for the magnitude
                spectrogram, for power spectrogram this is typically 2.0.
                Defaults to 2.0.
            normalized (bool, optional): Whether the resulting spectrogram is
                normalized. Defaults to False.
            center (bool, optional): Whether to pad input signal for centered
                frames. Defaults to False.
            pad_mode (str, optional): Padding mode. Defaults to "reflect".
            onesided (bool, optional): Whether to return a one-sided
                spectrogram. Defaults to True.

        Returns:
            torch.Tensor: Power Spectrogram of input waveform.
        """
        pass
