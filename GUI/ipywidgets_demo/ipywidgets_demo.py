from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
import time

def func(x):
    return x**2

# Create a slide bar
interact(func, x = 10)

# Create a checkbox
interact(func, x = True)

time.sleep(10)
