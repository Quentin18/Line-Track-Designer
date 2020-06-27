"""
The **tile** module manages the tiles that are used to build a track.

Note:
    You can see all the tiles here:
    :download:`linefollowtiles.pdf <pdf/linefollowtiles.pdf>`

Warnings:
    The tiles 10 and 32 can not be used by *Line Track Designer*.

"""
import os
import logging
from PIL import Image
import webbrowser
from line_track_designer.error import LineTrackDesignerError


class Tile:
    """
    Representation of a tile.
    An instance of the **Tile** class is composed of four fields:

    * **number**: number of the tile
    * **name**: name of the tile
    * **path**: path to the PNG image corresponding to the tile
    * **image**: PIL.Image format associated to the tile

    """
    SIDE = 200  # side of a tile in mm

    @staticmethod
    def is_valid(number):
        """
        Return True if the number corresponds to a valid tile.
        It is valid if the number is between 2 and 33, and the tiles
        10 and 32 are invalid.

        Args:
            number (int): number of a tile

        Returns:
            bool: Is a valid number

        """
        return number >= 2 and number < 34 and number not in [10, 32]

    def __init__(self, number):
        """
        Init a tile.

        Args:
            number (int): number of the tile

        Raises:
            LineTrackDesignerError: invalid tile number

        """
        if Tile.is_valid(number):
            self._number = number
            self._name = 'linefollowtiles-{}.png'.format(str(number).zfill(2))
            cwd = os.path.dirname(os.path.abspath(__file__))
            self._path = os.path.join(cwd, 'png', self._name)
            self._image = Image.open(self._path)
        else:
            raise LineTrackDesignerError('Tile {} is not valid'.format(number))
        logging.info('Tile {} created'.format(number))

    @property
    def number(self):
        """Get the number of the tile."""
        return self._number

    @property
    def name(self):
        """Get the name of the tile."""
        return self._name

    @property
    def path(self):
        """Get the path of the PNG image associated to the tile."""
        return self._path

    @property
    def image(self):
        """Get the image associated to the tile."""
        return self._image

    def __str__(self):
        """Make the sting format of the tile. It returns its name."""
        return self.name

    def __repr__(self):
        """
        Make the repr format of the tile.
        It's the same than the string format.
        """
        return str(self)

    def show(self, orient=0):
        """
        Show the tile in your picture viewer.

        Args:
            orient (int): orientation of the tile (default: 0)

        Raises:
            LineTrackDesignerError: invalid orient value

        """
        if orient not in [0, 1, 2, 3]:
            raise LineTrackDesignerError(
                    '{} is not a valid orient value'.format(orient))
        img = self.image.rotate(90*orient)
        img.show(title=self.name)
        logging.info('Showing tile')


class Tiles:
    """
    Manage all the tiles.
    The tiles are stocked in the dictionary **dict_tiles**.
    The keys correspond to the number of the tile and the values are
    the Tile objects corresponding to this number.
    """
    def __init__(self):
        """
        Init the tiles. It creates the dictionary **dict_tiles**.
        """
        self._dict_tiles = {}
        for i in range(2, 34):
            if i not in [10, 32]:
                self._dict_tiles[i] = Tile(i)
        logging.info('Tiles created')

    @property
    def dict_tiles(self):
        """
        Get the dictionary of tiles.
        """
        return self._dict_tiles

    def __str__(self):
        """
        Make the sting format of the tiles.
        It returns the names of the tiles.
        """
        return '\n'.join([str(self.dict_tiles[t]) for t in self.dict_tiles])

    def __repr__(self):
        """
        Make the repr format of the tiles.
        It's the same than the string format.
        """
        return str(self)

    def get_tile(self, number):
        """
        Get a tile from its number.

        Args:
            number (int): number of the tile

        Returns:
            Tile: tile associated to the number

        Raises:
            LineTrackDesignerError: tile not found

        """
        if number in self.dict_tiles:
            return self.dict_tiles[number]
        raise LineTrackDesignerError('tile {} not found'.format(number))

    @staticmethod
    def show():
        """
        Open the PDF file containing the tiles.

        Raises:
            LineTrackDesignerError: unable to open the PDF file

        """
        try:
            cwd = os.path.dirname(os.path.abspath(__file__))
            pdf = os.path.join(cwd, 'pdf', 'linefollowtiles.pdf')
            webbrowser.open_new(pdf)
            logging.info('Showing the tiles')
        except FileNotFoundError:
            raise LineTrackDesignerError('unable to open the PDF file')
