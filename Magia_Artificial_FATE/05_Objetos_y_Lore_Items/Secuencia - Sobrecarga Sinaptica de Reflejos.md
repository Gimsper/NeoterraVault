---
title: "Secuencia - Sobrecarga Sináptica de Reflejos"
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
  - combate/reflejos
  - objeto
  - fate/proeza
aliases:
  - Sobrecarga Sináptica
  - Acelerar Reflejos
  - Reflejos Acelerados
  - Secuencia Sobrecarga Sináptica de Reflejos
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 🧠 Secuencia: Sobrecarga Sináptica de Reflejos (Rango C)

> *"En un tiroteo en pasillo estrecho, doscientos milisegundos de retraso en tu cerebro significan que el proyectil llega antes que tu esquiva. Este código estimula la conducción en tus axones motores: el mundo parece moverse a la mitad de velocidad y tu mano desenfunda antes de que el rival pestañee."*
> — Tácticas de Duelo Cerrado, Kitsune Micro-Arcana

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Sobrecarga Sináptica de Reflejos (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Reducción de Latencia Axónica y Agilidad
================================================================
Afinidad:    Neutro (Neural)
Requisito:   [✨] Control (1)
Recarga:     Por Escena (4 asaltos de duración)
Complejidad: O(1)
Flujo:       6.5 kR/s

Acción:
Hiperpolariza la vaina de mielina de las vías motoras periféricas, 
reduciendo la latencia de respuesta refleja de 200 ms a 40 ms 
durante 4 asaltos para acelerar la esquiva, el desenfunde y la puntería.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

La **Sobrecarga Sináptica de Reflejos** es el software de aceleración neuromuscular básico para duelistas, escoltas y tiradores de vanguardia.

### Principios de Conducción Axónica Acelerada
1. **Reducción de Latencia de Conducción Saltatoria:** El catalizador emite un tren de microcorrientes bioeléctricas de baja potencia que optimizan el gradiente electroquímico de los nódulos de Ranvier en los nervios motores.
2. **Aceleración de Procesamiento Motriz:** El tiempo entre la percepción visual de un proyectil y la orden muscular de evasión se reduce drásticamente de 200 ms a 40 ms. El operador no se desplaza a velocidades sónicas (eso exigiría soporte cinético de Rango A), sino que su tiempo de reacción física y cognitiva se vuelve casi instantáneo.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Neural.Cognition AS NeuralCognition;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE SobrecargaSinaptica(CasterEntity: Entity) {
    HEADER {
        Rank: "C";
        Affinity: "Neutral";
        Control_Threshold: 1;
        Recycle: "Per_Scene";
        Complexity: "O(1)";
        Throughput: "6.5 kR/s";
    }

    PARAMETERS {
        Target_Latency_Ms: 40.0;
        Duration_Rounds: 4;
        Neuro_Current_Micro_A: 25.0;
    }

    EXECUTE {
        NeuralCognition.accelerate_synaptic_latency(
            target=CasterEntity,
            target_ms=Target_Latency_Ms,
            rounds=Duration_Rounds
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=CasterEntity);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Sobrecarga Sináptica de Reflejos [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Crear una Ventaja (con `[✨] Control`):** Colocar sobre sí mismo el aspecto situacional **`[Reflejos Hiperacelerados]`** con 1 invocación gratuita.
  2. **Defender (con `[✨] Control` o *Atletismo*):** Permite utilizar la invocación para ganar un **+2 a la defensa o a la iniciativa** en cualquier intercambio de combate durante la escena.
* **Bonificador por Afinidad (Neutro / Neural):**
  * Si el Especialista tiene afinidad con **Neutro** (o afinidad bioeléctrica/neural), la duración se extiende a toda la escena y puede reaccionar a emboscadas sin perder su primer turno.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Macro de Librerias SCMEH]]
* [[Artefacto - Little Fox]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
