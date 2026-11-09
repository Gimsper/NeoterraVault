---
title: "Secuencia - Parche de Coagulación Hidrostática"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Agua"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/agua
  - medicina/soporte
  - objeto
  - fate/proeza
aliases:
  - Parche de Coagulación
  - Apósito Hidrostático
  - Coagulación Rúnica
  - Secuencia Parche de Coagulación
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 💧 Secuencia: Parche de Coagulación Hidrostática (Rango C)

> *"El agua pura te lava una herida, pero si la dejas suelta, se desliza y no frena la sangre. Tienes que regular el ángulo de contacto a cero grados para que moje los bordes, espesar los enlaces hasta imitar una red de fibrina y nivelar la tonicidad a nueve gramos por litro para que las células no revienten por ósmosis. Entonces tienes un apósito estéril indestructible."*
> — Paramédico Táctico Sean O'Malley, Cuerpo Médico de la Federación

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Parche de Coagulación Hidrostática (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Capilaridad, Tensión Viscoelástica e Isotonía
================================================================
Afinidad:    Agua
Requisito:   [✨] Control (1)
Recarga:     Por Escena
Complejidad: O(1)
Flujo:       3.8 kR/s

Acción:
Condensa 50 ml de humedad, anula el ángulo de contacto para humectar 
los bordes de la herida, modula una matriz viscoelástica que sella 
la hemorragia por compresión superficial e iguala la salinidad isotónica.
================================================================
```

---

## 2. Descripción Operativa y Bioquímica Rúnica

En el campo de batalla de Neoterra, la hemorragia por metralla o disparos es la causa principal de bajas antes de llegar a la enfermería. El **Parche de Coagulación Hidrostática** es el estándar de primeros auxilios de bajo coste que permite a cualquier Especialista estabilizar heridas graves.

### Principios de Acción Bioquímica y Tensión Superficial
Para lograr un sellado hemostático seguro sin instrumental médico ni daño osmótico, la secuencia opera sobre tres variables fisicoquímicas fundamentales:
* **Paso 1 — Humectabilidad Superhidrofílica (`HydroCapillarity.set_contact_angle`):** Fuerza el ángulo de contacto entre el fluido condensado y el perímetro epidérmico a $\theta = 0.0^\circ$. El agua se extiende en una micro-película continua que se adhiere tenazmente a la piel y los bordes de la incisión sin escurrirse.
* **Paso 2 — Matriz Viscoelástica No-Newtoniana (`HydroDynamics.set_viscosity`):** Reordena los puentes de hidrógeno formando un retículo viscoelástico gelatinoso ($140\text{ cP}$). Este gel actúa como una lámina compresiva flexible: es suave cuando la piel se dobla, pero se vuelve ultra-rígida ante la presión hidrostática de la sangre, taponando el sangrado de inmediato (imitando la red de fibrina de un coágulo natural).
* **Paso 3 — Ajuste de Salinidad Isotónica (`HydroSolutes.dissolve_solute`):** Disuelve micro-trazas de sales atmosféricas hasta estabilizar una concentración fisiológica de $9.000\text{ ppm}$ ($0.9\%\text{ NaCl}$ equivalente). Esto garantiza que el parche no provoque lisis celular, alivie el ardor y cree un entorno estéril semipermeable.
* **Cumplimiento Ético:** No penetra en el tejido celular profundo ni deshidrata al paciente, por lo que **no activa el DRM anti-biocida** del catalizador.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python

IMPORT RuneScript.Elements.Water.Gathering AS HydroGather;
IMPORT RuneScript.Elements.Water.FluidDynamics AS HydroDynamics;
IMPORT RuneScript.Elements.Water.Capillarity AS HydroCapillarity;
IMPORT RuneScript.Elements.Water.Solutes AS HydroSolutes;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE ParcheCoagulacion(WoundTarget: Surface) {
    HEADER {
        Rank: "C";
        Affinity: "Water";
        Control_Threshold: 1;
        Recycle: "Per_Scene";
        Complexity: "O(1)";
        Throughput: "3.8 kR/s";
    }

    PARAMETERS {
        Required_Moisture_L: 0.05;
        Wound_Wetting_Angle_Deg: 0.0;
        Gel_Viscosity_Cp: 140.0;
        Saline_Tonicity_Ppm: 9000.0;
    }

    EXECUTE {
        Moisture = HydroGather.extract_ambient_moisture(
            origin=WoundTarget.Center,
            volume_liters=Required_Moisture_L
        );

        HydroCapillarity.set_contact_angle(
            fluid=Moisture,
            target_surface=WoundTarget,
            angle_deg=Wound_Wetting_Angle_Deg
        );

        HydroDynamics.set_surface_tension(
            fluid=Moisture,
            tension_coefficient=9.2
        );
        HydroDynamics.set_viscosity(
            fluid=Moisture,
            cP_viscosity=Gel_Viscosity_Cp
        );

        HydroSolutes.dissolve_solute(
            fluid=Moisture,
            solute_type=ELECTROLYTE_SALTS,
            concentration_ppm=Saline_Tonicity_Ppm
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=Moisture);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Parche de Coagulación Hidrostática [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Superar Obstáculos (con `[✨] Control`):** Iniciar inmediatamente el tratamiento y recuperación de una **Consecuencia Leve física** (como `[Hemorragia por Esquirla]` o `[Tajo Abierto en el Muslo]`) en medio de un tiroteo sin requerir equipo quirúrgico ni tiempo fuera de escena.
  2. **Crear una Ventaja (con `[✨] Control`):** Colocar el aspecto de situación **`[Herida Sellada con Apósilo Rúnico]`** sobre un aliado o sobre sí mismo con 1 invocación gratuita.
* **Bonificador por Afinidad Elemental (Agua):**
  * Si el Especialista tiene afinidad nativa con **Agua**, el parche limpia el dolor celular de inmediato, **eliminando 1 casilla de estrés físico marcada** además de sellar la herida.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefactos de Ejecucion]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
