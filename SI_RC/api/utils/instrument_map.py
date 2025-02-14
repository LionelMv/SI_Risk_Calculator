"""
CHOICES is a list of tuples containing instrument choices for a dropdown menu.
Each tuple consists of a value and a display label.
The dropdown menu allows users to select a specific instrument. The selected
instrument gives the value to be used in the INSTRUMENTS dictionary.

INSTRUMENTS is used to associate each Synthetic Index value from the
CHOICES list with its lowest allowable lot size as provided by Deriv.
Example Usage:
If a user selects 'b1000' as their Synthetic Index, the lot size for
'b1000' would be 0.2.
"""


CHOICES = [
    ('', 'Choose from dropdown'),
    ('b1000', 'Boom 1000 Index'),
    ('b300', 'Boom 300 Index'),
    ('b500', 'Boom 500 Index'),
    ('c1000', 'Crash 1000 Index'),
    ('c300', 'Crash 300 Index'),
    ('c500', 'Crash 500 Index'),
    ('j10', 'Jump 10 Index'),
    ('j100', 'Jump 100 Index'),
    ('j25', 'Jump 25 Index'),
    ('j50', 'Jump 50 Index'),
    ('j75', 'Jump 75 Index'),
    ('r100', 'Range Break 100 Index'),
    ('r200', 'Range Break 200 Index'),
    ('si', 'Step Index'),
    ('v10(1s)', 'Volatility 10 (1s) Index'),
    ('v10', 'Volatility 10 Index'),
    ('v100(1s)', 'Volatility 100 (1s) Index'),
    ('v100', 'Volatility 100 Index'),
    ('v200(1s)', 'Volatility 200 (1s) Index'),
    ('v25(1s)', 'Volatility 25 (1s) Index'),
    ('v25', 'Volatility 25 Index'),
    ('v300(1s)', 'Volatility 300 (1s) Index'),
    ('v50(1s)', 'Volatility 50 (1s) Index'),
    ('v50', 'Volatility 50 Index'),
    ('v75(1s)', 'Volatility 75 (1s) Index'),
    ('v75', 'Volatility 75 Index'),
    ('v150(1s)', 'Volatility 150 (1s) Index'),
    ('v250(1s)', 'Volatility 250 (1s) Index')
]


INSTRUMENTS = {
    'b1000': 0.2,
    'b300': 0.1,
    'b500': 0.2,
    'c1000': 0.2,
    'c300': 0.5,
    'c500': 0.2,
    'j10': 0.01,
    'j100': 0.01,
    'j25': 0.01,
    'j50': 0.01,
    'j75': 0.01,
    'r100': 0.01,
    'r200': 0.01,
    'si': 0.1,
    'v10(1s)': 0.2,
    'v10': 0.3,
    'v100(1s)': 0.1,
    'v100': 0.2,
    'v200(1s)': 0.02,
    'v25(1s)': 0.005,
    'v25': 0.5,
    'v300(1s)': 1,
    'v50(1s)': 0.005,
    'v50': 3,
    'v75(1s)': 0.005,
    'v75': 0.001,
    'v150(1s)': 0.001,
    'v250(1s)': 0.001
}
