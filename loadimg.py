import os
import sys
import pygame as p
import setting as s

def resource_path(relative_path):
    """Get the absolute path to a resource, works for development and PyInstaller."""
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def load_image(file_path, size):
    """Load and scale an image, with error handling."""
    try:
        full_path = resource_path(file_path)
        image = p.image.load(full_path)
        return p.transform.scale(image, size)
    except FileNotFoundError:
        print(f"Error: Could not load image at {full_path}")
        # Return a blank surface as a fallback
        return p.Surface(size)

def loadChessMan():
    """Load chess piece images."""
    chessMan = {}
    chessName = ['bch', 'bma', 'bph', 'bxe', 'bvo', 'bsi', 'btu', 'rch', 'rma', 'rph', 'rxe', 'rvo', 'rsi', 'rtu']
    for name in chessName:
        file_path = os.path.join('img', f'{name}.png')
        chessMan[name] = load_image(file_path, (s.CELL_SIZE, s.CELL_SIZE))
    return chessMan

def loadBoard():
    """Load the chess board image."""
    file_path = os.path.join('img', 'board.jpg')
    return load_image(file_path, (s.WIDTH, s.HEIGHT))

def loadLight():
    """Load the light effect image."""
    file_path = os.path.join('img', 'light.png')
    return load_image(file_path, (s.CELL_SIZE, s.CELL_SIZE))

def loadButton(button_type):
    """Load button images based on type."""
    button_configs = {
        'backward': {
            'states': ['backward.png', 'backwardActive.png', 'backwardClick.png', 'backwardHover.png'],
            'has_four_states': True
        },
        'nextstep': {
            'states': ['nextstep.png', 'nextstepActive.png', 'nextstepClick.png', 'nextstepHover.png'],
            'has_four_states': True
        },
        'reverse': {
            'states': ['exchange.png', 'exchangeActive.png', 'exchangeClick.png', 'exchangeHover.png'],
            'has_four_states': True
        },
        'start': {
            'states': ['start.png', 'startClick.png', 'startHover.png'],
            'has_four_states': False
        },
        'replay': {
            'states': ['replay.png', 'replayClick.png', 'replayHover.png'],
            'has_four_states': False
        }
    }

    if button_type not in button_configs:
        print(f"Error: Invalid button type '{button_type}'")
        return [p.Surface((s.BUT_WIDTH, s.BUT_HEIGHT))] * 4

    config = button_configs[button_type]
    buttons = []
    for state in config['states']:
        file_path = os.path.join('img', state)
        buttons.append(load_image(file_path, (s.BUT_WIDTH, s.BUT_HEIGHT)))

    # Pad with None if the button type has only 3 states
    if not config['has_four_states']:
        buttons.append(None)

    return buttons

def loadSquare():
    """Load the square origin image."""
    file_path = os.path.join('img', 'squareOrigin.png')
    return load_image(file_path, (s.CELL_SIZE, s.CELL_SIZE))

def loadCheckMate():
    """Load the checkmate image."""
    file_path = os.path.join('img', 'check.png')
    return load_image(file_path, (s.CELL_SIZE * 3, s.CELL_SIZE * 3))