# Alcance del Programa

## Objetivo general
Simular un torneo de fútbol de 20 equipos (una sola rueda) desde consola: cargar equipos, generar el fixture, simular goles, mostrar resultados, calcular la tabla de posiciones y exportar estadísticas para análisis externo.

## Módulos y responsabilidades
- `auth.py`: Login por consola. Hasta 3 intentos.
- `users.py`: ABM de usuarios y persistencia en `users.csv`.
- `equipos.py`: Carga manual o simulada de equipos y persistencia en `equipos_manuales.csv`.
- `fixture.py`: Generación del fixture (round‑robin) para 19 fechas.
- `goles.py`: Simulación de goles, resultados y tabla de posiciones.
- `estadisticas.py`: Cálculo y exportación de estadísticas a `estadisticas.csv`.
- `menu.py`: Orquestación del flujo por menús.
- `main.py`: Punto de entrada de la aplicación.
- `logger.py`: Registro de acciones del usuario y del sistema en `registro.txt`.

## Flujo de uso (alto nivel)
1. Ejecutar `main.py` y autenticarse.
2. Cargar 20 equipos (manual o desde `equipos_simulados.csv`).
3. Generar fixture.
4. Simular goles.
5. Consultar resultados, tabla y generar `estadisticas.csv`.

## Reglas de negocio y validaciones
- Son exactamente 20 equipos; si no, no se genera fixture.
- No se permite ver resultados/tabla/estadísticas sin fixture y sin goles simulados.
- ABM de usuarios persiste en `users.csv` (no se puede eliminar el usuario admin).
- Carga manual valida: nombre no vacío, hasta 30 caracteres, sin duplicados exactos en la sesión de carga.

## Algoritmos y lógica clave
- Fixture round‑robin (`fixture.generar_fixture`):
  - Empareja por fecha `equipos[i]` con `equipos[19 - i]` y rota la lista manteniendo fijo el primero.
  - Alterna la localía por paridad de fecha.
- Goles aleatorios (`goles.simular_goles`):
  - Asigna `random.randint(0, 5)` a cada equipo por partido.
- Tabla de posiciones:
  - Acumulados por equipo con `goles.calcular_tabla`: puntos (3‑1‑0), GF, GC y diferencia.
  - Ordenamiento en `goles.calcular_tabla_posiciones` usando `.sort()` in‑place con clave compuesta y descendente:
    - `lista_tabla.sort(key=lambda x: (x[1]['puntos'], x[1]['diferencia']), reverse=True)`
- Estadísticas (`estadisticas.mostrar_estadisticas`):
  - Máximos y mínimos con `max()`/`min()` sobre la tabla.
  - Agregación de goles por fecha con `sum()` y generador:
    - `goles_por_fecha[fecha] = sum(p['goles_local'] + p['goles_visitante'] for p in partidos)`

## Entradas y salidas
- Entradas por consola: credenciales, ABM de usuarios, carga manual de equipos, opciones de menú.
- Archivos leídos: `users.csv`, `equipos_simulados.csv`, `equipos_manuales.csv`.
- Archivos generados/actualizados:
  - `users.csv`: altas/bajas/modificaciones de usuarios.
  - `equipos_manuales.csv`: lista de equipos cargada manualmente o importada.
  - `estadisticas.csv`: reporte consolidado para gráficos/tablas en Excel.
  - `registro.txt`: bitácora de acciones (sin fecha ni hora).

## Estructura de archivos (resumen)
```
auth.py
users.py
equipos.py
fixture.py
goles.py
estadisticas.py
menu.py
main.py
logger.py
users.csv
equipos_manuales.csv
equipos_simulados.csv
estadisticas.csv
registro.txt
```

## Supuestos
- El torneo siempre tiene 20 equipos y 19 fechas (una rueda).
- La simulación de goles es uniforme e independiente.
- El uso es interactivo por consola (no hay interfaz web/GUI).

## Limitaciones y decisiones conocidas
- El fixture y los resultados se mantienen en memoria; no se persisten en disco (solo se exporta `estadisticas.csv`).
- Al salir por menú se limpia `equipos_manuales.csv` (decisión explícita del proyecto).
- Ordenamiento de tabla solo por Puntos y Diferencia (no hay tercer criterio como GF o enfrentamiento directo).
- Sin pruebas automatizadas; validaciones y manejo de errores básicos.

## Fuera de alcance
- Descensos, playoffs, ida/vuelta, tarjetas, lesiones u otras estadísticas avanzadas.
- Múltiples torneos paralelos o edición del fixture.
- Persistencia de temporada completa (fixture/resultados por archivo o DB).

## Cómo ejecutar (resumen)
- Requisito: Python 3.10+.
- Ejecutar desde la carpeta del proyecto:
  - `python3 main.py`

## Registro de acciones (logging)
- Archivo: `registro.txt` (texto plano, sin fecha ni hora por línea).
- Generado por: `logger.py` mediante la función `registrar_accion(mensaje)`.
- Eventos registrados (principales):
  - Inicio del sistema.
  - Login exitoso con usuario (ej.: `Login exitoso - Usuario: admin`).
  - Ingreso a menús: Usuarios, Equipos.
  - Intento y resultado de generar fixture.
  - Intento y resultado de simular goles.
  - Visualización de resultados y de la tabla de posiciones.
  - Exportación de estadísticas.
  - Errores de flujo (sin fixture / sin goles simulados).
  - Opción inválida en el menú.
  - Salida del sistema.

## Notas de entrega
- Salidas de consola normalizadas (sin tildes/acentos) para evitar incompatibilidades en terminal.
- Código modular y documentado con nombres claros.
