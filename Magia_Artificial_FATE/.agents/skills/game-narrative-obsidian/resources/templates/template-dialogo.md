---
title: "{{title}}"
type: dialogo
interlocutor_principal: "[[Personaje NPC]]"
ubicacion_escena: "[[Lugar]]"
mision_relacionada: "[[Mision Relacionada]]"
condicion_activacion: "primera_vez" # primera_vez | tras_mision | repetible | item_requerido
tags:
  - narrativa/dialogo
aliases: []
created: {{date}}
updated: {{date}}
---

# {{title}}

> **Contexto de la conversación**: Estado anímico del NPC, objetivo de la conversación y tensión dramática.

```mermaid
graph TD
    Start["[INICIO] Saludo de [[Personaje NPC]]"] --> Choice{"Opciones del Jugador"}
    Choice -->|Pregunta Amable| RespA["Respuesta Calida"]
    Choice -->|Pregunta Hostil| RespB["Respuesta Defensiva"]
    Choice -->|Pregunta de Lore| RespC["Exposicion Narrativa"]
    
    RespA --> Node_02["Siguiente Nivel de Conversacion"]
    RespB --> Node_Exit["El NPC corta el dialogo"]
    RespC --> Node_02
```

---

## Nodo: `[inicio]`
**[[Personaje NPC]]**:
> *"Línea de diálogo inicial o reacción al ver al jugador."*

**Opciones del Jugador**:
- **1. [Diplomático]** *"Línea de opción cordial."* $\rightarrow$ Ir a `[nodo_diplomatico]`
- **2. [Directo / Hostil]** *"Línea de opción exigente."* $\rightarrow$ Ir a `[nodo_hostil]`
- **3. [Requisito: [[Item Reliquia]]]** *"He encontrado esto en las ruinas..."* $\rightarrow$ Ir a `[nodo_recompensa]`

---

## Nodo: `[nodo_diplomatico]`
**[[Personaje NPC]]**:
> *"Respuesta abierta y colaborativa..."*

- **Desencadena**: Actualización en [[Mision Relacionada]], suma reputación con [[Faccion NPC]].

---

## Nodo: `[nodo_hostil]`
**[[Personaje NPC]]**:
> *"Respuesta cortante o amenaza..."*

- **Desencadena**: El NPC se niega a comerciar temporalmente.

---

## Nodo: `[nodo_recompensa]`
**[[Personaje NPC]]**:
> *"¡No puedo creer que lo tengas! Esto lo cambia todo..."*

- **Desencadena**: Completa objetivo en [[Mision Relacionada]], otorga recompensa.
