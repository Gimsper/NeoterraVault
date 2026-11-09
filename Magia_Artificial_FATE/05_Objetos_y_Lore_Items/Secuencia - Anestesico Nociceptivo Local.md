---
title: "Secuencia - Anestésico Nociceptivo Local"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Neutro"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/neutro
  - medicina/neural
  - objeto
  - fate/proeza
aliases:
  - Anestésico Nociceptivo
  - Bloqueador de Dolor Rúnico
  - Anestésico Local
  - Secuencia Anestésico Nociceptivo
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 🧠 Secuencia: Anestésico Nociceptivo Local (Rango C)

> *"El dolor es un reporte bioeléctrico de tus nervios periféricos a tu tálamo. Si sabes filtrar la frecuencia de las fibras nociceptivas, puedes coserte una herida abierta o seguir disparando con una costilla fisurada sin que el pulso te tiemble."*
> — Cirujano Militar de Frente, Aegis Dynamics

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Anestésico Nociceptivo Local (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Modulación Sináptica y Bloqueo Nociceptivo
================================================================
Afinidad:    Neutro (Neural)
Requisito:   [✨] Control (1)
Recarga:     Por Escena
Complejidad: O(1)
Flujo:       4.8 kR/s

Acción:
Emite una microcorriente galvánica polarizada sobre un nervio 
sensorial periférico, suprimiendo la transmisión del dolor en un 
miembro durante 15 minutos sin anular la movilidad ni el tacto motor.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

El **Anestésico Nociceptivo Local** es un programa bioeléctrico desarrollado para soporte táctico en combate. Permite a los Especialistas mantener la operatividad y la puntería tras sufrir traumas físicos que normalmente incapacitarían por dolor agudo.

### Principios de Supresión Nociceptiva Selectiva
A diferencia de los fármacos químicos que causan somnolencia o las parálisis nerviosas motoras:

1. **Bloqueo de Fibras A-Delta y C (`NeuralCognition.suppress_pain_receptors`):** El catalizador induce un gradiente de hiperpolarización en la membrana axónica de las terminaciones nerviosas nociceptivas del miembro objetivo. Impide que las señales químicas de desgarro tisular o quemadura generen potenciales de acción hacia la médula espinal.
2. **Preservación Propioceptiva Motora:** El algoritmo no afecta a los axones motores alfa ni a los mecanorreceptores de presión profunda. El operador conserva intacta la fuerza, el tacto fino y la destreza manual para empuñar su arma o manipular herramientas.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Neural.Cognition AS NeuralCognition;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE AnestesicoLocal(InjuredLimb: Entity) {
    HEADER {
        Rank: "C";
        Affinity: "Neutral";
        Control_Threshold: 1;
        Recycle: "Per_Scene";
        Complexity: "O(1)";
        Throughput: "4.8 kR/s";
    }

    PARAMETERS {
        Suppression_Window_Min: 15.0;
        Bandwidth_Nociceptive: 0.12;
    }

    EXECUTE {
        NeuralCognition.suppress_pain_receptors(
            target=InjuredLimb
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=InjuredLimb);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Anestésico Nociceptivo Local [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Crear una Ventaja (con `[✨] Control`):** Colocar el aspecto situacional **`[Indiferencia al Dolor Físico]`** sobre un aliado o sobre sí mismo con 1 invocación gratuita.
  2. **Superar Obstáculos (con `[✨] Control`):** Ignorar los penalizadores de combate o de movilidad derivados de una **Consecuencia Moderada o Grave** física durante la duración de la escena actual.
* **Margen de Fallo:**
  * Si se falla con margen de -3, una hiperpolarización errática adormece temporalmente el control motor del miembro, aplicando el aspecto negativo `[Pérdida de Sensibilidad Táctil]`.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Macro de Librerias SCMEH]]
* [[Artefacto - Little Fox]]
* [[Reglas FATE - Sistema de Magia Artificial]]
