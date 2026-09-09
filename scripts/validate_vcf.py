#!/usr/bin/env python3
import argparse, gzip, re, sys

TARGETS = {
    "GRCh38": [("chr11", 5227002, "T", "A"), ("11", 5227002, "T", "A")],
    "GRCh37": [("11", 5248232, "T", "A"), ("chr11", 5248232, "T", "A")],
}

def opener(path):
    return gzip.open(path, 'rt') if str(path).endswith('.gz') else open(path, 'rt', encoding='utf-8')

def main():
    ap = argparse.ArgumentParser(description='Busca la variante HbS rs334 en un VCF exportado de Galaxy.')
    ap.add_argument('vcf')
    ap.add_argument('--assembly', choices=['GRCh38','GRCh37'], default='GRCh38')
    args = ap.parse_args()
    hits=[]
    with opener(args.vcf) as fh:
        for line in fh:
            if not line or line.startswith('#'): continue
            f=line.rstrip('\n').split('\t')
            if len(f)<8: continue
            chrom,pos,vid,ref,alts,qual,flt,info=f[:8]
            try: pos=int(pos)
            except ValueError: continue
            for alt in alts.split(','):
                if (chrom,pos,ref,alt) in TARGETS[args.assembly]:
                    rec={'chrom':chrom,'pos':pos,'id':vid,'ref':ref,'alt':alt,'qual':qual,'filter':flt,'info':info}
                    if len(f)>=10:
                        keys=f[8].split(':'); vals=f[9].split(':')
                        rec['sample']=dict(zip(keys, vals))
                    hits.append(rec)
    if not hits:
        print(f'NO ENCONTRADA: variante HbS esperada para {args.assembly}.')
        print('Esto no implica por sí solo ausencia biológica: revisar cobertura, caller, filtros y ensamblaje.')
        return 2
    print(f'PASS: {len(hits)} registro(s) compatible(s) con HbS/rs334 en {args.assembly}.')
    for h in hits:
        print(h)
    return 0

if __name__=='__main__':
    raise SystemExit(main())
