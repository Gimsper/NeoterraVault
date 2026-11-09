---
title: "Secuencia - Espejismo Doppler Holográfico"
type: objeto
categoria: magia/secuencia
rango: "B"
afinidad: "Neutro"
control_requerido: 2
tags:
  - magia/secuencia
  - rango/b
  - afinidad/neutro
  - distraccion/holograma_activo
  - objeto
  - fate/proeza
aliases:
  - Espejismo Doppler
  - Holograma Cinético
  - Clon Rúnico Doppler
  - Secuencia Espejismo Doppler Holográfico
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 👁️ Secuencia: Espejismo Doppler Holográfico (Rango B)

> *"Un señuelo estático de Rango C engaña a un centinela novato en la penumbra. Este programa de Rango B proyecta un clon holográfico en movimiento a sesenta cuadros por segundo que corre hacia la trinchera enemiga, emite el eco de pisadas sobre grava y el sonido de disparos con corrimiento Doppler. La línea enemiga entera desata fuego de saturación sobre un fantasma mientras tu escuadra flanquea la posición en silencio absoluto."*
> — Guía de Guerra Electrónica y Espectros, Ghost Recon

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Espejismo Doppler Holográfico (Rango B)
CLASIFICACIÓN: S.C.M.E.H. de Difracción Fotónica Dinámica y Acústica Doppler
================================================================
Afinidad:    Neutro (o Aire / Luz)
Requisito:   [✨] Control (2)
Recarga:     Por Escena (duración 1 escena o 5 asaltos de combate)
Complejidad: O(n) (muestreo dinámico de biomecánica a 60 Hz)
Flujo:       24.0 kR/s

Acción:
Proyecta un clon holográfico cinético en movimiento continuo a hasta 30 m, 
replicando la biomecánica de carrera, salto y disparo del operador con 
firma acústica direccional y efecto Doppler sincronizado.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

El **Espejismo Doppler Holográfico** es el pináculo de la guerra psicológica y contramedidas de vanguardia. Diseñado para desarticular emboscadas y forzar el agotamiento de munición enemiga, genera una firma sensorial completa sin masa física.

### Telemetría Sensorial Dinámica en $\mathcal{O}(n)$
A diferencia de los señuelos estáticos, el algoritmo procesa la trayectoria y la respuesta óptica en tiempo real:

1. **Guía de Microaerosol Vectorial Móvil (`AeroFlow.stream_vector`):** Desplaza una matriz de microaerosol laminar coloidal a lo largo de una ruta programada (hasta 30 metros de radio a velocidades de hasta 25 km/h).
2. **Refracción Fotónica Dinámica (`SensoryOptics.refract_light`):** Modula la difracción a 60 hercios, ajustando sombras, brillos de equipo y reflejos balísticos según el ángulo de visión de múltiples observadores simultáneos ($\mathcal{O}(n)$).
3. **Acústica Sintetizada con Corrimiento Doppler (`AeroAcoustics.pulse_compression`):** Genera frentes de onda sonoros que imitan el impacto de botas en el suelo, respiración y chasquidos de cerrojo. Aplica modulación de frecuencia según la velocidad relativa del clon respecto a los centinelas enemigos, haciendo que el sonido coincida perfectamente con la distancia percibida.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Air.GasFlow AS AeroFlow;
IMPORT RuneScript.Elements.Air.Acoustics AS AeroAcoustics;
IMPORT RuneScript.Sensory.Optics AS SensoryOptics;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE EspejismoDoppler(OriginNode: Point, WaypointList: List[Point]) {
    HEADER {
        Rank: "B";
        Affinity: "Neutral";
        Control_Threshold: 2;
        Recycle: "Per_Scene";
        Complexity: "O(n)";
        Throughput: "24.0 kR/s";
    }

    PARAMETERS {
        Max_Range_M: 30.0;
        Refresh_Rate_Hz: 60.0;
        Acoustic_Output_Db: 75.0;
        Max_Active_Rounds: 5;
    }

    EXECUTE {
        FOR EACH Waypoint IN WaypointList {
            MovingAerosol = AeroFlow.stream_vector(
                origin=Waypoint,
                vector=Operator.VelocityVector,
                flux_liters_sec=1.2
            );

            SensoryOptics.refract_light(
                target=MovingAerosol
            );

            AeroAcoustics.pulse_compression(
                origin=Waypoint,
                vector=Operator.VelocityVector,
                decibels=Acoustic_Output_Db
            );
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=OriginNode);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Espejismo Doppler Holográfico [Rango B]*
* **Requisito de Activación:** Tener `[✨] Control` a **Regular (+2)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto de Rango B]].
* **Acciones Permitidas:**
  1. **Crear una Ventaja (con `[✨] Control`):** Colocar el aspecto de escena **`[Clon Holográfico en Avance Agresivo]`** con 2 invocaciones gratuitas a hasta 2 zonas de distancia.
  2. **Superar Obstáculos (con `[✨] Control`):** Neutralizar la vigilancia de torretas automáticas o unidades enemigas. Los oponentes deben superar una tirada de Investigar o Percepción contra dificultad **Grande (+4)** para no priorizar al clon como su blanco primario.
* **Efecto de Desvío en Combate:**
  * Mientras el clon esté activo, los dos primeros ataques enemigos dirigidos a la escuadra son absorbidos por el espejismo sin efecto alguno, revelando la posición exacta de los atacantes emboscados.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango B]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Secuencia - Senuelo Optico Estatico]]
* [[Calculo de Rangos SCMEH - Big-O y Flujo]]
* [[Reglas FATE - Sistema de Magia Artificial]]
