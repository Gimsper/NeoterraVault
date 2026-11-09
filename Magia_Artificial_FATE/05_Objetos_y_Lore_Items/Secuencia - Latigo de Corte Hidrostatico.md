---
title: "Secuencia - Látigo de Corte Hidrostático"
type: objeto
categoria: magia/secuencia
rango: "B"
afinidad: "Agua"
control_requerido: 2
tags:
  - magia/secuencia
  - rango/b
  - afinidad/agua
  - combate/filo_hidraulico
  - objeto
  - fate/proeza
aliases:
  - Látigo Hidrostático
  - Chorro de Corte Industrial
  - Látigo de Agua a Presión
  - Secuencia Látigo de Corte Hidrostático
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 💧 Secuencia: Látigo de Corte Hidrostático (Rango B)

> *"Treinta bares de agua en Rango C empujan a un hombre al suelo. Trescientos bares concentrados en un filamento líquido laminar de ocho metros oscilando a velocidad transónica cortan columnas de cemento, cables de ascensor y blindajes de titanio como si fueran alambre de cobre."*
> — Manual de Demolición Hidráulica de Choque, Ingenieros de Dragado

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Látigo de Corte Hidrostático (Rango B)
CLASIFICACIÓN: S.C.M.E.H. de Hidrocorte Ultra-Presurizado y Tensión Coherente
================================================================
Afinidad:    Agua
Requisito:   [✨] Control (2)
Recarga:     Usos Infinitos (cooldown de 1 asalto para presurización)
Complejidad: O(n) (control de tensión superficial y coherencia en curva)
Flujo:       32.0 kR/s

Acción:
Presuriza 40 L de fluido a 300 bar formando un filamento acuoso flexible 
de 8 m con velocidad de impacto supersónica, capaz de cortar blindajes 
de acero laminado de 15 mm y seccionar extremidades mecánicas a distancia.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

El **Látigo de Corte Hidrostático** traslada los principios del hidrocorte abrasivo industrial a una secuencia de combate táctico adaptable. Permite desarmar oponentes, derribar mamparos estructurales y amputar componentes mecánicos a media distancia con precisión quirúrgica.

### Dinámica de Tensión y Coherencia en Curva en $\mathcal{O}(n)$
Un chorro de agua a 300 bares tiende a fragmentarse violentamente en aerosol al curvarse. El algoritmo resuelve la hidrodinámica mediante cálculo iterativo por segmento:

1. **Hiperpresurización Hidrostática (`HydroDynamics.pressurize`):** Comprime la masa fluida hasta 300 bar en el acumulador piezoeléctrico del catalizador.
2. **Tensión Superficial Elástica Extrema (`HydroDynamics.set_surface_tension`):** Multiplica la cohesión molecular del agua, confiriéndole la elasticidad tensil de una cuerda de polímero sin perder su naturaleza líquida.
3. **Mantenimiento Laminar en Curvatura $\mathcal{O}(n)$ (`HydroFlow.set_flow_coherence`):** A medida que el operador azota el filamento, el algoritmo recalcula la tensión en cada uno de sus 8 metros, asegurando que el borde de impacto mantenga una sección de corte de apenas 1.5 milímetros. Al hacer contacto, el chorro cizalla el material por erosión hidrodinámica concentrada a más de $800	ext{ m/s}$.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Water.Gathering AS HydroGather;
IMPORT RuneScript.Elements.Water.FluidDynamics AS HydroDynamics;
IMPORT RuneScript.Elements.Water.FlowRegime AS HydroFlow;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE LatigoCorte(FluidSource: Object, TargetPoint: Point) {
    HEADER {
        Rank: "B";
        Affinity: "Water";
        Control_Threshold: 2;
        Recycle: "Infinite";
        Complexity: "O(n)";
        Throughput: "32.0 kR/s";
    }

    PARAMETERS {
        Pressure_Bar: 300.0;
        Whip_Length_M: 8.0;
        Cutting_Kerf_Mm: 1.5;
        Fluid_Volume_L: 40.0;
    }

    EXECUTE {
        FluidCore = HydroGather.extract_ambient_moisture(
            origin=FluidSource,
            volume_liters=Fluid_Volume_L
        );

        HydroDynamics.pressurize(
            fluid=FluidCore,
            bar_pressure=Pressure_Bar
        );

        HydroDynamics.set_surface_tension(
            fluid=FluidCore,
            tension_coefficient=85.0
        );

        FOR EACH Segment IN FluidCore.LengthSegments(Whip_Length_M) {
            HydroFlow.set_flow_coherence(
                fluid=Segment,
                regime=LAMINAR_COHERENT
            );
        }

        KineticVector.apply_impulse(
            target=FluidCore,
            vector=Operator.PointingVector,
            force_newtons=1800.0
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=FluidSource);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Látigo de Corte Hidrostático [Rango B]*
* **Requisito de Activación:** Tener `[✨] Control` a **Regular (+2)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto de Rango B]].
* **Acciones Permitidas:**
  1. **Atacar (con `[✨] Control`):** Atacar a objetivos a distancia (hasta 1 zona) infligiendo un daño de **Arma: 3**, ignorando armaduras blandas y reduciendo a la mitad blindajes medianos.
  2. **Crear una Ventaja (con `[✨] Control`):** Desarmar a un enemigo a distancia, seccionar un arma pesada o derribar una columna estructural, colocando el aspecto **`[Desarmado / Soporte Seccionado]`** con 2 invocaciones gratuitas.
* **Bonificador por Afinidad Elemental (Agua):**
  * Si el Especialista tiene afinidad con **Agua**, puede barrer a múltiples enemigos situados en la misma zona dividiendo los éxitos del ataque entre los objetivos sin penalizador por ataque múltiple.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango B]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Secuencia - Chorro Hidrostatico de Supresion]]
* [[Calculo de Rangos SCMEH - Big-O y Flujo]]
* [[Reglas FATE - Sistema de Magia Artificial]]
