import sys
sys.path[0] += "\\Lib\\site-packages"

import PyInstaller.__main__ as pi

pi.run(
    ["main.py", 
     "--name", 
     "Stopwatch" ,
     "--onefile", 
     "--noconsole"]
    )
