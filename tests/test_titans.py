import torch
import pytest

@pytest.mark.parametrize('seq_len', (32, 1024, 77))
def test_titans(
    seq_len
):

    from titans_pytorch import NeuralMemory

    mem = NeuralMemory(
        dim = 384,
        chunk_size = 64,
    )

    seq = torch.randn(2, seq_len, 384)
    retrieved = mem(seq)

    assert seq.shape == retrieved.shape

def test_titans_attn_memory():
    from titans_pytorch.titans_attn_memory import NeuralMemory

    mem = NeuralMemory(
        dim = 384,
        chunk_size = 64,
    )

    seq = torch.randn(2, 1024, 384)
    retrieved = mem(seq)

    assert seq.shape == retrieved.shape
