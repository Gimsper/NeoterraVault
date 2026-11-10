#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
========================================================================================
AEGIS-OS v4.12 // TERMINAL DE BIOCONTENCIÓN MÓVIL HAZMAT-07
Script interactivo para jugadores y directores de juego (NeoterraVault)
========================================================================================
"""

import os
import sys
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.005):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def header():
    clear_screen()
    print("=" * 80)
    print("  AEGIS FOUNDRY // SISTEMA DE CONTROL DE TELEMETRÍA CRIOGÉNICA")
    print("  TERMINAL HAZMAT-07 // BASE LOGÍSTICA SUBTERRÁNEA - HANGAR 4")
    print("  ESTADO DE RED: ENLACE MILITAR ENCRIPTADO [FED-NET // NODO 04]")
    print("=" * 80)
    print()

def menu():
    header()
    print("  [1] ESTADO TELEMÉTRICO DEL MÓDULO (PRESION / TEMPERATURA)")
    print("  [2] REGISTRO DE PERSONAL ASIGNADO (SUPERVISORES)")
    print("  [3] DATOS DEL ACTIVO EN TRÁNSITO (ESPECÍFICO DE CARGA)")
    print("  [4] HISTORIAL CRONOLÓGICO DE EVENTOS // PROGRAMA SILENTE")
    print("  [5] DESCARGAR REGISTROS A DISPOSITIVO PORTÁTIL (LITTLE FOX)")
    print("  [0] BLOQUEAR Y APAGAR CONSOLA")
    print("-" * 80)

def screen_1():
    header()
    print(">> PANTALLA 1: ESTADO TELEMÉTRICO DEL MÓDULO HAZMAT-07\n")
    print("  ESTADO GENERAL:                 [!] CRÍTICO // ALERTA NIVEL ROJO")
    print("  PRESIÓN EN CÁMARA PRIMARIA:     0.38 bar (NOMINAL: 1.20 bar) [FALLO DE PRESIÓN]")
    print("  TEMPERATURA INTERNA DEL NÚCLEO: -42.8 °C (NOMINAL: -140.0 °C) [ALZA TÉRMICA]")
    print("  LÍNEAS DE REFRIGERANTE ÉTER:    DESPRESURIZADAS [VÁLVULA D-4 FORZADA]")
    print("  AMORTIGUADORES DE BAQUELITA:    SATURADOS AL 100% [RESONANCIA NO ABSORBIDA]")
    print()
    print("  REGISTRO DE FALLAS DETECTADAS EN SECUENCIA:")
    print("  [02:18:04 UTC] Resonancia de baja frecuencia satura amortiguadores de cuarzo.")
    print("  [02:22:50 UTC] Desconexión de constantes vitales en terminal de control.")
    print("  [02:23:01 UTC] Telemetría de operadores: Trance cataléptico // EEG plano sin trauma.")
    print("  [02:30:15 UTC] Fuga de nitrógeno criogénico en esclusa de Hangar 4.")
    print()
    input("Presiona [ENTER] para regresar al menú principal...")

def screen_2():
    header()
    print(">> PANTALLA 2: REGISTRO DE PERSONAL ASIGNADO\n")
    print("  SUPERVISOR JEFE:   Dr. Lucian Aris (ID: AEG-BIO-4409)")
    print("  ESPECIALIDAD:      Bio-resonancia de Cuarzo y Estabilidad Sináptica")
    print("  ESTADO VITAL:      INCONSCIENTE // TRANCE CATALÉPTICO // PULSO: 28 PPM")
    print()
    print("  TÉCNICO ASOCIADO:  Mark Cole (ID: AEG-ENG-1182)")
    print("  ESPECIALIDAD:      Ingeniería de Sellado Criogénico y Matrices Rúnicas")
    print("  ESTADO VITAL:      INCONSCIENTE // TRANCE CATALÉPTICO // PULSO: 30 PPM")
    print()
    print("-" * 80)
    print("  DIAGNÓSTICO MÉDICO PRELIMINAR (AUTORIZADO POR SENSORES DE CABINA):")
    print("  «Sujetos humanos expuestos a proximidad no apantallada. Ausencia total de")
    print("   lesiones traumáticas o hemorragias. Ausencia de estrés cardíaco. Actividad")
    print("   neuronal sincronizada en frecuencia armónica uniforme. Diagnóstico preliminar:")
    print("   Absorción sináptica inducida por frecuencia madre».")
    print("-" * 80)
    print()
    input("Presiona [ENTER] para regresar al menú principal...")

def screen_3():
    header()
    print(">> PANTALLA 3: DATOS DEL ACTIVO EN TRÁNSITO\n")
    print("  DESIGNACIÓN DE SUJETO:  Espécimen Aguja-04")
    print("  ORIGEN DE CAPTURA:      Sector Suroeste 07 (Convoy Minero Pesado de Xenoferrita)")
    print("  FECHA DE INGRESO:       2026-11-08 :: 01:17:42 UTC")
    print("  MATERIA PREDOMINANTE:   Biometal líquido de níquel / Placas de obsidiana sónica fractal")
    print("  FRECUENCIA EMITIDA:     Bordón armónico de baja frecuencia (14.2 Hz) + Cuarzo sónico")
    print()
    print("  NOTAS DE BITÁCORA (DR. ARIS):")
    print("  «El espécimen no responde a los supresores cinéticos estándar. El frío extremo a -140 °C")
    print("   logró ralentizar la modulación de sus agujas dactilares durante la carga en el Sector")
    print("   Suroeste, pero la interacción con los umbilicales de éter de la base militar parece")
    print("   haber activado su antena central. Solicito refuerzos de la Guardia de Especialistas")
    print("   antes de autorizar la apertura de compuertas».")
    print()
    input("Presiona [ENTER] para regresar al menú principal...")

def screen_4():
    header()
    print(">> PANTALLA 4: HISTORIAL CRONOLÓGICO DE EVENTOS // PROGRAMA SILENTE\n")
    print("  CLASIFICACIÓN: MÁXIMO SECRETO // ARCHIVO CENTRAL DE CORRELACIÓN\n")
    
    events = [
        ("INC-07", "2025-12-14 :: 19:22:04 UTC", "Cuadrante Este 04-A (Asentamiento Agrario / Puesto Fronterizo)",
         "Aguja-01 (Incompleto)", "48 civiles en reposo cataléptico indoloro.",
         "«Intoxicación masiva por fisura en tanques de fertilizante agrícola».",
         "Fracaso de extracción; espécimen disuelto por incineración de seguridad."),
        
        ("INC-11", "2026-02-28 :: 04:15:33 UTC", "Sector Norte 08-C (Línea Ferroviaria de Ferrita)",
         "Vector Cuna-01 / Aguja-02", "Escolta militar silenciada (14 soldados regulares sin respuesta).",
         "«Descarrilamiento ferroviario por sabotaje de células insurgentes».",
         "Recuperación parcial de residuos de cuarzo negro. Catalizadores fundidos."),
        
        ("INC-14", "2026-05-12 :: 23:48:11 UTC", "Sector Sur 14-B (Caravana Civil de Reasentamiento)",
         "Aguja-03", "62 civiles silenciados; 4 operadores de trinchera con shock bio-eléctrico.\n                     * Registro Clínico Cruzado: Veterano Evergarden, R. (Daño pulmonar por éter).",
         "«Explosión accidental de convoy clandestino de combustible».",
         "Fallo de contención criogénica en tránsito; pérdida del espécimen tras deflagración."),
        
        ("INC-16", "2026-08-19 :: 11:05:50 UTC", "Cuadrante Central-Sur 02 (Estación de Transmisión Subterránea)",
         "Firma de resonancia múltiple (No asegurada)", "9 ingenieros de telecomunicaciones en estado silente.",
         "«Fallo estructural por deslizamiento de placas tectónicas».",
         "Sellado de compuertas con hormigón rúnico. Cuarentena permanente."),
        
        ("INC-19", "2026-11-08 :: 01:17:42 UTC", "Sector Suroeste 07 (Convoy Minero Pesado de Xenoferrita)",
         "Aguja-04 (Íntegro)", "31 operarios de maquinaria pesada en reposo cataléptico.",
         "[PENDIENTE DE EMISIÓN POR EL GABINETE DE PRENSA MILITAR]",
         "Sujeto asegurado en HazMat-07. Traslado a Hangar 4 para inspección previa a I+D.")
    ]
    
    for inc_id, fecha, sector, sujeto, expuestos, prensa, resultado in events:
        print(f"[{inc_id}] " + "-" * 70)
        print(f"  FECHA / HORA:        {fecha}")
        print(f"  SECTOR:              {sector}")
        print(f"  SUJETO IDENTIFICADO: {sujeto}")
        print(f"  POBLACIÓN EXPUESTA:  {expuestos}")
        print(f"  COMUNICADO OFICIAL:  {prensa}")
        print(f"  RESULTADO OPERATIVO: {resultado}")
        print()

    input("Presiona [ENTER] para regresar al menú principal...")

def screen_5():
    header()
    print(">> PANTALLA 5: TRANSFERENCIA DE REGISTROS A DISPOSITIVO EXTERNO\n")
    print("  DISPOSITIVO DETECTADO EN PUERTO ÓPTICO AUXILIAR:")
    print("  * Hardware: Terminal Kitsune 'Little Fox' v1.1 [ID Civil: L-EV-990]")
    print("  * Capacidad de Memoria Libre: 184 MB-Arcanos")
    print()
    print("  Iniciando volcado de datos encriptados...")
    time.sleep(0.5)
    print("  [####................] 20%  Copiando logs de telemetría...")
    time.sleep(0.4)
    print("  [########............] 45%  Extrayendo firmas espectrales de Aguja-04...")
    time.sleep(0.4)
    print("  [################....] 80%  Duplicando historial cronológico INC-07 / INC-19...")
    time.sleep(0.5)
    print("  [####################] 100% Transferencia completada con éxito.")
    print()
    print("  ADVERTENCIA DEL SISTEMA:")
    print("  La memoria interna del Módulo HazMat-07 ha registrado una copia local.")
    print("  Para evitar rastreo por auditoría de Aegis, se recomienda ejecutar purga térmica.")
    print()
    input("Presiona [ENTER] para regresar al menú principal...")

def main():
    while True:
        menu()
        choice = input("Seleccione una opción [0-5]: ").strip()
        if choice == "1":
            screen_1()
        elif choice == "2":
            screen_2()
        elif choice == "3":
            screen_3()
        elif choice == "4":
            screen_4()
        elif choice == "5":
            screen_5()
        elif choice == "0":
            clear_screen()
            print("Cerrando sesión en Aegis-OS... Consola bloqueada.")
            break
        else:
            print("Opción no válida.")
            time.sleep(0.8)

if __name__ == "__main__":
    main()
