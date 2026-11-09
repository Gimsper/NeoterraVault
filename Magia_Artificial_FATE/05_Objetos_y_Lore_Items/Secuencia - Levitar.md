---
title: "Secuencia - Levitar"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Aire"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/aire
  - objeto
  - fate/proeza
aliases:
  - Levitar
  - Telekinesis
  - Telekinesis de Rango C
  - Secuencia Levitar
status: revisado
created: 2026-11-05
updated: 2026-11-08
---

# 🌪️ Secuencia: Levitar (Rango C)

> *"El error de novato es creer que levitar un cajón de municiones es solo empujar aire hacia arriba. Si no calculas su centro de masa y no confinas un faldón de vórtice perimetral, la carga resbala como una pastilla de jabón mojada y le revienta los tobillos a tu compañero."*
> — Cátedra de Aerodinámica Aplicada, Academia de [[Ingenieros y Alquimistas]]

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Levitar (Rango C)
CLASIFICACIÓN: S.C.M.E.H. Barométrica, Centro de Masa y Sustentación
================================================================
Afinidad:    Aire
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       4.2 kR/s

Acción:
Anula la masa inercial de un cuerpo (hasta 250 kg), calcula su centro 
de gravedad y genera un cojín de sustentación barométrica de cuatro 
cuadrantes con faldón de vórtice para impedir deslizamiento lateral.
================================================================
```

---

## 2. Descripción Operativa y Mecánica Aerodinámica

La secuencia **Levitar** (a menudo llamada coloquialmente *Telekinesis de Rango C*) es una de las aplicaciones más elegantes de la ingeniería neumática de Neoterra. No es un rayo tractor místico; es un colchón de aire activo estabilizado mediante aerodinámica computacional.

### Arquitectura de Sustentación Activa
El algoritmo supera las limitaciones de la sustentación barométrica simple mediante el control activo del centro de gravedad y la contención perimetral del fluido:
1. **Supresión Inercial (`KineticGravity.nullify_inertial_mass`):** Reduce temporalmente la resistencia inercial del objeto a cero relativo. Esto significa que ya no se requieren toneladas de fuerza para vencer su peso en reposo; basta una presión barométrica moderada.
2. **Cojín Barométrico de 4 Cuadrantes (`AeroPressure.set_differential`):** El algoritmo divide la superficie inferior del objetivo en cuatro cuadrantes virtuales (Norte, Sur, Este, Oeste). Ajusta dinámicamente un gradiente de $\Delta P = 1.35\text{ bar}$ entre la cara inferior y superior. Si el objeto cabecea hacia delante, el cuadrante frontal aumenta la presión instantáneamente para nivelarlo.
3. **Faldón de Vórtice Centrífugo de Contención (`AeroGas.vortex_angular`):** Rodea el perímetro inferior del objeto con una cortina laminar rotatoria de aire a $1.200\text{ RPM}$. Este "faldón" neumático atrapa la burbuja de alta presión debajo del cuerpo, impidiendo que el aire escape lateralmente y evitando que la carga resbale.
4. **Vector de Arrastre Táctico (`KineticVector.lock_trajectory`):** Sincroniza la posición tridimensional del objeto suspendido con el vector de la mano del Especialista, permitiéndole empujar, atraer o desplazar la carga a paso de marcha hasta a 4 metros de distancia.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python

IMPORT RuneScript.Elements.Air.Pressure AS AeroPressure;
IMPORT RuneScript.Elements.Air.GasFlow AS AeroGas;
IMPORT RuneScript.Kinetics.Gravity AS KineticGravity;
IMPORT RuneScript.Kinetics.Vector AS KineticVector;
IMPORT RuneScript.Safety.Abort AS SafeAbort;

SEQUENCE Levitar(TargetObject: Object) {
    HEADER {
        Rank: "C";
        Affinity: "Air";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "4.2 kR/s";
    }

    PARAMETERS {
        Max_Mass_Kg: 250.0;
        Max_Altitude_M: 4.0;
        Hold_Duration_Sec: 30.0;
        Vortex_Skirt_Rpm: 1200;
        Stabilization_Delta_Bar: 1.35;
    }

    EXECUTE {
        KineticGravity.nullify_inertial_mass(
            target=TargetObject,
            duration_sec=Hold_Duration_Sec
        );

        AeroPressure.set_differential(
            surface_high=TargetObject.BottomSurface,
            surface_low=TargetObject.TopSurface,
            delta_bar=Stabilization_Delta_Bar
        );

        AeroGas.vortex_angular(
            axis_vector=Vector3(0, 1, 0),
            radius_m=TargetObject.BoundingRadius * 1.15,
            rpm=Vortex_Skirt_Rpm
        );

        KineticVector.lock_trajectory(
            target=TargetObject,
            vector=Operator.PointingVector,
            max_deviation_deg=5.0
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            AeroPressure.set_differential(
                surface_high=TargetObject.BottomSurface,
                surface_low=TargetObject.TopSurface,
                delta_bar=1.05
            );
            SafeAbort.collapse_confinement_inward(envelope=TargetObject);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Levitar [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Superar Obstáculos (con `[✨] Control`):** Cruzar abismos, transportar heridos en camillas neumáticas, elevarse verticalmente hasta un balcón o trasladar cargas pesadas (<250 kg) sin fatiga física.
  2. **Crear una Ventaja (con `[✨] Control`):** Colocar aspectos como `[Cajón Blindado Flotante de Cobertura]`, `[Suspendido a Salvo del Suelo Electrificado]` o `[Desarmado Flotante a Distancia]`.
* **Bonificador por Afinidad Elemental (Aire):**
  * Si el Especialista tiene afinidad nativa con **Aire**, el peso máximo se eleva a **400 kg** o puede mover dos objetos ligeros simultáneamente.
* **Margen de Fallo:**
  * Si se falla con un margen de -3 o más, el faldón de vórtice colapsa bruscamente; el objeto cae al suelo de forma descontrolada infligiendo 2 casillas de estrés físico al entorno inmediato.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Compendio de Artefactos de Neoterra]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
