---
title: "Secuencia - Placa de Escarcha Táctica"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Agua"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/agua
  - defensa/cobertura
  - objeto
  - fate/proeza
aliases:
  - Placa de Escarcha
  - Parapeto de Hielo Laminar
  - Escudo Criogénico Menor
  - Secuencia Placa de Escarcha Táctica
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 💧 Secuencia: Placa de Escarcha Táctica (Rango C)

> *"El hielo ordinario es una pésima cobertura balística: una bala de fusil lo estalla en mil esquirlas como si fuera vidrio de ventana. Si quieres detener plomo caliente, tienes que forzar la cristalización en láminas microscópicas cruzadas, igual que las capas de nácar de una ostra marina, y purgar el calor latente hacia el suelo para que no se funda a sí mismo al nacer."*
> — Manual de Fortificación Rápida, Frente del Norte

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Placa de Escarcha Táctica (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Cristalización Laminar y Cobertura Balística
================================================================
Afinidad:    Agua
Requisito:   [✨] Control (1)
Recarga:     Por Escena
Complejidad: O(1)
Flujo:       8.5 kR/s

Acción:
Condensa 15 litros de humedad atmosférica y los cristaliza en una 
matriz estratificada de microcapas de hielo hexagonal cruzado 
(5 cm de grosor), disipando el calor latente y resistiendo impactos.
================================================================
```

---

## 2. Descripción Operativa y Microestructura de Materiales

La **Placa de Escarcha Táctica** es una de las proezas defensivas más respetadas por las unidades de choque de la Federación. Permite crear un parapeto balístico desechable en fracciones de segundo en mitad de una calle o pasillo desprovisto de trincheras naturales.

### Principios de Estructuración Cristalina Laminar y Drenaje Térmico
A fin de evitar la fragmentación frágil por impacto y la degradación por calor latente, el código estructura el hielo mediante cristalografía compuesta:
El algoritmo estructura el hielo mediante **cristalografía compuesta**:

1. **Condensación Ulrarrápida (`HydroGather.extract_ambient_moisture`):** Recoge 15 litros de vapor atmosférico en 0.4 segundos y los confina en un plano vertical de $1.0\text{ m} \times 0.8\text{ m}$ por $50\text{ mm}$ de espesor (`Confinement.bind_sheet`).
2. **Cristalización Laminar Cruzada (`HydroPhase.crystallize_lamellar_matrix`):** En lugar de un solo bloque homogéneo, el código ordena las moléculas de agua en miles de microláminas hexagonales superpuestas de 50 micrómetros, alternando la orientación de sus ejes de corte. Cuando una bala penetra la primera capa, la grieta no puede continuar en línea recta: es desviada horizontalmente por la siguiente lámina, disipando la energía cinética del proyectil por fricción interna y deformación plástica sin quebrar la placa.
3. **Purga del Calor Latente (`SafeVent.shunt_heat_to_atmosphere`):** Durante la cristalización forzada, el artefacto drena los kilojulios térmicos liberados por el cambio de fase y los expulsa hacia el aire superior como una columna de vapor caliente, garantizando que el núcleo de la placa se mantenga subenfriado a $-25\text{ °C}$.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python

IMPORT RuneScript.Elements.Water.Gathering AS HydroGather;
IMPORT RuneScript.Elements.Water.Phase AS HydroPhase;
IMPORT RuneScript.Geometry.Confinement AS Confinement;
IMPORT RuneScript.Safety.Vent AS SafeVent;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE PlacaEscarcha(OriginPoint: Point) {
    HEADER {
        Rank: "C";
        Affinity: "Water";
        Control_Threshold: 1;
        Recycle: "Per_Scene";
        Complexity: "O(1)";
        Throughput: "8.5 kR/s";
    }

    PARAMETERS {
        Water_Volume_Liters: 15.0;
        Sheet_Width_M: 1.0;
        Sheet_Height_M: 0.8;
        Thickness_Mm: 50.0;
        Layer_Micro_M: 50.0;
        Core_Temperature_K: 248.0;
    }

    EXECUTE {
        Moisture = HydroGather.extract_ambient_moisture(
            origin=OriginPoint,
            volume_liters=Water_Volume_Liters
        );

        Sheet = Confinement.bind_sheet(
            target_core=Moisture,
            width_m=Sheet_Width_M,
            height_m=Sheet_Height_M,
            thickness_mm=Thickness_Mm
        );

        CompositeIce = HydroPhase.crystallize_lamellar_matrix(
            fluid=Sheet,
            layer_thickness_um=Layer_Micro_M,
            hardness_factor=4.5
        );

        SafeVent.shunt_heat_to_atmosphere(
            joules=5000.0
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            HydroPhase.sublimate_instant(fluid=Moisture);
            SafeAbort.collapse_confinement_inward(envelope=Moisture);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Placa de Escarcha Táctica [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Defender (con `[✨] Control`):** Otorga un bonificador de **+2 a la Defensa física** contra disparos de armas cortas, subfusiles o fragmentos de metralla en el arco frontal del Especialista.
  2. **Crear una Ventaja (con `[✨] Control`):** Colocar aspectos situacionales como **`[Parapeto Balístico de Hielo Laminar]`** o **`[Conducto de Ventilación Sellado por Escarcha]`** con 1 invocación gratuita. La placa resiste 2 intercambios de combate antes de sublimar.
* **Bonificador por Afinidad Elemental (Agua):**
  * Si el Especialista tiene afinidad con **Agua**, la placa resiste un asalto adicional de fuego concentrado y es inmune a ser derretida por llamas o granadas térmicas de baja temperatura.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
