#!c:\users\joser\documents\programación_dinámica_y_estocástica_con_python\.env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bokeh==2.0.1','console_scripts','bokeh'
__requires__ = 'bokeh==2.0.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bokeh==2.0.1', 'console_scripts', 'bokeh')()
    )
