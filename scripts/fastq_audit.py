#!/usr/bin/env python3
import argparse, gzip, statistics

def openq(p): return gzip.open(p,'rt') if p.endswith('.gz') else open(p,'rt')
def audit(path, limit):
    n=0; lens=[]; means=[]; ns=0; bases=0
    with openq(path) as f:
        while n < limit:
            h=f.readline(); s=f.readline().rstrip(); plus=f.readline(); q=f.readline().rstrip()
            if not q: break
            n+=1; lens.append(len(s)); bases+=len(s); ns+=s.upper().count('N')
            means.append(sum(ord(c)-33 for c in q)/len(q))
    return n, lens, means, ns, bases

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('fastq', nargs='+'); ap.add_argument('--reads', type=int, default=100000); a=ap.parse_args()
    for p in a.fastq:
        n,l,m,ns,b=audit(p,a.reads)
        print(p)
        print(' sampled_reads=',n)
        print(' length_min/median/max=',min(l),statistics.median(l),max(l))
        print(' mean_phred=',round(statistics.mean(m),2))
        print(' N_fraction=',round(ns/b,6) if b else 0)
if __name__=='__main__': main()
