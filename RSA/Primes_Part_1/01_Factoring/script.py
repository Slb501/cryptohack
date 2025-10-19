#!/usr/bin/env python3

#python3 -m venv ~/myenv
#source ~/myenv/bin/activate
#python -m pip install git+https://github.com/elliptic-shiho/primefac-fork.git
import primefac

N = 510143758735509025530880200653196460532653147
print("test (liste de facteurs) ->", list(primefac.primefac(N)))
