# Line Track Designer
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*Line Track Designer* is a library to design line following tracks for robots. With this tool, you can easily **edit**, **save**, **share** and **print** your tracks with a printer.

Tracks can be created in two different ways:

- with the command line interface (CLI)
- with the application programming interface in Python (API)

## Installation
*Line Track Designer* can be installed using [pip](https://pip.pypa.io/en/stable/):
```bash
pip3 install line_track_designer
```

## Quickstart
For example, we consider a file named ``track.txt``:
```
3;1 2;1 3;0
2;0 11;0 2;0
3;2 2;1 3;3
```
This file represents the following track:
![Track](https://github.com/Quentin18/Line-Track-Designer/blob/master/docs/source/img/track.png)

This picture can be obtained with the following command:
```bash
linetrack show track.txt
```

You can also generate documentation for your track using this command:
```bash
linetrack savemd track.txt
```

It generates a markdown file with informations about the track. You can see an example [here](docs/source/pdf/track.pdf).

You can also use the API to create tracks:
```python
import numpy as np
from line_track_designer.track import Track


# Arrays for the track
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

# Creation of the track
track = Track(tiles, orient, 'Test track')

# Save the track
track.save_txt('track.txt')
# Make png file
track.save_img('track.png')
# Make markdown file
track.save_md('track.md', 'Easy track')
```

For more details, see the documentation [here]().

## Links
- GitHub: https://github.com/Quentin18/Line-Track-Designer
- PyPI:
- Documentation:

## Author
Quentin Deschamps: quentindeschamps18@gmail.com

## License
[MIT](https://choosealicense.com/licenses/mit/)
