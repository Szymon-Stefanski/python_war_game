import pytest
from unittest.mock import patch
from game import Game

class TestsGame:

    def test_create_user(self):
        game = Game()
        username = 'Example'
        result = game.create_user(username)
        assert result == username, f"Expected {username}, but got {result}"

    @pytest.mark.parametrize("user_input, expected", [
        ('1', '1'),  # Add soldier
        ('2', '2'),  # Sell soldier
        ('3', '3'),  # Promote soldier
        ('4', '4'),  # Check army
        ('5', '5'),  # Attack
        ('6', '6'),  # End turn
        ('7', '7')  # Capitulation
    ])

    def test_game_interface(self, user_input, expected):
        with patch('builtins.input', return_value=user_input):
            game = Game()
            result = game.game_interface()
            assert result == expected, f"Expected {expected}, but got {result}"