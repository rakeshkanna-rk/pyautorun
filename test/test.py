# INIT
'''
>>> pyauto init

        PyAuto Run

Config file created @ E:\github\pyautorun\test 
Use: pyauto run
To run the script

Happy Coding!
'''

# Add
'''
>>> pyauto add -h python -s "show = pip show pyautorun"

        PyAuto Run

Config file: .pyscripts
Added command: python.show = pip show pyautorun
New header and script added @ .pyscripts 

Use: pyauto run
To run the script

Happy Coding!
'''

# FIND
'''
>>> pyauto find -l show                                

        PyAuto Run

Found 'show' @ line 4 in .pyscripts

Happy Coding!
'''

# RUN
'''
>>> pyauto run python  

        PyAuto Run

Config file: .pyscripts
Header Name: python

Header found @ line 3: [py.python]
Number of commands executing: 1

Commands:
pip show pyautorun

Executing Commands...
Executing: pip show pyautorun

Name: pyautorun
Version: 0.1.0
Summary: Runs multi-script with a sinple line of prompt with a config dot file
Home-page:
Author: Rakesh Kanna
Author-email: rakeshkanna0108@gmail.com
License: MIT
Location: C:\Users\Akash kanna\AppData\Roaming\Python\Python312\site-packages
Requires: textPlay
Required-by:

Happy Coding!
'''