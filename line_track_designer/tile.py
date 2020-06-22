"""
The **tile** module manages the tiles that are used to build a track.
This tiles originate from a pdf file and can be printed. They are
represented by a number between 2 and 33. The tiles are squares of 200 mm.

You can see all the tiles down below:

.. image:: tiles.png

"""
import os
from PIL import Image
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
        It's valid if the number is between 2 and 33, and the tiles
        10 and 32 are invalid.

        Args:
            number (int): number of a tile

        Returns:
            bool: valid number

        """
        return number >= 2 and number < 34 and number not in [10, 32]

    def __init__(self, number, cwd):
        """
        Init a tile.

        Args:
            number (int): number of the tile
            cwd (str): current work directory

        Raises:
            LineTrackDesignerError: invalid tile number

        """
        if Tile.is_valid(number):
            self._number = number
            self._name = 'linefollowtiles-{}.png'.format(str(number).zfill(2))
            self._path = os.path.join(cwd, 'png', self._name)
            self._image = Image.open(self._path)
        else:
            raise LineTrackDesignerError('Tile {} is not valid'.format(number))

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
        cwd = os.path.dirname(os.path.abspath(__file__))
        self._dict_tiles = {}
        for i in range(2, 34):
            if i not in [10, 32]:
                self._dict_tiles[i] = Tile(i, cwd)

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
