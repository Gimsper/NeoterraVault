---
title: "Secuencia - Apósito Hidrostático Escolar"
type: secuencia_hechizo
categoria: personaje/hechizos_propietarios
propietario: Luna Evergarden
id_caap: "CAAP-C03"
rango: "C"
afinidad: "Agua (RuneScript.Elements.Water)"
catalizador_recomendado: "Little Fox (Kitsune Micro-Arcana)"
complejidad_algoritmica: "O(1)"
flujo_biomagico: "3.8 kR/s"
umbral_control: 1
tags:
  - personaje/luna_evergarden
  - hechizo/rango_c
  - afinidad/water
  - runescript/secuencia
  - caap/acto_1
  - medicina/soporte
aliases:
  - Apósito Hidrostático Escolar
  - ApositoHidrostaticoEscolar
  - Gasa Hidrostática de Academia
  - CAAP-C03
status: archivado_academico
created: 2026-11-10
updated: 2026-11-10
---
_El archivo tiene la pulcritud fría de una tarea entregada a tiempo, firmada con un sobresaliente forzado._ %%Otra joya del plan de estudios de la Academia: 'Soporte Vital y Triage Rúnico I'. Seiscientas líneas de código hidroestático para convencer a niños asustados de que un poco de condensación con salitre los salvará de la muerte. Qué farsa tan tierna.%%

# 💧🎭 CAAP-C03: Apósito Hidrostático Escolar
### *Protocolo Reglamentario de Capilaridad, Tensión Viscoelástica y Medicina Superficial de Aula*
**ID Oficial de Registro:** `SEC-C-HYDRO-2044-LUNA-MED`  
**Clasificación:** Rango C (Soporte Médico Menor / Tarea Obligatoria de Recluta)  
**Complejidad:** $\mathcal{O}(1)$ | **Flujo Promedio:** $3.8\text{ kR/s}$  
**Atribución de Arquitectura Base:** Compilado a partir del estándar de instrucción del Cuerpo Médico de la Federación ([[Secuencia - Parche de Coagulacion Hidrostatica|Parche de Coagulación Hidrostática]]).

> *"Las heridas, el raspón sangrante en la mejilla o el uniforme desgarrado no son una tragedia: son parte de la puesta en escena. Añaden urgencia, contraste y drama a la actuación. ¿Pero esto? Esto es el equivalente rúnico a que te pongan una tirita con dibujitos infantiles. Los instructores te miran con orgullo de burócratas cuando sellas un arañazo de entrenamiento... como si eso fuera a servir de algo cuando el mundo de verdad empiece a romperse en pedazos."*  
> — **Luna Evergarden**, notas marginales en la libreta de Medicina de Campaña.

---

## 🩹 1. La Reseña de Luna: *"El Parche de los Rasguños Triviales"*

Para aprobar *Medicina Básica de Campaña*, la Academia te exige memorizar cómo condensar cincuenta mililitros de humedad ambiental, forzar el ángulo de contacto a cero grados y fabricar una membrana gelatinosa que imite una red de fibrina. 

El resultado técnico es impecable: un apósito estéril, flexible, suave como la seda y completamente inocuo.

**Y completamente inútil para lo que de verdad importa.**

La Federación adora venderte la ilusión de que el personal médico tiene el control. Pero yo estuve en la carretera. Yo vi a mis compañeros de caravana morir aplastados contra el barro en menos de diez segundos. Cuando un proyectil de mortero te arranca medio torso o las garras de un Heraldo te pulverizan la columna vertebral, **tu agüita salina sirve únicamente para lavar el cadáver antes de meterlo en la bolsa de lona**. 

Esta secuencia solo sirve para **heridas leves**:
* El cadete torpe que se cortó el pulgar abriendo una lata de raciones.
* El recluta que se rozó las rodillas arrastrándose por el polígono de tiro.
* La astilla impertinente que mancha de rojo un cuello de camisa recién planchado.

Para la muerte real, para el dolor que te arranca el alma y te deja en coma durante seis meses conectado a tubos en el Pabellón 4B... la magia de agua de la Academia no tiene respuestas. Solo silencio, respiradores mecánicos y formularios de pensión militar.

%%Aun así, le metí una mínima modificación óptica (`Optics.tint_fluid`). En vez de parecer una plasta transparente de baba de caracol, mi apósito refracta la luz con un tono zafiro pálido brillante. Si alguna vez tengo que taparme un rasguño frente a los oficiales, al menos parecerá un tratamiento cosmético de alta gama y no una toalla húmeda de cuartel.%%

---

## 🎛️ 2. Ficha Técnica Oficial (S.C.M.E.H.)

```
================================================================================
FICHA TÉCNICA: APÓSITO HIDROSTÁTICO ESCOLAR (CAAP-C03)
================================================================================
RANGO FEDERACIÓN : Rango C (Soporte Sanitario Básico / Nivel Escolar)
AFINIDAD         : Agua (RuneScript.Elements.Water)
COMPLEJIDAD      : O(1) - Extracción volumétrica fija (50 ml)
FLUJO BIO-MÁGICO : 3.8 kR/s (Mínimo, casi imperceptible para el Little Fox)
UMBRAL CONTROL   : [🎛️] Control (1) — Mediocre (+1)
RECARGA / RECYCLE: Por Escena (Duración: 2 asaltos de estabilización)
SALINIDAD ÓPTICA : 9,000 ppm (Isotonía estéril / 0.9% NaCl)
VISCOSIDAD GEL   : 140 cP (Matriz viscoelástica hidrocoloide)
ALCANCE EFECTIVO : Contacto directo / Zona inmediata (0 a 1 metro)
================================================================================
```

---

## 💻 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Water.Gathering AS HydroGather;
IMPORT RuneScript.Elements.Water.FluidDynamics AS HydroDynamics;
IMPORT RuneScript.Elements.Water.Capillarity AS HydroCapillarity;
IMPORT RuneScript.Elements.Water.Solutes AS HydroSolutes;
IMPORT RuneScript.Sensory.Optics AS Optics;
IMPORT RuneScript.Safety.Abort AS SafeAbort;
IMPORT RuneScript.Safety.Vent AS SafeVent;

/* ============================================================================
 * SEC-C-HYDRO-2044-LUNA-MED :: APÓSITO HIDROSTÁTICO ESCOLAR
 * Protocolo de primeros auxilios de la Federación / Tarea de Academia.
 * Ajuste cosmético de refracción zafiro por Luna Evergarden.
 * ============================================================================ */

SEQUENCE ApositoHidrostatico(WoundTarget: Surface) {
    HEADER {
        Rank: "C";
        Affinity: "Water";
        Control_Threshold: 1;
        Recycle: "Per_Scene";
        Complexity: "O(1)";
        Throughput: "3.8 kR/s";
    }

    PARAMETERS {
        Required_Moisture_L: 0.05;         /* 50 mililitros de vapor ambiental */
        Wound_Wetting_Angle_Deg: 0.0;       /* Superhidrofobicidad epidérmica nula */
        Gel_Viscosity_Cp: 140.0;            /* Consistencia viscoelástica no-newtoniana */
        Saline_Tonicity_Ppm: 9000.0;        /* 0.9% salinidad isotónica anti-lisis */
        Cosmetic_Hue_Hex: "#E0F7FA";        /* Tinte zafiro translúcido estético */
    }

    EXECUTE {
        /* 1. Condensación microscópica de humedad ambiental */
        Moisture = HydroGather.extract_ambient_moisture(
            origin=WoundTarget.Center,
            volume_liters=Required_Moisture_L
        );

        /* 2. Humectación perimetral completa sobre la herida */
        HydroCapillarity.set_contact_angle(
            fluid=Moisture,
            substrate=WoundTarget,
            angle_deg=Wound_Wetting_Angle_Deg
        );

        /* 3. Reordenamiento de enlaces para crear la membrana flexible */
        HydroDynamics.set_viscosity(
            fluid=Moisture,
            viscosity_cp=Gel_Viscosity_Cp
        );

        /* 4. Disolución de sales atmosféricas para alcanzar isotonía médica */
        HydroSolutes.dissolve_solute(
            fluid=Moisture,
            solute_type=MINERAL_SALTS,
            target_ppm=Saline_Tonicity_Ppm
        );

        /* 5. Inyección cosmética de refracción de Luna */
        Optics.tint_fluid(
            fluid=Moisture,
            hue_hex=Cosmetic_Hue_Hex,
            opacity=0.35
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            /* Disipación inocua como vaho templado en caso de error de cálculo */
            SafeVent.shunt_fluid_to_air(fluid=Moisture);
            SafeAbort.abort_execution();
    }
}
```

---

## 🎲 4. Implementación en FATE Básico

* **Nombre de la Proeza:** *S.C.M.E.H. Apósito Hidrostático [Rango C]*
* **Requisito de Activación:** `[✨] Control` a **Mediocre (+1)** o superior.
* **Acciones Permitidas:**
  1. **Tratamiento de Consecuencias Leves (`[2]`):** Permite realizar una tirada de `[✨] Control` o `Investigar` con dificultad **Normal (+1)** para iniciar la recuperación de una **Consecuencia Leve física** (como *«Corte superficial en el brazo»* o *«Quemadura leve por esquirla»*), renombrándola a su estado de alivio (ej. *«Herida vendada con apósito»*).
  2. **Eliminar Aspectos de Situación Menores:** Cierra sangrados cosméticos o elimina desventajas como `[Sangre en los Ojos]` o `[Polvo y Lodo en Herida]`.
* **Límite Estricto de Sistema:**
  * **Incapaz contra heridas reales:** No tiene efecto alguno sobre **Consecuencias Moderadas `[4]`** ni **Graves `[6]`**.
  * **Sin Afinidad:** Al no poseer Luna la afinidad elemental de Agua (su elemento es Fuego), no obtiene aumentos de duración ni invocaciones gratuitas adicionales. Es un remiendo puramente funcional de trámite escolar.

---

## 🔗 5. Referencias Cruzadas del Sistema
* 📋 Ficha de Operadora: [[Luna_Evergarden_Ficha_Fate]]
* 🎭 Compendio Maestro de Luna: [[MOC - Compendio de Arte de Autoria Personal|C.A.A.P.]]
* 📚 Secuencia Base de la Federación: [[Secuencia - Parche de Coagulacion Hidrostatica]]
* 🦊 Catalizador Activo: [[Artefacto - Little Fox]]
