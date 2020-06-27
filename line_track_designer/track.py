"""
With the **track** module, you can create, import, edit, save, and
export tracks.

"""
from pathlib import Path
import numpy as np
from PIL import Image
import logging
from line_track_designer.printer import Printer
from line_track_designer.tile import Tile, Tiles
from line_track_designer.error import LineTrackDesignerError
from line_track_designer.markdown import Markdown


class Track:
    """
    Representation of a track.
    An instance of the **Track** class is composed of three fields:

    * **tiles**: array which contains the number of each tile of the track
    * **orient**: array which indicates the orientation of each tile
    * **name**: name of the track

    """
    @staticmethod
    def read(file, name='track'):
        """
        Read a text file representing a track
        and return the track associated.

        Args:
            file (str): filename
            name (str): name of the track

        Returns:
            Track: the track associated to the file

        Raises:
            LineTrackDesignerError: file not found
            LineTrackDesignerError: bad filename extension: requires .txt

        """
        try:
            f = open(file, 'r')
        except IOError:
            raise LineTrackDesignerError('file {} not found'.format(file))
        p = Path(file)
        if p.suffix != '.txt':
            raise LineTrackDesignerError(
                    'bad filename extension: requires .txt')
        lines = f.readlines()
        f.close()
        tiles, orient = [], []
        for line in lines:
            line = line.strip('\n').split(' ')
            lt, lo = [], []
            for i in line:
                t, o = i.split(';')
                lt.append(int(t))
                lo.append(int(o))
            tiles.append(lt)
            orient.append(lo)
        logging.info('Reading track: {}'.format(file))
        return Track(
            np.array(tiles, dtype=int),
            np.array(orient, dtype=int), name)

    @staticmethod
    def zeros(nrow, ncol, name='track'):
        """
        Create an empty track.

        Args:
            nrow (int): number of rows
            ncol (int): number of columns
            name (str): name of the track

        Returns:
            Track: empty track (only zeros)

        """
        tiles = np.zeros((nrow, ncol), dtype=int)
        orient = np.zeros((nrow, ncol), dtype=int)
        return Track(tiles, orient, name)

    @staticmethod
    def max_shape(width, height):
        """
        Return the maximum number of rows and columns
        of a track limited by a width and a height in mm.

        Args:
            width (int): width in mm
            height (int): height in mm

        Returns:
            tuple of int: number of rows and columns

        """
        return width // Tile.SIDE, height // Tile.SIDE

    def __init__(self, tiles, orient, name='track'):
        """
        Init a track. The arguments tiles and orient must be numpy arrays.
        For example:

        .. code-block:: python

            import numpy as np
            from line_track_designer.track import Track

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

            track = Track(tiles, orient, 'my track')

        Args:
            tiles (numpy.array): array of tiles
            orient (numpy.array): array of orientations
            name (str): name of the track

        Raises:
            LineTrackDesignerError: tiles and orient must have the same shape
            LineTrackDesignerError: invalid values

        """
        if (tiles.shape != orient.shape):
            raise LineTrackDesignerError(
                    'tiles and orient must have the same shape')
        nrow, ncol = tiles.shape
        for i in range(nrow):
            for j in range(ncol):
                t, o = tiles[i][j], orient[i][j]
                if t != 0 and not Tile.is_valid(t):
                    raise LineTrackDesignerError(
                            '{} is not a valid tile value'.format(t))
                if not 0 <= o <= 3:
                    raise LineTrackDesignerError(
                            '{} is not a valid orient value'.format(o))
        self._name = name
        self._tiles = tiles.copy()
        self._orient = orient.copy()
        logging.info('Track created')

    @property
    def tiles(self):
        """Get the array of tiles."""
        return self._tiles

    @property
    def orient(self):
        """Get the array of orientations."""
        return self._orient

    @property
    def name(self):
        """Get the name of the track."""
        return self._name

    def __str__(self):
        """
        Make the string format of the track.
        The tiles and orient matrix are superposed in one matrix.
        Each couple of values is separated by a semicolon.

        With the last example, we obtain:

        .. code-block:: text

            3;1 2;1 3;0
            2;0 11;0 2;0
            3;2 2;1 3;3

        """
        lines = []
        for line_t, line_o in zip(self.tiles, self.orient):
            line = ' '.join(
                ['{};{}'.format(t, o) for t, o in zip(line_t, line_o)])
            lines.append(line)
        return '\n'.join(lines)

    def __repr__(self):
        """
        Make the repr format of the track.
        It's the same than the string format.
        """
        return str(self)

    def add_col(self):
        """
        Add a column to the track. This column is filled with 0.
        """
        new_col = np.zeros(self.tiles.shape[0], dtype=int)
        new_col = np.atleast_2d(new_col).T
        self._tiles = np.hstack([self.tiles, new_col])
        self._orient = np.hstack([self.orient, new_col])
        logging.info('Column added to track')

    def add_row(self):
        """
        Add a row to the track. This row is filled with 0.
        """
        new_row = np.zeros(self.tiles.shape[1], dtype=int)
        self._tiles = np.vstack([self.tiles, new_row])
        self._orient = np.vstack([self.orient, new_row])
        logging.info('Row added to track')

    def del_col(self, col):
        """
        Delete a column from the track.

        Args:
            col (int): index of the column to delete

        """
        self._tiles = np.delete(self.tiles, col, axis=1)
        self._orient = np.delete(self.orient, col, axis=1)
        logging.info('Column deleted from track')

    def del_row(self, row):
        """
        Delete a row from the track.

        Args:
            row (int): index of the row to delete

        """
        self._tiles = np.delete(self.tiles, row, axis=0)
        self._orient = np.delete(self.orient, row, axis=0)
        logging.info('Row deleted from track')

    def set_tile(self, row, col, tile, orient):
        """
        Set a tile of the track.

        Args:
            row (int): index of the row of the tile
            col (int): index of the column of the tile
            tile (int): number of the tile
            orient (int): orientation of the tile

        Raises:
            LineTrackDesignerError: invalid tile/orient value

        """
        if tile != 0 and not Tile.is_valid(tile):
            raise LineTrackDesignerError(
                    '{} is not a valid tile value'.format(tile))
        if not 0 <= orient <= 3:
            raise LineTrackDesignerError(
                    '{} is not a valid orient value'.format(orient))
        nrow, ncol = self.tiles.shape
        if row >= nrow:
            for _ in range(nrow - 1, row):
                self.add_row()
        if col >= ncol:
            for _ in range(ncol - 1, col):
                self.add_col()
        self._tiles[row][col] = tile
        self._orient[row][col] = orient
        logging.info('Tile ({}, {}) set to track'.format(row, col))

    def rotate(self, k=1):
        """
        Rotate the track.
        The argument k is the number of times the array
        is rotated by 90 degrees.

        Args:
            k (int): number of rotations (default: 1)

        """
        nrow, ncol = self.orient.shape
        shape = (nrow, ncol) if k % 2 == 0 else (ncol, nrow)
        self._tiles = np.rot90(self.tiles, k)
        self._orient = np.mod(
            (np.rot90(self.orient, k) + np.ones(shape, dtype=int) * k), 4)
        logging.info('Track rotated {} times'.format(k))

    def dimensions(self):
        """
        Return the dimensions in mm of the track.

        Returns:
            tuple of int: width and height in mm

        """
        nrow, ncol = self.tiles.shape
        return ncol*Tile.SIDE, nrow*Tile.SIDE

    def occurences(self):
        """
        Return the occurences of each tile used by the track.
        It returns a dictionary. The keys corresponds to the number
        of a tile and the values are the number of occurences.

        Returns:
            dict: occurences

        """
        occur = {}
        for i in range(2, 34):
            count = np.count_nonzero(self.tiles == i)
            if count != 0:
                occur[i] = count
        return occur

    def print_track(self):
        """
        Ask the printer to print the tiles to build the track.
        """
        occur = self.occurences()
        printer = Printer()
        logging.info('Printing track')
        for i in occur:
            printer.print_page(occur[i], i, self.name)

    def export_img(self):
        """
        Export the track to image. It uses the PIL library.

        Returns:
            Image: image of the track

        """
        SIDE = 1575
        t = Tiles()
        nrow, ncol = self.tiles.shape
        track_img = Image.new('RGB', (ncol*SIDE, nrow*SIDE))
        for i in range(nrow):
            for j in range(ncol):
                num_t = self.tiles[i][j]
                current_tile = t.get_tile(num_t if num_t != 0 else 11)
                current_orient = self.orient[i][j]
                track_img.paste(
                    current_tile.image.rotate(90*current_orient),
                    (j*SIDE, i*SIDE))
        track_img.thumbnail((SIDE, SIDE), Image.ANTIALIAS)
        logging.info('Track exported to image')
        return track_img

    def show(self):
        """
        Displays the track with the PIL library.
        The image is in PNG format.
        """
        track_img = self.export_img()
        track_img.show(title=self.name)
        logging.info('Showing track')

    def save_img(self, file):
        """
        Save the track as an image.

        Args:
            file (str): filename

        Raises:
            LineTrackDesignerError: bad filename extension: use .png

        """
        p = Path(file)
        if p.suffix != '.png':
            raise LineTrackDesignerError('bad filename extension: use .png')
        track_img = self.export_img()
        track_img.save(file)
        logging.info('Track saved as PNG file: {}'.format(file))

    def save_txt(self, file):
        """
        Save the track as a text file. The content of the text
        file corresponds to the string format of the track.

        Args:
            file (str): filename

        Raises:
            LineTrackDesignerError: bad filename extension: use .txt

        """
        p = Path(file)
        if p.suffix != '.txt':
            raise LineTrackDesignerError('bad filename extension: use .txt')
        f = open(file, 'w')
        f.write(str(self))
        f.close()
        logging.info('Track saved: {}'.format(file))

    def save_md(self, file, description=''):
        """
        Save the track as a markdown file. It also creates the PNG image
        associated to the track. The md file contains the following
        informtions:

        * name of the track
        * PNG image of the track
        * description of the track (optionnal)
        * dimensions (in mm)
        * tiles required to build the track

        Args:
            file (str): filename (markdown file)
            description (str): description of the track

        Raises:
            LineTrackDesignerError: bad extension file: use .md

        """
        p = Path(file)
        if p.suffix != '.md':
            raise LineTrackDesignerError('bad extension file: use .md')
        with Markdown(file) as m:
            m.add_title(self.name, 1)
            img = p.with_suffix('.png')
            self.save_img(img)
            m.add_image(img.name, self.name)
            if description != '':
                m.add_title('description', 2)
                m.write(description)
            m.add_title('dimensions', 2)
            w, h = self.dimensions()
            m.add_table([
                ['Width', 'Height'],
                ['{} mm'.format(w), '{} mm'.format(h)]])
            m.add_title('tiles', 2)
            occ = self.occurences()
            occ_array = [[i, occ[i]] for i in occ]
            occ_array.insert(0, ['Tile number', 'Number of copies required'])
            m.add_table(occ_array)
            m.write(('Built with [Line Track Designer]'
                     '(https://github.com/Quentin18/Line-Track-Designer)'))
        logging.info('Track saved as markdown file: {}'.format(file))
