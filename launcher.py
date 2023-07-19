import os

os.system("python3 -m pip install -r requirements.txt")

from main import *

app = VoxelEngine()
app.run()
