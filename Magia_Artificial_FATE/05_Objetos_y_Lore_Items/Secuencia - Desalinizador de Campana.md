---
title: "Secuencia - Desalinizador de Campaña"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Agua"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/agua
  - supervivencia/utilidad
  - objeto
  - fate/proeza
aliases:
  - Desalinizador de Campaña
  - Purificador Rúnico de Agua
  - Secuencia Desalinizador
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 💧 Secuencia: Desalinizador de Campaña (Rango C)

> *"En las marismas venenosas del Reino Olvidado no te mata el enemigo, te mata beber de sus charcos de azufre y salmuera. Diez segundos con este código en tu cantimplora y el agua se vuelve pura como el deshielo de un glaciar."*
> — Guía de Supervivencia de los Exploradores de Vanguardia

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Desalinizador de Campaña (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Precipitación de Solutos y Purificación
================================================================
Afinidad:    Agua
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       3.2 kR/s

Acción:
Altera la constante dieléctrica del agua en un contenedor (hasta 5 L), 
forzando la desolvatación y precipitación instantánea de sales, 
metales pesados y toxinas en un sedimento inerte decantado al fondo.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

El **Desalinizador de Campaña** es un software utilitario indispensable para patrullas de largo alcance, exploradores mineros y destacamentos fronterizos. Permite prescindir de filtros mecánicos pesados o pastillas de cloro en zonas con fuentes de agua salobre, fangosa o contaminada químicamente.

### Principios de Precipitación de Solutos y Estabilidad Hidrostática
El algoritmo actúa sobre las moléculas de agua líquida confinadas en un recipiente:

1. **Alteración del Potencial Dieléctrico (`HydroSolutes.precipitate_solutes`):** Modula temporalmente los dipolos de las moléculas de agua, reduciendo su capacidad de solvatación iónica. Los iones de sodio, cloruro, sulfatos y metales pesados disueltos no pueden mantenerse en solución y se aglomeran en microcristales densos que decantan rápidamente hacia la base del recipiente.
2. **Separación de Fase Coloidal (`HydroDynamics.set_viscosity`):** Reduce la viscosidad del líquido para acelerar la sedimentación de partículas en suspensión en menos de 10 segundos, dejando el 95% del volumen como agua potable estéril apta para el consumo humano.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Water.Solutes AS HydroSolutes;
IMPORT RuneScript.Elements.Water.FluidDynamics AS HydroDynamics;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE DesalinizadorCampana(WaterContainer: Object) {
    HEADER {
        Rank: "C";
        Affinity: "Water";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "3.2 kR/s";
    }

    PARAMETERS {
        Max_Volume_Liters: 5.0;
        Purification_Cycle_Sec: 10.0;
        Sediment_Decant_Rate: 0.95;
    }

    EXECUTE {
        HydroSolutes.precipitate_solutes(
            fluid=WaterContainer.LiquidCore
        );

        HydroDynamics.set_viscosity(
            fluid=WaterContainer.LiquidCore,
            cP_viscosity=1.0
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=WaterContainer.LiquidCore);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Desalinizador de Campaña [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Superar Obstáculos (con `[✨] Control`):** Purificar fuentes de agua corrompidas, estancadas o salobres en expediciones remotas, anulando complicaciones de escena derivadas de la deshidratación o el envenenamiento ambiental.
  2. **Crear una Ventaja (con `[✨] Control`):** Colocar el aspecto de escena **`[Reserva de Agua Dulce Estéril]`** con 1 invocación gratuita para el grupo.
* **Bonificador por Afinidad Elemental (Agua):**
  * Si el Especialista tiene afinidad con **Agua**, el volumen purificado por ciclo se eleva a **15 litros** y el proceso se completa en 3 segundos.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
