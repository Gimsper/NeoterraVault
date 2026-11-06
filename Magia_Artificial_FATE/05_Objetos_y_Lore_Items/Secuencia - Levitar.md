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
updated: 2026-11-05
---

# 🌪️ Secuencia: Levitar (Rango C)

> *"Una de las primeras lecciones en la academia: el aire tiene masa y el vacío pesa. Si sabes dónde presionar el código, 200 kilos de metal flotan como plumas."*

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: Levitar (Rango C)
CLASIFICACIÓN: S.C.M.E.H. de Manipulación Barométrica / Kinética
================================================================
Afinidad:   Aire
Requisito:  [✨] Control (1)
Recarga:    Usos Infinitos

Acción:
Permite controlar la densidad de objetos y el aire a su alrededor 
para generar una presión diferencial suficiente como para hacerlo 
flotar. Solo funciona en objetos que pesen menos de 250 kg.
================================================================
```

---

## 2. Descripción Operativa
**Levitar** (a menudo llamada coloquialmente *Telekinesis de Rango C*) es una de las secuencias básicas de instrucción que todo novato practica durante su etapa de acondicionamiento. Aunque pertenece al rango inicial, los veteranos reconocen su altísima versatilidad tanto en labores logísticas como en situaciones tácticas imprevistas.

* **Mecánica Física:** Al activarse mediante un [[Artefactos de Ejecución|Artefacto de Ejecución]] (como el [[Artefacto - Little Fox|Little Fox]]), el código polariza las partículas del aire bajo el objeto objetivo, creando un colchón de sustentación localizado y alterando transitoriamente el centro de gravedad del cuerpo.
* **Límite de Carga:** 250 kilogramos métricos. Intentar elevar pesos superiores provoca que el campo de presión colapse de forma inmediata.
* **Frecuencia de Uso:** Diseñada para ciclos estables de baja energía; su recarga es instantánea (*Usos Infinitos*), limitada únicamente por la fatiga del operador.

---

## 3. Implementación en FATE Básico (Proeza de Magia)

En el sistema **FATE Básico**, la secuencia **Levitar** se traduce como una **Proeza activa** vinculada a una ranura de un catalizador:

### Ficha de la Proeza en FATE
* **Nombre de la Proeza:** *S.C.M.E.H. Levitar [Rango C]*
* **Requisito de Activación:** Tener una habilidad de `[✨] Control` a **Mediocre (+1)** o superior, y tenerla cargada en un [[Artefactos de Ejecución|Artefacto]] de **Rango C o superior**.
* **Acciones Permitidas:**
  1. **Superar Obstáculos (con `[✨] Control`):** Permite cruzar abismos, escalar muros o rescatar objetos inalcanzables que pesen hasta 250 kg sin necesidad de herramientas físicas ni tiradas atléticas convencionales.
  2. **Crear una Ventaja (con `[✨] Control`):** Permite colocar aspectos de escena o de objetivo como `[Objeto Flotante de Cobertura]`, `[Suspendido en el Aire]` o `[Desarmado a Distancia]`.
* **Bonificador por Afinidad Elemental (Aire):**
  * Si el [[Los Especialistas|Especialista]] posee un aspecto que refleje **Afinidad con el Aire**, recibe un **+2 a su tirada de `[✨] Control`** al activar esta secuencia, o puede invocar gratuitamente el aspecto creado con éxito regular.
* **Margen de Fallo:**
  * Si se intenta activar sin el `[✨] Control (1)` necesario o con un resultado de dados catastrófico (fallo con margen de -3 o más), el objeto cae abruptamente infligiendo daño de estrés físico al objetivo o al propio usuario.

---

## 4. Entidades Relacionadas
* [[Artefactos de Ejecución]]
* [[Artefacto - Little Fox]]
* [[Secuencias de Hechizos (SCMEH)]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
