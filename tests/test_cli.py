from click.testing import CliRunner
from line_track_designer.__main__ import linetrack


def test_show():
    runner = CliRunner()
    result = runner.invoke(linetrack, ['show', 'track.txt'])
    assert result.exit_code == 0


def test_savepng():
    runner = CliRunner()
    result = runner.invoke(linetrack, ['savepng', 'track.txt'])
    assert result.exit_code == 0


def test_savemd():
    runner = CliRunner()
    result = runner.invoke(linetrack, ['savemd', 'track.txt'])
    assert result.exit_code == 0
