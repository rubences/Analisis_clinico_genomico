# Resultados esperados y criterios de interpretación

Este documento distingue **hechos de referencia** de **resultados que deben medirse** durante la ejecución.

## Hechos de referencia comprobables

- `HBB` es un gen codificante de la subunidad beta de la hemoglobina, localizado en 11p15.4.
- En GRCh38.p14, HBB ocupa `chr11:5225464-5227071` en la hebra negativa.
- La variante HbS canónica es `NM_000518.5:c.20A>T`, `p.Glu7Val`, `rs334`.
- En coordenadas genómicas GRCh38, esa sustitución corresponde a `chr11:5227002 T>A`.
- ClinVar Variation ID 15333 contiene clasificaciones patogénicas asociadas a enfermedad falciforme.
- El estudio de Moiani et al. (Nature Communications, 2024) deposita datos CAST-SEQ y otros datos bajo BioProject `PRJNA1117889`.
- La ejecución elegida `SRR29275383` corresponde a la biblioteca `SCD10-Mock-2`, usada como muestra HbS mock en un ejercicio independiente reproducible sobre HBB.

## Qué se espera observar, pero debe confirmarse en Galaxy

### QC inicial

Es razonable esperar señal de adaptadores y degradación de calidad en extremos de lecturas. No se deben inventar Q20/Q30, número de lecturas, GC o longitud: copiar únicamente los valores reales de FastQC/MultiQC.

### Limpieza

Tras fastp debería reducirse el contenido de adaptadores y mejorar el perfil en los extremos. La limpieza no se considera correcta solo porque el job termine: hay que mostrar la comparación FastQC/MultiQC antes/después.

### Alineamiento

Como el ensayo está dirigido a HBB, se espera cobertura densa del locus. Registrar el porcentaje alineado, pares correctamente alineados y cobertura real. No usar métricas de tutoriales como resultado propio.

### VCF

Se espera que la ejecución sea informativa en el sitio de HbS. Comprobar si el VCF real contiene `chr11:5227002 T>A` y registrar `GT`, `DP`, `AD`, `AF` y `QUAL` solo si el caller los proporciona.

### VEP

Si se llama `rs334`, VEP debería identificar una consecuencia missense en HBB y permitir relacionarla con `p.Glu7Val` y evidencia clínica. Los predictores computacionales no sustituyen la evidencia clínica consolidada.

## Nota sobre GRCh37

En GRCh37 la misma variante se sitúa en `11:5248232 T>A`. No mezclar ambas coordenadas dentro del mismo flujo. Si se usa GRCh38 en Galaxy, todo el informe principal debe mantenerse en GRCh38.
