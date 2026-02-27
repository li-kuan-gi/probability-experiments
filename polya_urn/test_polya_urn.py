import pytest
import numpy as np
from .polya_urn import PolyaUrn

def test_polya_urn_initialization():
    urn = PolyaUrn(initial_red=1, initial_green=1, add_count=1)
    assert urn.red == 1
    assert urn.green == 1
    assert urn.add_count == 1
    assert urn.history == []

def test_polya_urn_step():
    # Set seed for reproducibility or just check bounds
    np.random.seed(42)
    urn = PolyaUrn(initial_red=1, initial_green=1, add_count=1)
    urn.step()
    # Total balls should be 3 (1+1+1)
    assert urn.red + urn.green == 3
    # Either red or green should have increased by 1
    assert (urn.red == 2 and urn.green == 1) or (urn.red == 1 and urn.green == 2)

def test_polya_urn_simulate():
    urn = PolyaUrn(initial_red=1, initial_green=1, add_count=1)
    n_steps = 10
    history = urn.simulate(n_steps)
    
    assert len(history) == n_steps + 1
    assert len(urn.history) == n_steps + 1
    assert history[0] == 0.5  # 1/(1+1)
    
    # Check that proportions are always within [0, 1]
    assert np.all(history >= 0)
    assert np.all(history <= 1)
    
    # Total balls at the end should be initial + n_steps * add_count
    final_total = urn.red + urn.green
    assert final_total == 2 + n_steps * 1

def test_polya_urn_path_dependence():
    # Polya's urn is random, but we can check if it behaves reasonably
    # Trial with many steps should stay somewhat consistent at the end
    np.random.seed(123)
    urn = PolyaUrn(initial_red=1, initial_green=1, add_count=1)
    history = urn.simulate(100)
    # The last value is the final proportion
    assert 0 <= history[-1] <= 1
