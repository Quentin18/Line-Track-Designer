import os
import numpy as np
from line_track_designer.track import Track
import pytest


path = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def track():
    return Track.read(os.path.join(path, 'track.txt'))


@pytest.fixture
def track_hard():
    return Track.read(os.path.join(path, 'track_hard.txt'))


def test_track():
    # Arrays for the track
    tiles = np.array([
        [3, 2, 3],
        [2, 11, 2],
        [3, 2, 3]
    ])
    orient = np.array([
        [1, 1, 0],
        [0, 0, 0],
        [2, 1, 3]
    ])
    name = 'Test track'

    # Creation of the track
    track = Track(tiles, orient, name)
    assert (track.tiles == tiles).all()
    assert (track.orient == orient).all()
    assert track.name == name

    # Test string format
    with open(os.path.join(path, 'track.txt')) as f:
        assert f.read() == str(track)


def test_max_shape():
    assert Track.max_shape(2000, 1500) == (10, 7)
    assert Track.max_shape(200, 150) == (1, 0)


def test_add(track):
    # Test add col & row
    track.add_col()
    track.add_row()
    tiles = np.array([
        [3, 2, 3, 0],
        [2, 11, 2, 0],
        [3, 2, 3, 0],
        [0, 0, 0, 0]
    ])
    orient = np.array([
        [1, 1, 0, 0],
        [0, 0, 0, 0],
        [2, 1, 3, 0],
        [0, 0, 0, 0]
    ])
    assert (track.tiles == tiles).all()
    assert (track.orient == orient).all()


def test_del(track):
    # Test del col & row
    track.del_col(1)
    track.del_row(1)
    tiles = np.array([
        [3, 3],
        [3, 3]
    ])
    orient = np.array([
        [1, 0],
        [2, 3]
    ])
    assert (track.tiles == tiles).all()
    assert (track.orient == orient).all()


def test_set_tile(track):
    # Test set tile
    track.set_tile(1, 2, 26, 2)
    track.set_tile(3, 3, 12, 1)
    tiles = np.array([
        [3, 2, 3, 0],
        [2, 11, 26, 0],
        [3, 2, 3, 0],
        [0, 0, 0, 12]
    ])
    orient = np.array([
        [1, 1, 0, 0],
        [0, 0, 2, 0],
        [2, 1, 3, 0],
        [0, 0, 0, 1]
    ])
    assert (track.tiles == tiles).all()
    assert (track.orient == orient).all()


def test_rotate(track):
    # Test rotate
    track.rotate()
    with open(os.path.join(path, 'track_rotate_1.txt')) as f:
        assert f.read() == str(track)
    track.rotate(2)
    with open(os.path.join(path, 'track_rotate_2.txt')) as f:
        assert f.read() == str(track)


def test_dimensions(track, track_hard):
    # Test dimensions
    assert track.dimensions() == (600, 600)
    assert track_hard.dimensions() == (600, 1000)
