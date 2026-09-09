#!/usr/bin/env python3
import argparse, csv, sys

def main():
    ap=argparse.ArgumentParser(description='Comprueba una exportación TSV de Ensembl VEP para señales de HBB/rs334.')
    ap.add_argument('tsv')
    args=ap.parse_args()
    text=open(args.tsv, encoding='utf-8', errors='replace').read()
    checks={
        'HBB': 'HBB' in text,
        'rs334': 'rs334' in text,
        'Glu7Val_or_E7V': any(x in text for x in ['Glu7Val','E7V','p.Glu7Val']),
        'missense': 'missense' in text.lower(),
    }
    for k,v in checks.items(): print(f'{k}: {"PASS" if v else "NO"}')
    if not checks['HBB']:
        return 2
    print('Nota: este script solo verifica presencia textual; la interpretación clínica debe hacerse en el informe.')
    return 0
if __name__=='__main__': raise SystemExit(main())
