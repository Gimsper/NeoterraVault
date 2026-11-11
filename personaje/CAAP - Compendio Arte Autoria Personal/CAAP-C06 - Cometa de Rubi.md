---
title: "Secuencia - Cometa de Rubí"
type: secuencia_hechizo
categoria: personaje/hechizos_propietarios
propietario: Luna Evergarden
id_caap: "CAAP-C06"
rango: "C"
afinidad: "Pyro (RuneScript.Elements.Fire)"
catalizador_recomendado: "Little Fox (Kitsune Micro-Arcana)"
complejidad_algoritmica: "O(1)"
flujo_biomagico: "6.7 kR/s"
umbral_control: 1
tags:
  - personaje/luna_evergarden
  - hechizo/rango_c
  - afinidad/fire
  - runescript/secuencia
  - caap/acto_1
  - arma_principal
aliases:
  - Cometa de Rubí
  - CometaDeRubi
  - CAAP-C06
status: operativo_favorito
created: 2026-11-09
updated: 2026-11-09
---
_El encabezado brilla con un marcador táctil dorado en la memoria rápida del Little Fox._ %%Mi consentida. Mi arma de cabecera. La prueba irrefutable de que podar código basura es tan artístico como esculpir una estatua.%%

# ☄️🎭 CAAP-C06: Cometa de Rubí
### *Secuencia Balística Refinada de Cadencia Continua y Confinamiento Esférico*
**ID Oficial de Registro:** `SEC-C-PYRO-4108-LUNA-CUSTOM`  
**Clasificación:** Rango C (Táctico Personal / Cadencia Sin Enfriamiento)  
**Complejidad:** $\mathcal{O}(1)$ | **Flujo Promedio:** $6.7\text{ kR/s}$

> *"Estaba tratando de conseguir un buen ataque, algo memorable 'Pues usa tu arma' dices? Vamos, no es muy elegante un simple balazo, quiero algo que merezca una frase épica. Además un arma no tiene la versatilidad del fuego. Fue ahí que mientras revisaba mis notas recordé mi tarea,  miré mi vieja tarea de la aguja y lo vi claro como el plasma necesitaba algo como esto. ¿Problema? el tiempo de recarga, Solución? Teatralmente perfecta"*  
> — **Luna Evergarden**, notas de optimización en KMA-OS.

---

## 💡 1. La Epifanía de Medianoche: *Matar el Enfriamiento*

Estaba sentada en el suelo del barracón, desplazando archivos viejos y bocetos en la pantalla de mi *Little Fox*. Hacía horas que no podía dormir. En mi cabeza no dejaba de repetirse la misma pesadilla táctica: **el maldito tiempo de recarga**.

La [[CAAP-C01 - Aguja de Plasma Rubi|Aguja de Plasma Rubí (CAAP-C01)]] tenía su encanto visual, sí, pero tenía un defecto letal que ningún profesor cobarde quiso admitir: `Recycle: "Cooldown_1_Round"`. En una escaramuza real, seis segundos de espera con las manos vacías no es «disciplina de tiro»; es una invitación formal para que un enemigo te parta el cráneo con una pala o un engendro te desgarre el pecho.

Miré las líneas de la aguja con ojo clínico y me llegó el chispazo. **¿Por qué demonios arrastraba tanto equipaje inútil?**
* ¿Para qué comprimir gas previamente con `AeroDensity` si puedo ionizar el bolsillo de aire inmediato?
* ¿Para qué quemar búfer calculando un gradiente térmico de $+1.100\text{ K}$ solo para que la punta se vea más brillante que la cola? Bueno... Si era necesario, dramáticamente obligatorio. Sinceramente de lo más difícil de quitar, una pena terrible.
* ¿Para qué forzar una combustión secundaria de superficie si un impacto cinético de plasma concentrado ya pulveriza lo que toca?

Agarré la tijera digital e hice una carnicería con los módulos. 

### ⚖️ La Cirugía Algorítmica: De la Aguja al Cometa

| Parámetro / Módulo      | [[CAAP-C01 - Aguja de Plasma Rubi\|Aguja de Rubí (CAAP-C01)]] |      **Cometa de Rubí (CAAP-C06)**      | Decisión de Luna                                                                                                                             |
| :---------------------- | :------------------------------------------------------------: | :-------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------- |
| **Recarga / Recycle**   |                `Cooldown_1_Round` *(¡Peligro!)*                |        **`Infinite` (Continuo)**        | **El gran objetivo.** Disparar asalto tras asalto sin que el Little Fox se queje.                                                            |
| **Flujo Bio-Mágico**    |                       $8.8\text{ kR/s}$                        |          **$6.7\text{ kR/s}$**          | Reducción del **24%** de carga térmica. La batería y los cristales lo agradecen.                                                             |
| **Geometría**           |     Cilindro largo ($0.30\text{ m} \times 0.008\text{ m}$)     | **Esfera pura ($r = 0.025\text{ m}$)**  | La esfera es la forma más estable del universo. Menos gasto de confinamiento. La punta brillante no murió en vano, se ve una esfera hermosa. |
| **Módulos podados**     |                `AeroDensity`, `PyroCombustion`                 |         *Eliminados sin piedad*         | Menos llamadas = ejecución instantánea en milisegundos.                                                                                      |
| **Control Temporal**    |                Ninguno (Deriva balística libre)                | **`Chronos.OnTimer` ($0.18\text{ s}$)** | Si no impacta en $0.18\text{ s}$, colapsa limpio. Cero calor residual flotando.                                                              |
| **Impulso Cinético**    |                        $55.0\text{ N}$                         |           **$80.0\text{ N}$**           | Un $45\%$ más veloz. Cruza los 5 metros como un chasquido.                                                                                   |
| **Derivación de Fallo** |                     $900.0\text{ Joules}$                      |        **$250.0\text{ Joules}$**        | Si fallo, apenas suelta un soplido tibio en vez de abrasarme los guantes.                                                                    |

Sacrifiqué artificios barrocos, pero gané supervivencia. El *Cometa de Rubí* es una esfera del tamaño de una ciruela, de un carmesí denso y perfecto, que viaja a velocidad de vértigo y estalla con un chasquido seco. Se ha convertido en mi fiel compañero de armas: mi ataque principal, mi escudo proactivo y la voz con la que respondo cuando la mediocridad intenta acorralarme.

---

## 🎛️ 2. Ficha Técnica Oficial (S.C.M.E.H.)

```
================================================================================
FICHA TÉCNICA: COMETA DE RUBÍ (CAAP-C06)
================================================================================
RANGO FEDERACIÓN : Rango C (Combate Táctico / Ataque Básico Continuo)
AFINIDAD         : Fuego / Térmico (RuneScript.Elements.Fire)
COMPLEJIDAD      : O(1) - Blanco unitario y geometría esférica invariable
FLUJO BIO-MÁGICO : 6.7 kR/s (Óptimo, sostenido sin estrés de hardware)
UMBRAL CONTROL   : [🎛️] Control (1) — Mediocre (+1)
RECARGA / RECYCLE: INFINITE (Sin cooldown entre asaltos consecutivos)
ALCANCE EFECTIVO : 5.0 metros (Alcance puntual optimizado por ventana Chronos)
GEOMETRÍA        : Esfera confinada de plasma homogéneo (Radio: 2.5 cm)
TIEMPO DE VUELO  : 0.18 segundos (Auto-colapso por timeout si hay fallo de blanco)
IMPULSO CINÉTICO : 80.0 Newtons
================================================================================
```

---

## 💻 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Fire.Thermal AS PyroThermal;
IMPORT RuneScript.Elements.Fire.Plasma AS PyroPlasma;
IMPORT RuneScript.Elements.Fire.Confinement AS PyroConfinement;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Triggers.Collision AS Collision;
IMPORT RuneScript.Triggers.Chronos AS Chronos;
IMPORT RuneScript.Core.Math AS Math;
IMPORT RuneScript.Safety.Abort AS SafeAbort;
IMPORT RuneScript.Safety.Vent AS SafeVent;

SEQUENCE CometaDeRubi(Target: Entity, LaunchPocket: GasPocket) {
    HEADER {
        Rank: "C";
        Affinity: "Fire";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "6.7 kR/s";
    }

    PARAMETERS {
        Max_Range_M: 5.0;
        Core_Temp_Celsius: 950.0;
        Radius_M: 0.025;
        Launch_Impulse_N: 80.0;
        Max_Flight_Time_Sec: Math.sqrt(Max_Range_M / 160.0);
    }

    EXECUTE {
        PyroThermal.excite_molecules(
            target_zone=LaunchPocket,
            temp_celsius=Core_Temp_Celsius
        );

        PlasmaCore = PyroPlasma.ionize_gas(
            gas_pocket=LaunchPocket,
            energy_density=HIGH
        );

        Comet = PyroConfinement.bind_sphere(
            energy_core=PlasmaCore,
            radius_m=Radius_M
        );

        IF (!PyroConfinement.is_stable(envelope=Comet)) {
            SafeAbort.collapse_confinement_inward(envelope=Comet);
            ABORT("Inestabilidad del proyectil");
        }

        Direction = KineticVector.calculate_line(
            from=Operator.Hand,
            to=Target.CenterOfMass
        );

        KineticVector.apply_impulse(
            target=Comet,
            vector=Direction,
            force_newtons=Launch_Impulse_N
        );

        Collision.OnCollision(target=Comet) {
            PyroConfinement.release(envelope=Comet);
        }

        Chronos.OnTimer(duration_seconds=Max_Flight_Time_Sec) {
            IF (PyroConfinement.is_stable(envelope=Comet)) {
                SafeAbort.collapse_confinement_inward(envelope=Comet);
            }
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=Comet);
            SafeVent.shunt_heat_to_atmosphere(joules=250.0);
    }
}
```

%%Fíjense en el trigger de Chronos... $0.18\text{ segundos}$. Si el blanco esquiva, el cometa no sigue de largo estrellándose contra el mobiliario como un idiota; la envoltura colapsa sobre sí misma en silencio. Limpieza quirúrgica.%%
%%Nota mental para cálculos cinéticos: la masa confinada de la esfera es de aprox. 0.25 kg. Con un impulso F = 80.0 N, la aceleración media es a = F/m = 320 m/s². De la ecuación cinemática d = (1/2)*a*t², despejamos t² = 2d/a = 2d/320 = d/160, dando t = Math.sqrt(d / 160.0). Para el rango máximo d = 5.0 m, t = Math.sqrt(5/160) = Math.sqrt(0.03125) ≈ 0.1768 s (~0.18 s). ¡Bendito sea importar RuneScript.Core.Math! Si tuviera que resolver raíces cuadradas flotantes a mano en medio de un tiroteo, preferiría pedirle un revólver prestado a la infantería común.%%

---

## 🎲 4. Implementación en FATE Básico (Proeza de Magia)

### Mecánica de Combate Continuo
* **Acción Principal:** **Atacar** a distancia corta (misma zona o adyacente, hasta 5 m).
* **Cadencia:** **Sin tiempo de reutilización**. Luna puede disparar el *Cometa de Rubí* todos los asaltos que desee sin sufrir estrés en su catalizador ni penalizaciones por calor acumulado.
* **Habilidad de Tirada:** `Disparar` o `Voluntad`.
* **Dificultad de Control:** `Mediocre (+1)`. Gracias a la afinidad **Pyro** (+2 pasivo de Luna), esta secuencia se compila prácticamente en piloto automático.

### Resultados de la Tirada
* **Fallo:** La rutina `Chronos.OnTimer` o `SafeAbort` desactiva la esfera a mitad de trayectoria. El plasma implosiona suavemente. No hay consecuencias negativas ni casillas de estrés para el catalizador.
* **Empate:** El cometa impacta en el blindaje o escudo del oponente sin penetrar del todo; inflige 1 casilla de estrés físico o le concede a Luna un impulso táctico como *«Presión Térmica Sostenida»*.
* **Éxito:** Impacto esférico pleno. El colapso del plasma a $950\text{ }^\circ\text{C}$ inflige daño de estrés físico estándar igual a las casillas de cambio generadas.
* **Éxito con Estilo:** La esfera golpea con precisión demoledora en un punto blando. Inflige el daño de éxito y Luna decide entre:
  * Generar un aspecto con invocación gratuita: **«Aturdimiento por Destello Rubí»** o **«Blindaje Resquebrajado»**.
  * O reducir 1 casillero de estrés para obtener un impulso inmediato en su siguiente acción.

---

## 🔗 5. Enlaces del Compendio

* 🎭 Índice Maestro: [[MOC - Compendio de Arte de Autoria Personal]]
* 🔴 Antecesora Académica: [[CAAP-C01 - Aguja de Plasma Rubi]]
* 🦊 Consola de Compilación: [[Artefacto - Little Fox]]
* 📋 Ficha de Operadora: [[Luna_Evergarden_Ficha_Fate]]
