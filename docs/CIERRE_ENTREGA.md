# Cierre de entrega · MUBIO06 Actividad 2

## Estado técnico

- Caso de estudio fijado: enfermedad de células falciformes / `HBB`.
- Ensamblado de referencia: `GRCh38`.
- Variante clínica de referencia: `rs334` / `NM_000518.5:c.20A>T` / `p.Glu7Val`.
- Coordenada de control en GRCh38: `chr11:5227002 T>A`.
- Dataset humano paired-end: `SRR29275383`.
- Flujo documentado: ClinVar/OMIM → ENA → FastQC/MultiQC → fastp → alineamiento → VCF → VEP.
- Scripts de apoyo y validación presentes.
- CI configurada para comprobar sintaxis, manifiesto, estructura y ausencia de FASTQ/BAM/CRAM versionados.

## Checklist académico obligatorio antes de entregar

- [ ] Captura 1: búsqueda fenotípica/genómica que relacione enfermedad y `HBB`.
- [ ] Captura 2: registro humano de secuenciación seleccionado en ENA/SRA.
- [ ] Captura 3: FastQC/MultiQC sobre lecturas crudas, con interpretación escrita.
- [ ] Captura 4: limpieza de secuencias y QC posterior, comparando antes/después.
- [ ] Captura 5: alineamiento contra GRCh38 y comentario de métricas del BAM.
- [ ] Captura 6: llamado de variantes y visualización/documentación del VCF.
- [ ] Captura 7: anotación con Ensembl VEP e interpretación biológica/clínica.
- [ ] Sustituir todos los marcadores del DOCX/PDF por capturas auténticas.
- [ ] Comprobar que las cifras descritas en el texto coinciden con las capturas reales.
- [ ] Mantener Calibri 12, interlineado simple y un máximo de 20 páginas.
- [ ] Exportar y revisar visualmente el PDF definitivo.

## Qué no debe hacerse

- No inventar métricas de FastQC, cobertura, mapping rate, profundidad o calidad.
- No afirmar que `rs334` aparece en el VCF si la ejecución real no lo demuestra.
- No mezclar coordenadas GRCh37 y GRCh38 en el mismo análisis.
- No subir al repositorio FASTQ, BAM, CRAM u otros ficheros de secuenciación pesados.
- No sustituir las capturas exigidas por tablas o imágenes simuladas.

## Validación de resultados reales

Cuando existan los artefactos de ejecución:

```bash
python scripts/validate_vcf.py <archivo.vcf>
python scripts/validate_vep.py <vep_export.tsv>
python scripts/fastq_audit.py <R1.fastq.gz> <R2.fastq.gz>
```

Estos controles sirven como apoyo técnico. La evidencia evaluable sigue siendo la ejecución real documentada en el informe final.
