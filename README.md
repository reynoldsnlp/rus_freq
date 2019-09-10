# rus\_freq
Russian token- and lemma-frequency data

```python
import rus_freq

tok = rus_freq.RNC_tok_freq()
tok.freq['словами']
# 17669.0

lem = rus_freq.Sharoff_lem_freq()
lem.freq['слово']
# 957.14
lem.ambig_freq['стать']
# [(1659.89, '61', 'verb'), (6.28, '11761', 'noun')]
```
