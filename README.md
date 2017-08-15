# color-check
This python script alerts the user when a certain color is detected on the screen. It can check a part of the screen, test a variable percent of pixels, search for a range of RGB values, and pause upon a positive result.

## Usage:

Install the dependencies (preferably in a virtualenv):
```
pip2 install -r requirements.txt
```
Set the following variables in the script:

- **xMIN**: Smallest x-coordinate of pixels checked.

- **xMAX**: Largest x-coordinate of pixels checked.

- **yMIN**: Smallest y-coordinate of pixels checked.

- **yMAX**: Largest y-coordinate of pixels checked.

- **fractionCHECK**: Fraction of pixels checked. Should be between 0 and 1.

- **rRANGE**: Target range of R in RGB value of pixel.

- **gRANGE**: Target range of G in RGB value of pixel.

- **bRANGE**: Target range of B in RGB value of pixel.

- **timePAUSE**: How many seconds the script waits after alerting the user of a positive result.

Launch the script:
```
python colorcheck.py
```
 
Press CTRL+C at any time to interrupt the script.
