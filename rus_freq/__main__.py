import sys

from .models import RNC_tok_freq
from .models import Sharoff_lem_freq

tok = RNC_tok_freq()
lem = Sharoff_lem_freq()
print('token', 'tok_freq', 'lem_freq', sep='\t')
for line in sys.stdin:
    line = line.strip()
    print(line, tok.freq[line], lem.freq[line], sep='\t')
