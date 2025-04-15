import pytest
from src.app import main
from io import StringIO
import sys

def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert "2 + 3 = 5" in captured.out
    assert "5 - 2 = 3" in captured.out
