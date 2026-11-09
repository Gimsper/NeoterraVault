---
title: "Secuencia - Daga de Plasma Confinada"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Fuego"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/fuego
  - combate/filo_termico
  - objeto
  - fate/proeza
aliases:
  - Daga de Plasma
  - Filo Térmico Confinado
  - Espada Flameante Ligera
  - Secuencia Daga de Plasma Confinada
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 🔥 Secuencia: Daga de Plasma Confinada (Rango C)

> *"Una hoja de acero se desafila, pesa y puede ser bloqueada por un blindaje cerámico. Una lámina de plasma de doce mil grados confinado a veinticinco centímetros de tu muñeca corta cerrojos de latón, cables blindados y chalecos de fibra sintética como si fueran mantequilla caliente."*
> — Especificaciones de Armamento Compacto, Vulcan Arms

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Daga de Plasma Confinada (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Ionización Térmica y Contención Cúspide
================================================================
Afinidad:    Fuego
Requisito:   [✨] Control (1)
Recarga:     Por Escena (duración base: 2 asaltos antes de disipación)
Complejidad: O(1)
Flujo:       7.2 kR/s

Acción:
Ioniza una columna de gas ambiental en un filo lanceolado de 25 cm 
a 1,200 °C, confinado en una botella magnética diamagnética rígida 
que aísla la empuñadura del operador y secciona materiales densos.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

La **Daga de Plasma Confinada** es el arma secundaria de combate cerrado por excelencia entre ingenieros de choque e infiltradores. A diferencia de las espadas arcanas pesadas de grado militar, esta secuencia genera un filo compacto calibrado para no derretir los circuitos del artefacto emisor.

### Ionización Gaseosa y Botella Magnética Diamagnética
El funcionamiento del filo térmico se basa en un equilibrio preciso entre ionización y contención:

1. **Excitación Molecular e Ionización (`PyroThermal.excite_molecules` & `PyroPlasma.ionize_gas`):** Extrae una columna cilíndrica de 25 centímetros de aire frente a la tobera de emisión y excita sus partículas hasta romper el equilibrio atómico, transformando el gas en plasma incandescente a 1,200 °C.
2. **Confinamiento Cilíndrico Rígido (`PyroConfinement.bind_cylinder`):** Modula una cáscara magnética tubular con sección en bisel afilado. El campo diamagnético repele el calor radiante hacia adentro, concentrando la energía en el borde de corte y permitiendo que la empuñadura permanezca fría al tacto sin requerir guantes de asbesto.
3. **Corte por Fusión y Sublimación:** Al entrar en contacto con materia sólida, el campo colapsa de forma microscópica en el punto de contacto exacto, transfiriendo calor inmediato que vaporiza polímeros, cuerdas y carne al instante.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Fire.Thermal AS PyroThermal;
IMPORT RuneScript.Elements.Fire.Plasma AS PyroPlasma;
IMPORT RuneScript.Elements.Fire.Confinement AS PyroConfinement;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE DagaPlasma(EmitterNode: Point) {
    HEADER {
        Rank: "C";
        Affinity: "Fire";
        Control_Threshold: 1;
        Recycle: "Per_Scene";
        Complexity: "O(1)";
        Throughput: "7.2 kR/s";
    }

    PARAMETERS {
        Blade_Length_M: 0.25;
        Blade_Radius_M: 0.02;
        Core_Temp_Celsius: 1200.0;
    }

    EXECUTE {
        ThermalCore = PyroThermal.excite_molecules(
            target_zone=EmitterNode,
            temp_celsius=Core_Temp_Celsius
        );

        PlasmaBlade = PyroPlasma.ionize_gas(
            gas_pocket=ThermalCore,
            energy_density=HIGH
        );

        BladeEnvelope = PyroConfinement.bind_cylinder(
            energy_core=PlasmaBlade,
            length_m=Blade_Length_M,
            radius_m=Blade_Radius_M
        );

        PyroConfinement.compress(
            envelope=BladeEnvelope,
            factor=1.8
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=EmitterNode);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Daga de Plasma Confinada [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Duración Operativa de la Secuencia:**
  * **Duración Base (Sin Afinidad):** La daga permanece encendida durante **2 Asaltos / Turnos** de combate. Al finalizar el segundo turno, el confinamiento magnético se apaga automáticamente para evitar fatiga térmica en el catalizador.
* **Acciones Permitidas:**
  1. **Atacar (con `[✨] Control`):** Atacar en combate cerrado cuerpo a cuerpo utilizando la habilidad de `[✨] Control` en lugar de Combate físico, infligiendo un valor de daño de **Arma: 2** que ignora blindajes ligeros (cuero, telas antibalas convencionales).
  2. **Superar Obstáculos (con `[✨] Control`):** Fundir cerraduras de latón, cortar cables gruesos de acero o seccionar barrotes metálicos en menos de diez segundos.
* **Bonificador por Afinidad Elemental (Fuego):**
  * **Duración Extendida:** Si el Especialista posee afinidad con **Fuego**, la duración se duplica a **4 Asaltos / Turnos**.
  * **Efecto Crítico por Éxito con Estilo:** Si el atacante supera la tirada de defensa enemiga por **3 o más aumentos** (Éxito con Estilo), además de infligir el daño correspondiente, prende fuego a las ropas o revestimientos del blanco, creando el aspecto de situación **`[En Llamas]`** con 1 invocación gratuita para el grupo.
* **Margen de Fallo:**
  * Si se falla con un margen de -3, una fuga magnética transfiere un pulso térmico al chasis del artefacto, provocando 1 casilla de estrés físico por quemadura en la mano del portador.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Secuencia - Calibrador Termico de Materiales]]
* [[Artefacto - Little Fox]]
* [[Reglas FATE - Sistema de Magia Artificial]]
