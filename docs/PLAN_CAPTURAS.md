# Plan de capturas obligatorias

Guardar las capturas en `evidence/` con estos nombres. No versionar información personal del historial de Galaxy si aparece en pantalla.

| Nº | Fichero sugerido | Evidencia | Debe verse |
|---:|---|---|---|
| 01 | `01_clinvar_hbb_rs334.png` | Búsqueda fenotípica/genómica | HBB, rs334/c.20A>T, enfermedad/significancia |
| 02 | `02_ena_srr29275383.png` | Obtención de datos | SRR29275383, Homo sapiens, paired FASTQ / descripción HBB |
| 03 | `03_fastqc_raw.png` | QC inicial | FastQC/MultiQC de R1/R2 y uno o más módulos interpretables |
| 04 | `04_fastp_y_qc_post.png` | Limpieza | job fastp + comparación QC post-limpieza |
| 05 | `05_alignment_flagstat_hbb.png` | Alineamiento | BWA finalizado + flagstat/coverage; idealmente vista HBB |
| 06 | `06_vcf_hbb.png` | Llamado de variantes | VCF visible con cabecera/campos y variante(s) de HBB |
| 07 | `07_vep_hbb.png` | Análisis de variantes | consecuencia, gene, HGVS, existing variant y evidencia clínica |

## Regla de evidencia

La captura debe ser real. No usar una imagen de un tutorial para sustituir una ejecución propia. Las fuentes externas pueden citarse en la discusión, pero no reemplazan la evidencia de Galaxy requerida por la actividad.
