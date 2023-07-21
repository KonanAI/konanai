from typing import Callable, Optional, Type, TypeVar


import torch


from .time import Waveform


T = TypeVar("T", bound="Spectrogram")


class Spectrogram:
    """
    Class to represent and manipulate spectrogram data.

    TODO: Replace this with a more specific class description.
    """

    def __init__(self, data: torch.Tensor) -> None:
        """
        Initialize a Spectrogram object.

        Args:
            data (torch.Tensor): The spectrogram data.

        TODO: Replace this with a more specific method description.
        """
        pass

    @classmethod
    def from_waveform_file(
        cls: Type[T],
        filename: str,
        custom_transform: Optional[Callable[..., torch.Tensor]] = None,
    ) -> T:
        """
        Create a Spectrogram object from a waveform file.

        Args:
            filename (str): Path to the file.
            custom_transform (Callable[..., torch.Tensor], optional): Custom transform function.

        Returns:
            T: A Spectrogram object.

        TODO: Replace this with a more specific method description.
        """
        pass

    @classmethod
    def from_waveform(
        cls: Type[T],
        waveform: Waveform,
        transform: Optional[Callable[..., torch.Tensor]] = None,
    ) -> T:
        """
        Create a Spectrogram object from a Waveform object.

        Args:
            waveform (Waveform): The waveform object.
            transform (Callable[..., torch.Tensor], optional): Transform function.

        Returns:
            T: A Spectrogram object.

        TODO: Replace this with a more specific method description.
        """
        pass

    @staticmethod
    def _default_transform(waveform_data: torch.Tensor) -> torch.Tensor:
        """
        Apply the default transform to the waveform data.

        Args:
            waveform_data (torch.Tensor): The waveform data.

        Returns:
            torch.Tensor: The transformed data.

        TODO: Replace this with a more specific method description.
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
        Compute the short-time Fourier transform (STFT) of the waveform data.

        Args:
            waveform_data (torch.Tensor): The waveform data.
            pad (int, optional): Amount of padding. Defaults to 0.
            custom_window_fn (Optional[Callable[..., torch.Tensor]], optional): Custom window function. Defaults to None.
            n_fft (int, optional): FFT size. Defaults to 640.
            hop_length (int, optional): Hop size. Defaults to 160.
            win_length (int, optional): Window size. Defaults to 640.
            power (Optional[float], optional): Power for magnitude spectrogram. Defaults to None.
            normalized (bool, optional): Whether to normalize. Defaults to False.
            center (bool, optional): Whether to center. Defaults to False.
            pad_mode (str, optional): Padding mode. Defaults to "reflect".
            onesided (bool, optional): Whether to return a one-sided spectrogram. Defaults to True.

        Returns:
            torch.Tensor: The spectrogram.

        TODO: Replace this with a more specific method description.
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
        Create a Hann window.

        Args:
            window_length (int): The window length.
            periodic (bool, optional): Whether the window is periodic. Defaults to True.
            dtype (optional): The desired data type of returned tensor. If specified, the input tensor is casted to dtype before the operation is performed. Defaults to None.
            device (optional): The desired device of returned tensor. If specified, the input tensor is casted to device before the operation is performed. Defaults to None.
            requires_grad (bool, optional): If autograd should record operations on the returned tensor. Defaults to False.

        Returns:
            torch.Tensor: The window.

        TODO: Replace this with a more specific method description.
        """
        pass


class PowerSpectrogram(Spectrogram):
    """
    Class to represent and manipulate power spectrogram data.

    TODO: Replace this with a more specific class description.
    """

    @staticmethod
    def _default_transform(waveform_data: torch.Tensor) -> torch.Tensor:
        """
        Apply the default transform to the waveform data.

        Args:
            waveform_data (torch.Tensor): The waveform data.

        Returns:
            torch.Tensor: The transformed data.

        TODO: Replace this with a more specific method description.
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
        Create a Hamming window.

        Args:
            window_length (int): The window length.
            periodic (bool, optional): Whether the window is periodic. Defaults to True.
            alpha (float, optional): The alpha parameter of the Hamming window. Defaults to 25/46.
            beta (float, optional): The beta parameter of the Hamming window. Defaults to 21/46.
            dtype (optional): The desired data type of returned tensor. If specified, the input tensor is casted to dtype before the operation is performed. Defaults to None.
            device (optional): The desired device of returned tensor. If specified, the input tensor is casted to device before the operation is performed. Defaults to None.
            requires_grad (bool, optional): If autograd should record operations on the returned tensor. Defaults to False.

        Returns:
            torch.Tensor: The window.

        TODO: Replace this with a more specific method description.
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
        Compute the short-time Fourier transform (STFT) of the waveform data.

        Args:
            waveform_data (torch.Tensor): The waveform data.
            pad (int, optional): Amount of padding. Defaults to 0.
            custom_window_fn (Optional[Callable[..., torch.Tensor]], optional): Custom window function. Defaults to None.
            n_fft (int, optional): FFT size. Defaults to 640.
            hop_length (int, optional): Hop size. Defaults to 160.
            win_length (int, optional): Window size. Defaults to 640.
            power (float, optional): Power for magnitude spectrogram. Defaults to 2.0.
            normalized (bool, optional): Whether to normalize. Defaults to False.
            center (bool, optional): Whether to center. Defaults to False.
            pad_mode (str, optional): Padding mode. Defaults to "reflect".
            onesided (bool, optional): Whether to return a one-sided spectrogram. Defaults to True.

        Returns:
            torch.Tensor: The spectrogram.

        TODO: Replace this with a more specific method description.
        """
        pass
