"""
Command line interface from Line Track Designer
"""
import click
from pathlib import Path
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
    """Delete column COL from track FILENAME.

    COL is the number of the column to delete.
    """
    track = Track.read(filename)
    track.del_col(col)
    track.save_txt(filename)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
@click.argument('row', type=int)
def delrow(filename, row):
    """Delete row ROW from track FILENAME.

    ROW is the number of the row to delete.
    """
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
@click.option('-s', '--show', is_flag=True, help='Show the file created')
def savepng(filename, filename_png, show):
    """Save track FILENAME as PNG file."""
    track = Track.read(filename)
    p = Path(filename)
    if filename_png == '':
        filename_png = p.with_suffix('.png')
    track.save_img(filename_png)
    if show:
        track.show()


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
    p = Path(filename)
    if filename_md == '':
        filename_md = p.with_suffix('.md')
    track.save_md(filename_md, description)


@linetrack.command()
@click.argument('filename', type=click.Path(exists=True))
def printing(filename):
    """Print track FILENAME."""
    if click.confirm('Do you want to print the track?'):
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
    webbrowser.open('https://line-track-designer.readthedocs.io/en/latest/')
    logging.info('Doc opened')
