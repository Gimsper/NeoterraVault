---
title: "Secuencia - Silenciador Barométrico"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Aire"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/aire
  - sigilo/acustica
  - objeto
  - fate/proeza
aliases:
  - Silenciador Barométrico
  - Supresor Acústico Rúnico
  - Desacoplo Acústico
  - Secuencia Silenciador Barométrico
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 🌪️ Secuencia: Silenciador Barométrico (Rango C)

> *"Un supresor de titanio pesa medio kilo en la punta de tu cañón, arruina tu balance y retiene tanto calor que te delata en los visores térmicos. Este código genera una cámara de descompresión adiabática e inversión de fase acústica en el aire justo frente a la boca de fuego: el estruendo de un calibre cincuenta se convierte en el chasquido sordo de una grapadora de oficina."*
> — Tirador Designado de Operaciones Clandestinas, Aegis Dynamics

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Silenciador Barométrico (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Interferencia Acústica Destructiva y Desacople
================================================================
Afinidad:    Aire
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       4.5 kR/s

Acción:
Sincronizado al microsegundo con la detonación. Abre una cámara de 
baja presión frente al cañón, enfría los gases de combustión por 
expansión adiabática y emite una contrafase sónica que atenúa 45 dB.
================================================================
```

---

## 2. Descripción Operativa y Física Acústica

El disparo de un arma balística o el chasquido de un catalizador mágico genera dos componentes sónicos:
1. **La Explosión de Boca (*Muzzle Blast*):** La súbita salida de gases a miles de atmósferas y altísima temperatura que chocan contra el aire frío exterior, creando una onda de choque esférica ensordecedora ($140-165\text{ dB}$).
2. **El Chasquido Balístico (*Sonic Crack*):** La estela de choque del proyectil al romper la barrera del sonido en vuelo.

### Principios de Supresión Barométrica y Cancelación Acústica
El algoritmo sincroniza con el percutor una ventana operativa de 3 milisegundos estructurada en las siguientes fases:

1. **Cámara de Desacoplo Barométrico (`AeroPressure.depressurize_zone`):** En el instante en que el proyectil abandona la corona del cañón, el código crea una burbuja de baja densidad barométrica ($0.2\text{ bar}$) de 35 centímetros de radio. Al haber menos moléculas de aire por centímetro cúbico, la onda de choque no encuentra un medio elástico denso al que transferir su energía mecánica.
2. **Expansión Adiabática y Choque Térmico (`AeroThermal.joule_thomson_expansion`):** Descomprime bruscamente los gases de pólvora o plasma al salir del ánima, enfriándolos en cientos de grados en una fracción de milisegundo. Esto elimina instantáneamente el fogonazo luminoso visible en la boca del cañón, evitando que el tirador sea detectado por visores nocturnos o térmicos.
3. **Cancelación por Interferencia de Fase Destructiva (`AeroAcoustics.pulse_compression`):** El catalizador calcula el frente de onda de la detonación y emite un pulso acústico gemelo invertido a $180^\circ$ de desfase ($\Delta \phi = \pi$). Las crestas de presión de la detonación colisionan con los valles de la onda invertida, cancelándose mutuamente y reduciendo el sonido en **45 decibeles** (de un estampido atronador a un susurro de baja frecuencia inaudible a 5 metros).
4. **Cero Fricción en el Proyectil:** A diferencia de los silenciadores físicos tradicionales con deflectores de goma o metal, la burbuja es aire enrarecido: la bala **no pierde velocidad de salida, alcance ni precisión balística**.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python

IMPORT RuneScript.Elements.Air.Acoustics AS AeroAcoustics;
IMPORT RuneScript.Elements.Air.Pressure AS AeroPressure;
IMPORT RuneScript.Elements.Air.ThermalShift AS AeroThermal;
IMPORT RuneScript.Triggers.Chronos AS TriggersChronos;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE SilenciadorBarometrico(MuzzlePoint: Point) {
    HEADER {
        Rank: "C";
        Affinity: "Air";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "4.5 kR/s";
    }

    PARAMETERS {
        Baffle_Radius_M: 0.35;
        Depressurization_Bar: 0.20;
        Attenuation_Db: 45.0;
        Window_Duration_Ms: 3.0;
    }

    EXECUTE {
        AeroPressure.depressurize_zone(
            volume_m3=0.04,
            target_bar=Depressurization_Bar
        );

        AeroThermal.joule_thomson_expansion(
            gas_pocket=MuzzlePoint.GasEnvelope,
            ratio=3.5
        );

        AeroAcoustics.decouple_vibration(
            zone=MuzzlePoint
        );

        TriggersChronos.OnTimer(duration_seconds=0.003) {
            SafeAbort.collapse_confinement_inward(envelope=MuzzlePoint);
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=MuzzlePoint);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Silenciador Barométrico [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Crear una Ventaja (con `[✨] Control`):** Permite disparar un arma balística de fuego o un ataque mágico rúnico manteniendo el aspecto situacional **`[Disparo Sordo e Inaudible]`** o conservando intacto un aspecto de `[Oculto en las Sombras]`, sin alertar a patrullas en zonas o habitaciones contiguas.
  2. **Superar Obstáculos (con `[✨] Control`):** Neutralizar centinelas o cámaras de vigilancia a distancia con disparos limpios sin activar alarmas sonoras perimetrales.
* **Bonificador por Afinidad Elemental (Aire):**
  * Si el Especialista tiene afinidad con **Aire**, el silenciador elimina completamente el fogonazo luminoso visible en la oscuridad, otorgando invisibilidad contra visores nocturnos y térmicos en el momento del disparo.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
