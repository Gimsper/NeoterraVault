---
title: "Secuencia - Señuelo Óptico Estático"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Neutro"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/neutro
  - distraccion/ilusion
  - objeto
  - fate/proeza
aliases:
  - Señuelo Óptico
  - Ilusión Menor
  - Espejismo Estático
  - Secuencia Señuelo Óptico Estático
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 👁️ Secuencia: Señuelo Óptico Estático (Rango C)

> *"En la oscuridad de los callejones de la Ciudad Baja, el cerebro humano dispara primero y pregunta después. Proyecta un gradiente de luz refractada que parezca una figura agachada tras un contenedor: el centinela vaciará medio cargador en una sombra vacía mientras tú lo flanqueas por la espalda."*
> — Manual de Tácticas de Infiltración, Ghost Operatives

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Señuelo Óptico Estático (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Difracción Fotónica y Proyección Estática
================================================================
Afinidad:    Neutro (o Luz)
Requisito:   [✨] Control (1)
Recarga:     Por Escena (duración 4 asaltos)
Complejidad: O(1)
Flujo:       4.2 kR/s

Acción:
Proyecta un holograma estático tridimensional de escala humana a una 
distancia de hasta 10 metros, simulando una silueta humanoide creíble 
bajo iluminación media o escasa durante 4 asaltos.
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

El **Señuelo Óptico Estático** es una herramienta de guerra psicológica, distracción y camuflaje táctico. A diferencia de los complejos sistemas de proyección volumétrica móvil de Rango B, este algoritmo genera una imagen estática fija de bajo costo computacional.

### Difracción Fotónica sobre Microaerosol Confinado
La trampa visual se compone en dos fases fotofísicas:

1. **Suspensión de Matriz de Refracción (`AeroFlow.stream_vector`):** Despliega una película estática de microaerosol invisible a la distancia deseada (hasta 10 metros), manteniendo las partículas coloidales estacionarias mediante un bolsón de presión neutra.
2. **Curvatura y Modulación Fotónica (`SensoryOptics.refract_light`):** Curva los fotones ambientales que atraviesan la matriz coloidal, creando una interferencia de difracción luminosa que reproduce el contorno, volumen y textura de una figura humana inmóvil (arrodillada, en cobertura o apuntando).
3. **Límites Físicos del Holograma:** La imagen no genera sonido, calor ni masa física; cualquier proyectil o contacto físico la atraviesa sin resistencia, disolviendo temporalmente la luz en un remolino fotónico antes de que la matriz se recomponga.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.Air.GasFlow AS AeroFlow;
IMPORT RuneScript.Sensory.Optics AS SensoryOptics;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE SenueloOptico(ProjectionPoint: Point) {
    HEADER {
        Rank: "C";
        Affinity: "Neutral";
        Control_Threshold: 1;
        Recycle: "Per_Scene";
        Complexity: "O(1)";
        Throughput: "4.2 kR/s";
    }

    PARAMETERS {
        Max_Distance_M: 10.0;
        Hologram_Height_M: 1.75;
        Hologram_Width_M: 0.60;
        Persistence_Rounds: 4;
    }

    EXECUTE {
        AeroMatrix = AeroFlow.stream_vector(
            origin=ProjectionPoint,
            vector=Vector3(0, 1, 0),
            flux_liters_sec=0.5
        );

        SensoryOptics.refract_light(
            target=AeroMatrix
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeAbort.collapse_confinement_inward(envelope=ProjectionPoint);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Señuelo Óptico Estático [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Crear una Ventaja (con `[✨] Control`):** Colocar el aspecto de escena **`[Silueta Señuelo en Cobertura]`** con 1 invocación gratuita a una distancia de hasta 1 zona.
  2. **Superar Obstáculos (con `[✨] Control`):** Desviar la atención de centinelas, patrullas o torretas automáticas, obligándolas a superar una dificultad Media (+2) con Investigar o Percepción para no confundir el señuelo con una amenaza real.
* **Efecto en Combate:**
  * Si un atacante enemigo dirige un disparo o golpe hacia el señuelo, su acción se gasta por completo sin causar daño a ningún combatiente real.
* **Margen de Fallo:**
  * Si se falla con un margen de -3, la luz se refracta de forma invertida, apuntando un haz luminoso directo hacia la posición del operador y aplicando el aspecto `[Ubicación Revelada por Destello]`.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Secuencia - Velo de Refraccion Simple]]
* [[Artefacto - Little Fox]]
* [[Reglas FATE - Sistema de Magia Artificial]]
