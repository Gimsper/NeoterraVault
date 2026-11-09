---
title: "Secuencia - Cresta Litológica de Parapeto"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Tierra"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/tierra
  - defensa/cobertura
  - objeto
  - fate/proeza
aliases:
  - Cresta Litológica
  - Parapeto Rúnico
  - Muro Bajo de Cobertura
  - Secuencia Cresta Litológica de Parapeto
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# ⛰️ Secuencia: Cresta Litológica de Parapeto (Rango C)

> *"Cuando te emboscan en una calle abierta sin coberturas naturales, un segundo de vacilación te cuesta la vida. Clavas la rodilla, activas el pulso de cizallamiento y una barrera de granito de tres cuartos de metro emerge del asfalto antes de que los proyectiles enemigos alcancen tu pecho."*
> — Manual de Supervivencia Urbana, Legión de Acero

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Cresta Litológica de Parapeto (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Elevación Litológica y Compactación Rápida
================================================================
Afinidad:    Tierra
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos (requiere sustrato mineral en el suelo)
Complejidad: O(1)
Flujo:       6.8 kR/s

Acción:
Aplica cizallamiento y elevación mecánica sobre el suelo mineral, 
alzando un parapeto de roca y asfalto de 75 cm de alto, 1.2 m de ancho 
y 20 cm de grosor (~250 kg) en 0.4 segundos para cobertura táctica.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

La **Cresta Litológica de Parapeto** es la solución inmediata de fortificación improvisada para tiradores, zapadores y unidades de contención sorprendidas en campo abierto. A diferencia de las murallas megalíticas de Rango B, este algoritmo no crea masa de la nada: reorganiza el suelo existente bajo los pies del usuario.

### Cizallamiento Litológico y Sinterización de Balasto
La formación del parapeto se ejecuta en tres pasos mecánicos inmediatos:

1. **Corte y Fractura de Estratos (`GeoLattice.cleave_fault`):** Introduce una vibración de corte en una línea transversal de 1.2 metros en el pavimento o roca viva a un metro frente al operador, delimitando un bloque trapezoidal de 20 centímetros de espesor.
2. **Elevación Vectorial Hidroneumática (`KineticVector.apply_linear_acceleration`):** Desplaza verticalmente el bloque de 250 kg hacia arriba a una altura de 75 centímetros (altura óptima de parapeto para disparar cuerpo a tierra o arrodillado).
3. **Compactación Granular Instantánea (`GeoGranular.recompact_soil` & `GeoLattice.densify_mineral`):** Compacta las microfisuras de la piedra alzada aumentando su densidad atómica para absorber metralla y balística pesada sin desgranarse en escombros ante el primer impacto.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Earth.Lattice AS GeoLattice;
IMPORT RuneScript.Elements.Earth.Granular AS GeoGranular;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE CrestaLitologica(GroundContactPoint: Point) {
    HEADER {
        Rank: "C";
        Affinity: "Earth";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "6.8 kR/s";
    }

    PARAMETERS {
        Height_M: 0.75;
        Width_M: 1.20;
        Thickness_M: 0.20;
        Lift_Time_Sec: 0.40;
    }

    EXECUTE {
        FaultLine = GeoLattice.cleave_fault(
            plane_vector=Vector3(1, 0, 0),
            stress_joules=12000.0
        );

        KineticVector.apply_linear_acceleration(
            target=FaultLine,
            vector=Vector3(0, 1, 0),
            distance_m=Height_M
        );

        GeoGranular.recompact_soil(
            ground_area=FaultLine
        );

        GeoLattice.densify_mineral(
            stone_target=FaultLine,
            density_ratio=1.5
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=GroundContactPoint);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Cresta Litológica de Parapeto [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Crear una Ventaja (con `[✨] Control`):** Colocar el aspecto de escena **`[Parapeto Litológico Improvisado]`** con 1 invocación gratuita en la zona del operador.
  2. **Defender (con `[✨] Control`):** Otorga un bonificador de **+2 a la defensa** contra ataques balísticos o proyectiles a distancia mientras el personaje permanezca agachado tras la cobertura.
* **Capacidad de Absorción de Daño:**
  * El parapeto posee **2 casillas de estrés** estructural. Puede absorber daño en lugar del operador si éste falla una defensa contra proyectiles. Al llenarse sus casillas de estrés, el parapeto se fragmenta en grava inerte.
* **Bonificador por Afinidad Elemental (Tierra):**
  * Si el Especialista tiene afinidad con **Tierra**, la resistencia estructural del parapeto aumenta a **4 casillas de estrés**.
* **Condición de Terreno:**
  * Requiere sustrato mineral (roca, asfalto, ladrillo, tierra compacta). Falla sobre madera pura, metal liso o agua.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Secuencia - Traccion Litologica Ultra-Grip]]
* [[Artefacto - Little Fox]]
* [[Reglas FATE - Sistema de Magia Artificial]]
