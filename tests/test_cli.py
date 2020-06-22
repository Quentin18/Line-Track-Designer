import os
from click.testing import CliRunner
from line_track_designer.__main__ import linetrack


path = os.path.dirname(os.path.abspath(__file__))


def test_show():
    runner = CliRunner()
    result = runner.invoke(
        linetrack, ['show', os.path.join(path, 'track.txt')])
    assert result.exit_code == 0


def test_write():
    runner = CliRunner()
    result = runner.invoke(
        linetrack, ['write', os.path.join(path, 'track.txt')])
    assert result.exit_code == 0


def test_savepng():
    runner = CliRunner()
    result = runner.invoke(
        linetrack, ['savepng', os.path.join(path, 'track.txt')])
    assert result.exit_code == 0


def test_savemd():
    runner = CliRunner()
    result = runner.invoke(
        linetrack, ['savemd', os.path.join(path, 'track.txt')])
    assert result.exit_code == 0
