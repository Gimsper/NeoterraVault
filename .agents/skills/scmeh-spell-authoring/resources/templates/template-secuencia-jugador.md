---
title: "Secuencia - {{NOMBRE_SECUENCIA}}"
type: objeto
categoria: magia/secuencia
rango: "{{RANGO_C_B_A_S}}"
afinidad: "{{AFINIDAD_ELEMENTAL}}"
control_requerido: {{NIVEL_CONTROL}}
tags:
  - magia/secuencia
  - rango/{{RANGO_MINUSCULA}}
  - afinidad/{{AFINIDAD_MINUSCULA}}
  - objeto
  - fate/proeza
aliases:
  - {{ALIAS_1}}
  - {{ALIAS_2}}
  - Secuencia {{NOMBRE_SECUENCIA}}
status: revisado
created: {{FECHA}}
updated: {{FECHA}}
---

# {{EMOJI}} Secuencia: {{NOMBRE_SECUENCIA}} (Rango {{RANGO_C_B_A_S}})

> *"{{CITA_LORE_IN_UNIVERSE}}"*
> — {{AUTOR_DE_LA_CITA}}

---

## 1. Ficha Técnica Oficial (S.C.M.E.H.)

```text
================================================================
NOMBRE: {{NOMBRE_SECUENCIA}} (Rango {{RANGO_C_B_A_S}})
CLASIFICACIÓN: S.C.M.E.H. de {{CLASIFICACION_TECNICA}}
================================================================
Afinidad:    {{AFINIDAD_ELEMENTAL}}
Requisito:   [✨] Control ({{NIVEL_CONTROL}})
Recarga:     {{CICLO_RECARGA}}
Complejidad: {{BIG_O}}
Flujo:       {{FLUJO_KR_S}} kR/s

Acción:
{{RESUMEN_ACCION_CONCISO}}
================================================================
```

---

## 2. Descripción Operativa y Principios Físicos

{{DESCRIPCION_OPERATIVA_DIRECTA}}

### Principios de {{PRINCIPIO_FISICO_1}} y {{PRINCIPIO_FISICO_2}}
{{EXPLICACION_TECNICA_AUTORITARIA_SIN_PREGUNTAS}}

1. **Fase 1 — {{NOMBRE_FASE_1}}:** {{DESCRIPCION_FASE_1}}
2. **Fase 2 — {{NOMBRE_FASE_2}}:** {{DESCRIPCION_FASE_2}}
3. **Fase 3 — {{NOMBRE_FASE_3}}:** {{DESCRIPCION_FASE_3}}

---

## 3. Código Algorítmico Oficial (RuneScript)

```python
IMPORT RuneScript.Elements.{{MODULO}} AS {{ALIAS}};
IMPORT RuneScript.Geometry.{{MODULO}} AS {{ALIAS}};
IMPORT RuneScript.Kinetics.{{MODULO}} AS {{ALIAS}};
IMPORT RuneScript.Safety.{{MODULO}} AS {{ALIAS}};

SEQUENCE {{NOMBRE_CAMELCASE}}(Target: {{TIPO_TARGET}}) {
    HEADER {
        Rank: "{{RANGO_C_B_A_S}}";
        Affinity: "{{AFINIDAD_ELEMENTAL}}";
        Control_Threshold: {{NIVEL_CONTROL}};
        Recycle: "{{CICLO_RECARGA}}";
        Complexity: "{{BIG_O}}";
        Throughput: "{{FLUJO_KR_S}} kR/s";
    }

    PARAMETERS {
        {{PARAM_1}}: {{VALOR_1}};
        {{PARAM_2}}: {{VALOR_2}};
    }

    EXECUTE {
        {{INSTRUCCIONES_SIN_COMENTARIOS_NUMERADOS}}
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            {{INSTRUCCIONES_DE_SEGURIDAD}}
    }
}
```

---

## 4. Implementación en FATE Básico (Proeza de Magia)

* **Nombre de la Proeza:** *S.C.M.E.H. {{NOMBRE_SECUENCIA}} [Rango {{RANGO_C_B_A_S}}]*
* **Requisito de Activación:** Tener `[✨] Control` a **{{NIVEL_FATE}}** o superior, y cargada en un [[Artefactos de Ejecución|Artefacto]].
* **Acciones Permitidas:**
  1. **{{ACCION_1}} (con `[✨] Control`):** {{DETALLE_ACCION_1}}
  2. **{{ACCION_2}} (con `[✨] Control`):** {{DETALLE_ACCION_2}}
* **Bonificador por Afinidad Elemental ({{AFINIDAD_ELEMENTAL}}):**
  * Si el Especialista tiene afinidad con **{{AFINIDAD_ELEMENTAL}}**, recibe un **+2 a la tirada de `[✨] Control`** o {{BENEFICIO_EXTRA}}.
* **Margen de Fallo:**
  * Si se falla por 3 o más puntos, {{CONSECUENCIA_DE_FALLO}}.

---

## 5. Entidades Relacionadas
* [[Compendio de Secuencias SCMEH - Rango {{RANGO_C_B_A_S}}]]
* [[Compendio de Librerias Elementales SCMEH]]
* [[Artefactos de Ejecucion]]
* [[Los Especialistas]]
* [[Reglas FATE - Sistema de Magia Artificial]]
