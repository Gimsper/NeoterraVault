### {{NUMERO}}. {{EMOJI}} {{NOMBRE_SECUENCIA}} (`{{IDENTIFICADOR_RUESCRIPT}}`)

#### Dilema Físico y Análisis de Ingeniería:
{{EXPLICACION_DEL_DILEMA_FISICO_Y_POR_QUE_FALLARIA_LA_FISICA_INGENUA}}
* **Solución del Código:** {{DESCRIPCION_DE_LA_SOLUCION_ALGORITMICA}}
* **Pautas para el GM en Mesa:** {{LIMITES_RIGIDOS_ADJUDICACION_EXPLOITS_Y_CONTRAMEDIDAS}}

#### Código Fuente Completo con Comentarios de Ingeniería:
```python
IMPORT RuneScript.Elements.{{MODULO}} AS {{ALIAS}};
IMPORT RuneScript.Geometry.{{MODULO}} AS {{ALIAS}};
IMPORT RuneScript.Kinetics.{{MODULO}} AS {{ALIAS}};
IMPORT RuneScript.Safety.{{MODULO}} AS {{ALIAS}};

SEQUENCE {{NOMBRE_CAMELCASE}}(Target: {{TIPO_TARGET}}) {
    HEADER {
        Rank: "{{RANGO}}";
        Affinity: "{{AFINIDAD}}";
        Control_Threshold: {{NIVEL_CONTROL}};
        Recycle: "{{CICLO}}";
        Complexity: "{{BIG_O}}";
        Throughput: "{{FLUJO}} kR/s";
    }

    PARAMETERS {
        {{PARAMETROS_COMENTADOS}}
    }

    EXECUTE {
        # PASO 1: {{EXPLICACION_PASO_1}}
        {{LINEA_1}}

        # PASO 2: {{EXPLICACION_PASO_2}}
        {{LINEA_2}}

        # PASO 3: {{EXPLICACION_PASO_3}}
        {{LINEA_3}}
    }

    SAFETY_OVERFLOW {
        ON Control_Failure:
            # {{MITIGACION_DE_EMERGENCIA}}
            {{LINEA_SAFETY}}
    }
}
```
