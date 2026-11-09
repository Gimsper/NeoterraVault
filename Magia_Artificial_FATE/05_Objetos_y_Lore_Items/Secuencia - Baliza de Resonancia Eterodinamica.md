---
title: "Secuencia - Baliza de Resonancia Eterodinámica"
type: objeto
categoria: magia/secuencia
rango: "B"
afinidad: "Tierra"
control_requerido: 2
tags:
  - magia/secuencia
  - rango/b
  - afinidad/tierra
  - rastreo/telemetria_activa
  - objeto
  - fate/proeza
aliases:
  - Baliza de Resonancia
  - Rastreador Eterodinámico
  - Baliza Telemétrica de 5 km
  - Secuencia Baliza de Resonancia Eterodinámica
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# ⛰️ Secuencia: Baliza de Resonancia Eterodinámica (Rango B)

> *"El espectrómetro de Rango C te dice quién estuvo aquí hace un par de horas si te arrodillas a examinar el lodo. Esta baliza de Rango B le implanta una firma armónica piezoeléctrica en la armadura o el catalizador a cincuenta metros de distancia: a partir de ese segundo, sabes exactamente en qué piso, qué habitación y hacia dónde corre en un radio de cinco kilómetros durante veinticuatro horas."*
> — Sabueso Mayor Dax, Unidad de Caza de Fugitivos Arcanos

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Baliza de Resonancia Eterodinámica (Rango B)
CLASIFICACIÓN: S.C.M.E.H. de Marcado Piezoeléctrico y Telemetría Espectral
================================================================
Afinidad:    Tierra (o Neutro)
Requisito:   [✨] Control (2)
Recarga:     Usos Infinitos
Complejidad: O(n) (triangulación continua de nodos en mapa urbano)
Flujo:       18.5 kR/s

Acción:
Implanta un nodo de resonancia armónica de baja frecuencia en el objetivo 
a hasta 50 m, permitiendo su triangulación continua a través de roca, 
blindaje y muros en un radio de 5 km durante 24 horas.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

La **Baliza de Resonancia Eterodinámica** es el sistema de interdicción y cacería de objetivos por excelencia en operaciones especiales. Permite realizar seguimiento táctico de precisión sin depender de satélites, líneas de visión directa ni antenas de telecomunicación civiles.

### Marcado Piezoeléctrico y Triangulación Continua en $\mathcal{O}(n)$
El sistema opera en dos etapas perfectamente sincronizadas:

1. **Inyección de Resonancia Armónica (`ElectroMagnetics.polarize_dipole` & `GeoPiezo.excite_piezo_discharge`):** Proyecta un pulso guiado de radiofrecuencia polarizada que induce una microvibración de resonancia piezoeléctrica en el chasis del artefacto o la estructura mineral/metálica del equipo del objetivo. La baliza no emite luz ni calor detectable.
2. **Triangulación Elástica de Subsuelo en $\mathcal{O}(n)$ (`GeoSeismic.listen_elastic_waves`):** El artefacto del operador monitorea continuamente las micro-ondas de retorno propagadas a través de la corteza litológica (ondas Rayleigh subterráneas). El bucle $\mathcal{O}(n)$ filtra el ruido ambiental de la ciudad y calcula el azimut, elevación y distancia exacta del blanco en tiempo real.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Earth.Seismic AS GeoSeismic;
IMPORT RuneScript.Elements.Earth.Piezoelectric AS GeoPiezo;
IMPORT RuneScript.Elements.Lightning.Circuit AS ElectroCircuit;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE BalizaResonancia(TargetLimbOrChassis: Entity) {
    HEADER {
        Rank: "B";
        Affinity: "Earth";
        Control_Threshold: 2;
        Recycle: "Infinite";
        Complexity: "O(n)";
        Throughput: "18.5 kR/s";
    }

    PARAMETERS {
        Lock_Range_M: 50.0;
        Tracking_Radius_Km: 5.0;
        Harmonic_Frequency_Khz: 142.5;
        Duration_Hours: 24.0;
    }

    EXECUTE {
        ElectroCircuit.polarize_dipole(
            node_a=Operator.OriginHand,
            node_b=TargetLimbOrChassis.Coordinates,
            delta_volts=450.0
        );

        GeoPiezo.excite_piezo_discharge(
            crystal_core=TargetLimbOrChassis.FerrousComponents,
            mechanical_stress_pascals=850.0
        );

        FOR EACH Sector IN CityLithology.SectorsWithin(Tracking_Radius_Km) {
            GeoSeismic.listen_elastic_waves(
                contact_point=Sector,
                sample_rate_hz=Harmonic_Frequency_Khz
            );
        }
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=TargetLimbOrChassis);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Baliza de Resonancia Eterodinámica [Rango B]*
* **Requisito de Activación:** Tener `[✨] Control` a **Regular (+2)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto de Rango B]].
* **Acciones Permitidas:**
  1. **Crear una Ventaja (con `[✨] Control`):** Marcar a un objetivo a hasta 2 zonas de distancia, colocando el aspecto **`[Firma Telemétrica Bloqueada a 5 km]`** con 2 invocaciones gratuitas.
  2. **Superar Obstáculos (con `[✨] Control`):** Seguir el rastro del objetivo en entornos urbanos densos, redes de alcantarillado subterráneas o bosques minerales, ignorando cualquier intento de esconderse o usar aspectos de sigilo convencionales.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango B]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Secuencia - Espectrometro de Residuos Runicos]]
* [[Calculo de Rangos SCMEH - Big-O y Flujo]]
* [[Reglas FATE - Sistema de Magia Artificial]]
