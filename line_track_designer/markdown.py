"""
The **markdown** module is usefull to export tracks to markdown files.
The **Markdown** class creates a markdown file and can add elements such
as titles, images, and tables.

A markdown file can be edited using the *with* statement.

Note:
    You can read markdown files using *Zettlr*.

"""


class Markdown:
    """
    Create a markdown file. A Markdown object is composed of two fields:

    * **filename** (str)
    * **f** (file object)

    """
    def __init__(self, filename):
        """
        Init a markdown file. It creates and opens the file.

        Args:
            filename (str): filename (markdown file)

        """
        self._filename = filename
        self._f = open(filename, 'w')

    @property
    def filename(self):
        """Get the filename."""
        return self._filename

    @property
    def f(self):
        """Get the file object."""
        return self._f

    def __enter__(self):
        """Enter in a with statement."""
        return self

    def write(self, text, break_before=True, break_after=True):
        """
        Write text in the file. You can precise if you want a break line
        before and/or after the text.

        Args:
            text (str): text to add
            breack_before (bool): add a break line before the text if True
            breack_after (bool): add a break line after the text if True

        """
        text = '\n' + text if break_before else text
        text = text + '\n' if break_after else text
        self.f.write(text)

    def close(self):
        """Close the file."""
        self.f.close()

    def add_title(self, title, level):
        """
        Add a title to the file. You can choose the level of the title.

        Args:
            title (str): title to add
            level (int): level of the title (must be between 1 and 6)

        Raises:
            Exception: invalid level for a title in md

        """
        if not 1 <= level <= 6:
            raise Exception('invalid level for a title in md')
        self.write(''.join([level*'#', ' ', title.capitalize()]), level != 1)

    def add_image(self, file, name='Track'):
        """
        Add an image to the file.

        Args:
            file (str): filename of the image to add
            name (str): label of the image

        """
        self.write('![{}]({})'.format(name, file))

    def add_separator(self):
        """Add a separator to the file."""
        self.write('---')

    def add_table(self, array, head=True):
        """
        Add a table to the file. You can precise if you want a header or not.

        Args:
            array(numpy.array): table to add
            head(bool): make a header if True

        """
        add_hline = False
        for line in array:
            str_line = [str(i) for i in line]
            self.write(' | '.join(str_line), False)
            if not add_hline and head:
                self.write(' | '.join([':---:']*len(line)), False)
            add_hline = True

    def __exit__(self, exc_type, exc_value, traceback):
        """Exit and close the file."""
        self.close()
