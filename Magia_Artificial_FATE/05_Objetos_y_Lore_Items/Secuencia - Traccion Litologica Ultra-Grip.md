---
title: "Secuencia - Tracción Litológica Ultra-Grip"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Tierra"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/tierra
  - movilidad/escalada
  - objeto
  - fate/proeza
aliases:
  - Tracción Litológica
  - Ultra-Grip Litológico
  - Adhesión de Suela
  - Secuencia Tracción Litológica
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# ⛰️ Secuencia: Tracción Litológica Ultra-Grip (Rango C)

> *"Si pegas tus botas a la roca con fuerza bruta constante, no puedes dar el siguiente paso y te caes de bruces. El truco de la naturaleza (como las patas de un geco sobre el granito) es la fricción direccional por cizalla: la suela se clava como acero cuando tu peso tira hacia abajo, pero se suelta sin resistencia cuando despegas el talón para avanzar."*
> — Explorador Veterano del Frente Montañoso

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Tracción Litológica Ultra-Grip (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Fricción Direccional y Desacople de Ciclo de Marcha
================================================================
Afinidad:    Tierra
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       3.0 kR/s

Acción:
Polariza los enlaces moleculares entre la suela del calzado y el 
sustrato mineral. Activa ultra-fricción por cizalla ante carga lateral 
o vertical, pero libera la adherencia cuando el pie se alza normal.
================================================================
```

---

## 2. Descripción Operativa y Biomecánica de Marcha

La secuencia **Tracción Litológica Ultra-Grip** es el software de escalada e infiltración por excelencia de los exploradores mineros y fuerzas especiales que operan en túneles subterráneos, búnkeres de concreto o cañones escarpados del [[El Hallazgo de los Fosiles de Dragon|Reino Olvidado]].

### Principios de Fricción Direccional y Marcha Biomecánica
Para permitir un desplazamiento fluido por muros y techos sin trabar el movimiento de las extremidades, el algoritmo modula una respuesta de adhesión selectiva:
El algoritmo replica los principios de las fuerzas de Van der Waals direccionales y el micro-anclaje mecánico:

1. **Adhesión Asimétrica por Cizalla (`GeoTexture.set_directional_shear_friction`):** El artefacto polariza los microcristales de sílice, basalto o cemento bajo el calzado. Establece un coeficiente de fricción asimétrico:
   * **Bajo Esfuerzo de Cizalla (Carga Paralela al Muro / Peso del Cuerpo):** $\mu_s = 4.2$. La suela resiste toneladas de fuerza hacia abajo sin deslizar un milímetro, sosteniendo al Especialista en paredes verticales de 90° o techos de cuevas.
   * **Bajo Levantamiento Perpendicular (Despegue Normal de la Suela):** $\mu_n \approx 0.0$. Cuando el Especialista dobla la articulación del tobillo para dar el siguiente paso, la polarización cristalina se disipa en microsegundos, permitiendo que la pierna avance con total soltura y sin resistencia.
2. **Amortiguación Acústica de Impacto (`GeoSeismic.dampen_seismic_vibrations`):** Como subproducto de la polarización elástica superficial, el impacto de las botas contra losas o rocas sueltas es amortiguado a nivel molecular, silenciando por completo el crujido de pisadas sobre grava o concreto.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python

IMPORT RuneScript.Elements.Earth.SurfaceTexture AS GeoTexture;
IMPORT RuneScript.Elements.Earth.Seismic AS GeoSeismic;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE TraccionLitologica(CasterBoots: Surface) {
    HEADER {
        Rank: "C";
        Affinity: "Earth";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "3.0 kR/s";
    }

    PARAMETERS {
        Duration_Sec: 60.0;
        Max_Shear_Coefficient_Mu: 4.2;
        Acoustic_Dampening_Db: 25.0;
    }

    EXECUTE {
        GeoTexture.set_directional_shear_friction(
            stone_surface=CasterBoots,
            normal_release=TRUE,
            max_shear_mu=Max_Shear_Coefficient_Mu
        );

        GeoSeismic.dampen_seismic_vibrations(
            zone=CasterBoots.ContactArea
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            GeoTexture.set_friction_profile(
                stone_surface=CasterBoots,
                profile=MIRROR_POLISHED_ZERO_FRICTION
            );
            SafeAbort.collapse_confinement_inward(envelope=CasterBoots);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Tracción Litológica Ultra-Grip [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Superar Obstáculos (con `[✨] Control`):** Escalar murallas de concreto, pilares de piedra o desplazarse por el techo de túneles minerales sin necesidad de tiradas de Atletismo ni arneses de escalada.
  2. **Defender (con `[✨] Control`):** Otorga un bonificador de **+2 a la defensa física** contra intentos enemigos de derribar, barrer con explosiones, empujar o desestabilizar la posición del Especialista.
  3. **Crear una Ventaja (con `[✨] Control`):** Colocar el aspecto situacional **`[Anclado al Techo Fuera de Línea de Fuego]`** o **`[Pisadas Silenciadas en Terreno Rocoso]`** con 1 invocación gratuita.
* **Bonificador por Afinidad Elemental (Tierra):**
  * Si el Especialista tiene afinidad con **Tierra**, la secuencia puede compartirse por inducción de contacto con un aliado cercano que camine pegado a su espalda.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
