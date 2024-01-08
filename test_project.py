from project import get_lives, get_word, get_valid_level
import pytest

def main():
    test_rangeOfWord()
    test_level()
    test_lives()

def test_rangeOfWord():
    assert len(get_word(1)) > 0 and len(get_word(1)) <= 5
    assert len(get_word(2)) > 5 and len(get_word(2)) < 10
    assert len(get_word(3)) >= 10

def test_level():
    assert get_valid_level(1) == 1
    assert get_valid_level(2) == 2
    assert get_valid_level(3) == 3

def test_lives():
    assert get_lives(3) == 3
    assert get_lives(2) == 5
    assert get_lives(1) == 7
    with pytest.raises(ValueError):
        get_lives(0)
    with pytest.raises(ValueError):
        get_lives(4)


if __name__ == "__main__":
    main()