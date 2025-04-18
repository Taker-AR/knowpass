
██╗  ██╗███╗   ██╗ ██████╗ ██╗    ██╗██████╗  █████╗ ███████╗███████╗
██║ ██╔╝████╗  ██║██╔═══██╗██║    ██║██╔══██╗██╔══██╗██╔════╝██╔════╝
█████╔╝ ██╔██╗ ██║██║   ██║██║ █╗ ██║██████╔╝███████║███████╗███████╗
██╔═██╗ ██║╚██╗██║██║   ██║██║███╗██║██╔═══╝ ██╔══██║╚════██║╚════██║
██║  ██╗██║ ╚████║╚██████╔╝╚███╔███╔╝██║     ██║  ██║███████║███████║
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝ ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝

              KNOWPASS - OSINT PWD GENERATOR
                      by Taker-AR
                      
Know Pass es una herramienta OSINT de línea de comandos para generar diccionarios de contraseñas personalizadas, basada en la información recolectada sobre un objetivo. Es útil para analistas de seguridad en procesos de auditoría.

---

# Instalación

Know Pass está disponible como paquete `.deb` para sistemas basados en Debian como Kali Linux.

¡ ES FACILISIMO DE INSTALAR !

# Requisitos

- Python 3
- El paquete `python3-click` debe estar instalado:
  ```bash
  sudo apt install python3-click
  ```

# Instrucciones

1. Cloná el repositorio:
   ```bash
   git clone https://github.com/Taker-AR/knowpass.git
   cd knowpass
   ```

2. Instalá el paquete `.deb`:
   ```bash
   sudo dpkg -i knowpass_0.1-1_source.deb
   ```

3. Verificá la instalación:
   ```bash
   knowpass --help
   ```

---

# Comandos disponibles (por ahora, se aceptan criticas y comentarios)

| Comando               | Alias | Descripción                                                        |
|-----------------------|-------|--------------------------------------------------------------------|
| `--charge <perfil>`   | `-c`  | Carga datos del perfil objetivo de forma interactiva              |
| `--show <perfil>`     | `-s`  | Muestra los datos guardados de un perfil                          |
| `--list`              | `-l`  | Lista todos los perfiles disponibles                              |
| `--remove <perfil>`   | `-r`  | Elimina un perfil guardado (con confirmación)                     |
| `--generate <perfil>` | `-g`  | Genera un diccionario a partir de un perfil                       |
| `--chars <n>`         |       | Limita la longitud máxima de las contraseñas (por defecto: 16)    |
| `--preview <n>`       |       | Muestra las primeras `n` contraseñas generadas (por defecto: 10)  |
| `--help`              | `-h`  | Muestra la ayuda y el banner personalizado                        |

---

# Funcionalidades del generador (`--generate`)

Al ejecutar:

```bash
knowpass -g <perfil> --chars 12 --preview 15
```

Se genera un archivo `.txt` en `~/.knowpass/diccionarios/` con contraseñas generadas a partir del perfil. El algoritmo incluye:

- Variantes en mayúsculas, minúsculas y capitalización
- Reemplazos tipo leet (por ejemplo: `a` → `4`, `e` → `3`)
- Fragmentos de palabras (inicio, fin, combinaciones)
- Partes de fechas de nacimiento (día, mes, año, combinaciones)
- Combinaciones dobles y triples entre datos
- Sufijos y prefijos comunes: `123`, `2023`, `!`, etc.
- Preview final con conteo y primeras líneas

---

## Ubicación de los archivos

- Perfiles guardados: `~/.knowpass/perfiles/`
- Diccionarios generados: `~/.knowpass/diccionarios/`

---

## Ejemplo de uso

```bash
knowpass -c JhonDoe             # Crear perfil
knowpass -s JhonDoe             # Ver datos cargados
knowpass -g JhonDoe             # Generar diccionario
knowpass -g JhonDoe --chars 10  # Generar con longitud máxima
knowpass -g JhonDoe --preview 20  # Ver las primeras 20 contraseñas
knowpass -r JhonDoe             # Eliminar perfil
```

---

## Autor

Taker-AR (Jcolmegna)  
Analista en Ciberseguridad  
Proyecto de código abierto en evolución

---
