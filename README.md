# image-to-ascii

A small Python project, built to learn the language, that converts an image into ASCII art and prints it in the terminal.

## How it works

1. Opens the image with [Pillow](https://python-pillow.github.io/).
2. Converts it to grayscale (`L` mode), so color images work too.
3. Resizes it so the output fits in a terminal. The width is scaled less than the height to compensate for characters being taller than they are wide.
4. Maps each pixel's brightness (0-255) to a character from a ramp, from darkest to brightest, and prints the result line by line.

The character ramp is designed for a **dark terminal background** (`@` looks brightest). For a white background, reverse the ramp.

## Requirements

- Python 3.15+
- [uv](https://docs.astral.sh/uv/)

## Usage

```bash
uv sync
uv run main.py
```

By default it reads `image.png` from the project folder. The output size is controlled by the `scale` variable in `main.py` (a higher value gives a smaller output).

## Status

Work in progress. Planned next steps:

- Choose the output width from the command line
- Contrast stretching so low-contrast images keep their detail
- Better handling of transparent images
- Split the code into functions
