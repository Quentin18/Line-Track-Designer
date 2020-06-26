"""
Example 5: Create a track with zeros
"""
from line_track_designer.track import Track

if __name__ == "__main__":
    # Create an empty track
    track = Track.zeros(2, 3)
    # Set the tiles of the track manually
    track.set_tile(1, 0, 17, 1)
    track.set_tile(1, 1, 3, 3)
    track.set_tile(0, 1, 3, 1)
    track.set_tile(0, 2, 17, 3)
    # Show the track
    track.show()
