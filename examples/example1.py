"""
Example 1: Creation of a track with arrays and exportation to PNG an MD
"""
import os
import numpy as np
from line_track_designer.track import Track


if __name__ == "__main__":
    # Creation of a folder
    if not os.path.exists('track_test'):
        os.makedirs('track_test')

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

    # Creation of the track
    track = Track(tiles, orient, 'Test track')

    # Save the track
    track.save_txt('track_test/track.txt')
    track.save_img('track_test/track.png')
    track.save_md('track_test/track.md', 'Easy track')
