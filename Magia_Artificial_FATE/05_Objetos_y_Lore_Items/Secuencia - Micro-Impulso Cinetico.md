---
title: "Secuencia - Micro-Impulso Cinético"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Aire"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/aire
  - movilidad/esquiva
  - objeto
  - fate/proeza
aliases:
  - Micro-Impulso
  - Impulso Rúnico
  - Desplazamiento Vectorial
  - Secuencia Micro-Impulso Cinético
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 💨 Secuencia: Micro-Impulso Cinético (Rango C)

> *"No te teletransportas, solo engañas a la inercia por un tercio de segundo. Un latigazo neumático en tu centro de gravedad te catapulta cuatro metros a la izquierda en una décima de segundo. El tirador enemigo jura que te desvaneciste en el aire, pero solo fuiste más rápido que la respuesta de su dedo en el gatillo."*
> — Tácticas de Evasión Reactiva, Vanguardia Ligera de Kitsune

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Micro-Impulso Cinético (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Asistencia Neumática Vectorial y Evasión
================================================================
Afinidad:    Aire
Requisito:   [✨] Control (1)
Recarga:     1 Turno de por medio (Enfriamiento de 1 Asalto entre usos)
Complejidad: O(1)
Flujo:       6.0 kR/s

Acción:
Genera un chorro de empuje reactivo ultracorto en la espalda o cadera 
del operador, desplazándolo instantáneamente 4 metros en un vector 
elegido sin alterar su postura ni provocar pérdida de equilibrio.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

El **Micro-Impulso Cinético** es un algoritmo de supervivencia esencial para operadores ligeros, mensajeros de asalto y exploradores. Transforma la masa gaseosa ambiental en un cohete neumático instantáneo acoplado a la biomecánica del usuario.

### Vectorización de Empuje Neumático Centrado
El algoritmo calcula las variables físicas de la aceleración para no dislocar la columna ni quebrar los tobillos del operador:

1. **Lectura de Centro de Gravedad (`KineticVector.read_center_of_mass`):** Detecta la masa corporal del operador e identifica el centro barimétrico entre la pelvis y la espina lumbar.
2. **Desbalance de Presión Asimétrico (`AeroPressure.set_differential`):** Genera una sobrepresión súbita de 4 atmósferas en una cáscara hemisférica de aire comprimido a 10 centímetros detrás del operador, mientras induce una depresión técnica relativa en la dirección de avance.
3. **Amortiguación de Frenado Aerodinámico (`AeroDrag.set_drag_coefficient`):** Durante los últimos 50 centímetros del desplazamiento de 4 metros, modula el coeficiente de arrastre del aire circundante para frenar suavemente la inercia, permitiendo que los pies aterricen en tracción perfecta listos para disparar o correr.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Air.Pressure AS AeroPressure;
IMPORT RuneScript.Elements.Air.Drag AS AeroDrag;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE MicroImpulsoCinetico(OperatorEntity: Entity, TargetVector: Vector3) {
    HEADER {
        Rank: "C";
        Affinity: "Air";
        Control_Threshold: 1;
        Recycle: "Cooldown_1_Round";
        Complexity: "O(1)";
        Throughput: "6.0 kR/s";
    }

    PARAMETERS {
        Thrust_Distance_M: 4.0;
        Burst_Duration_Sec: 0.12;
        Overpressure_Delta_Bar: 4.0;
        Deceleration_Window_M: 0.5;
    }

    EXECUTE {
        AeroPressure.set_differential(
            surface_high=OperatorEntity.RearCenter,
            surface_low=OperatorEntity.FrontCenter,
            delta_bar=Overpressure_Delta_Bar
        );

        KineticVector.apply_linear_acceleration(
            target=OperatorEntity,
            vector=TargetVector,
            distance_m=Thrust_Distance_M
        );

        AeroDrag.set_drag_coefficient(
            target=OperatorEntity,
            drag_factor=2.5
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=OperatorEntity.RearCenter);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Micro-Impulso Cinético [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Tiempo de Recarga / Enfriamiento de Mesa:**
  * **1 Turno de por medio:** Exige un asalto de enfriamiento biomecánico e inercial entre activaciones. No puede ejecutarse en dos turnos consecutivos por el mismo operador.
* **Acciones Permitidas:**
  1. **Superar Obstáculos (con `[✨] Control`):** Moverse 1 zona de inmediato como acción complementaria gratuita dentro de tu turno, sorteando pozos, trampas de presión o líneas de fuego enemigo.
  2. **Defender (con `[✨] Control`):** Otorga un bonificador de **+2 a la defensa** al esquivar ataques de área (explosiones, derrumbes) o disparos a distancia mediante un salto angular reactivo.
* **Bonificador por Afinidad Elemental (Aire):**
  * Si el Especialista posee afinidad con **Aire**, el desplazamiento se extiende a **6 metros** y puede ejecutarse verticalmente para alcanzar cornisas o techos bajos.
* **Margen de Fallo:**
  * Si se falla con un margen de -3, la fuerza vectorial no frena a tiempo, impactando contra un obstáculo rígido o tropezando aparatosamente y sufriendo el aspecto `[Aturdido por Caída]`.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Secuencia - Pulso Neumatico de Rechazo]]
* [[Artefacto - Little Fox]]
* [[Reglas FATE - Sistema de Magia Artificial]]
