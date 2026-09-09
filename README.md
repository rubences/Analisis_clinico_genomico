# MUBIO06 · Actividad 2 · Análisis clínico genómico

Propuesta reproducible para realizar la actividad sobre **enfermedad de células falciformes** y el gen **HBB**, utilizando datos humanos de secuenciación pública y un flujo de trabajo en Galaxy.

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

## Evidencia académica

El enunciado exige capturas de los pasos realizados. Este repositorio **no contiene capturas simuladas** ni métricas inventadas. Las cifras de FastQC, alineamiento, profundidad, genotipo y calidad de variantes deben proceder de la ejecución real en Galaxy.

## Datos

No versionar los FASTQ ni BAM en GitHub. Los dos FASTQ de `SRR29275383` se pueden importar en Galaxy mediante URL desde ENA:

```text
https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR292/083/SRR29275383/SRR29275383_1.fastq.gz
https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR292/083/SRR29275383/SRR29275383_2.fastq.gz
```

## Referencias clave

- NCBI Gene HBB: https://www.ncbi.nlm.nih.gov/gene/3043
- ClinVar rs334 / Variation ID 15333: https://www.ncbi.nlm.nih.gov/clinvar/variation/15333/
- Moiani A. et al. Nature Communications 15, 4965 (2024). DOI: 10.1038/s41467-024-49353-3
- Ensembl VEP: https://www.ensembl.org/Tools/VEP
- Galaxy: https://usegalaxy.org/
