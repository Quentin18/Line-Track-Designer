CLI
===

The command line interface of *Line Track Designer* is only available for Linux and Mac OS.
It uses *Click*. To check if you successfully installed the library, you can entry in a command prompt:

.. code-block:: bash

    linetrack --help

You should see the following content:

.. code-block:: text

    Usage: linetrack [OPTIONS] COMMAND [ARGS]...

    Generate line following tracks for robots.

    Options:
    --help  Show this message and exit.

    Commands:
    create    Create empty track FILENAME.
    edit      Edit track FILENAME.
    printing  Print track FILENAME.
    rotate    Rotate track FILENAME.
    savemd    Save track FILENAME as MD file.
    savepng   Save track FILENAME as PNG file.
    show      Show track FILENAME as PNG file.
    write     Write track FILENAME in the command prompt.

Creating a track
----------------
To create a track, you can use the ``create`` command:

.. code-block:: bash

    linetrack create [OPTIONS] FILENAME NROW NCOL

FILENAME must be a text file. You need to indicates the number of rows and columns of the track.
It creates a track with only blank tiles and open it so you can edit it.

For example:

.. code-block:: bash

    linetrack create track.txt 3 4

This command creates the file ``track.txt`` and open it with this content:

.. code-block:: text

    0;0 0;0 0;0 0;0
    0;0 0;0 0;0 0;0
    0;0 0;0 0;0 0;0

Editing a track
---------------
The ``edit`` command is usefull to open a track with your default text editor and modify it.

.. code-block:: bash

    linetrack edit [OPTIONS] FILENAME

The file must be a text file corresponding to a track.


Showing a track
---------------
You can display a track in two different ways:

- writing it in the command prompt using the ``write`` command

.. code-block:: bash

    linetrack write [OPTIONS] FILENAME

- showing it in your picture viewer using the ``show`` command

.. code-block:: bash

    linetrack show [OPTIONS] FILENAME

For example, we consider the ``track.txt`` file with this content:

.. code-block:: text

    3;1 2;1 3;0
    2;0 11;0 2;0
    3;2 2;1 3;3

The first command will display its content in the command prompt:

.. code-block:: bash

    linetrack write track.txt

With the second command,

.. code-block:: bash

    linetrack show track.txt

We can see this PNG image:

.. image:: img/track.png


Exporting a track
-----------------
