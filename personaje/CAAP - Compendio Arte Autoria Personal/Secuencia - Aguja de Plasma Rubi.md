---
title: "Secuencia - Aguja de Plasma Rubí"
type: secuencia_hechizo
categoria: personaje/hechizos_propietarios
propietario: Luna Evergarden
id_caap: "CAAP-C01"
rango: "C"
afinidad: "Pyro (RuneScript.Elements.Fire)"
catalizador_recomendado: "Little Fox (Kitsune Micro-Arcana)"
complejidad_algoritmica: "O(1)"
flujo_biomagico: "8.8 kR/s"
umbral_control: 1
tags:
  - personaje/luna_evergarden
  - hechizo/rango_c
  - afinidad/fire
  - runescript/secuencia
  - caap/acto_1
aliases:
  - Aguja de Plasma Rubí
  - AgujaPlasmaRubi
  - CAAP-C01
status: archivado_academico
created: 2026-11-09
updated: 2026-11-09
---
_El archivo huele a resignación burocrática intervenida con lápiz labial y chispas de estática._ %%Sí, lo sé. Es repugnantemente seguro. Pero era esto o reprobar 'Protocolos de Seguridad I' con el amargado del Instructor Vane. Lo guardo aquí para no tener que volver a escribirlo en mi vida.%%

# 🔴🎭 CAAP-C01: Aguja de Plasma Rubí
### *Ejercicio Académico de Confinamiento Focal y Micro-Balística de Salón*
**ID Oficial de Registro:** `SEC-C-PYRO-4091-LUNA`  
**Clasificación:** Rango C (Civil / Instrucción de Cadetes)  
**Complejidad:** $\mathcal{O}(1)$ | **Flujo Promedio:** $8.8\text{ kR/s}$

> *"El instructor dijo: 'Mantengan el volumen de gas por debajo de dos centímetros cúbicos y no osen superar los cinco metros de alcance'. Yo digo que si me obligan a disparar a quemarropa, al menos el proyectil no va a parecer una cerilla apagada. Si voy a pinchar a alguien, lo haré con un rubí incandescente."*  
> — **Luna Evergarden**, notas al pie de la entrega final.

---

## 💅 1. La Reseña de Luna: *"El Bostezo Mejor Confinado del Aula"*

Vamos a ser brutalmente honestos: este código es **un insulto a mi vocación dramática**. 

Nació como una tarea obligatoria de la Academia: *«Práctica de Laboratorio 03: Síntesis Cilíndrica y Derivación Segura de Sobretensión»*. Básicamente, el manual de la Federación para cobardes que le tienen miedo a quemarse las pestañas. Los instructores vigilaron cada parámetro como halcones seniles:
* *«¡Luna, no excedas los 10 kR/s o sobrecalentarás la placa!»* (Por favor, el *Little Fox* ni siquiera entibia su chasis con esa miseria).
* *«¡Luna, rango máximo 5 metros, estamos en un polígono cerrado!»* (Cinco metros... ¡eso no es balística, es una conversación incómoda!).
* *«¡Obligatorio meter dos rutinas de aborto y chimenea de ventilación atmosférica!»*

Aun así... algo de dignidad tenía que meterle. No iba a permitir que mi terminal compilara una vulgar chispa anaranjada de fogata de campamento. Le ajusté la excitación molecular en la cola a $1.300\text{ }^\circ\text{C}$ y le metí un gradiente térmico de $+1.100\text{ K}$ hacia la punta. ¿El resultado visual? Una aguja esbelta de 30 centímetros, comprimida en un cilindro perfecto de ocho milímetros de radio que brilla con un tono rubí profundo antes de rematar en un destello de plasma blanco cegador.

%%Admito algo a regañadientes: la aburrida obsesión de la academia con el confinamiento estricto tiene su encanto físico. Comprimir el gas a razón 2.2 dentro de un envoltorio magnético cerrado hace que el vector vuele recto como una cuerda de violín. Tal vez... solo tal vez... haya algo útil que saquear de toda esta basura reglamentaria.%%

---

## 🎛️ 2. Ficha Técnica Oficial (S.C.M.E.H.)

```
================================================================================
FICHA TÉCNICA: AGUJA DE PLASMA RUBÍ (CAAP-C01)
================================================================================
RANGO FEDERACIÓN : Rango C (Mediocre / Soporte Táctico Menor)
AFINIDAD         : Fuego / Térmico (RuneScript.Elements.Fire)
COMPLEJIDAD      : O(1) - Blanco unitario y masa gaseosa constante
FLUJO BIO-MÁGICO : 8.8 kR/s (Pico transitorio: 9.4 kR/s en ignición)
UMBRAL CONTROL   : [🎛️] Control (1) — Mediocre (+1)
RECARGA / RECYCLE: Cooldown de 1 Asalto (Dispersión térmica del catalizador)
ALCANCE EFECTIVO : 5.0 metros (Límite impuesto por directiva docente)
DIMENSIÓN FÍSICA : Longitud: 0.30 m | Radio focal: 0.008 m
GEOMETRÍA        : Cilindro con gradiente longitudinal termodinámico
DAÑO ESTIMADO    : Perforación térmica puntual + ignición residual de 0.25 m
================================================================================
```

---

## 💻 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Air.Density AS AeroDensity;
IMPORT RuneScript.Elements.Fire.Thermal AS PyroThermal;
IMPORT RuneScript.Elements.Fire.Plasma AS PyroPlasma;
IMPORT RuneScript.Elements.Fire.Confinement AS PyroConfinement;
IMPORT RuneScript.Elements.Fire.Combustion AS PyroCombustion;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Triggers.Collision AS TriggerCollision;
IMPORT RuneScript.Safety.Abort AS SafeAbort;
IMPORT RuneScript.Safety.Vent AS SafeVent;

SEQUENCE AgujaPlasmaRubi(Target: Entity) {
    HEADER {
        Rank: "C";
        Affinity: "Fire";
        Control_Threshold: 1;
        Recycle: "Cooldown_1_Round";
        Complexity: "O(1)";
        Throughput: "8.8 kR/s";
    }

    PARAMETERS {
        Max_Range_M: 5.0;
        Gas_Volume_M3: 0.002;
        Gas_Ratio: 6.0;
        Tail_Temp_Celsius: 1300.0;
        Tip_Delta_K: 1100.0;
        Needle_Length_M: 0.30;
        Needle_Radius_M: 0.008;
        Compression_Factor: 2.2;
        Max_Deviation_Deg: 1.5;
        Impulse_Newtons: 55.0;
        Impact_Burn_Radius_M: 0.25;
    }

    EXECUTE {
        IF (Target.Distance > Max_Range_M) {
            ABORT("Blanco fuera del alcance puntual");
        }

        GasPocket = AeroDensity.compress_gas(
            volume_m3=Gas_Volume_M3,
            ratio=Gas_Ratio
        );

        PyroThermal.excite_molecules(
            target_zone=GasPocket,
            temp_celsius=Tail_Temp_Celsius
        );

        PlasmaCore = PyroPlasma.ionize_gas(
            gas_pocket=GasPocket,
            energy_density=HIGH
        );

        PyroThermal.set_thermal_gradient(
            from_point=PlasmaCore.Rear,
            to_point=PlasmaCore.Front,
            delta_k=Tip_Delta_K
        );

        Needle = PyroConfinement.bind_cylinder(
            energy_core=PlasmaCore,
            length_m=Needle_Length_M,
            radius_m=Needle_Radius_M
        );

        PyroConfinement.compress(
            envelope=Needle,
            factor=Compression_Factor
        );

        IF (!PyroConfinement.is_stable(envelope=Needle)) {
            ABORT("Presión de núcleo excesiva: envoltura inestable");
        }

        Trajectory = KineticVector.calculate_line(
            from_point=Operator.Hand,
            to_point=Target.CenterOfMass
        );

        KineticVector.lock_trajectory(
            target=Needle,
            vector=Trajectory,
            max_deviation_deg=Max_Deviation_Deg
        );

        KineticVector.apply_impulse(
            target=Needle,
            vector=Trajectory,
            force_newtons=Impulse_Newtons
        );

        TriggerCollision.OnCollision(target=Needle) {
            PyroConfinement.release(envelope=Needle);
            PyroCombustion.ignite_surface(
                radius_m=Impact_Burn_Radius_M,
                burn_rate=RAPID
            );
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=Needle);
            SafeVent.shunt_heat_to_atmosphere(joules=900.0);
    }
}
```

%%Miren esa rutina de SAFETY_OVERFLOW... 'shunt_heat_to_atmosphere'. Es literalmente convertir mi obra en una tetera hirviendo si pestañeo mal. Humillante. Pero al profesor le brillaron los ojos cuando vio que no quemé las cortinas del laboratorio.%%

---

## 🎲 4. Implementación en FATE Básico (Proeza de Magia)

### Mecánica de Activación y Acción
* **Acción Principal:** **Atacar** o **Crear una Ventaja** contra un blanco a distancia corta (misma zona o zona adyacente inmediata, máx. 5 m).
* **Tirada:** `Disparar` o `Voluntad` (según si se prioriza el vector balístico o el confinamiento bio-mágico).
* **Dificultad de Control:** `Mediocre (+1)`. Al ser afín a **Pyro**, Luna obtiene automáticamente su bonificación pasiva `+2` al manipular igniciones térmicas, garantizando una compilación prácticamente infalible bajo condiciones estándar.

### Resultados de la Tirada
* **Fallo:** La rutina de seguridad intercepta la compilación (`SafeAbort`). La aguja colapsa hacia adentro y los 900 Joules se ventilan como una ráfaga de aire tibio con olor a ozono. No hay daño colateral, pero el catalizador entra en bloqueo térmico por 1 asalto.
* **Empate:** El proyectil roza al blanco o impacta de refilón; inflige 1 casilla de estrés físico o concede un aspecto temporal menor como *«Ropa humeante»*.
* **Éxito:** Impacto directo. Inflige daño de estrés físico estándar igual al margen de éxito y genera una quemadura confinada de $0.25\text{ m}$.
* **Éxito con Estilo:** La punta de plasma blanco perfora el punto exacto deseado. Además del daño correspondiente, crea el aspecto de situación con 1 invocación gratuita: **«Quemadura de Rubí Focalizada»** o **«Costura Térmica Abierta»**.

---

## 🔮 5. Bitácora de Luna: *Próximamente... La Versión 2.0*

> [!TIP]
> ### ⚡ EN EL BANCO DE TRABAJO: *Aguja Carmesí v2.0 (The Director's Cut)*
> Ya entregué la tarea, ya tengo mi nota aprobatoria y los ancianos de la academia están tranquilos. Ahora empieza lo divertido.
> 
> En mis ratos libres en el cuartel estoy rediseñando el script entero:
> 1. **Multi-Vector Simultáneo:** Nada de $\mathcal{O}(1)$ aburrido. Quiero compilar tres agujas en abanico giratorio que converjan en el blanco como los reflectores de un teatro ($\mathcal{O}(n)$).
> 2. **Desprecio por los 5 Metros:** El nuevo cálculo cinético elevará el impulso a más de $200\text{ N}$. Si voy a perforar algo, lo haré desde el fondo de la sala mientras mantengo mi copa intacta.
> 3. **Deflagración Escénica:** Al colisionar, el plasma no va a *liberarse* estúpidamente como un mechero; va a abrirse en una flor simétrica de plasma blanco que cegará a todo el que no esté usando protección ocular.
> 
> *Próximamente en este compendio... cuando consiga que el Little Fox no se reinicie por exceso de vanidad.* ✨💅

---

## 🔗 Enlaces del Compendio

* 🎭 Índice Maestro: [[MOC - Compendio de Arte de Autoria Personal]]
* 🦊 Consola de Compilación: [[Artefacto - Little Fox]]
* 📋 Ficha de Operadora: [[Luna_Evergarden_Ficha_Fate]]
