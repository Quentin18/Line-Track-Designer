"""
Example 3: Importation, exportation and show a track
"""
from line_track_designer.track import Track

if __name__ == "__main__":
    # Import the track saved in a text file
    track = Track.read('track_cool_guy/track_cool_guy.txt', 'Cool guy track')
    # Export the track as png and markdown files
    track.save_img('track_cool_guy/track_cool_guy.png')
    track.save_md('track_cool_guy/track_cool_guy.md',
                  'track_cool_guy/track_cool_guy.png',
                  'It looks like a face...')
    # Show the track
    track.show()
