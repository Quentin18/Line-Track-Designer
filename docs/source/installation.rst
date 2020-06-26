Installation
============

Using pip
---------
You can install latest release of the *Line Track Designer* library with ``pip3``:

.. code-block:: bash

    pip3 install line_track_designer

Using setuptools
----------------
The second way to install the library is to clone the GitHub repository and to use *setuptools*:

.. code-block:: bash

    git clone https://github.com/Quentin18/Line-Track-Designer.git
    python3 setup.py install

Installing on Windows
---------------------
On Windows, you can install the library with the two methods above.
But, you probably will see the warning bellow:

.. code-block:: bash

    The script linetrack.exe is installed in 'C:\Users\...' which is not on PATH.

To fix this warning, add the path indicated in the message to the PATH. You can follow the tutorial
`here <https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/>`_.

Markdown editor
---------------
If you do not have any markdown editor, you can download `Zettlr <https://www.zettlr.com/>`_.
It is very usefull to see markdown files built with *Line Track Designer*. In addition, to convert
markdown files into PDF files, you need to install:

* `Pandoc <https://pandoc.org/installing.html>`_
* `MiKTeX <https://miktex.org/download>`_

Running tests
-------------
If you cloned the repository, the tests can be run using:

.. code-block:: bash

    python3 setup.py pytest
