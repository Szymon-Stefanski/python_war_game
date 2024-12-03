import pytest
import unittest
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


    def test_soldier_promote(self):
        game = Game()
        result = game.soldier_promote()
        assert result == True, f"Expected True, but got {result}"



class TestSoldierPromotion(unittest.TestCase):

    def setUp(self):
        self.soldiers = [
            {"rank": "private", "experience": 1},
            {"rank": "corporal", "experience": 2},
            {"rank": "captain", "experience": 3},
            {"rank": "sergeant", "experience": 4},
            {"rank": "major", "experience": 5},
        ]


    @patch("random.randint", return_value=0)
    def test_private_to_corporal(self, mock_randint):
        game = Game()
        game.soldier_promote(self.soldiers)
        self.assertEqual(self.soldiers[0]["rank"], "corporal")
        self.assertEqual(self.soldiers[0]["experience"], 2)


    @patch("random.randint", return_value=1)
    def test_corporal_to_captain(self, mock_randint):
        game = Game()
        game.soldier_promote(self.soldiers)
        self.assertEqual(self.soldiers[1]["rank"], "captain")
        self.assertEqual(self.soldiers[1]["experience"], 3)


    @patch("random.randint", return_value=2)
    def test_captain_to_sergeant(self, mock_randint):
        game = Game()
        game.soldier_promote(self.soldiers)
        self.assertEqual(self.soldiers[2]["rank"], "sergeant")
        self.assertEqual(self.soldiers[2]["experience"], 4)


    @patch("random.randint", return_value=3)
    def test_sergeant_to_major(self, mock_randint):
        game = Game()
        game.soldier_promote(self.soldiers)
        self.assertEqual(self.soldiers[3]["rank"], "major")
        self.assertEqual(self.soldiers[3]["experience"], 5)


    @patch("random.randint", return_value=4)
    def test_major_no_promotion(self, mock_randint):
        with patch("builtins.print") as mock_print:
            game = Game()
            game.soldier_promote(self.soldiers)
            mock_print.assert_called_with("Already have the highest rank")
        self.assertEqual(self.soldiers[4]["rank"], "major")

