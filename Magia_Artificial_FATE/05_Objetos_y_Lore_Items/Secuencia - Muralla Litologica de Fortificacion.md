---
title: "Secuencia - Muralla Litológica de Fortificación"
type: objeto
categoria: magia/secuencia
rango: "B"
afinidad: "Tierra"
control_requerido: 2
tags:
  - magia/secuencia
  - rango/b
  - afinidad/tierra
  - defensa/fortificacion
  - objeto
  - fate/proeza
aliases:
  - Muralla Litológica
  - Muro de Fortificación
  - Muralla Megalítica Rúnica
  - Secuencia Muralla Litológica de Fortificación
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# ⛰️ Secuencia: Muralla Litológica de Fortificación (Rango B)

> *"Un parapeto de Rango C te cubre las rodillas de un fusilero suelto. Cuando la artillería enemiga empieza a saturar la posición con proyectiles explosivos de cien milímetros, ejecutas esta secuencia: el suelo se parte en dos y cinco toneladas de granito sinterizado se alzan dos metros y medio frente a toda tu escuadra."*
> — Comandante Varek Stone, Zapadores de Asedio de la Guardia

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Muralla Litológica de Fortificación (Rango B)
CLASIFICACIÓN: S.C.M.E.H. de Alzamiento Megalítico y Sinterización Cúbica
================================================================
Afinidad:    Tierra
Requisito:   [✨] Control (2)
Recarga:     1 Asalto (cooldown mecánico de disipación de tensión)
Complejidad: O(n) (sinterización iterativa de microfracturas por volumen)
Flujo:       42.0 kR/s

Acción:
Cizalla, eleva y densifica un monolito de roca y hormigón de 2.5 m de alto, 
3.0 m de ancho y 30 cm de grosor (~5.4 toneladas) en 0.8 segundos, 
brindando cobertura total de escuadra y absorbiendo fuego de artillería.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

La **Muralla Litológica de Fortificación** es el estándar de ingeniería militar pesada para la protección de destacamentos bajo fuego concentrado. Transforma la litosfera local en una fortificación abaluartada con resistencia balística equivalente a búnkeres permanentes.

### Sinterización Cúbica Volumétrica en $\mathcal{O}(n)$
Para que 5.4 toneladas de roca no colapsen por su propio peso ni se fracturen ante impactos de cañón, el algoritmo procesa el sustrato mediante un barrido volumétrico continuo:

1. **Fractura Litológica Profunda (`GeoLattice.cleave_fault`):** Introduce una red de cizalla a 1.2 metros bajo el nivel del suelo, aislando un bloque monolítico de $2.25	ext{ m}^3$ de roca o sustrato mineral consolidado.
2. **Elevación Hidrostática-Piezoeléctrica (`KineticVector.apply_linear_acceleration`):** Eyecta verticalmente el monolito a 2.5 metros de altura en menos de un segundo, anclando sus raíces en el lecho rocoso profundo.
3. **Sinterización y Compactación Iterativa (`GeoLattice.densify_mineral` & `GeoGranular.recompact_soil`):** Mediante un bucle $\mathcal{O}(n)$ que itera por cada capa geométrica del bloque, elimina porosidades microscópicas, funde las fisuras internas y compacta el balasto circundante, otorgando al muro una integridad estructural impenetrable contra armamento de infantería.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Earth.Lattice AS GeoLattice;
IMPORT RuneScript.Elements.Earth.Granular AS GeoGranular;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE MurallaLitologica(AnchorPoint: Point) {
    HEADER {
        Rank: "B";
        Affinity: "Earth";
        Control_Threshold: 2;
        Recycle: "Per_Round";
        Complexity: "O(n)";
        Throughput: "42.0 kR/s";
    }

    PARAMETERS {
        Wall_Height_M: 2.5;
        Wall_Width_M: 3.0;
        Wall_Thickness_M: 0.30;
        Lift_Time_Sec: 0.80;
        Target_Density_Ratio: 1.85;
    }

    EXECUTE {
        BedrockFault = GeoLattice.cleave_fault(
            plane_vector=Vector3(1, 0, 0),
            stress_joules=95000.0
        );

        KineticVector.apply_linear_acceleration(
            target=BedrockFault,
            vector=Vector3(0, 1, 0),
            distance_m=Wall_Height_M
        );

        GeoGranular.recompact_soil(
            ground_area=BedrockFault
        );

        FOR EACH Layer IN BedrockFault.VolumetricLayers {
            GeoLattice.densify_mineral(
                stone_target=Layer,
                density_ratio=Target_Density_Ratio
            );
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=AnchorPoint);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Muralla Litológica de Fortificación [Rango B]*
* **Requisito de Activación:** Tener `[✨] Control` a **Regular (+2)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto de Rango B]].
* **Acciones Permitidas:**
  1. **Crear una Ventaja (con `[✨] Control`):** Colocar el aspecto de escena **`[Muralla Megalítica de Fortificación]`** con 2 invocaciones gratuitas, protegiendo a todos los aliados situados en la misma zona con cobertura total (+3 a Defender contra ataques a distancia).
  2. **Bloquear Zonas (con `[✨] Control`):** Sellar completamente pasillos, puertas de hangar o accesos urbanos, impidiendo el paso de infantería o vehículos hasta que la muralla sea físicamente demolida.
* **Capacidad de Absorción de Daño:**
  * La muralla posee un medidor de estrés estructural independiente de **6 casillas de estrés**. Absorbe impactos de artillería, explosiones y proyectiles pesados en lugar de los personajes.
* **Bonificador por Afinidad Elemental (Tierra):**
  * Si el Especialista tiene afinidad con **Tierra**, el medidor aumenta a **8 casillas de estrés**, y la muralla repara automáticamente 1 casilla de estrés por asalto si permanece conectada a roca viva o lecho geológico continuo.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango B]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Secuencia - Cresta Litologica de Parapeto]]
* [[Calculo de Rangos SCMEH - Big-O y Flujo]]
* [[Reglas FATE - Sistema de Magia Artificial]]
