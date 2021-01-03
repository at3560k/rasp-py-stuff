import sys

from nuke.core import run_exit

if sys.argv[0].endswith('__main__.py'):
    sys.argv[0] = '%s -m nuke' % sys.executable

    run_exit()
