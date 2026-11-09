---
title: "Secuencia - Micro-Sinterización de Grietas"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Tierra"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/tierra
  - ingenieria/reparacion
  - objeto
  - fate/proeza
aliases:
  - Micro-Sinterización
  - Reparar Fisuras
  - Sinterización Rúnica
  - Secuencia Micro-Sinterización de Grietas
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 🛠️ Secuencia: Micro-Sinterización de Grietas (Rango C)

> *"Los artesanos arcaicos martillaban el hierro durante horas para soldar una fisura. Un Especialista enfoca una micro-resonancia de red atómica a lo largo de la grieta y las moléculas de acero o silicato se fusionan de nuevo en cinco segundos sin fragilizar el chasis."*
> — Compendio del Gremio de [[Ingenieros y Alquimistas]]

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Micro-Sinterización de Grietas (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Cohesión Litológica y Soldadura Molecular
================================================================
Afinidad:    Tierra (o Neutro)
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       3.5 kR/s

Acción:
Aplica excitación térmica focalizada y reorganización de red mineral 
a lo largo de fracturas o fisuras en objetos inorgánicos (metal, piedra, 
vidrio, polímero), soldando el material a nivel molecular.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

La **Micro-Sinterización de Grietas** es una herramienta esencial para ingenieros de campo, armeros y Especialistas que operan con hardware rúnico bajo desgaste extremo. Repara daños mecánicos antes de que una fisura provoque el colapso catastrófico de un arma, catalizador o blindaje.

### Principios de Sinterización y Recompactación Litológica
1. **Detección de Planos de Corte (`GeoLattice.densify_mineral`):** El catalizador escanea la microgeometría de la fisura en un objeto inorgánico de hasta 50 kg de masa.
2. **Soldadura Molecular por Excitación:** Eleva la temperatura molecular estrictamente en el plano de interfaz fracturado mientras induce una fuerza de cohesión atómica que reorganiza la red cristalina de metales o silicatos, eliminando la discontinuidad estructural sin alterar las propiedades templadas del material circundante.
3. **Límites de Operación:** Repara fisuras, grietas o roturas limpias. No regenera material faltante pulverizado ni tiene efecto alguno sobre tejidos biológicos vivos.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Earth.Lattice AS GeoLattice;
IMPORT RuneScript.Elements.Fire.Thermal AS PyroThermal;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE MicroSinterizacion(TargetObject: Object) {
    HEADER {
        Rank: "C";
        Affinity: "Earth";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "3.5 kR/s";
    }

    PARAMETERS {
        Max_Fault_Length_Cm: 30.0;
        Bonding_Temp_C: 280.0;
        Lattice_Compaction_Ratio: 1.8;
    }

    EXECUTE {
        PyroThermal.excite_molecules(
            target_zone=TargetObject.FractureLine,
            temp_celsius=Bonding_Temp_C
        );

        GeoLattice.densify_mineral(
            stone_target=TargetObject.FractureLine,
            density_ratio=Lattice_Compaction_Ratio
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=TargetObject.FractureLine);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Micro-Sinterización de Grietas [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Superar Obstáculos (con `[✨] Control`):** Reparar en el acto un objeto de equipo dañado con consecuencias como `[Cañón Fisurado]`, `[Chasis Agrietado]` o `[Blindaje Abollado]`, eliminando el aspecto negativo sin necesidad de un taller metalúrgico.
  2. **Crear una Ventaja (con `[✨] Control`):** Reforzar preventivamente la integridad de un cerrojo, mamparo o puente de piedra colocando el aspecto **`[Estructura Sinterizada y Reforzada]`** con 1 invocación gratuita.
* **Bonificador por Afinidad Elemental (Tierra):**
  * Si el Especialista tiene afinidad con **Tierra**, el tiempo de reparación se reduce a una sola acción de combate rápido.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Ingenieros y Alquimistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
