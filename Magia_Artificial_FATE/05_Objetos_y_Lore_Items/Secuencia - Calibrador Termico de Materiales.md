---
title: "Secuencia - Calibrador Térmico de Materiales"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Fuego"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/fuego
  - afinidad/agua
  - objeto
  - fate/proeza
aliases:
  - Calibrador Térmico
  - Termómetro Rúnico
  - Bomba de Calor Adiabática
  - Secuencia Calibrador Térmico de Materiales
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 🌡️ Secuencia: Calibrador Térmico de Materiales (Rango C)

> *"Un buen herrero o cerrajero sabe que la temperatura cambia la física de cualquier aleación. Enfría un cerrojo a menos cuarenta y se rompe como cristal con un martillazo; calienta un rodamiento a trescientos grados y se dilata hasta bloquear el motor."*
> — Manual de Ingeniería Mecánica y Térmica, Vulcan Arms

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Calibrador Térmico de Materiales (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Bomba de Calor y Desplazamiento Adiabático
================================================================
Afinidad:    Fuego (o Agua)
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       4.0 kR/s

Acción:
Aplica transferencia térmica forzada sobre un objeto inorgánico de hasta 
20 kg, pudiendo elevar su temperatura hasta 350 °C o enfriarlo hasta 
-40 °C drenando su energía calórica hacia un disipador.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

El **Calibrador Térmico de Materiales** es una secuencia bidireccional utilizada en herrería táctica, sabotaje de maquinaria y manipulación de metales. A diferencia de las secuencias de combustión abierta, transfiere calor sin generar llamaradas.

### Principios de Modulación Térmica Bidireccional
1. **Modo Exotérmico (Calentamiento - Afinidad Fuego):** Utiliza `PyroThermal.excite_molecules` para acelerar la vibración atómica del cuerpo hasta 350 °C, provocando dilatación térmica de pernos, fusión de grasas lubricantes o carbonización de sellos de goma.
2. **Modo Endotérmico (Enfriamiento Criogénico - Afinidad Agua):** Utiliza `PyroThermal.absorb_heat` para extraer julios calóricos y derivarlos al aire circundante, congelando el objeto hasta -40 °C. En metales de bajo carbono y aleaciones comunes, esto induce **fragilización por baja temperatura** (transición dúctil-frágil), haciendo que un golpe seco fracture el material sin necesidad de herramientas pesadas.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Fire.Thermal AS PyroThermal;
IMPORT RuneScript.Geometry.Confinement AS Confinement;
IMPORT RuneScript.Safety.Vent AS SafeVent;

SEQUENCE CalibradorTermico(TargetObject: Object, Mode: String) {
    HEADER {
        Rank: "C";
        Affinity: "Fire";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "4.0 kR/s";
    }

    PARAMETERS {
        Max_Mass_Kg: 20.0;
        Hot_Target_Temp_C: 350.0;
        Cold_Target_Temp_C: -40.0;
    }

    EXECUTE {
        IF (Mode == "HEAT") {
            PyroThermal.excite_molecules(
                target_zone=TargetObject,
                temp_celsius=Hot_Target_Temp_C
            );
        } ELSE IF (Mode == "COOL") {
            PyroThermal.absorb_heat(
                source=TargetObject,
                sink=CHASSIS_HEAT_SINK,
                joules=4500.0
            );
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeVent.shunt_heat_to_atmosphere(joules=500.0);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Calibrador Térmico de Materiales [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Crear una Ventaja (con `[✨] Control`):** Colocar aspectos situacionales como **`[Cerradura Criogénicamente Quebradiza]`** (para fracturarla en la siguiente tirada) o **`[Engranajes Dilatados y Atascados]`** con 1 invocación gratuita.
  2. **Superar Obstáculos (con `[✨] Control`):** Manipular piezas mecánicas agarrotadas, encajar pernos dilatados o descongelar compuertas heladas en entornos árticos.
* **Bonificador por Afinidad Elemental:**
  * Afinidad **Fuego:** Permite calentar el objeto hasta 500 °C en la mitad de tiempo.
  * Afinidad **Agua:** Permite alcanzar -60 °C induciendo escarcha instantánea sobre superficies conductoras.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Corporaciones y Fabricantes de Neoterra]]
* [[Reglas FATE - Sistema de Magia Artificial]]
