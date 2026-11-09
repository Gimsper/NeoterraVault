---
title: "Secuencia - Dardo Neumático"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Aire"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/aire
  - objeto
  - fate/proeza
aliases:
  - Dardo Neumático
  - Vórtice Toroidal de Impacto
  - Proyectil de Aire
  - Secuencia Dardo Neumático
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 🌪️ Secuencia: Dardo Neumático (Rango C)

> *"Cualquiera que intente lanzar una masa de aire comprimido verá cómo se disipa en dos metros como un soplido inútil. Si quieres que el aire golpee como un puño de madera a quince metros, tienes que moldearlo en un anillo de vórtice toroidal: la rotación poloidal viaja sin rozamiento hasta reventar contra la nuca del centinela."*
> — Principios de Balística Barométrica, Academia Militar de Aegis

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Dardo Neumático (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Vórtice Toroidal y Presión de Estancamiento
================================================================
Afinidad:    Aire
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       6.0 kR/s

Acción:
Comprime aire ambiental y le imprime momento angular poloidal para 
formar un anillo de vórtice toroidal autosostenido. Viaja a 95 km/h 
sin disipación atmosférica y descarga 120 N de impacto cinético puro.
================================================================
```

---

## 2. Descripción Operativa y Física de Vórtice

El **Dardo Neumático** es la principal secuencia cinética de instrucción de la infantería de la Federación. A diferencia de las armas de fuego convencionales, no produce casquillos, no genera calor detectable y utiliza la propia atmósfera como cargador de munición infinita.

### Principio de Vorticidad Toroidal y Presión de Estancamiento
A fin de evitar la dispersión por rozamiento atmosférico a lo largo de su trayectoria, el algoritmo estructura la masa de gas según los principios de la dinámica de solitones:

1. **Compresión Gaseosa Inicial (`AeroDensity.compress_gas`):** Condensa un volumen de $0.05\text{ m³}$ de aire ambiental en un núcleo denso con ratio de compresión $4.5:1$.
2. **Generación de Momento Angular Toroidal (`AeroGas.create_vortex_ring`):** En lugar de empujarlo simplemente en línea recta, el catalizador le imprime una circulación de vorticidad poloidal ($\Gamma = 18.5\text{ m}^2/\text{s}$). El aire gira sobre sí mismo en forma de anillo (similar a un toroide o anillo de humo denso). Las capas exteriores que giran inducen una baja presión relativa que "succiona" y confina la masa interior, impidiendo el rozamiento con la atmósfera circundante.
3. **Impulso Balístico Direccional (`KineticVector.apply_impulse`):** Proyecta el toroide en la línea de mira a una velocidad inicial de $26\text{ m/s}$ ($95\text{ km/h}$).
4. **Descarga de Presión de Estancamiento (`Triggers.OnCollision`):** Al impactar contra un sólido (una persona, un cristal o un interruptor), la rotación colapsa bruscamente. Toda la energía cinética del vórtice se convierte instantáneamente en **presión de estancamiento**, liberando un golpe seco concentrado de $120\text{ Newtons}$ en un área circular de 8 cm.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python

IMPORT RuneScript.Elements.Air.Density AS AeroDensity;
IMPORT RuneScript.Elements.Air.GasFlow AS AeroGas;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Triggers.Collision AS Triggers;
IMPORT RuneScript.Safety.Vent AS SafeVent;

SEQUENCE DardoNeumatico(Target: Entity) {
    HEADER {
        Rank: "C";
        Affinity: "Air";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "6.0 kR/s";
    }

    PARAMETERS {
        Base_Air_Volume_M3: 0.05;
        Toroid_Radius_M: 0.04;
        Circulation_Gamma: 18.5;
        Impact_Force_N: 120.0;
        Max_Range_M: 15.0;
    }

    EXECUTE {
        GasPocket = AeroDensity.compress_gas(
            volume_m3=Base_Air_Volume_M3,
            ratio=4.5
        );

        AimVector = KineticVector.calculate_line(
            from_point=Operator.Hand,
            to_point=Target.CenterOfMass
        );

        VortexRing = AeroGas.create_vortex_ring(
            origin=Operator.Hand,
            vector=AimVector,
            core_radius_m=Toroid_Radius_M,
            circulation_gamma=Circulation_Gamma
        );

        KineticVector.apply_impulse(
            target=VortexRing,
            vector=AimVector,
            force_newtons=Impact_Force_N
        );

        Triggers.OnCollision(target=VortexRing) {
            AeroDensity.expand_gas(
                gas_pocket=VortexRing,
                expansion_rate=12.0
            );
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeVent.shunt_heat_to_atmosphere(joules=180.0);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Dardo Neumático [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Atacar (con `[✨] Control`):** Ataque balístico a distancia (hasta 15 metros). Inflige daño de estrés físico no letal.
  2. **Crear una Ventaja (con `[✨] Control`):** Colocar aspectos situacionales con 1 invocación gratuita como:
     * `[Puntería Enemiga Desestabilizada]`
     * `[Interruptor de Alarma Accionado a Distancia]`
     * `[Linterna del Centinela Pulverizada]`
  3. **Superar Obstáculos (con `[✨] Control`):** Quebrar cristales delgados, hacer caer escaleras plegables o abollar cerraduras ligeras sin acercarse al objetivo.
* **Bonificador por Afinidad Elemental (Aire):**
  * Si el Especialista tiene afinidad nativa con **Aire**, el alcance efectivo aumenta a **30 metros** y el impacto gana suficiente masa para derribar a un oponente si la tirada tiene éxito con estilo.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Secuencia - Levitar]]
* [[Reglas FATE - Sistema de Magia Artificial]]
