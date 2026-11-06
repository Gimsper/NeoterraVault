---
title: "Artefactos de Ejecución"
type: lore
categoria: magia_tecnologia
relevancia_en_trama: alta
tags:
  - narrativa/lore
  - tecnologia/artefactos
  - magia_artificial
  - fate/equipo
aliases:
  - Artefactos de Ejecución
  - Artefactos de Ejecucion
  - Artefactos Catalizadores
  - Artefactos Pseudo-Mágicos
  - Catalizador
status: revisado
created: 2026-11-05
updated: 2026-11-05
---

# 📱 Artefactos de Ejecución

> *"Un Especialista sin Artefacto es una batería sin circuito: solo almacena energía estática. El Artefacto es el compilador, la lente y el gatillo que traduce la vida en milagros programados."*

---

## 1. Naturaleza y Propósito
Los **Artefactos de Ejecución** (también conocidos como *Artefactos Catalizadores* o *Artefactos Pseudo-Mágicos*) son dispositivos electro-rúnicos desarrollados por la raza humana hace mucho tiempo como complemento indispensable para que su creación, [[Los Especialistas]], pudiera manifestar la [[Magia Artificial y Reino Olvidado|Magia Artificial]].

Funcionan físicamente como un almacén de hardware y firmware donde se guardan las **[[Secuencias de Hechizos (SCMEH)]]**, dotadas de instrucciones analíticas precisas que se activan mediante la resonancia bioenergética del usuario.

---

## 2. Jerarquía de Rangos

Tanto los Artefactos de Ejecución como las Secuencias de Hechizos se clasifican en una escala estricta de cinco rangos, ordenada de menor a mayor potencia destructiva y complejidad técnica:

```mermaid
graph LR
    C["🥉 Rango C (Básico / Principiante)"] --> B["🥈 Rango B (Militar / Intermedio)"]
    B --> A["🥇 Rango A (Avanzado / Élite)"]
    A --> S["💎 Rango S (Maestro / Estratégico)"]
    S --> SSS["👑 Rango SSS (Calamidad / Singularidad)"]
```

1. **Rango C:** Dispositivos introductorios, civiles o de entrenamiento militar inicial. Estructura simple y segura.
2. **Rango B:** Artefactos estándar para fuerzas de asalto y especialistas veteranos.
3. **Rango A:** Equipamiento de alta gama, fabricado por maestros [[Ingenieros y Alquimistas]]. Capaces de manejar flujos de energía severos.
4. **Rango S:** Tecnologías raras y prototipos de grado militar clasificado o gubernamental.
5. **Rango SSS:** Artefactos legendarios o singulares, creados con aleaciones puras del Reino Olvidado. Capaces de alterar el mapa geográfico.

---

## 3. Sistema de Ranuras (Slots) y Retrocompatibilidad

### A. Ranuras de Memoria (Slots)
Cada artefacto dispone de un número limitado de **ranuras o slots** según su rango constructivo y su calidad de forja:
* En cada ranura se puede alojar exactamente una [[Secuencias de Hechizos (SCMEH)|Secuencia de Hechizo]].
* Por ejemplo, el catalizador de iniciación **[[Artefacto - Little Fox|Little Fox (Rango C)]]** posee 3 slots de Rango C:
  * *Slot #1:* (Nombre de la Secuencia)
  * *Slot #2:* (Nombre de la Secuencia)
  * *Slot #3:* (Nombre de la Secuencia)

### B. Ley de Compatibilidad Descendente
Un Artefacto de Ejecución puede almacenar y compilar secuencias de su **mismo rango y de rangos inferiores**:
* Un artefacto de **Rango A** puede albergar secuencias de **Rango A, B y C**, siempre que el [[Los Especialistas|Especialista]] posea el nivel de `[✨] Control` requerido para activarlas.
* **Prohibición Ascendente:** Un artefacto nunca puede ejecutar de forma segura una secuencia de rango superior al suyo.

---

## 4. Requisitos de Activación y Protocolos de Seguridad

Para activar una secuencia sin comprometer la vida del usuario ni destruir el entorno circundante, deben cumplirse dos condiciones estrictas:

```text
Condición 1: Rango(Artefacto) >= Rango(Secuencia)
Condición 2: [✨] Control(Usuario) >= [✨] Control_Requerido(Secuencia)
```

| Factor Crítico | Regla de Activación | Consecuencia en caso de Incumplimiento |
| :--- | :--- | :--- |
| **Rango del Artefacto** | Debe ser igual o superior al de la secuencia cargada. | **Fallo Crítico del Hardware:** El artefacto sufre errores de compilación, sobrecalentamiento, bloqueo de memoria o destrucción total de sus micro-circuitos. |
| **Capacidad del Usuario** | Debe poseer un valor de `[✨] Control` igual o mayor al exigido. | **Fallo Crítico Bio-mágico:** El Especialista sufre retroceso energético, quemaduras sinápticas o detonaciones incontroladas en su entorno inmediato. *(Los Alquimistas e Ingenieros declinan toda responsabilidad).* |

---

## 5. Implementación en FATE Básico

En las mesas de juego de rol con **FATE Básico**, los Artefactos de Ejecución se tratan como **Extras de Equipo** con slots de Proezas (Stunts):

### Anatomía de un Artefacto en FATE
* **Nombre del Extra:** Nombre del modelo y su rango (ej. *Catalizador Portátil [[Artefacto - Little Fox|Little Fox]] [Rango C]*).
* **Aspecto del Artefacto:** Aspecto propio que describe su fabricación o estado (ej. *Resistente pero Básico*, *Circuitería de Cobre Refinado*). Puede ser invocado para beneficiar tiradas de canalización o forzado por el DJ si el artefacto sufre daños mecánicos.
* **Capacidad de Ranuras:** Dicta cuántas secuencias activas puede llevar el personaje listas para su uso.
* **Estrés / Consecuencias de Equipo (Opcional):**
  * Si un jugador fuerza una secuencia de rango mayor a la de su artefacto, el artefacto absorbe daño o recibe la Consecuencia Leve/Moderada: `[Sobrecarga de Circuitos]` o `[Catalizador Inutilizado]`.

---

## 6. Entidades Relacionadas
* [[Magia Artificial y Reino Olvidado]]
* [[Los Especialistas]]
* [[Secuencias de Hechizos (SCMEH)]]
* [[Ingenieros y Alquimistas]]
* [[Artefacto - Little Fox]]
* [[Reglas FATE - Sistema de Magia Artificial]]
