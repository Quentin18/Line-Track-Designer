"""
Example 4: Edition functions
"""
from line_track_designer.track import Track

if __name__ == "__main__":
    # Import the track saved in a text file
    track = Track.read('track_hard/track_hard.txt', 'Hard track')
    # Export the track as png and markdown files
    track.save_img('track_hard/track_hard.png')
    track.save_md('track_hard/track_hard.md',
                  'track_hard/track_hard.png',
                  'A very hard track')
    # Delete a row
    track.del_row(1)
    # Rotate the track
    track.rotate()
    # Show the track
    track.show()
