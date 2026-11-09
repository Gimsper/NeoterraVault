---
title: "Secuencia - Velo de Refracción Simple"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Neutro"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/neutro
  - sensorial/optica
  - objeto
  - fate/proeza
aliases:
  - Velo de Refracción
  - Camuflaje Facial Rúnico
  - Pixelado Óptico
  - Secuencia Velo de Refracción Simple
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 👁️ Secuencia: Velo de Refracción Simple (Rango C)

> *"El problema de los hechizos de invisibilidad baratos es que si desvías toda la luz alrededor de tu cabeza, ninguna luz entra en tus ojos y te quedas ciego. Este código curva los fotones sobre tu mandíbula, tu nariz y tus pómulos, pero mantiene dos canales rectos y limpios frente a tus pupilas: tú ves el mundo con total claridad mientras las cámaras de Aegis solo registran una mancha borrosa que sus algoritmos no pueden fichar."*
> — Diseñador de Software Subversivo, Kitsune Micro-Arcana

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Velo de Refracción Simple (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Guía de Onda Fotónica y Apertura Ocular
================================================================
Afinidad:    Neutro (Sensorial)
Requisito:   [✨] Control (1)
Recarga:     Por Escena
Complejidad: O(1)
Flujo:       7.5 kR/s

Acción:
Genera un gradiente de índice de refracción biconvexo en el aire a 
3 cm del rostro, desviando fotones de rasgos faciales para anular 
visión artificial, pero preservando un canal axial recto para las pupilas.
================================================================
```

---

## 2. Descripción Operativa y Óptica de Antivigilancia

El **Velo de Refracción Simple** fue desarrollado originalmente por desertores de la división de I+D de [[Corporaciones y Fabricantes de Neoterra|Kitsune Micro-Arcana]]. Es la contramedida por excelencia contra la omnipresente red de reconocimiento biométrico y cámaras de vigilancia urbana de la Federación.

### Principios de Refracción Biconvexa y Corredor Axial
La secuencia divide el volumen facial en dos zonas ópticas diferenciadas para difuminar los rasgos sin afectar la visión del usuario:
La secuencia soluciona la paradoja dividiendo el volumen facial en dos zonas ópticas diferenciadas:

1. **Guía de Onda Perimétrica Biconvexa (`SensoryOptics.refract_light`):** Modula una cáscara de aire ionizado de 3 centímetros de espesor sobre la frente, pómulos, nariz, orejas y mandíbula. Los fotones incidentes sufren un desfase angular de 14 milímetros, curvándose tangencialmente alrededor de la cabeza. Para cualquier cámara o testigo situado a más de 2 metros, los rasgos fisonómicos se difuminan como si estuvieran sumergidos bajo agua turbulenta.
2. **Canal Axial Recto de Pupila:** El algoritmo calcula en tiempo real el vector de mirada del operador (`Operator.PupilAxes`). Mantiene dos cilindros de aire de 8 mm de diámetro con índice de refracción neutro ($n = 1.000$) exactamente alineados con los ojos del usuario. La luz entra sin interferencia en sus retinas, permitiéndole apuntar, leer y desplazarse con visión 100% normal.
3. **Micro-Oscilación Anti-Algorítmica (30 Hz):** El velo oscila a 30 Hertz, la frecuencia exacta que interfiere con los algoritmos de detección de puntos de referencia faciales (como redes neuronales de 68 puntos biométricos). Las inteligencias artificiales de seguridad de Aegis registran un error de clasificación y descartan la captura.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python

IMPORT RuneScript.Sensory.Optics AS SensoryOptics;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE VeloRefraccion(FaceArea: Area) {
    HEADER {
        Rank: "C";
        Affinity: "Neutral";
        Control_Threshold: 1;
        Recycle: "Per_Scene";
        Complexity: "O(1)";
        Throughput: "7.5 kR/s";
    }

    PARAMETERS {
        Refraction_Shell_Depth_Cm: 3.0;
        Refraction_Offset_Mm: 14.0;
        Pupil_Aperture_Diameter_Mm: 8.0;
        Oscillation_Rate_Hz: 30.0;
        Duration_Sec: 120.0;
    }

    EXECUTE {
        SensoryOptics.refract_light(
            target=FaceArea
        );

        SensoryOptics.maintain_pupil_corridors(
            eye_axes=Operator.PupilAxes,
            aperture_diameter_mm=Pupil_Aperture_Diameter_Mm
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=FaceArea);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Velo de Refracción Simple [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Crear una Ventaja (con `[✨] Control`):** Colocar el aspecto situacional **`[Rostro Borroso e Inclasificable]`** con 1 invocación gratuita.
  2. **Defender:** Otorga un bonificador de **+2 a tiradas de Sigilo** para evitar ser identificado por cámaras de seguridad, drones de vigilancia o patrulleros en puestos de control aduanero.
* **Bono de Especialidad (Kitsune):**
  * Si se dispara desde un artefacto de la serie [[Artefacto - Little Fox|Kitsune]], el velo puede cubrir también las manos del operador para no dejar huellas dactilares ni marcas en escáneres táctiles.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Macro de Librerias SCMEH]]
* [[Artefacto - Little Fox]]
* [[Corporaciones y Fabricantes de Neoterra]]
* [[Reglas FATE - Sistema de Magia Artificial]]
