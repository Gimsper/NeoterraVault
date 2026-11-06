---
title: "Secuencias de Hechizos (SCMEH)"
type: lore
categoria: magia_tecnologia
relevancia_en_trama: alta
tags:
  - narrativa/lore
  - magia/secuencias
  - tecnologia/software
  - fate/proezas
aliases:
  - SCMEH
  - Secuencias de Hechizos
  - S.C.M.E.H.
  - Secuencias de Código para la Manifestación y Evocación de Hechizos
status: revisado
created: 2026-11-05
updated: 2026-11-05
---

# 📜 Secuencias de Hechizos (S.C.M.E.H.)

> *"Un hechizo no es una plegaria ni un misterio esotérico: es un algoritmo riguroso. Si el código está limpio, el artefacto lo ejecuta; si hay un error de sintaxis, pierdes la mano o fundes el catalizador."*
> — Manual de Instrucción de la Academia de [[Ingenieros y Alquimistas]]

---

## 1. Definición y Naturaleza
Las **Secuencias de Código para la Manifestación y Evocación de Hechizos** (conocidas comúnmente como **Secuencias de Hechizos** o por sus siglas **S.C.M.E.H.**) son la base de la [[Magia Artificial y Reino Olvidado|Magia Artificial]]. Son paquetes de instrucciones lógicas programadas a partir de la observación de las configuraciones rúnicas utilizadas originalmente por los dioses en el [[Magia Artificial y Reino Olvidado|Reino Olvidado]].

---

## 2. Propiedades Fundamentales

```mermaid
mindmap
  root((S.C.M.E.H.))
    Composición Digital
      No se memorizan
      Requiere compilación de [[Ingenieros y Alquimistas]]
      Instalación en [[Artefactos de Ejecución]]
    Chips de Memoria
      Portabilidad física
      Límite de UN SOLO USO
      Sobrecarga del chip al disparar
    Escala de Rangos
      Rango C
      Rango B
      Rango A
      Rango S
      Rango SSS
    Afinidad Elemental
      Sincronía con [[Los Especialistas]]
      Aumento de potencia
      Reducción de dificultad de [✨] Control
```

### A. Composición Digital Inmutable
Las secuencias poseen una naturaleza puramente digital. Ningún [[Los Especialistas|Especialista]] puede "aprenderlas" o memorizarlas de forma tradicional:
* Solo un [[Ingenieros y Alquimistas|Ingeniero o Alquimista]] cualificado posee el instrumental y los permisos de compilación para instalar, reprogramar o afinar secuencias dentro de un [[Artefactos de Ejecución|Artefacto de Ejecución]].

### B. Protocolo de Intercambio: Chips de Memoria
Las secuencias pueden transferirse físicamente mediante **chips de memoria de datos**:
* Permiten cargar una secuencia en un artefacto sin necesidad de acudir inmediatamente a un taller.
* **La gran limitación:** Estos chips sufren desintegración por quemado térmico-mágico durante la descarga; por lo tanto, **solo duran exactamente un único uso** si se comparten de este modo.

### C. Escala de Rangos (C a SSS) y Auditoría Técnica
El rango no es una convención arbitraria: se deduce mediante auditoría de código combinando la **complejidad algorítmica Big-O** con el **flujo bio-mágico (throughput)** que atraviesa los circuitos (véase el compendio técnico en [[Calculo de Rangos SCMEH - Big-O y Flujo]]).
* **Rango C:** Complejidad constante $\mathcal{O}(1)$ y bajo flujo bioeléctrico. Alteraciones físicas locales, campos cinéticos de bajo tonelaje, chispas elementales.
* **Rango B:** Complejidad lineal $\mathcal{O}(n)$ o flujo medio. Balística mágica de asalto, barreras balísticas, manipulación elemental sostenida.
* **Rango A:** Complejidad cuadrática $\mathcal{O}(n^2)$ o flujo alto. Devastación de área, transmutación de materia a gran escala, interferencia climática.
* **Rango S:** Complejidad exponencial $\mathcal{O}(2^n)$, multi-hilo o fusiones elementales. Armamento estratégico de nivel metropolitano.
* **Rango SSS:** Singularidad $\mathcal{O}(n!)$ o flujo crítico. Desgarro del tejido espacial, evocaciones de poder comparable a las runas divinas originales.

### D. Afinidad Elemental y Resonancia
Toda secuencia posee un vector elemental intrínseco (Aire, Fuego, Agua, Tierra, etc.):
* **Sincronía Armónica:** Si la secuencia es disparada por un Especialista con su misma afinidad elemental:
  * **Mayor Potencia:** La escala del daño o alcance aumenta drásticamente.
  * **Menor Dificultad:** El umbral de fatiga o la resistencia de `[✨] Control` se aligera en beneficio del portador.

---

## 3. Estructura Estándar de una Secuencia

Toda ficha técnica de una S.C.M.E.H. sigue este esquema homologado:

```text
Nombre de la Secuencia (Rango)

Afinidad: [Elemento correspondiente o Neutro]
Requisito: [✨] Control (Nivel mínimo requerido)

Acción: [Descripción exacta del algoritmo físico y límites operativos]

Recarga: [Usos Infinitos / Usos por Escena / Sobrecarga]
```

*Ejemplo canónico:* Véase la ficha técnica de **[[Secuencia - Levitar]]**.

---

## 4. Traducción a Reglas de FATE Básico

En **FATE Básico**, las Secuencias de Hechizos son el motor de las **Proezas (Stunts)** y acciones mágicas:

1. **Slots del Artefacto = Proezas Disponibles:** Cada secuencia configurada en un slot de un [[Artefactos de Ejecución|Artefacto de Ejecución]] se comporta como una Proeza activa para el personaje.
2. **Acciones FATE asociadas:**
   * **Superar:** Resolver obstáculos ambientales (e.g. levitar sobre un abismo con [[Secuencia - Levitar]]).
   * **Crear una Ventaja:** Crear aspectos temporales en la escena (e.g. `[Suelo Congelado]`, `[Objetos Suspendidos]`).
   * **Atacar:** Infligir estrés físico o mental según el elemento.
   * **Defender:** Proyectar campos o desviar proyectiles.
3. **Mecánica de Afinidad Elemental:**
   * Proporciona un bonificador pasivo de **+2** al resultado de la acción mágica cuando se actúa dentro del dominio elemental afín, o reduce la dificultad de la tirada de Control en 1 nivel.
4. **Chips de Memoria en FATE:**
   * Se gestionan como **Proezas Consumibles**: otorgan el beneficio de la secuencia durante una sola tirada sin ocupar una ranura fija del artefacto, quemándose inmediatamente tras su resolución.

---

## 5. Entidades Relacionadas
* [[Artefactos de Ejecución]]
* [[Los Especialistas]]
* [[Magia Artificial y Reino Olvidado]]
* [[Ingenieros y Alquimistas]]
* [[Secuencia - Levitar]]
* [[Reglas FATE - Sistema de Magia Artificial]]
