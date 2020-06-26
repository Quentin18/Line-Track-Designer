"""
Example 2: Importation of a track and exportation to PNG and MD
"""
from line_track_designer.track import Track

if __name__ == "__main__":
    # Import the track saved in a text file
    track = Track.read('track_colors/track_colors.txt', 'Colors track')
    # Export the track as png and markdown files
    track.save_img('track_colors/track_colors.png')
    track.save_md('track_colors/track_colors.md',
                  'track_colors/track_colors.png', 'A track with colors')
