import pytest
from game import Game

class TestsGame:

    def test_create_user(self):
        game = Game()
        username = 'Example'
        result = game.create_user(username)
        assert result == username, f"Expected {username}, but got {result}"
