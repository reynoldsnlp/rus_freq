"""Simple module to provide Russian token frequency data."""

import bz2
from collections import defaultdict
from pkg_resources import resource_filename
import sys

__all__ = ['RNC_tok_freq', 'RNC_2gram_freq', 'Sharoff_lem_freq']

RSRC_PATH = resource_filename('rus_freq', 'resources/')


def absent():
    """Used as default in defaultdict's."""
    return 0


class RNC_tok_freq:
    """Token freq data from Russian National Corpus 1-gram data.

    Taken from: http://ruscorpora.ru/corpora-freq.html
    """
    def __init__(self, path=RSRC_PATH + 'RNC_1grams-3.txt.bz2'):
        """Initialize frequency dictionary."""
        self.freq = defaultdict(absent)
        with bz2.open(path, 'rt', encoding='utf8') as freq_file:
            for line in freq_file:
                token_freq, token = line.split()
                self.freq[token] = float(token_freq)


class RNC_2gram_freq:
    """Bigram freq data from Russian National Corpus 2-gram data.

    Taken from: http://ruscorpora.ru/corpora-freq.html
    """
    def __init__(self, path=RSRC_PATH + 'RNC_2grams-3.txt.bz2'):
        """Initialize frequency dictionaries."""
        self.freq_w_punct = defaultdict(absent)
        self.freq = defaultdict(absent)
        with bz2.open(path, 'rt', encoding='utf8') as freq_file:
            for line in freq_file:
                token_freq, token1, punct, token2 = line.split()
                self.freq_w_punct[(token1, punct, token2)] = float(token_freq)
                if (token1, token2) not in self.freq:
                    self.freq[(token1, token2)] = float(token_freq)
                else:
                    self.freq[(token1, token2)] += float(token_freq)


class Sharoff_lem_freq:
    """Lemma freq data from Serge Sharoff.

    Taken from: http://www.artint.ru/projects/frqlist/frqlist-en.php
    """
    def __init__(self, path=RSRC_PATH + 'Sharoff_lemma_freq.txt.bz2'):
        """Initialize frequency dictionary."""
        self.freq = defaultdict(absent)
        self.freq_w_rank_and_pos = defaultdict(absent)
        self.ambig_freq = defaultdict(absent)
        self.ambigs = []
        with bz2.open(path, 'rt', encoding='utf8') as freq_file:
            for line in freq_file:
                rank, freq, lemma, pos = line.split()
                freq = float(freq)
                if lemma in self.freq:
                    self.ambigs.append(lemma)
                self.freq[lemma] = freq
                self.freq_w_rank_and_pos[lemma] = (freq, rank, pos)
                try:
                    self.ambig_freq[lemma].append((freq, rank, pos))
                except AttributeError:
                    self.ambig_freq[lemma] = [(freq, rank, pos)]
            print('WARNING: the following lemma names are ambiguous. Using '
                  'the ambig_freq dictionary is highly recommended:',
                  list(sorted(set(self.ambigs))), file=sys.stderr)
