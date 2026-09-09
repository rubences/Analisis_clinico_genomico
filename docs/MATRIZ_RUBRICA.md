# Matriz de trazabilidad de la rúbrica

| Criterio | Peso | Evidencia prevista | Sección del informe |
|---|---:|---|---|
| 1. Búsqueda en bases fenotípicas | 10 % | ClinVar/NCBI Gene: SCD ↔ HBB; rs334; significancia clínica | 1 |
| 2. Búsqueda correcta de datos de secuenciación | 10 % | ENA/SRA `SRR29275383`; Homo sapiens; paired-end; HBB | 2 |
| 3. Control de calidad documentado | 20 % | FastQC R1/R2 + MultiQC, interpretación por-base/adaptadores | 3 |
| 4. Limpieza tras QC | 10 % | fastp paired-end + FastQC/MultiQC post-limpieza | 4 |
| 5. Alineamiento y comentario | 15 % | BWA-MEM/MEM2 a GRCh38; BAM ordenado/indexado; flagstat/coverage | 5 |
| 6. Llamado de variantes y VCF | 15 % | FreeBayes/bcftools; explicación CHROM/POS/REF/ALT/QUAL/INFO/FORMAT | 6 |
| 7. Análisis de variantes | 20 % | Ensembl VEP; gen/consecuencia/HGVS/ClinVar/dbSNP/priorización | 7 |
| **Total** | **100 %** | **Cobertura completa** | |

## Controles de máxima puntuación

- Mantener **una sola asamblea** durante el flujo: GRCh38/hg38.
- Explicar por qué HBB está en hebra negativa: la variante transcriptómica `c.20A>T` corresponde genómicamente a `T>A` en GRCh38.
- Comparar FastQC antes/después de fastp, no limitarse a mostrar dos capturas.
- Comentar métricas de alineamiento y cobertura, no solo que “terminó correctamente”.
- Explicar el formato VCF y distinguir `REF/ALT`, `QUAL`, `FILTER`, `INFO` y `FORMAT`.
- En VEP, priorizar por consecuencia, gen, coincidencia con variantes conocidas y evidencia clínica; no reducir el análisis a “patogénica/no patogénica”.
- No usar valores simulados como si fueran resultados de Galaxy.
