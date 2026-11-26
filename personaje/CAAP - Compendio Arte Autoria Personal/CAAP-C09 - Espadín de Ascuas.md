---
title: "Secuencia - Espadín de Ascuas"
type: secuencia_hechizo
categoria: personaje/hechizos_propietarios
propietario: Luna Evergarden
id_caap: "CAAP-C09"
rango: "C"
afinidad: "Pyro (RuneScript.Elements.Fire)"
catalizador_recomendado: "Little Fox (Kitsune Micro-Arcana)"
complejidad_algoritmica: "O(1)"
flujo_biomagico: "7.5 kR/s"
umbral_control: 1
tags:
  - personaje/luna_evergarden
  - hechizo/rango_c
  - afinidad/fire
  - runescript/secuencia
  - caap/acto_1
  - combate/filo_termico
  - esgrima_escenica
aliases:
  - Espadín de Ascuas
  - EspadinDeAscuas
  - Espadín de Ascuas Rubí
  - Espada de Plasma Rubí
  - CAAP-C09
status: operativo_refinado
created: 2026-11-10
updated: 2026-11-10
---
_El terminal muestra una simulación tridimensional: una hoja esbelta de sesenta y cinco centímetros que oscila entre un rubí sangre y un blanco de plasma cegador, desprendiendo pétalos de ascuas en cada arco de corte._ %%¿Quién demonios en Vulcan Arms tuvo el chispazo de genialidad para concebir plasma portátil y luego fue tan cobarde como para recortarlo a una vulgar navajita de veinticinco centímetros? Tranquilos, caballeros de la Federación: Luna Evergarden ha venido a reparar su falta de ambición.%%

# 🗡️🎭 CAAP-C09: Espadín de Ascuas
### *Variación Virtuosa de Esgrima Térmica, Confinamiento Ahusado y Cromaticidad Espectral*
**ID Oficial de Registro:** `SEC-C-PYRO-4112-LUNA-BLADE`  
**Clasificación:** Rango C (Combate Cerrado de Precisión / Modificación Propietaria)  
**Complejidad:** $\mathcal{O}(1)$ | **Flujo Promedio:** $7.5\text{ kR/s}$  
**Atribución de Arquitectura Base:** Inspirada y reconstruida sobre el módulo oficial [[Secuencia - Daga de Plasma Confinada|Daga de Plasma Confinada (Vulcan Arms / Estándar S.C.M.E.H. Rango C)]].

> *"Admito mi asombro: cuando revisaba el índice de dotación reglamentaria de la Academia, esperaba manuales para cavar letrinas y encender fogatas con chispitas grises. Y de pronto, escondida entre expedientes de intendencia, veo la ficha de la Daga de Plasma. Casi se me cae el Little Fox de la impresión. ¿La Academia aprobando un filo de plasma en la muñeca? ¡Un auténtico milagro entre tanta mediocridad! Claro que, siendo la Federación, tenían que arruinarlo haciéndola corta, tosca y sin una pizca de gracia. Así que tomé su fórmula... y le di alma."*  
> — **Luna Evergarden**, notas de ingeniería estética en KMA-OS.

---

## 🌹 1. La Crítica de Luna: *"El Milagro que Vulcan Arms Dejó a Medias"*

Tengo que ser justa con el gremio de ingenieros de *Vulcan Arms*: la base de [[Secuencia - Daga de Plasma Confinada|su daga]] es sólida como una roca. La idea de generar una botella diamagnética tubular que aísle la muñeca del operador mientras comprime gas ionizado a $1.200\text{ }^\circ\text{C}$ es francamente brillante. 

**Pero su sentido estético merece un consejo de guerra.**

¿Una hoja de apenas veinticinco centímetros? ¿Para qué? ¿Para cortar latas de ración en el barro o amenazar a reclutas desarmados en una esquina? Si un adversario se te acerca con una bayoneta larga o las fauces de un engendro se abren sobre ti, esos veinticinco centímetros te obligan a pelear a distancia de escupitajo. Además, visualmente parecía un soplete ancho de fontanero: una espada monocromático amarillo sucio, ruidoso y sin filo diferenciado.

Decidí que no iba a plagiar su trabajo; iba a **hacerles el favor de graduarlo con honores artísticos**:

1. **De Navaja de Trinchera a Espadín de Esgrima ($0.65\text{ m}$):** Extendí la botella de confinamiento longitudinal hasta los 65 centímetros con un perfil lanceolado de doble filo, ahusado desde la base hasta una punta de aguja. No es un mandoble pesado de Rango B que fundiría la batería de mi *Little Fox* en tres segundos; es un florete ágil, veloz y con alcance suficiente para mantener a los idiotas fuera de mi espacio personal.
2. **Cromaticidad Espectral y Gradiente Rubí:** La magia sin belleza es simple combustión química. Introduje la librería `RuneScript.Sensory.Optics` para inyectar un gradiente térmico: el alma central del espadín palpita en un carmesí rubí denso (`#9B111E`), mientras que el filo laminar de corte se acelera a una ionización de plasma blanco puro ($1.780\text{ K}$).
3. **Estela Escénica de Ascuas Suspendidas:** En cada finta o estocada, el confinamiento deja escapar un velo calculado de micro-ascuas suspendidas que trazan el arco del corte en el aire durante un cuarto de segundo. Intimidación psicológica pura: nadie quiere acercarse a una hoja que dibuja constelaciones de fuego a su paso.
4. **Cazoleta Floral de Confinamiento:** Modulé la base de la empuñadura para que el campo diamagnético no sea un anillo plano, sino una corola de pétalos ígneos que protege los nudillos como la guarnición de un estoque clásico.

---

## 🔬 2. El Truco Termodinámico: *Calor Extra Gratis por Compresión Adiabática*

¿Cómo es posible alargar la hoja a más del doble sin requerir un reactor de Rango B ni hacer que el *Little Fox* me calcine el brazo entero? 

Los ingenieros de la Federación trataron el plasma como agua en una manguera de jardín. **Grave error: el plasma es gas ionizado, y los gases obedecen la termodinámica molecular.**

* **Conservación de Masa Gaseosa:** La daga reglamentaria es gordo y tosco ($0.25\text{ m} \times 0.02\text{ m}$ de radio), con un volumen de gas de ~$0.31\text{ litros}$. Mi espadín mide $0.65\text{ m}$, pero tiene una silueta cónica ahusada ultra-esbelta (radio base de solo $0.016\text{ m}$ afinándose a una punta de aguja de $0.003\text{ m}$). ¿El volumen total resultante? ¡Apenas ~$0.21\text{ litros}$! Es decir, **contiene un 30% menos de volumen gaseoso que la navajita de la Academia.**
* **Compresión Adiabática Extrema (`Compression_Factor: 2.4`):** Al tomar esa misma masa de gas base a $1.200\ ^\circ\text{C}$ e inyectarla en un espacio geométricamente más estrecho y comprimido, la energía cinética molecular se dispara por pura física de confinamiento magnético:
  * El **núcleo** salta naturalmente de $1.200\ ^\circ\text{C}$ a **$1.320\ ^\circ\text{C}$**, logrando ese rojo rubí denso sin pedirle un solo julio extra a la batería.
  * El **bisel laminar exterior** (el filo de corte comprimido al grosor de micras) se comprime con tanta ferocidad que su temperatura salta a **$1.780\text{ K}$ ($1.507\ ^\circ\text{C}$)**.
  * Según la física de radiación de cuerpo negro, $1.780\text{ K}$ es el umbral exacto donde el plasma entra en incandescencia **blanco puro / magnesio**. Corta con una ferocidad molecular limpia y deslumbrante, todo mientras el flujo biomágico se mantiene en unos prudentes y seguros **$7.5\text{ kR/s}$**.

%%En resumen: más alcance, más filo, un degradado visual bellísimo y cero riesgo de quemadura dérmica en mis manos. A eso le llamo optimización virtuosa.%%

---

## ⚖️ 3. Tabla Comparativa: De la Dotación a la Virtuosa

| Parámetro Operativo | [[Secuencia - Daga de Plasma Confinada\|Daga Oficial (Vulcan Arms)]] | **Espadín de Ascuas (CAAP-C09)** | Criterio de Modificación de Luna |
| :--- | :---: | :---: | :--- |
| **Longitud de Hoja** | $0.25\text{ m}$ (Daga corta) | **$0.65\text{ m}$ (Espadín ahusado)** | Alcance táctico real sin sacrificar ligereza ni entrar en zona de mordida. |
| **Perfil Geométrico** | Cilindro tosco sin bisel | **Cono truncado ahusado con filo biselado** | Menor volumen total de gas que la daga, reduciendo el arrastre inercial. |
| **Temperatura Núcleo** | $1.200\ ^\circ\text{C}$ (Plano) | **$1.320\ ^\circ\text{C}$** | Calor ganado gratis por compresión adiabática ($\Delta T \approx +120\ ^\circ\text{C}$). |
| **Temperatura Filo** | $1.200\ ^\circ\text{C}$ | **$1.780\text{ K}$ ($1.507\ ^\circ\text{C}$)** | Incandescencia blanco de plasma en el borde de corte sin exigir Rango B. |
| **Flujo Bio-Mágico** | $7.2\text{ kR/s}$ | **$7.5\text{ kR/s}$** | Carga térmica segura, muy por debajo del límite del *FoxCore*. |
| **Cromática Visual** | Fogonazo plano amarillo | **Gradiente Rubí $\rightarrow$ Blanco Magnesio** | Elegancia teatral. El filo corta mejor porque está más comprimido. |
| **Efecto de Movimiento** | Silbido estéril | **Estela de ascuas suspendidas ($0.25\text{ s}$)** | Marca la trayectoria de combate con una firma estética inconfundible. |
| **Protección de Mano** | Anillo plano de baquelita | **Cazoleta diamagnética en corola floral** | Seguridad activa para los nudillos sin cargar una guarda de acero pesada. |
| **Créditos y Origen** | Manual Reglamentario de Infantería | **Inspirada en Vulcan Arms / Modificada por Luna** | Reconocimiento a la base técnica original: el buen arte sabe de dónde viene. |

---

## 🎛️ 4. Ficha Técnica Oficial (S.C.M.E.H.)

```
================================================================================
FICHA TÉCNICA: ESPADÍN DE ASCUAS (CAAP-C09)
================================================================================
RANGO FEDERACIÓN : Rango C (Combate Cerrado / Esgrima Térmica de Precisión)
AFINIDAD         : Fuego / Térmico (RuneScript.Elements.Fire)
COMPLEJIDAD      : O(1) - Volumen gaseoso acotado con compresión adiabática
FLUJO BIO-MÁGICO : 7.5 kR/s (Óptimo, sostenido sin estrés de hardware)
UMBRAL CONTROL   : [🎛️] Control (1) — Mediocre (+1)
RECARGA / RECYCLE: Por Escena (Duración: 4 asaltos por Afinidad Pyro)
DIMENSIÓN HOJA   : Longitud: 0.65 m | Base: 0.016 m | Punta: 0.003 m | Cazoleta: 0.08 m
TEMPERATURA NÚCLEO: 1,320 °C (Carmesí Rubí denso por compresión)
TEMPERATURA FILO : 1,780 °K / 1,507 °C (Plasma Blanco Puro por compresión laminar)
DAÑO ESTIMADO    : Arma: 2 (Penetración térmica total de blindajes convencionales)
================================================================================
```

---

## 💻 5. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Fire.Thermal AS PyroThermal;
IMPORT RuneScript.Elements.Fire.Plasma AS PyroPlasma;
IMPORT RuneScript.Elements.Fire.Confinement AS PyroConfinement;
IMPORT RuneScript.Sensory.Optics AS Optics;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Safety.Abort AS SafeAbort;
IMPORT RuneScript.Safety.Vent AS SafeVent;

/* ============================================================================
 * SEC-C-PYRO-4112-LUNA-BLADE :: ESPADÍN DE ASCUAS
 * Basada en el protocolo base de Vulcan Arms (Secuencia Daga de Plasma Confinada)
 * Modificación cromática, compresión adiabática y balance por Luna Evergarden.
 * ============================================================================ */

SEQUENCE EspadinDeAscuas(EmitterHilt: Point) {
    HEADER {
        Rank: "C";
        Affinity: "Fire";
        Control_Threshold: 1;
        Recycle: "Per_Scene";
        Complexity: "O(1)";
        Throughput: "7.5 kR/s";
    }

    PARAMETERS {
        /* Dimensiones físicas de la hoja de esgrima estilizada */
        Blade_Length_M: 0.65;
        Blade_Base_Radius_M: 0.016;       /* Perfil fino para reducir volumen total de gas */
        Blade_Tip_Radius_M: 0.003;        /* Punta de aguja hipodérmica */
        Hilt_Guard_Radius_M: 0.08;

        /* Termodinámica: Base de 1.200 °C + Compresión adiabática */
        Core_Temp_Celsius: 1320.0;        /* +120 °C extra ganados por reducción de volumen */
        Edge_Temp_Kelvin: 1780.0;         /* 1.507 °C en filo laminar: Blanco Magnesio estricto */
        Color_Core_Hex: "#9B111E";        /* Rubí Profundo */
        Color_Edge_Hex: "#F8F8FF";        /* Blanco Plasma Incandescente */
        Chromatic_Dispersion_K: 450.0;

        /* Dinámica escénica y factor de compresión volumétrica */
        Trail_Persistence_Sec: 0.25;
        Compression_Factor: 2.4;          /* Compresión extrema para afilar el borde molecular */
    }

    EXECUTE {
        /* 1. Síntesis e ionización del núcleo térmico primario */
        ThermalCore = PyroThermal.excite_molecules(
            target_zone=EmitterHilt,
            temp_celsius=Core_Temp_Celsius
        );

        HighDensityPlasma = PyroPlasma.ionize_gas(
            gas_pocket=ThermalCore,
            energy_density=HIGH
        );

        /* 2. Modulación óptica: inyección de gradiente cromático rubí-blanco */
        Optics.apply_chromatic_gradient(
            plasma_body=HighDensityPlasma,
            core_color=Color_Core_Hex,
            edge_color=Color_Edge_Hex,
            dispersion=Chromatic_Dispersion_K
        );

        /* 3. Confinamiento cónico ahusado de 65 cm (Masa gaseosa acotada) */
        BladeEnvelope = PyroConfinement.bind_cone_truncated(
            energy_core=HighDensityPlasma,
            length_m=Blade_Length_M,
            base_radius_m=Blade_Base_Radius_M,
            tip_radius_m=Blade_Tip_Radius_M
        );

        /* Compresión adiabática para elevar la densidad energética en el filo */
        PyroConfinement.compress(
            envelope=BladeEnvelope,
            factor=Compression_Factor
        );

        /* 4. Proyección de la cazoleta floral de protección en la guarda */
        HiltGuard = PyroConfinement.bind_flanged_disc(
            anchor=EmitterHilt,
            radius_m=Hilt_Guard_Radius_M,
            insulation_factor=MAXIMUM
        );

        /* 5. Activación del rastro cinético de ascuas en suspensión */
        KineticVector.enable_motion_trail(
            source=BladeEnvelope,
            lifespan_sec=Trail_Persistence_Sec,
            particle_density=MEDIUM
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            /* Colapso axial instantáneo hacia la tobera y purga de calor */
            SafeAbort.collapse_confinement_inward(envelope=BladeEnvelope);
            SafeVent.shunt_heat_to_atmosphere(joules=350.0);
    }
}
```

---

## 🎲 6. Implementación en FATE Básico

* **Nombre de la Proeza:** *S.C.M.E.H. Espadín de Ascuas [Rango C]*
* **Requisito de Activación:** `[✨] Control` a **Mediocre (+1)** o superior, cargada en un slot del *Little Fox*.
* **Duración:** **4 Asaltos** completos (gracias a la Afinidad Pyro de Luna).
* **Acciones y Usos Tácticos:**
  1. **Ataque Cuerpo a Cuerpo con Sinergia de Linaje:**
     * Luna puede atacar usando `[✨] Control (+4)` o su habilidad física `Pelear (+3)`.
     * **¡Sinergia con *Sincronía de Linaje*!** Al blandirla combinada con tácticas de esgrima/trinchera aprendidas de su padre, obtiene un **bonificador adicional de +2**.
     * **Daño:** **Arma: 2**. El plasma funde armaduras balísticas ordinarias, cuero y corazas cerámicas sin resistencia.
  2. **Éxito con Estilo:** Si supera la defensa enemiga por 3 o más aumentos, además del daño masivo, coloca el aspecto de situación **`[En Llamas]`** o **`[Cercenado con Rubí]`** con una invocación gratuita.
  3. **Superar Obstáculos (Utilidad de Demolición Silenciosa):** Permite usar `[✨] Control` para cortar cerrojos acorazados, mamparas de hangar, barrotes de celdas o cables de alta tensión de un solo tajo limpio y sin el estrépito de un tiroteo.

---

## 🔗 7. Referencias Cruzadas del Sistema
* 📋 Ficha de Operadora: [[Luna_Evergarden_Ficha_Fate]]
* 🎭 Compendio Maestro de Luna: [[MOC - Compendio de Arte de Autoria Personal|C.A.A.P.]]
* 📚 Secuencia Original de Referencia: [[Secuencia - Daga de Plasma Confinada]]
* 🦊 Catalizador Activo: [[Artefacto - Little Fox]]
* ☄️ Secuencia Balística Hermana: [[CAAP-C06 - Cometa de Rubi]]
