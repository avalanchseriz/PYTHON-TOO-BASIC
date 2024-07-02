import os
import shutil

path = "test.txt"

try:
    os.remove(path)

except FileNotFoundError:
    print("that file wasn't found")
except PermissionError:
    os.rmdir(path)
except OSError:
    shutil.rmtree(path)