from app.core.calculate_epsilon import calculate_epsilon

def test_without_mode():
    assert calculate_epsilon(0.9, 'WITHOUT', 0, 100) == 0.0

def test_therapy_mode_before_start():
    assert calculate_epsilon(0.9, 'THERAPY', 50, 30) == 0.0

def test_therapy_mode_after_start():
    assert calculate_epsilon(0.9, 'THERAPY', 50, 60) == 0.9

def test_interruption_mode():
    result = calculate_epsilon(0.9, 'INTERRUPTION', 0.5, 0.125)
    assert 0.0 <= result <= 0.9

def test_resistance_mode():
    result = calculate_epsilon(0.9, 'RESISTANCE', 0.01, 100)
    assert 0.0 < result < 0.9