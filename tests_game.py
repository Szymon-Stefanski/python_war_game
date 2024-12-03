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


    @pytest.mark.parametrize("user_input, expected", [
        ('1', '1'),  # Private - 10 gold
        ('2', '2'),  # Corporal - 20 gold
        ('3', '3'),  # Captain - 30 gold
        ('4', '4'),  # Sergeant - 40 gold
        ('5', '5'),  # Major - 50 gold
    ])


    def test_army_management(self, user_input, expected):
        with patch('builtins.input', return_value=user_input):
            game = Game()
            result = game.army_management()
            assert result == expected, f"Expected {expected}, but got {result}"


    def test_clear_screen(self):
        game = Game()
        result = game.clear_screen()
        assert result == True, f"Expected True, but got {result}"
