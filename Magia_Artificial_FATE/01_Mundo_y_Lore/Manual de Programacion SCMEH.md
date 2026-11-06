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

> *"Un buen Especialista no recita conjuros: escribe código estéril, compila variables limpias y no deja cabos sueltos en el bloque de seguridad."*
> — Compendio Técnico del Gremio de [[Ingenieros y Alquimistas]]

---

## 1. Fundamentos del Lenguaje RuneScript

**RuneScript** es el lenguaje formal de programación pseudo-mágica desarrollado por la humanidad para transcribir las runas del [[Magia Artificial y Reino Olvidado|Reino Olvidado]] a los circuitos lógicos de los **[[Artefactos de Ejecución]]**. 

Cada jugador que diseñe una **[[Secuencias de Hechizos (SCMEH)|Secuencia de Hechizo (S.C.M.E.H.)]]** debe estructurarla respetando **4 bloques canónicos obligatorios** y **1 bloque optativo**.

```text
┌───────────────────────────────────────────────────────────────────┐
│ [BLOQUE 1] HEADER          -> Metadatos (Rango, Afinidad, Coste)   │
│ [BLOQUE 2] PARAMETERS      -> Variables de Entrada y Tolerancias  │
│ [BLOQUE 3] EXECUTE         -> Algoritmo Lógico y Efecto Físico    │
│ [BLOQUE 4] SAFETY_OVERFLOW -> Protocolo de Excepción / Fallo      │
│ [BLOQUE 5] CUSTOM_EXPLOIT  -> Modificación personal del Jugador   │
└───────────────────────────────────────────────────────────────────┘
```

---

## 2. Especificación de Bloques

### Bloque 1: `HEADER` (Metadatos del Sistema)
Declara las compatibilidades de hardware y bio-requisitos:
* `Rank`: Rango requerido (`"C"`, `"B"`, `"A"`, `"S"`, `"SSS"`).
* `Affinity`: Vector elemental intrínseco (`"Air"`, `"Fire"`, `"Water"`, `"Earth"`, `"Lightning"`, `"Neutral"`).
* `Control_Threshold`: Nivel mínimo de `[✨] Control` del operador.
* `Recycle`: Ciclo de recarga (`"Infinite"`, `"Per_Scene"`, `"Single_Use_Burn"`).

### Bloque 2: `PARAMETERS` (Entradas del Mundo Real)
Define qué o a quién afecta el algoritmo y sus límites medibles:
* `Target`: Tipo de objetivo (`Entity`, `Object`, `Terrain`, `Self`).
* `Max_Range`: Distancia máxima operativa en metros.
* `Tolerances`: Límites numéricos (masa en kg, temperatura en °C, presión en bar).

### Bloque 3: `EXECUTE` (Cuerpo del Algoritmo)
Las instrucciones paso a paso que manipulan el entorno físico mediante palabras clave estandarizadas:
* **Funciones de polarización y fuerza:** `POLARIZE()`, `CHANNEL()`, `PROJECT()`, `LOCK_VECTOR()`, `PRESSURIZE()`.
* **Condicionales de flujo:** `IF (condicion) ... ELSE ...` y bucles de canalización `WHILE (Operador.HasFocus())`.

### Bloque 4: `SAFETY_OVERFLOW` (Gestión de Fallos)
Instrucciones que se disparan de forma automática si la tirada de dados en FATE resulta en fallo o si el operador es interrumpido:
* Define cómo se dispersa la energía residual para evitar consecuencias mortales (e.g. `VENT_HEAT_SLOWLY()`, `COLLAPSE_FIELD_INWARD()`).

### Bloque 5: `CUSTOM_EXPLOIT` *(Opcional / Aporte del Jugador)*
Un parámetro o instrucción casera añadida por el jugador que no forma parte del estándar comercial.
* **Mecánica en FATE:** Otorga un **Aspecto Situacional con una invocación gratuita** o un efecto narrativo ventajoso si el jugador lo justifica lógicamente.

---

## 3. Glosario de Palabras Clave y Librerías Oficiales

Para evitar que los jugadores tengan que inventar nombres de métodos desde cero, existen **Librerías Oficiales del Gremio** que pueden importarse:
* **[[Libreria SCMEH - AeroUtils|Librería de Utilidades de Aire (AeroUtils)]]:** Clases como `AirPressure`, `WindFlow`, `AeroAcoustics` y `AeroSafety`.
* *(Próximamente: PyroUtils, GeoUtils, HydroUtils, ElectroUtils).*

### Palabras Clave (Keywords Universales)

| Instrucción | Tipo | Descripción Operativa |
| :--- | :---: | :--- |
| `POLARIZE(area, value)` | Acción | Modifica polaridad magnética, gravitatoria o térmica de un punto. |
| `CHANNEL(affinity, rate)` | Flujo | Drena energía latente del Especialista hacia el catalizador. |
| `PROJECT(vector, speed)` | Vector | Lanza o propaga el efecto hacia una coordenada. |
| `BARRIER(geometry, hard)` | Defensa | Genera una geometría sólida de energía o densidad modificada. |
| `LOCK_DENSITY(target)` | Estado | Congela la masa relativa o fricción de un objeto. |
| `VENT_TO_CHASSIS()` | Seguridad | Disipa el calor residual en el metal del artefacto. |
| `ABORT(reason)` | Seguridad | Detiene la secuencia antes de quemar los micro-circuitos. |

---

## 4. Ejemplos de Referencia para Jugadores

### Ejemplo 1: Secuencia de Utilidad / Manipulación
```python
# =========================================================
# S.C.M.E.H. PROTOCOL // COMPILADO POR: Kaelen Vane
# CATALOGADO EN: LITTLE FOX [SLOT #1]
# =========================================================

SEQUENCE Levitar(Target: Object) {
    HEADER {
        Rank: "C";
        Affinity: "Air";
        Control_Threshold: 1;
        Recycle: "Infinite";
    }

    PARAMETERS {
        Max_Weight: 250.kg;
        Max_Altitude: 4.meters;
        Range: 15.meters;
    }

    EXECUTE {
        IF (Target.weight > Max_Weight) {
            ABORT("Exceso de tonelaje: colapso de sustentacion");
        }

        # Genera colchon barometrico inverso
        POLARIZE(surface=Target.bottom, pressure=+2.5.bar);
        Target.LOCK_DENSITY();

        WHILE (Operator.HasFocus()) {
            PROJECT(vector=VECTOR_UP, speed=1.2.mps);
            MAINTAIN_CUSHION(altitude=Target.current_alt);
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            # Descenso asistido para no reventar la carga contra el suelo
            DEPRESSURIZE_STEPWISE(rate=0.5.bar_per_sec);
            VENT_TO_CHASSIS(circuit=MAIN_BUS);
    }

    CUSTOM_EXPLOIT {
        # Modificacion personal: silenciador de flujo de viento
        AirFlow.mute_frequencies(band="SubSonic"); 
        # En FATE: Permite invocar [Levitación Sigilosa] gratis una vez
    }
}
```

---

### Ejemplo 2: Secuencia de Ataque / Balística Térmica
```python
# =========================================================
# S.C.M.E.H. PROTOCOL // PROYECTIL TERMICOKINÉTICO
# AUTOR: Alquimista Clandestino "Kuro"
# =========================================================

SEQUENCE DardoIgneo(Target: Entity) {
    HEADER {
        Rank: "C";
        Affinity: "Fire";
        Control_Threshold: 1;
        Recycle: "Infinite";
    }

    PARAMETERS {
        Range: 25.meters;
        Ignition_Temp: 850.celsius;
        Projectile_Speed: 45.mps;
    }

    EXECUTE {
        # Comprime oxigeno ambiental y excita moleculas
        CHANNEL(affinity="Fire", rate=CRITICAL_MASS);
        Spark = POLARIZE(volume=0.05.m3, heat=Ignition_Temp);
        
        # Balistica vectorial de impacto
        Trajectory = CALCULATE_VECTOR(origin=CHASSIS, target=Target.CenterOfMass);
        PROJECT(payload=Spark, vector=Trajectory, speed=Projectile_Speed);
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            # Si el operador pierde control, el fuego se expulsa hacia arriba
            FORCE_VECTOR_SKYWARD();
            Operator.TakeStress(amount=1, type="Mental");
    }
}
```

---

## 5. Integración en Mesa de Juego (FATE Básico)

* **El "Momento Compilación":** Al inicio de la sesión o en un descanso largo, cada jugador entrega su hoja/tarjeta de código para registrar las secuencias cargadas en sus slots.
* **Auditoría del DJ (Control de Bugs):**
  * Si un jugador no programa un bloque `SAFETY_OVERFLOW`, cualquier fallo en la tirada de dados se convierte automáticamente en una Consecuencia grave o daño directo.
  * Si programa un buen protocolo de emergencia, un fallo de dados puede resolverse como un simple "reinicio de artefacto" (Éxito con coste o complicación menor).
* **Renderizado y Presentación:** Se anima a los jugadores a escribirlo en fichas milimetradas o renderizarlo digitalmente mediante **Ray.so** o **Carbon.now.sh** con tipografía de consola para usarlo como tarjeta física en la mesa.

---

## 6. Entidades Relacionadas
* [[Artefactos de Ejecucion]]
* [[Secuencias de Hechizos SCMEH]]
* [[Los Especialistas]]
* [[Ingenieros y Alquimistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
* [[Artefacto - Little Fox]]
* [[Secuencia - Levitar]]
