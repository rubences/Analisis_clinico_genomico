# Flujo exacto en Galaxy

## 0. Preparación del historial

Crear un historial nuevo llamado `MUBIO06_Act2_HBB_SCD`. Mantener en todo el análisis la asamblea **GRCh38/hg38**.

## 1. Obtención de lecturas

En **Upload data → Paste/Fetch data**, cargar las dos URL de ENA:

```text
https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR292/083/SRR29275383/SRR29275383_1.fastq.gz
https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR292/083/SRR29275383/SRR29275383_2.fastq.gz
```

Renombrar como:

- `SCD10-Mock-2_R1.fastq.gz`
- `SCD10-Mock-2_R2.fastq.gz`

Comprobar datatype `fastqsanger.gz` y, si Galaxy lo permite, asignar database/build `hg38` solo cuando corresponda a datos alineados; los FASTQ no necesitan build.

## 2. Control de calidad inicial

Ejecutar **FastQC** sobre R1 y R2. Después ejecutar **MultiQC** sobre ambas salidas.

Interpretar al menos:

- Per base sequence quality.
- Per sequence quality scores.
- Adapter content.
- Sequence length distribution.
- Overrepresented sequences.
- GC content.

No registrar una métrica numérica si no aparece realmente en la salida. En este dataset se espera observar señal de adaptadores y una degradación de calidad en extremos, por lo que la limpieza está justificada.

## 3. Limpieza

Ejecutar **fastp** en modo paired-end:

- Input 1: R1.
- Input 2: R2.
- Adapter trimming: detección automática para paired-end.
- Quality filtering: Phred >= 20 como umbral inicial razonable.
- Minimum read length: 50 nt.
- Conservar pares sincronizados.

Si el FastQC real muestra un patrón distinto, adaptar los parámetros y documentar el motivo.

Repetir FastQC + MultiQC con las lecturas limpiadas y comparar antes/después: reducción de adaptadores, mejora de extremos y ausencia de un deterioro excesivo de longitud/cobertura.

## 4. Alineamiento

Preferencia: **Map with BWA-MEM / BWA-MEM2** usando referencia integrada `Human (Homo sapiens): hg38/GRCh38`.

- Paired reads: outputs de fastp.
- Reference: hg38/GRCh38.
- Read group: asignar ID/SM si la herramienta lo solicita (`SCD10-Mock-2`).

Después:

1. Ordenar BAM por coordenada si la herramienta no lo hace.
2. Indexar BAM.
3. Ejecutar **Samtools flagstat**.
4. Opcional pero muy recomendable: `samtools idxstats`, `samtools depth` o una herramienta de cobertura sobre HBB.
5. Visualizar el BAM con IGV/JBrowse en Galaxy sobre `chr11:5225464-5227071`.

Interpretar porcentaje alineado, pares correctamente alineados, duplicación si se evalúa y cobertura del locus HBB.

## 5. Llamado de variantes

Opción recomendada en Galaxy: **FreeBayes** con GRCh38.

- BAM: ordenado/indexado.
- Ploidy: diploide.
- Región objetivo (si se desea restringir): `chr11:5225464-5227071`.
- Mantener parámetros por defecto salvo que la cobertura real justifique cambios.

Alternativa: `bcftools mpileup` + `bcftools call`.

Después, filtrar de forma conservadora (ejemplo, no regla universal):

- `QUAL >= 20`.
- Profundidad suficiente para el locus; documentar el umbral elegido.

Revisar el VCF y localizar, si la llamada real lo contiene, la variante diana:

```text
GRCh38: chr11 5227002 T>A
rs334
NM_000518.5:c.20A>T
p.Glu7Val
```

## 6. Interpretación del VCF

Explicar en el informe:

- `CHROM`: cromosoma.
- `POS`: posición 1-based.
- `ID`: identificador conocido si está anotado.
- `REF`: alelo de referencia.
- `ALT`: alelo alternativo.
- `QUAL`: calidad de llamada.
- `FILTER`: estado de filtros.
- `INFO`: anotaciones globales (DP, AF, etc., según caller).
- `FORMAT` + muestra: genotipo y métricas de la muestra (GT, DP, AD, GQ, etc., según caller).

No confundir una variante conocida/esperada con una variante realmente llamada: la evidencia debe ser la línea real del VCF exportado.

## 7. Ensembl VEP

Descargar el VCF de Galaxy y cargarlo en **Ensembl VEP** con genoma humano GRCh38.

Activar, cuando estén disponibles:

- HGVS.
- Existing variations / dbSNP.
- ClinVar / phenotype associations.
- Population frequencies (gnomAD/1000G).
- SIFT/PolyPhen u otros predictores, solo como evidencia complementaria.

Priorizar variantes en HBB por:

1. consecuencia funcional;
2. coincidencia con variante conocida;
3. evidencia ClinVar/fenotipo;
4. frecuencia poblacional contextualizada;
5. calidad y soporte en el VCF.

Para `rs334`, la referencia clínica de control es `NM_000518.5:c.20A>T (p.Glu7Val)`, variante missense con asociación patogénica a enfermedad falciforme. El resultado VEP real debe capturarse y comentarse.
