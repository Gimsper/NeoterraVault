---
title: "Secuencia - Mechero Térmico Táctico"
type: objeto
categoria: magia/secuencia
rango: "C"
afinidad: "Fuego"
control_requerido: 1
tags:
  - magia/secuencia
  - rango/c
  - afinidad/fuego
  - objeto
  - fate/proeza
aliases:
  - Mechero Térmico
  - Ignición Táctica
  - Cortador Térmico Quirúrgico
  - Secuencia Mechero Térmico Táctico
status: revisado
created: 2026-11-08
updated: 2026-11-08
---

# 🔥 Secuencia: Mechero Térmico Táctico (Rango C)

> *"Cualquier novato puede encender una llamarada y quemarse los dedos. Un profesional proyecta una aguja colimada de cuatrocientos cincuenta grados envuelta en un gradiente adiabático: cortas una brida de polímero pegada a la piel de tu muñeca y tu carne ni siquiera siente calor."*
> — Protocolos de Infiltración y Escape, Null-Sector

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Mechero Térmico Táctico (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Colimación Térmica y Aislamiento Adiabático
================================================================
Afinidad:    Fuego
Requisito:   [✨] Control (1)
Recarga:     Usos Infinitos
Complejidad: O(1)
Flujo:       2.5 kR/s

Acción:
Colima la agitación cinética microscópica en un microhaz cilíndrico 
de 2 mm de grosor a 450 °C, confinado por una funda adiabática que 
evita la disipación térmica hacia la piel o materiales adyacentes.
================================================================
```

---

## 2. Descripción Operativa y Física de Micro-Corte

A diferencia de las secuencias piroquinéticas militares diseñadas para inflamar áreas amplias, el **Mechero Térmico Táctico** es una herramienta de microingeniería térmica de precisión. Su objetivo es cortar, fundir o encender con exactitud milimétrica sin generar destellos visibles ni quemaduras accidentales al operador.

### Arquitectura de Colimación y Aislamiento Adiabático
Para operar a distancias milimétricas de la piel sin causar daño térmico colateral, la secuencia implementa un doble mecanismo de protección:

1. **Aislamiento por Gradiente Térmico Inverso (`PyroThermal.set_thermal_gradient`):** Antes de iniciar la excitación térmica, el algoritmo crea una micro-barrera de aire inmóvil alrededor del punto de corte con una caída térmica radical ($\Delta K = 400\text{ K}$ en apenas 3 milímetros). La energía no puede propagarse lateralmente hacia la piel.
2. **Colimación en Haz Cilíndrico (`Confinement.bind_cylinder`):** Modula el campo en una aguja térmica lineal de 2 milímetros de diámetro por 15 milímetros de largo. Toda la vibración molecular queda encerrada en este canal.
3. **Excitación de Enlaces Moleculares (`PyroThermal.excite_molecules`):** Eleva la temperatura del material objetivo a 450 °C en 0.2 segundos. Si es polímero, nylon o tela sintética, rompe las cadenas poliméricas por pirólisis casi instantánea; si es madera o mecha de pólvora, inicia una combustión química controlada (`PyroCombustion.ignite_mix`).
4. **Corte Automático por Desacople de Impedancia:** En cuanto la soga o brida se parte (desconexión física de la masa continua), el algoritmo detecta la caída de carga térmica y apaga la aguja inmediatamente, evitando quemar la ropa inferior.

---

## 3. Código Algorítmico Oficial (RuneScript)

```python

IMPORT RuneScript.Elements.Fire.Thermal AS PyroThermal;
IMPORT RuneScript.Elements.Fire.Combustion AS PyroCombustion;
IMPORT RuneScript.Geometry.Confinement AS Confinement;
IMPORT RuneScript.Safety.Vent AS SafeVent;

SEQUENCE MecheroTermico(TargetPoint: Point) {
    HEADER {
        Rank: "C";
        Affinity: "Fire";
        Control_Threshold: 1;
        Recycle: "Infinite";
        Complexity: "O(1)";
        Throughput: "2.5 kR/s";
    }

    PARAMETERS {
        Beam_Diameter_Mm: 2.0;
        Beam_Length_Mm: 15.0;
        Operating_Temp_C: 450.0;
        Insulation_Delta_K: 400.0;
    }

    EXECUTE {
        PyroThermal.set_thermal_gradient(
            from_point=TargetPoint,
            to_point=TargetPoint.Offset(3.0.mm),
            delta_k=Insulation_Delta_K
        );

        BeamEnvelope = Confinement.bind_cylinder(
            target_core=TargetPoint,
            length_m=0.015,
            radius_m=0.001
        );

        PyroThermal.excite_molecules(
            target_zone=BeamEnvelope,
            temp_celsius=Operating_Temp_C
        );

        PyroCombustion.ignite_mix(
            flammable_target=TargetPoint,
            oxygen_ratio=0.21
        );
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            SafeVent.shunt_heat_to_atmosphere(joules=250.0);
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. Mechero Térmico Táctico [Rango C]*
* **Requisito de Activación:** Tener `[✨] Control` a **Mediocre (+1)** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **Superar Obstáculos (con `[✨] Control`):** Liberarse de esposas plásticas, cuerdas o alambres delgados sin sufrir daño por quemadura, derretir cerraduras de policarbonato o encender mechas y fogatas en condiciones de viento hostil.
  2. **Crear una Ventaja (con `[✨] Control`):** Colocar aspectos situacionales como `[Amarras Quirúrgicamente Fundidas]`, `[Mecha Encendida a Tiempo]` o `[Bisagra Desoldada]` con 1 invocación gratuita.
* **Bonificador por Afinidad Elemental (Fuego):**
  * Si el Especialista tiene afinidad con **Fuego**, la temperatura puede elevarse a 650 °C, permitiendo cortar alambres de cobre dulce o mallas metálicas delgadas sin penalización de tiempo.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango C]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefacto - Little Fox]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
