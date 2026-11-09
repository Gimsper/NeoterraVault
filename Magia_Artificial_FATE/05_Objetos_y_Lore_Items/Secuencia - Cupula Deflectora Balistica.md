---
title: "Secuencia - Cúpula Deflectora Balística"
type: objeto
categoria: magia/secuencia
rango: "B"
afinidad: "Neutro"
control_requerido: 2
tags:
  - magia/secuencia
  - rango/b
  - afinidad/neutro
  - defensa/cupula
  - objeto
  - fate/proeza
aliases:
  - Cúpula Deflectora
  - Domo Balístico
  - Escudo Semiesférico Rúnico
  - Secuencia Cúpula Deflectora Balística
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 🛡️ Secuencia: Cúpula Deflectora Balística (Rango B)

> *"Un broquel de sesenta centímetros en Rango C te salva de un disparo certero en el pecho si ves venir la bala. Esta cúpula de Rango B sella un hemisferio de dos metros y medio a tu alrededor: detiene ráfagas completas de ametralladora pesada de calibre cincuenta y metralla de mortero desde cualquier dirección sin pestañear."*
> — Capitán Elena Ruiz, Escudo de la Federación

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Cúpula Deflectora Balística (Rango B)
CLASIFICACIÓN: S.C.M.E.H. de Confinamiento Esférico y Deflexión Tensil Continua
================================================================
Afinidad:    Neutro (o Aire)
Requisito:   [✨] Control (2)
Recarga:     1 Asalto (enfriamiento de bobinas de descarga)
Complejidad: O(n) (distribución de vectores de impacto balístico múltiple)
Flujo:       48.0 kR/s

Acción:
Proyecta un domo hemisférico translúcido de 2.5 m de radio en 360°, 
capaz de repeler ráfagas de ametralladora pesada, esquirlas de explosión 
y ataques mágicos directos mediante deflexión inercial distribuida.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

La **Cúpula Deflectora Balística** es el estándar de defensa perimétrica para escuadras de asalto y posiciones defensivas expuestas a fuego cruzado. Distribuye la energía cinética de impactos balísticos a lo largo de toda la superficie esférica para disiparla hacia el suelo.

### Distribución Inercial Esférica en $\mathcal{O}(n)$
A diferencia de los deflectores planos de Rango C, la cúpula gestiona múltiples impactos simultáneos:

1. **Envoltura Hemisférica Rígida (`Confinement.bind_sphere`):** Modula una cáscara de fuerza translúcida de 2.5 metros de radio anclada en el suelo circular alrededor del artefacto.
2. **Deflexión Tensil Vectorial en $\mathcal{O}(n)$ (`KineticVector.lock_trajectory`):** Ante cada proyectil balístico incidente, el algoritmo altera localmente la tensión de la malla esférica, curvando el ángulo de incidencia para que las balas reboten tangencialmente hacia arriba o hacia los lados sin transmitir energía al centro.
3. **Descarga a Tierra:** Las sobretensiones mecánicas se conducen hacia el anillo base en contacto con el suelo, impidiendo la saturación de los condensadores internos del artefacto.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Geometry.Confinement AS Confinement;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Elements.Air.Pressure AS AeroPressure;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE CupulaDeflectora(CenterGroundPoint: Point) {
    HEADER {
        Rank: "B";
        Affinity: "Neutral";
        Control_Threshold: 2;
        Recycle: "Per_Round";
        Complexity: "O(n)";
        Throughput: "48.0 kR/s";
    }

    PARAMETERS {
        Radius_M: 2.5;
        Wall_Thickness_Mm: 12.0;
        Max_Kinetic_Tolerated_J: 45000.0;
        Duration_Rounds: 1;
    }

    EXECUTE {
        DomeField = Confinement.bind_sphere(
            energy_core=CenterGroundPoint,
            radius_m=Radius_M
        );

        AeroPressure.set_differential(
            surface_high=DomeField.OuterSurface,
            surface_low=DomeField.InnerSurface,
            delta_bar=1.8
        );

        FOR EACH Threat IN RadarSensor.IncomingProjectiles {
            KineticVector.lock_trajectory(
                target=DomeField.InterceptNode(Threat),
                vector=Threat.TrajectoryVector.tangent(),
                max_deviation_deg=45.0
            );
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=CenterGroundPoint);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Cúpula Deflectora Balística [Rango B]*
* **Requisito de Activación:** Tener `[✨] Control` a **Regular (+2)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto de Rango B]].
* **Acciones Permitidas:**
  1. **Defender (con `[✨] Control`):** Otorga un bonificador de **+3 a la Defensa** contra todos los ataques a distancia (armas de fuego, metralla, ráfagas continuas) dirigidos contra el operador o cualquier aliado dentro de su misma zona.
* **Medidor de Resistencia de la Cúpula:**
  * Posee **4 casillas de estrés defensivo**. Puede absorber daño resultante de tiradas de ataque exitosas de los rivales antes de que el estrés alcance a los defensores. Si se agotan sus casillas, la cúpula se quiebra en un destello de luz neutra.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango B]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Secuencia - Pantalla Deflectora de Punto]]
* [[Calculo de Rangos SCMEH - Big-O y Flujo]]
* [[Reglas FATE - Sistema de Magia Artificial]]
