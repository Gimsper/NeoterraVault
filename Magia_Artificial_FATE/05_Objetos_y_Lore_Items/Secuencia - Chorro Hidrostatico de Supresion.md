---
title: "Secuencia - Chorro Hidrostático de Supresión"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Agua"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/agua
  - combate/control_masas
  - objeto
  - fate/proeza
aliases:
  - Chorro Hidrostático
  - Splash Rúnico
  - Torrente de Supresión
  - Secuencia Chorro Hidrostático de Supresión
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 💧 Secuencia: Chorro Hidrostático de Supresión (Rango C)

> *"Treinta bares de agua a diez metros de distancia no parecen gran cosa hasta que impactan contra tu plexo solar. El sospechoso sale volando cuatro metros hacia atrás, sin fracturas óseas ni heridas sangrantes, pero completamente sin aire en los pulmones y desarmado."*
> — Manual de Contención Antidisturbios, Policía de Aegis

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Chorro Hidrostático de Supresión (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Propulsión Hidrostática y Control de Masas
================================================================
Afinidad:    Agua
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos (cooldown de 1 asalto si condensa del aire)
Complejidad: O(1)
Flujo:       5.5 kR/s

Acción:
Presuriza 15 litros de masa fluida a 30 bar y la proyecta en un chorro 
laminar coherente a 5 metros, derribando o desplazando a un objetivo 
humanoide con 600 N de empuje cinético no penetrante.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

El **Chorro Hidrostático de Supresión** es el algoritmo estándar de control de multitudes y neutralización incruenta utilizado por fuerzas del orden y especialistas tácticos. Su propósito es repeler agresores en aproximación rápida sin producir traumatismos letales ni perforación tisular.

### Dinámica de Flujo Confinado a 30 Bar
La secuencia divide su ciclo de trabajo en tres fases hidrodinámicas:

1. **Captación y Acumulación de Fluido (`HydroGather.extract_ambient_moisture`):** Capta instantáneamente 15 litros de agua líquida desde un reservorio táctico (cantimplora, mochila hidrostática) o condensa vapor ambiental mediante un gradiente higroscópico forzado en la tobera del artefacto.
2. **Presurización Volumétrica (`HydroDynamics.pressurize`):** Comprime la columna de fluido hasta 30 bares de sobrepresión dentro del acumulador piezoeléctrico de la tobera.
3. **Coherencia Laminar de Eyección (`HydroFlow.set_flow_coherence`):** Configura la tensión superficial del chorro en régimen laminar coherente, evitando que el agua se atomice en aerosol al abandonar la tobera. El chorro se mantiene cilíndrico hasta los 5 metros de alcance, entregando un impacto frontal contundente de 600 Newtons que derriba al blanco de espaldas.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Water.Gathering AS HydroGather;
IMPORT RuneScript.Elements.Water.FluidDynamics AS HydroDynamics;
IMPORT RuneScript.Elements.Water.FlowRegime AS HydroFlow;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE ChorroHidrostatico(WaterSource: Object, TargetEntity: Entity) {
    HEADER {
        Rank: "C";
        Affinity: "Water";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "5.5 kR/s";
    }

    PARAMETERS {
        Pressure_Bar: 30.0;
        Fluid_Volume_Liters: 15.0;
        Effective_Range_M: 5.0;
        Impact_Force_N: 600.0;
    }

    EXECUTE {
        Fluid = HydroGather.extract_ambient_moisture(
            origin=WaterSource,
            volume_liters=Fluid_Volume_Liters
        );

        HydroDynamics.pressurize(
            fluid=Fluid,
            bar_pressure=Pressure_Bar
        );

        HydroFlow.set_flow_coherence(
            fluid=Fluid,
            regime=LAMINAR_COHERENT
        );

        KineticVector.apply_impulse(
            target=Fluid,
            vector=Operator.PointingVector,
            force_newtons=Impact_Force_N
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=WaterSource);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Chorro Hidrostático de Supresión [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Atacar (con `[✨] Control`):** Realiza un ataque a distancia hasta 1 zona infligiendo estrés físico contundente no letal.
  2. **Crear una Ventaja (con `[✨] Control`):** Empujar violentamente al objetivo a una zona adyacente o derribarlo al suelo, colocando el aspecto situacional **`[Derribado y Empapado]`** con 1 invocación gratuita.
* **Bonificador por Afinidad Elemental (Agua):**
  * Si el Especialista posee afinidad con **Agua**, el efecto de derribo se aplica automáticamente sobre cualquier oponente cuyo Físico/Fuerza no sea el doble del `[✨] Control` del lanzador.
* **Margen de Fallo:**
  * Si se falla con un margen de -3, la tobera hidrostática sufre una sobrepresión inversa, arrojando agua a alta velocidad contra el rostro del propio operador y colocándole el aspecto `[Visión Cegada por Agua]`.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
