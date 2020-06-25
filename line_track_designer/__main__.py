"""
Command line interface from Line Track Designer
"""
import click
import os
import logging
import webbrowser
from line_track_designer.track import Track
from line_track_designer.tile import Tile, Tiles


@click.group()
@click.option('-v', '--verbosity', is_flag=True, help='Set the verbosity')
def linetrack(verbosity):
    """Generate line following tracks for robots."""
    if verbosity:
        logging.basicConfig(format='%(levelname)s:%(message)s',
                            level=logging.INFO)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
def show(filename):
    """Show track FILENAME as PNG file.

    FILENAME is a text file following the track file's conventions.
    """
    track = Track.read(filename)
    track.show()


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
def write(filename):
    """Write track FILENAME in the command prompt."""
    track = Track.read(filename)
    click.echo(track)
    logging.info('Track writed')


@linetrack.command()
@click.argument('filename', type=click.Path())
@click.argument('nrow', type=int)
@click.argument('ncol', type=int)
def create(filename, nrow, ncol):
    """Create empty track FILENAME.

    NROW is the number of rows.
    NCOL is the number of columns.
    """
    track = Track.zeros(nrow, ncol)
    track.save_txt(filename)
    click.edit(filename=filename)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
def edit(filename):
    """Edit track FILENAME."""
    logging.info('Editing track: {}'.format(filename))
    click.edit(filename=filename)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
def addcol(filename):
    """Add a column to track FILENAME."""
    track = Track.read(filename)
    track.add_col()
    track.save_txt(filename)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
def addrow(filename):
    """Add a row to track FILENAME."""
    track = Track.read(filename)
    track.add_row()
    track.save_txt(filename)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
@click.argument('col', type=int)
def delcol(filename, col):
    """Delete the column COL from track FILENAME."""
    track = Track.read(filename)
    track.del_col(col)
    track.save_txt(filename)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
@click.argument('row', type=int)
def delrow(filename, row):
    """Delete the column ROW from track FILENAME."""
    track = Track.read(filename)
    track.del_row(row)
    track.save_txt(filename)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-n', default=1, help='Number of rotations')
def rotate(filename, n):
    """Rotate track FILENAME."""
    track = Track.read(filename)
    track.rotate(n)
    track.save_txt(filename)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-o', '--output', 'filename_png', default='',
              help='Name of the PNG file')
def savepng(filename, filename_png):
    """Save track FILENAME as PNG file."""
    track = Track.read(filename)
    if filename_png == '':
        filename_png = os.path.splitext(filename)[0] + '.png'
    track.save_img(filename_png)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
@click.option('-o', '--output', 'filename_md', default='',
              help='Name of the MD file')
@click.option('-n', '--name', 'name', default='Track',
              prompt='Name', help='Name of the track')
@click.option('-d', '--description', 'description', default='',
              prompt='Description', help='Description of the track')
def savemd(filename, filename_md, name, description):
    """Save track FILENAME as MD file."""
    track = Track.read(filename, name)
    pre, _ = os.path.splitext(filename)
    if filename_md == '':
        filename_md = pre + '.md'
    filename_png = pre + '.png'
    track.save_img(filename_png)
    track.save_md(filename_md, filename_png, description)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
def printing(filename):
    """Print track FILENAME."""
    track = Track.read(filename)
    track.print_track()


@linetrack.command()
@click.argument('number', type=int)
@click.option('-o', '--orient', default=0, help='Orientation')
def showtile(number, orient):
    """Show tile NUMBER."""
    t = Tile(number)
    t.show(orient)


@linetrack.command()
def pdf():
    """Open the PDF file containing the tiles."""
    Tiles.show()


@linetrack.command()
def doc():
    """Open the documentation."""
    # TODO change url
    webbrowser.open('https://github.com/Quentin18/Line-Track-Designer')
    logging.info('Doc opened')
