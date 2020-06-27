"""
With the **printer** module, you can print the tracks built with the
library. It uses *CUPS*.

Warnings:
    This module can be used only on Linux and macOS.

"""
import os
import cups
import logging
from line_track_designer.error import LineTrackDesignerError


class Printer:
    """
    Manage the printer to print a track. It is composed of three fields:

    * **conn**: connection to the *CUPS* server
    * **printer_name**: the name of the default printer
    * **file_tiles**: the path to the PDF document with the tiles to print

    Raises:
        LineTrackDesignerError: no printers found

    Note:
        If no printer is found, you need to add one in your devices.

    """
    def __init__(self):
        """Init a Printer object."""
        self._conn = cups.Connection()
        printers = self._conn.getPrinters()
        if printers:
            self._printer_name = list(printers.keys())[0]
            cwd = os.path.dirname(os.path.abspath(__file__))
            self._file_tiles = os.path.join(cwd, 'pdf', 'linefollowtiles.pdf')
        else:
            raise LineTrackDesignerError('no printers found')
        logging.info('Printer {} found'.format(self.printer_name))

    @property
    def conn(self):
        """Get the connection."""
        return self._conn

    @property
    def printer_name(self):
        """Get the name of the printer."""
        return self._printer_name

    @property
    def file_tiles(self):
        """Get the path of the PDF file."""
        return self._file_tiles

    def __str__(self):
        """
        Make the string format of the Printer object.
        It returns the name of the printer.
        """
        return self.printer_name

    def __repr__(self):
        """
        Make the repr format of the Printer object.
        It's the same than the string format.
        """
        return str(self)

    def print_page(self, copies, pages, title, media='a4'):
        """
        Ask to the printer to print pages of the PDF file.

        Args:
            copies (int): number of copies to print
            pages (int): pages to print
            title (str): name of the printing
            media (str): format (default: 'a4')

        Raises:
            LineTrackDesignerError: printing failed

        """
        try:
            self.conn.printFile(
                self.printer_name,
                self.file_tiles,
                title,
                {
                    'copies': str(copies),
                    'page-ranges': str(pages),
                    'media': media,
                    'sides': 'one-sided'})
        except Exception:
            raise LineTrackDesignerError('printing failed')
        logging.info('Pages {} printed'.format(pages))
