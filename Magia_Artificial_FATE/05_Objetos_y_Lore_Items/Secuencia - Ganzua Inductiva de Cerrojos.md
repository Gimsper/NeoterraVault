---
title: "Secuencia - Ganzúa Inductiva de Cerrojos"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Rayo"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/rayo
  - tecnologia/software
  - objeto
  - fate/proeza
aliases:
  - Ganzúa Inductiva
  - Ganzúa Magnética
  - Apertura Rúnica
  - Secuencia Ganzúa Inductiva
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# ⚡ Secuencia: Ganzúa Inductiva de Cerrojos (Rango C)

> *"Las corporaciones gastan fortunas en cilindros mecánicos de seis pernos de acero templado. Con este código no metes una aguja de metal: aplicas un par magnético de cizalla al rotor, elevas cada perno con pulsos electromagnéticos micrométricos hasta la línea de corte y dejas que la propia física de la cerradura haga 'click'."*
> — Saboteador de Sistemas Clandestinos, Null-Sector

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Ganzúa Inductiva de Cerrojos (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Manipulación de Cizalla y Reluctancia Magnética
================================================================
Afinidad:    Rayo
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       4.0 kR/s

Acción:
Mapea la reluctancia magnética del bombín para ubicar pernos ferrosos. 
Aplica un par de giro tangencial continuo al rotor (tensión de cizalla) 
y eleva secuencialmente los contrapernos con pulsos de atracción 
enfocados hasta liberar la línea de corte y retraer el pestillo.
================================================================
```

---

## 2. Descripción Operativa y Mecánica de Cerrajería

A diferencia de un simple "pulso eléctrico destructor", la **Ganzúa Inductiva de Cerrojos** es un programa de cerrajería analógica de ultra-precisión. Opera bajo los mismos principios mecánicos que una ganzúa física tradicional (tensión rotacional + elevación de pernos), pero ejecuta la fuerza mediante vectores magnéticos invisibles sin rayar el ojo de la cerradura ni dejar virutas metálicas.

### Principios de Manipulación Electromecánica y Cizalla
El algoritmo replica con vectores magnéticos la técnica de ganzuado analógico de un cilindro de pernos (*pin-tumbler*), operando en cuatro fases secuenciales:

1. **Mapeo Inductivo por Reluctancia (`detect_ferrous_nodes`):** Al apoyar la punta del artefacto contra la bocallave, emite un campo de sondeo de $0.15\text{ Tesla}$. Mide las variaciones microscópicas de permeabilidad magnética dentro del metal, identificando cuántos pernos tiene el bombín ($N = 4, 5, 6$) y la profundidad exacta de cada cavidad.
2. **Aplicación del Par de Torsión Continuo (`apply_rotational_torque`):** Ninguna cerradura se abre sin tensión rotacional. El artefacto induce un campo magnético dipolar tangencial sobre el rotor ferroso con una fuerza continua de $0.20\text{ N}\cdot\text{m}$. Esta tensión de cizalla hace que el rotor intente girar, provocando que los contrapernos queden ligeramente aprisionados contra las paredes de la carcasa ("binding pins").
3. **Elevación Perno a Perno y Asentamiento en la Línea de Corte (`pulse_focused_attraction`):** El código barre los pernos detectados. Aplica un pulso magnético vertical enfocado sobre cada perno activo con una fuerza calculada de $0.85\text{ Newtons}$ (suficiente para vencer la resistencia del resorte). Cuando el contraperno cruza la línea de corte (`Shear Line`), el par de torsión del Paso 2 hace que el rotor avance una fracción de milímetro, atrapando el contraperno en la carcasa superior y liberando el rotor. La caída instantánea de reluctancia confirma el éxito y el catalizador emite un micro-pulso háptico en la mano del Especialista ("click" táctil).
4. **Giro del Rotor y Retracción del Pestillo:** Cuando todos los pernos han liberado la línea de corte, el algoritmo incrementa el par de giro a $1.5\text{ N}\cdot\text{m}$, rotando el rotor a 90° y retrayendo suavemente el resbalón o cerrojo mecánico.
5. **Subrutina Electrónica (Relés y Solenoides):** Si la cerradura no es mecánica sino un teclado con bobina de apertura electromagnética, el sensor omite los pines mecánicos e inyecta un pulso inductivo calibrado de $1.4\text{ A}$ directamente sobre la bobina del actuador, retrayendo el perno de seguridad sin fundir la placa de control.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python

IMPORT RuneScript.Elements.Lightning.Magnetics AS ElectroMag;
IMPORT RuneScript.Elements.Lightning.Circuit AS ElectroCircuit;
IMPORT RuneScript.Sensory.Haptics AS SensoryHaptics;
IMPORT RuneScript.Safety.Vent AS SafeVent;

SEQUENCE GanzuaInductiva(LockTarget: Object) {
    HEADER {
        Rank: "C";
        Affinity: "Lightning";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "4.0 kR/s";
    }

    PARAMETERS {
        Scan_Field_Tesla: 0.15;
        Tension_Torque_Nm: 0.20;
        Max_Pins: 6;
        Pulse_Lift_Newtons: 0.85;
    }

    EXECUTE {
        PinNodes = ElectroMag.detect_ferrous_nodes(
            target=LockTarget.Cylinder,
            flux_density_tesla=Scan_Field_Tesla
        );

        ElectroMag.apply_rotational_torque(
            target_core=LockTarget.Plug,
            torque_newton_meters=Tension_Torque_Nm,
            axis=LockTarget.RotationAxis
        );

        FOR EACH Pin IN PinNodes {
            ElectroMag.pulse_focused_attraction(
                node=Pin,
                lift_force_newtons=Pulse_Lift_Newtons
            );

            SensoryHaptics.project_haptic_pulse(
                target_contact_point=Operator.Fingertip,
                pattern_id="PIN_SET_FEEDBACK",
                intensity_mw=10.0
            );
        }

        ElectroMag.apply_rotational_torque(
            target_core=LockTarget.Plug,
            torque_newton_meters=1.5,
            axis=LockTarget.RotationAxis
        );

        IF (LockTarget.has_actuator_solenoid()) {
            ElectroCircuit.generate_magnetic_pulse(
                current_amperes=1.4,
                radius_m=0.08
            );
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            ElectroMag.apply_rotational_torque(
                target_core=LockTarget.Plug,
                torque_newton_meters=0.0,
                axis=LockTarget.RotationAxis
            );
            SafeVent.ground_electrical_surge();
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Ganzúa Inductiva de Cerrojos [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Superar Obstáculos (con `[✨] Control`):** Permite abrir cerraduras mecánicas convencionales, candados, taquillas metálicas o puertas con cerradura electrónica **utilizando la habilidad `[✨] Control` en lugar de *Hurtar***. No requiere ganzúas físicas ni deja signos visibles de allanamiento forzado.
  2. **Crear una Ventaja (con `[✨] Control`):** Invertir la secuencia para fijar magnéticamente los pernos en la posición cerrada, otorgando el aspecto de situación `[Cerradura Mecánicamente Trancada]` con 1 invocación gratuita para impedir el paso a perseguidores.
* **Bonificador por Afinidad Elemental (Rayo):**
  * Si el Especialista tiene afinidad con **Rayo**, recibe un **+2 a su tirada de `[✨] Control`** al manipular cerrojos electrónicos o cerraduras acorazadas de grado industrial.
* **Margen de Fallo:**
  * Si se falla por 3 o más puntos, el exceso de torsión dobla un resorte interno o dispara la microalarma de sabotaje del cerrojo, alertando a los guardias de la instalación.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Macro de Librerias SCMEH]]
* [[Artefacto - Little Fox]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
