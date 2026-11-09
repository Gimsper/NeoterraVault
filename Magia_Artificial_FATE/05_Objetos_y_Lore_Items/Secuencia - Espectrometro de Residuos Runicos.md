---
title: "Secuencia - Espectrómetro de Residuos Rúnicos"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Tierra"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/tierra
  - investigacion/rastreo
  - objeto
  - fate/proeza
aliases:
  - Espectrómetro Rúnico
  - Rastreo Residual
  - Escaneo de Huella Mágica
  - Secuencia Espectrómetro de Residuos Rúnicos
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# ⛰️ Secuencia: Espectrómetro de Residuos Rúnicos (Rango C)

> *"La magia artificial no es un fantasma invisible; es un flujo brutal de kilo-runas que recalienta y polariza los átomos de sílice y hierro del suelo. Un Especialista que haya conjurado aquí hace tres horas deja una firma litológica tan clara como una huella de bota en el lodo fresco."*
> — Inspector de Delitos Arcanos, Null-Sector

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Espectrómetro de Residuos Rúnicos (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Detección de Polarización Litológica Residual
================================================================
Afinidad:    Tierra
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       3.0 kR/s

Acción:
Sondea la polarización magnética y piezoeléctrica remanente en el suelo 
de roca, asfalto o mampostería, revelando la firma elemental y dirección 
de escape de cualquier usuario de magia que haya operado hace 6 horas.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

El **Espectrómetro de Residuos Rúnicos** es el software forense y de persecución utilizado por fuerzas de seguridad y rastreadores de frontera para seguir la pista a Especialistas o unidades de combate mágicas.

### Principios de Histéresis Rúnica en Sustratos Minerales
1. **Polarización Remanente (`GeoFerrous.polarize_mineral_domain`):** Toda descarga bio-mágica induce una histéresis electrostática en las inclusiones ferrosas y prismas de cuarzo del suelo.
2. **Espectrometría de Frecuencia Pasiva:** Al rozar el suelo con el catalizador, el sensor mide el decaimiento de esta carga latente. Permite determinar la **afinidad elemental** del conjuro ejecutado (fuego deja huellas de deshidratación térmica, rayo deja caminos de ionización ferrosa, etc.) y la dirección vectorial del escape según el desvanecimiento progresivo de la señal en un radio de 20 metros.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Earth.Ferrous AS GeoFerrous;
IMPORT RuneScript.Elements.Earth.Piezoelectric AS GeoPiezo;
IMPORT RuneScript.Sensory.Haptics AS SensoryHaptics;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE EspectrometroRunico(GroundSample: Point) {
    HEADER {
        Rank: "C";
        Affinity: "Earth";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "3.0 kR/s";
    }

    PARAMETERS {
        Scan_Depth_Cm: 5.0;
        Memory_Window_Hours: 6.0;
        Decay_Threshold_Tesla: 0.005;
    }

    EXECUTE {
        DomainMatrix = GeoFerrous.polarize_mineral_domain(
            target_area=GroundSample.BoundingArea(1.0.m),
            field_tesla=Decay_Threshold_Tesla
        );

        SensoryHaptics.project_haptic_pulse(
            target_contact_point=Operator.PalmSkin,
            pattern_id="RESIDUAL_TRACE_BEARING",
            intensity_mw=12.0
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=GroundSample);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Espectrómetro de Residuos Rúnicos [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Superar Obstáculos (con `[✨] Control`):** Rastrear a un individuo o criatura que haya canalizado magia o porte un artefacto activo a través de calles, túneles o ruinas minerales en sustitución de la habilidad de *Investigar*.
  2. **Crear una Ventaja (con `[✨] Control`):** Colocar el aspecto **`[Firma Elemental del Fugitivo Identificada]`** con 1 invocación gratuita, descubriendo qué tipo de magia utiliza antes de entrar en combate.
* **Bonificador por Afinidad Elemental (Tierra):**
  * Si el Especialista tiene afinidad con **Tierra**, la ventana temporal se amplía a **12 horas** y revela la masa aproximada del objetivo.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
