---
title: "Secuencia - Detector Sísmico Pasivo"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Tierra"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/tierra
  - sensorial/sismica
  - objeto
  - fate/proeza
aliases:
  - Detector Sísmico
  - Sonar Sísmico Pasivo
  - Escaneo de Pisadas
  - Secuencia Detector Sísmico Pasivo
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# ⛰️ Secuencia: Detector Sísmico Pasivo (Rango C)

> *"Cierra los ojos y apoya la palma enguantada en la roca. No necesitas ver a través de las paredes: los micro-impactos mecánicos del suelo viajan hasta tus sensores y tu catalizador los traduce en un pulso rítmico en las yemas de tus dedos. Tu mano siente la dirección; tu oído interno escucha los pasos."*
> — Sabiduría de los Pioneros del Reino Olvidado

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Detector Sísmico Pasivo (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Sismología de Escucha y Telemetría Háptica
================================================================
Afinidad:    Tierra
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       2.8 kR/s

Acción:
Sintoniza el catalizador con el tren de ondas elásticas superficiales 
del suelo mineral al apoyar la mano. Filtra ruidos, calcula el retardo 
de fase entre los sensores del guantelete y traduce la dirección y 
proximidad del enemigo en pulsos táctiles y audio binaural fantasma.
================================================================
```

---

## 2. Descripción Operativa y Decodificación de Señales

A diferencia de los radares activos o escáneres electromagnéticos que delatan la posición del usuario, el **Detector Sísmico Pasivo** opera con **cero emisiones activas**, convirtiéndolo en la herramienta de sigilo perfecta.

### Principios de Telemetría Elástica y Traducción Bio-Sensorial
Al apoyar la palma o los dedos sobre un sustrato mineral continuo, el algoritmo procesa y traduce las ondas mecánicas en tiempo real mediante la siguiente cadena operativa:

1. **Filtro Paso-Banda Digital:** El algoritmo aísla únicamente las frecuencias fundamentales de la marcha bípeda humana con carga militar (entre $1.5\text{ Hz}$ y $6.0\text{ Hz}$), descartando el viento exterior, zumbidos de cables de alta tensión o la acústica de tuberías lejanas.
2. **Triangulación de Retardo de Fase ($\Delta t$):** Los tres nodos piezoeléctricos rúnicos ubicados en la palma, índice y meñique del catalizador detectan la milésima de segundo de diferencia con la que el frente de onda impacta cada punto. Con esto, calcula el **vector angular de azimut** (rumbo relativo en grados) y la distancia estimada mediante el decaimiento de la amplitud.
3. **Decodificación Háptica a la Mano (`Sensory.Haptics`):** El Especialista no mira una pantalla. El artefacto emite microcorrientes galvánicas indoloras en la piel de la palma: cada pisada enemiga se percibe como un "latido" táctil sincronizado. La posición del hormigueo en la mano indica la orientación (pulgar = izquierda, índice = frente, meñique = derecha) y la intensidad indica la cercanía y el peso de la masa (infantería ligera vs. exoesqueletos blindados).
4. **Traducción en Audio Fantasma (`Sensory.Acoustics`):** Como apoyo secundario, el catalizador induce un chasquido binaural tridimensional directamente en el canal auditivo del operador, permitiéndole "escuchar" el paso crujiente en el oído izquierdo o derecho como si no hubiera un muro de concreto en medio.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python

IMPORT RuneScript.Elements.Earth.Seismic AS GeoSeismic;
IMPORT RuneScript.Sensory.Haptics AS SensoryHaptics;
IMPORT RuneScript.Sensory.Acoustics AS SensoryAcoustics;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE SonarSismico(GroundTouchPoint: Point) {
    HEADER {
        Rank: "C";
        Affinity: "Earth";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "2.8 kR/s";
    }

    PARAMETERS {
        Listen_Duration_Sec: 15.0;
        Bandpass_Low_Hz: 1.5;
        Bandpass_High_Hz: 6.0;
        Max_Distance_M: 15.0;
    }

    EXECUTE {
        RawWaveform = GeoSeismic.listen_elastic_waves(
            contact_point=GroundTouchPoint,
            sample_rate_hz=500.0
        );

        FilteredSignal = RawWaveform.filter_bandpass(
            min_hz=Bandpass_Low_Hz,
            max_hz=Bandpass_High_Hz
        );

        Bearing = GeoSeismic.triangulate_phase_delay(
            sensor_array=Operator.HandSensors,
            signal=FilteredSignal
        );

        SensoryHaptics.project_haptic_pulse(
            target_contact_point=Operator.PalmSkin,
            pattern_id="BEARING_CADENCE_TICK",
            intensity_mw=15.0
        );

        SensoryAcoustics.project_phantom_audio(
            coords=Operator.Ear,
            audio_sample=Bearing.to_binaural_audio()
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SensoryHaptics.project_haptic_pulse(
                target_contact_point=Operator.PalmSkin,
                pattern_id="NULL",
                intensity_mw=0.0
            );
            SafeAbort.collapse_confinement_inward(envelope=GroundTouchPoint);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Detector Sísmico Pasivo [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Crear una Ventaja (con `[✨] Control`):** Colocar aspectos de escena con 1 invocación gratuita como:
     * `[Posición del Centinela Rastreada tras el Muro]`
     * `[Cadencia y Rumbo de la Patrulla Mapeados]`
  2. **Defender (con `[✨] Control`):** Anula totalmente la ventaja de oponentes que intenten tender emboscadas desde la oscuridad, niebla de humo o esquinas ciegas, siempre que se desplacen sobre suelo mineral.
* **Bonificador por Afinidad Elemental (Tierra):**
  * Si el Especialista tiene afinidad con **Tierra**, el radio de telemetría se duplica (30 metros) y la vibración háptica permite distinguir si el objetivo porta blindaje pesado o armas ligeras.
* **Margen de Fallo:**
  * Si se produce un fallo catastrófico (margen de -3), una vibración parásita sobrecarga el nervio ulnar de la mano, aplicando la consecuencia situacional leve `[Mano Entumecida por Rebote Sísmico]`.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Macro de Librerias SCMEH]]
* [[Artefacto - Little Fox]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
