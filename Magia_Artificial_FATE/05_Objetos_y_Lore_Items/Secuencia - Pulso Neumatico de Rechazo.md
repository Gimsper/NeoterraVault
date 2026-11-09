---
title: "Secuencia - Pulso Neumático de Rechazo"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Aire"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/aire
  - combate/cinetica
  - objeto
  - fate/proeza
aliases:
  - Pulso Neumático
  - Pulso de Rechazo
  - Puño Aéreo Rúnico
  - Secuencia Pulso Neumático de Rechazo
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 🌪️ Secuencia: Pulso Neumático de Rechazo (Rango C)

> *"No todos los ataques necesitan matar. Cuando un atacante cuerpo a cuerpo te acorrala contra una pared, una onda de choque neumática de ciento cincuenta newtons en el pecho lo proyecta dos metros atrás y te compra el tiempo necesario para desenfundar."*
> — Tácticas de Disuasión y Rechazo, Fuerzas de Seguridad de Aegis

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Pulso Neumático de Rechazo (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Sobrepresión Cónica y Repulsión Inmediata
================================================================
Afinidad:    Aire
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       5.0 kR/s

Acción:
Comprime súbitamente el aire en la palma del artefacto y lo libera 
en un cono de sobrepresión frontal divergente (1.5 m de alcance), 
entregando 150 N de fuerza cinética que derriba o empuja al oponente.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

El **Pulso Neumático de Rechazo** es la defensa reactiva básica contra hostigadores cuerpo a cuerpo. A diferencia del [[Secuencia - Dardo Neumatico|Dardo Neumático]] (que es un proyectil toroidal de precisión a 15 metros), esta secuencia está diseñada para dispersión de impacto a corta distancia.

### Principios de Sobrepresión Convexa Rápida
1. **Compresión Gaseosa Perimétrica (`AeroDensity.compress_gas`):** Condensa 0.1 m³ de aire ambiente frente al chasis del artefacto en una décima de segundo.
2. **Expansión Cónica Divergente (`AeroDensity.expand_gas`):** Al activarse el gatillo, el gas se descomprime bruscamente en un ángulo de apertura de 45°. El frente de onda genera una sobrepresión mecánica concentrada de 150 N a menos de 1.5 metros, suficiente para empujar a un individuo hacia atrás, desequilibrar armas largas o abrir compuertas atascadas hacia afuera.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Air.Density AS AeroDensity;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Safety.Vent AS SafeVent;

SEQUENCE PulsoRechazo(TargetZone: Area) {
    HEADER {
        Rank: "C";
        Affinity: "Air";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "5.0 kR/s";
    }

    PARAMETERS {
        Cone_Angle_Deg: 45.0;
        Max_Reach_M: 1.5;
        Impact_Force_N: 150.0;
    }

    EXECUTE {
        GasVolume = AeroDensity.compress_gas(
            volume_m3=0.10,
            ratio=3.8
        );

        KineticVector.apply_impulse(
            target=GasVolume,
            vector=Operator.PointingVector,
            force_newtons=Impact_Force_N
        );

        AeroDensity.expand_gas(
            gas_pocket=GasVolume,
            expansion_rate=10.0
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeVent.shunt_heat_to_atmosphere(joules=120.0);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Pulso Neumático de Rechazo [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Crear una Ventaja (con `[✨] Control`):** Empujar a un adversario en combate cuerpo a cuerpo hacia una zona adyacente o colocarle el aspecto **`[Desequilibrado y Derribado]`** con 1 invocación gratuita.
  2. **Defender (con `[✨] Control`):** Otorga un bonificador de **+2 a la defensa** contra ataques cuerpo a cuerpo con armas contundentes o de filo interponiendo la onda neumática.
  3. **Superar Obstáculos:** Forzar la apertura de puertas trabadas, ventanas tapiadas o apartar escombros ligeros del camino.
* **Bonificador por Afinidad Elemental (Aire):**
  * Si el Especialista tiene afinidad con **Aire**, la fuerza del impacto se eleva a **220 N**, pudiendo golpear a dos oponentes adyacentes en el mismo cono.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Secuencia - Dardo Neumatico]]
* [[Artefacto - Little Fox]]
* [[Reglas FATE - Sistema de Magia Artificial]]
