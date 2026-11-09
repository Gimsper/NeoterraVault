---
title: "Secuencia - Mandoble de Plasma Confinado"
type: objeto
categoria: magia/secuencia
rango: "B"
afinidad: "Fuego"
control_requerido: 2
tags:
  - magia/secuencia
  - rango/b
  - afinidad/fuego
  - combate/filo_pesado
  - objeto
  - fate/proeza
aliases:
  - Mandoble de Plasma
  - Filo Térmico Pesado
  - Espada de Plasma Militar
  - Secuencia Mandoble de Plasma Confinado
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 🔥 Secuencia: Mandoble de Plasma Confinado (Rango B)

> *"Una daga de plasma de Rango C corta cerrojos y cuerdas. Este mandoble de un metro y diez centímetros, alimentado a treinta y ocho kilo-runas por segundo y mantenido por un solenoide magnético continuo a casi cuatro mil grados, corta por la mitad el blindaje frontal de un vehículo blindado ligero de un solo tajo descendente."*
> — Mariscal Korbin Vane, División Blindada de Vulcan Arms

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Mandoble de Plasma Confinado (Rango B)
CLASIFICACIÓN: S.C.M.E.H. de Ionización Pesada y Confinamiento Solenoidal Activo
================================================================
Afinidad:    Fuego
Requisito:   [✨] Control (2)
Recarga:     Por Escena (duración 4 asaltos; enfriamiento forzado)
Complejidad: O(n) (bucle dinámico de auto-estabilización magnética)
Flujo:       38.5 kR/s

Acción:
Genera y contiene una hoja colosal de plasma denso de 1.10 m a 3,800 °C 
mediante un solenoide magnético activo de alta frecuencia, capaz de 
vaporizar aleaciones balísticas pesadas y atravesar blindajes reforzados.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

El **Mandoble de Plasma Confinado** es un arma de asalto pesado de grado militar diseñada para la neutralización de objetivos mecanizados, exoesqueletos y búnkeres de hormigón reforzado. A diferencia de las dagas ligeras de Rango C, la masa plasmática y la transferencia térmica requieren hardware de catalizador de Rango B con disipador asistido.

### Confinamiento Solenoidal Dinámico en Bucle $\mathcal{O}(n)$
Para sostener una columna de plasma de semejante masa sin dispersión explosiva ni quemar al portador, el sistema ejecuta un bucle activo de retroalimentación:

1. **Ionización Gaseosa de Alta Densidad (`PyroThermal.excite_molecules` & `PyroPlasma.ionize_gas`):** Eleva el gas atmosférico a 3,800 °C y fuerza un estado de ionización cuasi-completa, alcanzando una densidad energética de plasma tres órdenes de magnitud superior al filo de Rango C.
2. **Estabilización por Solenoide Activo (`ElectroMagnetics.induce_magnetic_solenoid`):** Un campo magnético helicoidal envuelve la hoja. Cuando el filo impacta contra blindaje denso (acero balístico, titanio o cerámica), el bucle $\mathcal{O}(n)$ detecta la deformación del plasma e incrementa instantáneamente los teslas del campo en la zona de cizallamiento para impedir el rebote o deflexión del arma.
3. **Penetración por Sublimación Adiabática:** La temperatura del núcleo supera el punto de ebullición del hierro y el plomo, desintegrando el material objetivo por gasificación instantánea y eliminando la resistencia mecánica del blindaje.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Fire.Thermal AS PyroThermal;
IMPORT RuneScript.Elements.Fire.Plasma AS PyroPlasma;
IMPORT RuneScript.Elements.Fire.Confinement AS PyroConfinement;
IMPORT RuneScript.Elements.Lightning.Magnetics AS ElectroMagnetics;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE MandoblePlasma(CatalystEmitter: Point, StrikeTarget: Entity) {
    HEADER {
        Rank: "B";
        Affinity: "Fire";
        Control_Threshold: 2;
        Recycle: "Per_Scene";
        Complexity: "O(n)";
        Throughput: "38.5 kR/s";
    }

    PARAMETERS {
        Blade_Length_M: 1.10;
        Blade_Width_M: 0.12;
        Core_Temp_Celsius: 3800.0;
        Field_Intensity_Tesla: 4.5;
        Active_Rounds: 4;
    }

    EXECUTE {
        ThermalCore = PyroThermal.excite_molecules(
            target_zone=CatalystEmitter,
            temp_celsius=Core_Temp_Celsius
        );

        DensePlasma = PyroPlasma.ionize_gas(
            gas_pocket=ThermalCore,
            energy_density=EXTREME
        );

        MagneticSheath = ElectroMagnetics.induce_magnetic_solenoid(
            axis_vector=Operator.PointingVector,
            radius_m=Blade_Width_M,
            field_tesla=Field_Intensity_Tesla
        );

        BladeEnvelope = PyroConfinement.bind_cylinder(
            energy_core=DensePlasma,
            length_m=Blade_Length_M,
            radius_m=Blade_Width_M
        );

        FOR EACH Slice IN BladeEnvelope.Segments {
            PyroConfinement.compress(
                envelope=Slice,
                factor=2.4
            );
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=CatalystEmitter);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Mandoble de Plasma Confinado [Rango B]*
* **Requisito de Activación:** Tener `[✨] Control` a **Regular (+2)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto de Rango B]].
* **Acciones Permitidas:**
  1. **Atacar (con `[✨] Control`):** Atacar en combate cuerpo a cuerpo infligiendo un devastador daño de **Arma: 4**. Anula por completo cualquier blindaje de armadura física ligera o media; contra blindajes pesados de vehículos o fortificaciones, reduce su blindaje a la mitad.
  2. **Superar Obstáculos (con `[✨] Control`):** Partir mamparos blindados de acorazados, portones de aleación reforzada o columnas de soporte estructural en un único asalto.
* **Bonificador por Afinidad Elemental (Fuego):**
  * Si el Especialista tiene afinidad con **Fuego**, la duración se extiende a **6 asaltos** y genera el aspecto de escena **`[Zona Incandescente y Metales Fundidos]`** con 1 invocación gratuita en caso de impacto con estilo.
* **Margen de Fallo:**
  * Si se falla con un margen de -3, el solenoide magnético no puede confinar la sobretensión térmica, provocando un retroceso calórico que inflige 2 casillas de estrés físico al operador y quema el fusible de la ranura del artefacto por el resto de la escena.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango B]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Secuencia - Daga de Plasma Confinada]]
* [[Calculo de Rangos SCMEH - Big-O y Flujo]]
* [[Reglas FATE - Sistema de Magia Artificial]]
