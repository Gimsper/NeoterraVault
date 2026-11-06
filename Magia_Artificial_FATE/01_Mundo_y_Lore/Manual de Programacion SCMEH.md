---
title: "Manual de Programación S.C.M.E.H. - Estándar RuneScript"
type: lore
categoria: magia_tecnologia
relevancia_en_trama: alta
tags:
  - narrativa/lore
  - magia/programacion
  - tecnologia/software
  - fate/reglas
aliases:
  - RuneScript
  - Manual SCMEH
  - Estándar de Scripting
  - Sintaxis SCMEH
status: revisado
created: 2026-11-05
updated: 2026-11-05
---

# 💻 Manual de Programación S.C.M.E.H. (Estándar RuneScript)

> *"Un buen Especialista no recita conjuros: escribe código estéril, ensambla variables físicas atómicas, confina la geometría de su energía y no deja fugas en el bloque de seguridad."*
> — Compendio Técnico del Gremio de [[Ingenieros y Alquimistas]]

---

## 1. Fundamentos del Lenguaje RuneScript

**RuneScript** es el lenguaje formal de programación pseudo-mágica desarrollado por la humanidad para transcribir las runas del [[Magia Artificial y Reino Olvidado|Reino Olvidado]] a los circuitos lógicos de los **[[Artefactos de Ejecución]]**. 

Cada jugador que diseñe una **[[Secuencias de Hechizos SCMEH|Secuencia de Hechizo (S.C.M.E.H.)]]** debe estructurarla respetando **4 bloques canónicos obligatorios** y **1 bloque optativo**.

```text
┌───────────────────────────────────────────────────────────────────┐
│ [BLOQUE 1] HEADER          -> Metadatos (Rango, Afinidad, Coste)   │
│ [BLOQUE 2] PARAMETERS      -> Variables de Entrada y Tolerancias  │
│ [BLOQUE 3] EXECUTE         -> Algoritmo Modular Paso a Paso       │
│ [BLOQUE 4] SAFETY_OVERFLOW -> Protocolo de Excepción / Fallo      │
│ [BLOQUE 5] CUSTOM_EXPLOIT  -> Modificación personal del Jugador   │
└───────────────────────────────────────────────────────────────────┘
```

---

## 2. Especificación de los Bloques

### Bloque 1: `HEADER` (Metadatos del Sistema)
Declara las compatibilidades de hardware y bio-requisitos:
* `Rank`: Rango auditado del algoritmo (`"C"`, `"B"`, `"A"`, `"S"`, `"SSS"`).
* `Affinity`: Afinidad elemental nativa (`"Air"`, `"Fire"`, `"Water"`, `"Earth"`, `"Lightning"`, `"Neutral"`).
* `Control_Threshold`: Nivel mínimo de `[✨] Control` del operador.
* `Recycle`: Ciclo de recarga del slot (`"Infinite"`, `"Per_Scene"`, `"Single_Use_Burn"`).

### Bloque 2: `PARAMETERS` (Entradas del Mundo Real)
Define qué o a quién afecta el algoritmo y sus tolerancias medibles:
* `Target`: Tipo de objetivo (`Entity`, `Object`, `Area`, `Self`).
* `Max_Range`: Distancia máxima operativa en metros.
* `Tolerances`: Límites numéricos (masa en kg, temperatura en °C, presión en bar, radio de área en metros).

### Bloque 3: `EXECUTE` (Cuerpo del Algoritmo Modular)
**Regla de oro:** No existen funciones monolíticas de conjuro completo. El bloque `EXECUTE` debe concatenar lógicamente las fases físicas de la secuencia:
1. **Preparación / Masa:** Captar humedad, aislar comburente o licuar superficie.
2. **Transformación de Estado:** Modificar temperatura, enlace cristalino o ionizar plasma.
3. **Confinamiento Geométrico:** Contener la energía dentro de un radio o envoltura (`Envelope`).
4. **Validaciones de Seguridad:** Comprobar estabilidad de campo antes del lanzamiento (`IF (!Envelope.is_stable()) ABORT(...)`).
5. **Vectorización Cinética:** Asignar trayectorias o impulsos con `Kinetics.*`.
6. **Disparadores de Impacto / Evento:** Definir qué ocurre en colisión (`Triggers.OnCollision`).

### Bloque 4: `SAFETY_OVERFLOW` (Gestión de Excepciones y Fallos)
Instrucciones automáticas que se disparan si la tirada de dados en FATE resulta en fallo o si el operador es aturdido:
* Define cómo se purga la energía residual para evitar que estalle en el cuerpo del lanzador (e.g. `Safe.Vent.shunt_heat_to_atmosphere()`, `Safe.Abort.collapse_confinement_inward()`).
* **Regla en FATE:** Un buen bloque de seguridad mitiga consecuencias físicas graves, transformando un fallo en una complicación menor o estrés temporal.

### Bloque 5: `CUSTOM_EXPLOIT` *(Opcional / Aporte del Jugador)*
Una modificación artesanal en los parámetros o subrutinas creada por el jugador que no forma parte del estándar comercial.
* **Mecánica en FATE:** Otorga un **Aspecto Situacional con una invocación gratuita** o una ventaja narrativa táctica si está debidamente justificada.

---

## 3. Arquitectura del SDK y Librerías Oficiales

Para programar secuencias, los jugadores importan los módulos atómicos especificados en el [[Compendio de Librerias Elementales SCMEH]] y el [[Macro de Librerias SCMEH]]:

```text
RuneScript/
├── Elements/          -> Primitivas de Materia (Air, Fire, Water, Earth, Lightning, Aether)
├── Geometry/          -> Confinamiento de formas (bind_sphere, bind_cylinder, scale_volume)
├── Kinetics/          -> Dinámica de vectores, velocidad, inercia y gravedad
├── Triggers/          -> Eventos (OnCollision, OnProximity, OnTimer, OnVocalCommand)
├── Sensory/           -> Refracción óptica, audio fantasma y silenciamiento
├── Neural/            -> Telepatía y amortiguación sensorial
├── Engineering/       -> Diagnóstico térmico y compilación en chips desechables
└── Safety/            -> Purgas calóricas, polo a tierra y descompresión segura
```

---

## 4. Ejemplos de Referencia para Jugadores

### Ejemplo 1: Secuencia de Utilidad / Manipulación Neumática
Demuestra la preparación de masa de aire, diferencial de presión barométrica y bucle de sostenimiento:

```python
# ==============================================================================
# S.C.M.E.H. PROTOCOL // COMPILADO POR: Kaelen Vane
# CATALOGADO EN: LITTLE FOX [SLOT #1]
# ==============================================================================

IMPORT RuneScript.Elements.Air AS Aero;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Safety AS Safe;

SEQUENCE Levitar(Target: Object) {
    HEADER {
        Rank: "C";
        Affinity: "Air";
        Control_Threshold: 1;
        Recycle: "Infinite";
    }

    PARAMETERS {
        Max_Weight: 250.kg;
        Target_Altitude: 3.5.meters;
        Range: 15.meters;
    }

    EXECUTE {
        # Validación de peso para evitar sobrecarga del inductor
        IF (Target.weight > Max_Weight) {
            ABORT("Masa superior a tolerancia: riesgo de sobrecalentamiento");
        }

        # PASO 1: Generar gradiente barométrico diferencial bajo la base del objetivo
        Aero.Pressure.set_differential(
            surface_high=Target.bottom_surface,
            surface_low=Target.top_surface,
            delta_bar=+2.2
        );

        # PASO 2: Iniciar corriente laminar ascendente de sustentación
        Stream = Aero.GasFlow.stream_vector(
            origin=Target.position,
            vector=VECTOR_UP,
            flux_liters_sec=120.0
        );

        # PASO 3: Bucle de canalización mientras el Especialista mantenga la concentración
        WHILE (Operator.HasFocus() AND Target.altitude < Target_Altitude) {
            KineticVector.apply_impulse(target=Target, vector=VECTOR_UP, force_newtons=18.0);
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            # Descompresión escalonada para evitar que la carga caiga en seco
            Aero.Pressure.set_differential(
                surface_high=Target.bottom_surface,
                surface_low=Target.top_surface,
                delta_bar=0.0
            );
            Safe.Vent.shunt_heat_to_atmosphere(joules=600.0);
    }

    CUSTOM_EXPLOIT {
        # Supresión acústica en frecuencias subsónicas
        Sensory.Acoustics.mute_frequencies(band="LowSubSonic");
        # En FATE: Permite invocar gratuitamente una vez el aspecto [Ascenso Silencioso]
    }
}
```

---

### Ejemplo 2: Secuencia Ofensiva Balística / Dardo Ígneo Perforante
Demuestra la compresión de gas, agitación térmica, confinamiento cilíndrico, aceleración balística y detonación superficial:

```python
# ==============================================================================
# S.C.M.E.H. PROTOCOL // PROYECTIL TERMICOKINÉTICO DE PERFORACIÓN
# COMPILADO POR: Alquimista Clandestino "Kuro"
# ==============================================================================

IMPORT RuneScript.Elements.Air AS Aero;
IMPORT RuneScript.Elements.Fire AS Pyro;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Triggers AS Triggers;
IMPORT RuneScript.Safety AS Safe;

SEQUENCE DardoIgneo(Target: Entity) {
    HEADER {
        Rank: "C";
        Affinity: "Fire";
        Control_Threshold: 1;
        Recycle: "Infinite";
    }

    PARAMETERS {
        Range: 30.meters;
        Ignition_Temp: 1400.celsius;
        Thrust_Force: 320.newtons;
    }

    EXECUTE {
        # PASO 1: Condensar comburente gaseoso en un bolsón cilíndrico
        GasPocket = Aero.Density.compress_gas(volume_m3=0.10, ratio=4.0);

        # PASO 2: Agitación molecular extrema (excitación térmica)
        Pyro.Thermal.excite_molecules(target_zone=GasPocket, temp_celsius=Ignition_Temp);
        Core = Pyro.Combustion.ignite_mix(flammable_target=GasPocket, oxygen_ratio=0.35);

        # PASO 3: Confinamiento en dardo aerodinámico de alta presión
        Envelope = Pyro.Confinement.bind_cylinder(energy_core=Core, length_m=0.45, radius_m=0.04);
        Envelope.compress(factor=1.6);

        # PASO 4: Chequeo de contención de la envoltura
        IF (!Envelope.is_stable()) {
            ABORT("Presión térmica excesiva: envoltura inestable");
        }

        # PASO 5: Impulso vectorial balístico directo al objetivo
        Trajectory = KineticVector.calculate_line(from=Operator.Hand, to=Target.CenterOfMass);
        KineticVector.apply_impulse(target=Envelope, vector=Trajectory, force_newtons=Thrust_Force);

        # PASO 6: Disparador en colisión
        Triggers.OnCollision(target=Envelope) {
            Envelope.release(); # Libera la punta térmica
            Pyro.Combustion.ignite_surface(radius_m=1.5, burn_rate=RAPID);
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            # Si el operador pierde el control antes de disparar, el dardo se disipa verticalmente
            Envelope.release();
            Safe.Vent.shunt_heat_to_atmosphere(joules=2500.0);
            Operator.TakeStress(amount=1, type="Physical");
    }
}
```

---

## 5. Integración en Mesa de Juego (FATE Básico)

* **El "Momento Compilación":** Al inicio de la sesión o durante descansos largos en el taller, cada jugador presenta o revisa las tarjetas de código de sus secuencias equipadas en los slots de su artefacto.
* **Auditoría del Director de Juego (Caza de Bugs):**
  * Si un jugador omite un paso crítico (por ejemplo, genera calor intenso pero olvida el confinamiento geométrico), el DJ puede forzar una complicación o daño por dispersión térmica.
  * Si el jugador no incluye bloque `SAFETY_OVERFLOW`, cualquier fallo en la tirada de `[✨] Control` acarrea consecuencias graves o estrés severo. Si está bien programado, el fallo se absorbe de forma segura.
* **Tarjetas Físicas:** Se recomienda pasar el código por herramientas de renderizado con tipografía monoespaciada para usar tarjetas plastificadas como accesorios de juego en la mesa.

---

## 6. Entidades Relacionadas
* [[Compendio de Librerias Elementales SCMEH]]
* [[Macro de Librerias SCMEH]]
* [[Calculo de Rangos SCMEH - Big-O y Flujo]]
* [[Secuencias de Hechizos SCMEH]]
* [[Artefactos de Ejecucion]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]