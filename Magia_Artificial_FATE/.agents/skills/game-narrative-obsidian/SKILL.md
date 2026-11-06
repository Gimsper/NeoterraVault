---
name: game-narrative-obsidian
description: >-
  Diseña, estructura y expande la narrativa, mundo, personajes, misiones y diálogos de un videojuego utilizando el sistema de notas enlazadas de Obsidian (Markdown, frontmatter YAML, wikilinks [[...]], MOCs y Dataview). Usa esta skill cuando el usuario quiera crear lore, diseñar personajes, estructurar tramas, redactar misiones ramificadas, o construir la biblia narrativa de un videojuego en Obsidian.
---

# Game Narrative Design System (Obsidian Vault)

Esta skill proporciona los estándares, convenciones y flujos de trabajo para diseñar la arquitectura narrativa completa de un videojuego utilizando notas hipervinculadas en Obsidian.

---

## 1. Convenciones Estrictas de Obsidian

Al crear o modificar cualquier documento narrativo en el vault, debes aplicar las siguientes reglas:

1. **Wikilinks Obligatorios**:
   - Cada entidad clave (personaje, facción, lugar, misión, objeto o concepto de lore) **debe** escribirse como un wikilink: `[[Nombre Exacto de la Nota]]`.
   - Si se necesita variar la gramática o el género en el texto, usa alias: `[[Elandor|del propio Elandor]]`.
   - Para citar secciones específicas: `[[Reino de Solaris#El Gran Cisma]]`.
   - Para embeber fragmentos (transclusión): `![[Nombre de Nota#Resumen]]`.

2. **Frontmatter YAML Estandarizado**:
   - Toda nota debe comenzar con un bloque YAML cerrado entre `---`.
   - Campos mínimos universales:
     ```yaml
     ---
     title: "Nombre legible"
     type: [personaje | faccion | lugar | mision | lore | dialogo | moc]
     tags:
       - narrativa/<tipo>
     aliases: []
     status: [borrador | revisado | final]
     created: YYYY-MM-DD
     updated: YYYY-MM-DD
     ---
     ```

3. **Atomicidad (Notas Atómicas)**:
   - Una entidad o evento significativo por nota. No agrupar varios personajes o misiones en un único archivo extenso; en su lugar, crear notas individuales y enlazarlas a través de un **MOC (Map of Content)**.

4. **Compatibilidad con Dataview**:
   - Usar pares `clave:: valor` o propiedades frontmatter para permitir tablas y listas dinámicas automáticas dentro de Obsidian.

---

## 2. Taxonomía de Carpetas Recomendada

```text
00_MOCs/                 # Índices temáticos (MOC - General, MOC - Personajes, etc.)
01_Mundo_y_Lore/        # Historia, cosmología, facciones, magia/tecnología, religión
02_Personajes/          # Fichas de personajes (protagonistas, antagonistas, NPCs)
03_Lugares/             # Geografía, reinos, regiones, ciudades, mazmorras
04_Misiones_y_Trama/    # Arcos narrativos, misiones principales, secundarias, finales
05_Objetos_y_Lore_Items/# Reliquias, documentos in-game, equipo narrativo
06_Dialogos/            # Árboles de diálogo, interacciones ramificadas
Templates/              # Plantillas maestras Markdown para creación rápida
```

---

## 3. Protocolos de Creación por Tipo de Entidad

### A. Personajes (`02_Personajes/`)
- **Objetivo**: Ficha psicológica, funcional y relacional del personaje.
- **Campos YAML obligatorios**: `rol` (protagonista, antagonista, npc_aliado, mercader, etc.), `faccion` (`[[Facción]]`), `ubicacion_habitual` (`[[Lugar]]`), `estado` (vivo, muerto, desaparecido).
- **Secciones clave**:
  - **Concepto / Logline**: Definición en una frase.
  - **Motivación y Conflicto**: Qué desea, qué necesita, qué teme.
  - **Relaciones de Red**: Enlaces directos a otros personajes (`aliado_de: [[Personaje]]`, `rival_de: [[Personaje]]`, `subordinado_a: [[Personaje]]`).
  - **Misiones Asociadas**: Enlaces a las misiones en las que participa o que otorga.

### B. Lugares (`03_Lugares/`)
- **Objetivo**: Espacios físicos, atmósfera y conexiones de juego.
- **Campos YAML obligatorios**: `region_padre` (`[[Region Mayor]]`), `controlado_por` (`[[Faccion]]`), `peligro` (1-5 o pacífico).
- **Secciones clave**:
  - **Navegación / Rutas**: `conecta_al_norte: [[Lugar]]`, `entrada_a: [[Mazmorra]]`.
  - **Atmósfera y Puntos de Interés (POIs)**.
  - **Eventos y Encuentros Narrativos**.

### C. Misiones y Decisiones Ramificadas (`04_Misiones_y_Trama/`)
- **Objetivo**: Documentar misiones principales y secundarias con lógica de videojuegos.
- **Campos YAML obligatorios**: `arco` (`[[Arco Principal]]`), `dada_por` (`[[NPC]]`), `tipo_mision` (principal, secundaria, encargo), `prerrequisitos` (`[[Mision Anterior]]`), `desbloquea` (`[[Siguiente Mision]]`).
- **Estructura de Ramificación**:
  - **Premisa**: Detonante narrativo.
  - **Objetivos paso a paso**.
  - **Puntos de Elección (Branching Points)**:
    - *Opción A*: Consecuencia inmediata + Enlace a `[[Consecuencia A]]` o `[[Faccion X]]` (+Reputación).
    - *Opción B*: Consecuencia inmediata + Enlace a `[[Consecuencia B]]` o `[[Faccion Y]]`.
  - **Recompensas**: Objetos `[[Item]]`, revelaciones de lore `[[Lore]]`, o acceso a nuevas zonas `[[Lugar]]`.

### D. Facciones y Lore (`01_Mundo_y_Lore/`)
- **Campos YAML**: `lider` (`[[Personaje]]`), `sede` (`[[Lugar]]`), `ideologia`.
- **Estructura**: Doctrina, historia del origen, relaciones diplomáticas (`en_guerra_con`, `aliados`).

### E. Árboles de Diálogo (`06_Dialogos/`)
- Formato estructurado para exportación a motores (Godot Dialogue Manager, Twine, Ink o Unity Yarn Spinner):
  - ID de nodo (`nodo_01`).
  - Requisito de entrada (e.g. `requiere: [[Item Llave]]` o `reputacion_con([[Facción]]) >= 50`).
  - Opciones de respuesta del jugador y enlace al siguiente nodo o consecuencia.

---

## 4. Flujo de Trabajo para Mantener la Red Saludable

Cada vez que se introduzca un nuevo elemento narrativo:
1. **Crear la nota correspondiente** en su carpeta respectiva utilizando su plantilla.
2. **Conectar en ambos sentidos**:
   - Enlazar la nueva nota a las notas existentes que tengan relación.
   - Si la nueva nota menciona entidades que aún no existen, crear el wikilink igualmente (enlace fantasma `[[Entidad Futura]]`) para documentar el grafo.
3. **Actualizar el MOC Temático**:
   - Agregar el enlace de la nueva nota en el MOC correspondiente (e.g., añadir la nueva ciudad en `00_MOCs/MOC - Lugares.md`).
4. **Validación de Consistencia**:
   - Comprobar que no haya paradojas temporales ni contradicciones entre motivaciones de personajes o historia del mundo.

---

## 5. Referencias y Plantillas

Las plantillas maestras listas para usar se encuentran en:
- `resources/templates/template-personaje.md`
- `resources/templates/template-lugar.md`
- `resources/templates/template-mision.md`
- `resources/templates/template-faccion.md`
- `resources/templates/template-lore.md`
- `resources/templates/template-dialogo.md`
