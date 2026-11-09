---
title: "Secuencia - Pantalla Deflectora de Punto"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Neutro"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/neutro
  - defensa/escudo
  - objeto
  - fate/proeza
aliases:
  - Pantalla Deflectora
  - Escudo de Punto
  - Deflector Frontal
  - Secuencia Pantalla Deflectora de Punto
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 🛡️ Secuencia: Pantalla Deflectora de Punto (Rango C)

> *"No intentes sostener una cúpula de energía de trescientos sesenta grados si no llevas una batería militar de diez mil kilo-runas. Para no morir, solo necesitas interponer un disco de sesenta centímetros en el ángulo exacto donde viene el proyectil."*
> — Manual de Combate Defensivo, Aegis Dynamics

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Pantalla Deflectora de Punto (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Confinamiento Geométrico y Dispersión Cinética
================================================================
Afinidad:    Neutro (o Aire)
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       7.0 kR/s

Acción:
Proyecta un disco plano hexagonal de 60 cm de diámetro frente a la mano 
del operador durante 0.5 segundos, desviando angularmente un único 
impacto balístico, esquirla o golpe físico directo sin absorción térmica.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

La **Pantalla Deflectora de Punto** es el método defensivo básico de duelistas y tropas ligeras de Aegis. A diferencia de las cúpulas pesadas que absorben toneladas de daño estático, esta secuencia actúa como un broquel balístico invisible que desvía la energía cinética mediante deflexión angular.

### Principios de Deflexión Rúnica Angular
1. **Confinamiento de Pantalla Plana (`Confinement.bind_sheet`):** Proyecta una lámina rígida hexagonal de 60 cm de diámetro y 5 mm de grosor a 30 cm de la palma del usuario.
2. **Desviación de Vector Inercial:** No intenta frenar un proyectil de frente a cero (lo que sobrecargaría el bus térmico de un artefacto de Rango C). El campo está angulado a 30° respecto a la línea de fuego incidente: los proyectiles de plomo o esquirlas resbalan contra la superficie rúnica y rebotan hacia los lados con pérdida mínima de energía en el catalizador.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Geometry.Confinement AS Confinement;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE PantallaDeflectora(OriginHand: Point) {
    HEADER {
        Rank: "C";
        Affinity: "Neutral";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "7.0 kR/s";
    }

    PARAMETERS {
        Diameter_M: 0.60;
        Deflection_Angle_Deg: 30.0;
        Active_Window_Sec: 0.5;
    }

    EXECUTE {
        Shield = Confinement.bind_sheet(
            target_core=OriginHand,
            width_m=Diameter_M,
            height_m=Diameter_M,
            thickness_mm=5.0
        );

        KineticVector.lock_trajectory(
            target=Shield,
            vector=Operator.PointingVector,
            max_deviation_deg=Deflection_Angle_Deg
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=OriginHand);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Pantalla Deflectora de Punto [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Defender (con `[✨] Control`):** Otorga un bonificador de **+2 a la defensa** contra un ataque físico directo (un disparo singular, un hachazo o un proyectil mágico de Rango C) por intercambio.
* **Margen de Fallo:**
  * Si se falla con margen de -3 o más, el ángulo de deflexión colapsa y el impacto rebota directamente contra el antebrazo del operador, infligiendo 1 casilla de estrés físico.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Corporaciones y Fabricantes de Neoterra]]
* [[Reglas FATE - Sistema de Magia Artificial]]
