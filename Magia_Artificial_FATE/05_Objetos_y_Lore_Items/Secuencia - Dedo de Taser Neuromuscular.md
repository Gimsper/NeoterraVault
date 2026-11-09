---
title: "Secuencia - Dedo de Táser Neuromuscular"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Rayo"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/rayo
  - combate/no_letal
  - objeto
  - fate/proeza
aliases:
  - Dedo de Táser
  - Táser Neuromuscular
  - Micro-Arco Bioeléctrico
  - Secuencia Dedo de Táser
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# ⚡ Secuencia: Dedo de Táser Neuromuscular (Rango C)

> *"La piel seca de un soldado tiene diez mil ohmios de resistencia. Si descargas una chispa tonta, solo le pica el brazo. Un verdadero táser rúnico dispara primero un microarco de alto voltaje que ioniza la ropa y la epidermis sin quemarla, y luego inyecta diecinueve pulsos bifásicos por segundo directamente en el nervio motor: su brazo se contrae con tanta fuerza que su propia mano suelta el fusil."*
> — Instructor de Combate Cuerpo a Cuerpo, Aegis Dynamics

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Dedo de Táser Neuromuscular (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Ruptura Dieléctrica y Parálisis Bifásica
================================================================
Afinidad:    Rayo
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       5.5 kR/s

Acción:
Emite un precursor dieléctrico que quiebra la resistencia cutánea o 
de tela e inyecta un tren de pulsos bifásicos de 19 Hz en nervios 
motores periféricos, causando incapacitación muscular instantánea.
================================================================
```

---

## 2. Descripción Operativa y Neurofisiología Bioeléctrica

El **Dedo de Táser Neuromuscular** es la técnica predilecta de arresto táctico, captura viva e interrogatorio de campo entre fuerzas de seguridad corporativa y agentes clandestinos. Su objetivo es anular la capacidad de combate de un individuo en una fracción de segundo sin causarle daño tisular permanente ni arriesgar una falla cardíaca letal.

### Principios de Ruptura Dieléctrica y Modulación Neuromuscular
Para garantizar una incapacitación motora instantánea y segura sin riesgo cardiovascular ni activación del DRM ético, el algoritmo ejecuta dos fases consecutivas:
* **Fase 1 — Ruptura Dieléctrica Precursora (`ElectroDielectric.ionize_channel`):** En el microsegundo de contacto físico con la ropa o piel del adversario, el artefacto emite un filamento ionizado de altísimo voltaje pero bajísimo amperaje ($< 1\text{ mA}$). Este precursor rompe la barrera dieléctrica de la tela y la capa córnea de la piel en un microcanal de resistencia nula.
* **Fase 2 — Estimulación Motora Bifásica Cuadrada (`ElectroBio.stimulate_motor_nerve`):** A través del canal ionizado, descarga un tren de ondas cuadradas bifásicas a $19\text{ Hz}$ (la frecuencia resonante que anula el control voluntario del sistema nervioso periférico). Actúa directamente sobre los axones motores alfa del plexo braquial o del cuello, provocando **Incapacitación Neuromuscular (NMI)**. El músculo se bloquea en espasmo tetánico absoluto: el brazo se agarrota de golpe y los dedos se abren involuntariamente, soltando armas o soltando rehenes.
* **Bucle de Retorno Local y Protección Cardíaca:** La corriente no viaja por todo el cuerpo; el catalizador establece un electrodo cátodo de retorno a solo 3 centímetros del punto de contacto (en la empuñadura del propio guantelete). La electricidad circula exclusivamente por el miembro impactado, garantizando **cero riesgo de fibrilación cardíaca**.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python

IMPORT RuneScript.Elements.Lightning.Dielectric AS ElectroDielectric;
IMPORT RuneScript.Elements.Lightning.Charge AS ElectroCharge;
IMPORT RuneScript.Elements.Lightning.Bioelectric AS ElectroBio;
IMPORT RuneScript.Safety.Vent AS SafeVent;

SEQUENCE DedoTaser(TargetLimb: Entity) {
    HEADER {
        Rank: "C";
        Affinity: "Lightning";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "5.5 kR/s";
    }

    PARAMETERS {
        Capacitance_Charge_Coulombs: 0.02;
        Pulse_Rate_Hz: 19.0;
        Pulse_Width_Microseconds: 100.0;
        Lock_Pattern: TETANIC_LOCK;
    }

    EXECUTE {
        Channel = ElectroDielectric.ionize_channel(
            start_point=Operator.FingerTip,
            end_point=TargetLimb.ContactSkin,
            target_resistance=0.0
        );

        ChargeNode = ElectroCharge.accumulate(
            capacitance_source=Hardware.Capacitor,
            coulombs=Capacitance_Charge_Coulombs
        );

        ElectroBio.stimulate_motor_nerve(
            target_entity=TargetLimb,
            limb=TargetLimb.ContactLimb,
            pulse_pattern=Lock_Pattern
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeVent.ground_electrical_surge();
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Dedo de Táser Neuromuscular [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Atacar (con `[✨] Control`):** Ataque a contacto cuerpo a cuerpo. Inflige **2 casillas de estrés físico o mental no letal**. Si inflige una consecuencia, se traduce en aspectos como `[Brazo Entumecido e Inmóvil]` o `[Aturdimiento Nervioso]`.
  2. **Crear una Ventaja (con `[✨] Control`):** Desarmar de forma forzosa a un oponente o soltar un rehén colocando el aspecto situacional **`[Fusil Soltado por Espasmo Motor]`** con 1 invocación gratuita.
* **Bonificador por Afinidad Elemental (Rayo):**
  * Si el Especialista tiene afinidad con **Rayo**, el arco puede atravesar capas gruesas de cuero, chalecos tácticos o guantes aislantes sin penalización en la dificultad de la tirada.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
