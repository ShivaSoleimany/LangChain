import os
import sys

# Dynamically add the root project directory to Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Debugging: Print the path to ensure it's correct
print("Added to PYTHONPATH:", os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
