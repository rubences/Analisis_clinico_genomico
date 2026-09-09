# MUBIO06 · Actividad 2 · Análisis clínico genómico

[![Genomic Workflow QA](https://github.com/rubences/Analisis_clinico_genomico/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/rubences/Analisis_clinico_genomico/actions/workflows/ci.yml)

Propuesta reproducible para realizar la actividad sobre **enfermedad de células falciformes** y el gen **HBB**, utilizando datos humanos de secuenciación pública y un flujo de trabajo en Galaxy.

## Estado de validación

La estructura del proyecto y sus controles automatizados están preparados y validados en CI. El flujo cubre los siete criterios de la rúbrica: búsqueda fenotípica, obtención de secuenciación, control de calidad, limpieza, alineamiento, llamado/documentación VCF y análisis de variantes.

La evidencia final de Galaxy, ClinVar, ENA y VEP **no se simula**: debe obtenerse mediante ejecución real y sustituir los marcadores del informe antes de la entrega. Véase `docs/CIERRE_ENTREGA.md`.

## Caso de estudio

- Enfermedad: enfermedad de células falciformes (Hb SS disease / sickle cell disease).
- Gen: `HBB` (NCBI Gene 3043; Ensembl ENSG00000244734).
- Variante clínica de referencia: `rs334`, `NM_000518.5:c.20A>T`, `p.Glu7Val`.
- GRCh38: `chr11:5227002 T>A`.
- ClinVar Variation ID: `15333` (patogénica para Hb SS disease).
- Dataset de trabajo: `SRR29275383`, biblioteca `SCD10-Mock-2`, datos humanos paired-end dirigidos al locus HBB.

## Por qué este caso

Es un caso especialmente adecuado para la rúbrica porque permite conectar de forma directa fenotipo, gen, secuenciación, control de calidad, alineamiento, VCF y anotación funcional. Además, existe una variante causal canónica bien documentada y el conjunto de datos tiene una finalidad experimental explícita sobre HBB.

## Entregables

- `MUBIO06_Actividad2_Analisis_Clinico_Genomico_preparado.docx`: informe editable, con marcadores de capturas reales.
- `MUBIO06_Actividad2_Analisis_Clinico_Genomico_preparado.pdf`: PDF preparado para revisión; antes de entregar debe sustituirse cada marcador por su captura real de Galaxy/ClinVar/ENA/VEP.
- `docs/GALAXY_WORKFLOW.md`: flujo paso a paso en Galaxy con parámetros recomendados.
- `docs/PLAN_CAPTURAS.md`: lista exacta de evidencias que hay que capturar.
- `docs/MATRIZ_RUBRICA.md`: trazabilidad completa de los 10 puntos.
- `docs/RESULTADOS_ESPERADOS.md`: qué observar y cómo interpretarlo sin inventar métricas.
- `docs/CIERRE_ENTREGA.md`: checklist de cierre previo a la entrega.
- `config/analysis_manifest.json`: coordenadas, accesiones y decisiones de referencia.
- `scripts/validate_vcf.py`: comprobación del VCF exportado.
- `scripts/validate_vep.py`: comprobación de una tabla TSV exportada desde VEP.
- `scripts/fastq_audit.py`: auditoría básica de FASTQ locales.

## Flujo resumido

1. Documentar SCD/HBB en ClinVar y NCBI Gene/OMIM.
2. Localizar en ENA/SRA la ejecución `SRR29275383` y cargar R1/R2 en Galaxy.
3. Ejecutar FastQC + MultiQC sobre lecturas crudas.
4. Limpiar con fastp y repetir FastQC + MultiQC.
5. Alinear contra `GRCh38/hg38` con BWA-MEM/BWA-MEM2; ordenar/indexar BAM y revisar métricas.
6. Llamar variantes con FreeBayes (o bcftools) y revisar el VCF.
7. Anotar el VCF con Ensembl VEP y priorizar variantes de HBB, verificando `rs334` si aparece en la ejecución real.

## Cobertura de la rúbrica

| Criterio | Peso | Cobertura del repositorio |
|---|---:|---|
| Búsqueda en bases fenotípicas | 10 % | ClinVar + NCBI Gene/OMIM |
| Búsqueda de secuenciación | 10 % | ENA/SRA · `SRR29275383` |
| Control de calidad | 20 % | FastQC + MultiQC pre-limpieza |
| Limpieza | 10 % | fastp + QC post-limpieza |
| Alineamiento | 15 % | BWA-MEM/BWA-MEM2 + BAM + métricas |
| Llamado/documentación VCF | 15 % | FreeBayes/bcftools + VCF + validador |
| Análisis de variantes | 20 % | Ensembl VEP + interpretación clínica |
| **Total** | **100 %** | **Cobertura completa** |

## Evidencia académica

El enunciado exige capturas de los pasos realizados. Este repositorio **no contiene capturas simuladas** ni métricas inventadas. Las cifras de FastQC, alineamiento, profundidad, genotipo y calidad de variantes deben proceder de la ejecución real en Galaxy.

Antes de entregar el PDF final deben existir evidencias reales de:

- búsqueda del fenotipo/gen;
- búsqueda y selección de secuenciación humana en ENA;
- QC inicial;
- limpieza y QC posterior;
- alineamiento y métricas;
- VCF y llamado de variantes;
- anotación/interpretación en VEP.

## Datos

No versionar los FASTQ ni BAM en GitHub. Los dos FASTQ de `SRR29275383` se pueden importar en Galaxy mediante URL desde ENA:

```text
https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR292/083/SRR29275383/SRR29275383_1.fastq.gz
https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR292/083/SRR29275383/SRR29275383_2.fastq.gz
```

## Validación automática

GitHub Actions comprueba en cada `push` a `main` y en cada Pull Request que:

- los scripts Python compilan;
- `analysis_manifest.json` mantiene HBB, GRCh38 y la variante de referencia coherentes;
- los entregables canónicos existen;
- no se han versionado FASTQ, BAM o CRAM.

Los validadores `validate_vcf.py` y `validate_vep.py` están preparados para aplicarse a los ficheros reales exportados del análisis.

## Referencias clave

- NCBI Gene HBB: https://www.ncbi.nlm.nih.gov/gene/3043
- ClinVar rs334 / Variation ID 15333: https://www.ncbi.nlm.nih.gov/clinvar/variation/15333/
- Moiani A. et al. Nature Communications 15, 4965 (2024). DOI: 10.1038/s41467-024-49353-3
- Ensembl VEP: https://www.ensembl.org/Tools/VEP
- Galaxy: https://usegalaxy.org/
