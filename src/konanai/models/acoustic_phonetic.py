
import torch


class BaseEstimator(torch.nn.Module):
    """
    Base class for RNN-based estimators, including GRU and LSTM types.
    """

    def __init__(
        self,
        input_size: int,
        output_size: int,
        rnn_type: str = "GRU",
        bidirectional: bool = True,
    ) -> None:
        """
        Initializes a BaseEstimator instance, constructing the RNN and linear
        layers.

        Args:
            input_size (int): The number of input features.
            output_size (int): The number of output features.
            rnn_type (str, optional): The type of RNN layer to use. Supports
                "GRU" and "LSTM". Defaults to "GRU".
            bidirectional (bool, optional): If True, the RNN layer is made
                bidirectional. Defaults to True.
        """
        super(BaseEstimator, self).__init__()

        if rnn_type == "GRU" and bidirectional == True:
            self.rnn = torch.nn.GRU(321, 256, 4, bidirectional=True, batch_first=True)
        elif rnn_type == "LSTM" and bidirectional == True:
            self.rnn = torch.nn.LSTM(321, 256, 4, bidirectional=True, batch_first=True)
        elif rnn_type == "GRU" and bidirectional == False:
            self.rnn = torch.nn.GRU(321, 512, 4, bidirectional=False, batch_first=True)
        elif rnn_type == "LSTM" and bidirectional == False:
            self.rnn = torch.nn.LSTM(321, 512, 4, bidirectional=False, batch_first=True)

        self.linear1 = torch.nn.Linear(512, 256)
        self.linear2 = torch.nn.Linear(256, 128)
        self.linear3 = torch.nn.Linear(128, output_size)

        self.act = torch.nn.ReLU()

    def forward(self, spectrogram: torch.Tensor) -> torch.Tensor:
        """
        Defines the forward pass for the BaseEstimator.

        Args:
            spectrogram (torch.Tensor): The input spectrogram.

        Returns:
            torch.Tensor: The model's output tensor.
        """
        hidden, _ = self.rnn(spectrogram)
        hidden = self.linear1(hidden)
        hidden = self.act(hidden)
        hidden = self.linear2(hidden)
        hidden = self.act(hidden)
        output = self.linear3(hidden)

        return output


class AcousticEstimator(BaseEstimator):
    """
    Class for estimating acoustic features from spectrograms. Inherits from
    BaseEstimator.
    """

    def __init__(
        self,
        rnn_type: str = "GRU",
        bidirectional: bool = True,
    ) -> None:
        """
        Initializes an AcousticEstimator instance.

        Args:
            rnn_type (str, optional): The type of RNN layer to use. Supports
                "GRU" and "LSTM". Defaults to "GRU".
            bidirectional (bool, optional): If True, the RNN layer is made
                bidirectional. Defaults to True.
        """
        super(AcousticEstimator, self).__init__(
            input_size=321,
            output_size=25,
            rnn_type=rnn_type,
            bidirectional=bidirectional,
        )


class PhoneticEstimator(BaseEstimator):
    """
    Class for estimating phonetic features from spectrograms. Inherits from
    BaseEstimator.
    """

    def __init__(
        self,
        rnn_type: str = "GRU",
        bidirectional: bool = True,
    ) -> None:
        """
        Initializes a PhoneticEstimator instance.

        Args:
            rnn_type (str, optional): The type of RNN layer to use. Supports
                "GRU" and "LSTM". Defaults to "GRU".
            bidirectional (bool, optional): If True, the RNN layer is made
                bidirectional. Defaults to True.
        """
        super(PhoneticEstimator, self).__init__(
            input_size=321,
            output_size=42,
            rnn_type=rnn_type,
            bidirectional=bidirectional,
        )
