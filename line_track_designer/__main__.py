"""
Command line interface from Line Track Designer
"""
import click
import os
from line_track_designer.track import Track


@click.group()
def linetrack():
    """Generate line following tracks for robots."""
    pass


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
def show(filename):
    """Show track FILENAME as PNG file.

    FILENAME is a text file following the track file's conventions.
    """
    click.echo('Show track')
    track = Track.read(filename)
    track.show()


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
def write(filename):
    """Write track FILENAME in the command prompt."""
    click.echo('Write track')
    track = Track.read(filename)
    click.echo(str(track))


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
def edit(filename):
    """Edit track FILENAME."""
    click.echo('Edit track')
    click.edit(filename=filename)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-o', '--output', 'filename_png', default='',
              help='Name of the PNG file')
def savepng(filename, filename_png):
    """Save track FILENAME as PNG file."""
    click.echo('Save track')
    track = Track.read(filename)
    if filename_png == '':
        filename_png = os.path.splitext(filename)[0] + '.png'
    track.save_img(filename_png)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-o', '--output', 'filename_md', default='',
              help='Name of the MD file')
@click.option('-d', '--description', 'description', default='',
              prompt='Description', help='Description of the track')
def savemd(filename, filename_md, description):
    """Save track FILENAME as MD file."""
    click.echo('Save track')
    track = Track.read(filename)
    pre, _ = os.path.splitext(filename)
    if filename_md == '':
        filename_md = pre + '.md'
    filename_png = pre + '.png'
    track.save_img(filename_png)
    track.save_md(filename_md, filename_png, description)
