---
title: "{{title}}"
type: mision
tipo_mision: principal # principal | secundaria | encargo | evento_aleatorio
arco: "[[Arco Narrativo]]"
dada_por: "[[NPC Dador]]"
lugar_inicio: "[[Lugar Inicio]]"
prerrequisitos:
  - "[[Mision Previa]]"
desbloquea:
  - "[[Mision Siguiente]]"
estado: disponible # bloqueada | disponible | activa | completada | fallida
tags:
  - narrativa/mision
aliases: []
created: {{date}}
updated: {{date}}
---

# {{title}}

> **Resumen del Quest**: Breve descripción del detonante y qué está en juego (apuestas / stakes).

## 1. Contexto Narrativo
- **Detonante (Inciting Incident)**: Qué ocurre para que el jugador se involucre.
- **Intereses en conflicto**: Quién gana y quién pierde según lo que decida el jugador.

## 2. Flujo de Objetivos
1. [ ] **Fase 1**: Hablar con [[NPC Dador]] en [[Lugar Inicio]].
2. [ ] **Fase 2**: Investigar [[Lugar de Pista]] y obtener información sobre [[Lore Relevante]].
3. [ ] **Fase 3**: Enfrentar a [[Enemigo o Desafio]] en [[Lugar del Enfrentamiento]].
4. [ ] **Fase 4 (Punto de Decisión)**: Ver sección de ramificaciones abajo.

## 3. Ramificaciones y Elecciones Morales / Mecánicas

```mermaid
graph TD
    Decision{"Punto de Eleccion: ¿Que hacer?"}
    Decision -->|Opcion A| RutaA["Opcion A: Apoyar a [[Faccion A]]"]
    Decision -->|Opcion B| RutaB["Opcion B: Respaldar a [[Personaje Rebelde]]"]
    Decision -->|Opcion C| RutaC["Opcion C: Solucion Oculta / Negociacion"]

    RutaA --> ConsecuenciaA["Consecuencia A: Desbloquea [[Mision 03A]]"]
    RutaB --> ConsecuenciaB["Consecuencia B: Desbloquea [[Mision 03B]]"]
    RutaC --> ConsecuenciaC["Consecuencia C: Final pacifico y [[Item Reliquia]]"]
```

### Detalle de Opciones:
- **Opción A (Lealtad)**:
  - **Acción**: El jugador entrega el artefacto a [[NPC A]].
  - **Consecuencias**: Reputación positiva con [[Faccion A]], hostilidad con [[Faccion B]].
  - **Desbloquea**: [[Mision Rama A]].
- **Opción B (Traición / Pragmatismo)**:
  - **Acción**: El jugador vende o destruye el artefacto.
  - **Consecuencias**: Reputación positiva con [[Faccion B]], recompensa monetaria inmediata.
  - **Desbloquea**: [[Mision Rama B]].

## 4. Recompensas
- **Narrativas**: Revelación sobre el pasado de [[Personaje Clave]], entrada en el códice [[Lore Secreto]].
- **Mecánicas**: Objeto [[Item Obtenido]], experiencia, acceso al área [[Nueva Zona]].
