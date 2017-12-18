"""
1st option
"""

import profile
from june5 import pokemone_parse

profile.run('pokemone_parse.max_total(pokemone_parse.load())')


"""
2st option
"""
'pip install line_profiler'
'kernprof -l pokemone_parse.py'
'python -m line_profiler pokemon_parse.py.lprof'


"""
3d option
"""
'pip install memory_profiler' '+' 'pip intsll psutil'
'python -m memory_profiler pokemon_parse.py'

"""
4d option
"""
'pip install pympler'