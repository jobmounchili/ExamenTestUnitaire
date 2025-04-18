import pytest
import random
from unittest.mock import patch, MagicMock
from src.main import Wordle

@pytest.fixture
def wordle():
    return Wordle(["apple", "grape", "mango", "peach", "berry", "poris", "papal"])

# Test unitaire : Validation des mots
def test_validate_word(wordle):
    assert wordle.validate_word("apple") is True
    assert wordle.validate_word("xyzzy") is False

# Test unitaire : Vérification du retour de feedback
def test_check_guess(wordle):
    wordle.target_word = "apple"
    feedback = wordle.check_guess("apple")
    assert feedback == ["Green", "Green", "Green", "Green", "Green"]

# Test unitaire : Mot invalide
def test_invalid_guess(wordle):
    assert wordle.check_guess("appl") == "Invalid word. Must be in dictionary."

# Test unitaire : Fin du jeu
def test_game_over(wordle):
    wordle.target_word = "grape"
    for _ in range(6):
        wordle.check_guess("mango")
    assert wordle.is_game_over() is True

# Test unitaire : Statistiques
def test_statistics(wordle):
    wordle.target_word = "apple"
    wordle.check_guess("apple")
    stats = wordle.get_statistics()
    assert stats["wins"] == 1
    assert stats["streak"] == 1

# Test avec Mock : Simulation du choix du mot cible
def test_mocked_word_selection():
    with patch('random.choice', return_value="apple") as mock_choice:
        wordle = Wordle(["apple", "grape", "mango", "peach", "berry"])
        assert wordle.target_word == "apple"
        mock_choice.assert_called_once()

# Test avec Fake : Création d'une version simplifiée
def test_fake_wordle():
    class FakeWordle(Wordle):
        def __init__(self):
            self.word_list = ["apple", "grape", "mango", "peach", "berry"]
            self.target_word = "apple"
            self.attempts = 6
            self.history = []
            self.wins = 0
            self.total_attempts = 0
            self.games_played = 0
            self.streak = 0
    
    game = FakeWordle()
    feedback = game.check_guess("apple")
    assert feedback == ["Green", "Green", "Green", "Green", "Green"]

# Test avec Stub : Simulation d'une validation de mot
def test_stub_validation():
    game = Wordle(["apple", "grape", "mango", "peach", "berry"])
    game.validate_word = MagicMock(return_value=True)
    assert game.validate_word("fakeword") is True

# Test avec Spy : Vérification des appels
def test_spy_check_guess():
    game = Wordle(["apple", "grape", "mango", "peach", "berry"])
    game.check_guess = MagicMock(return_value=["Green"] * 5)
    result = game.check_guess("apple")
    game.check_guess.assert_called_once_with("apple")
    assert result == ["Green", "Green", "Green", "Green", "Green"]