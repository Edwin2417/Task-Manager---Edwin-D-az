
# Task Manager - Odoo 17

Este módulo permite gestionar tareas dentro de una empresa, con características como asignación de tareas a usuarios, establecimiento de fechas límite y control de su estado (pendiente, en progreso, completada). Es compatible con Odoo 17.

## Instalación

### Opción 1: Instalación en un Proyecto Existente

1. **Copiar la carpeta del módulo:**
   - Copia la carpeta `task_manager` desde el directorio `extra-addons` de este repositorio.
   - Pega la carpeta `task_manager` en la carpeta `extra-addons` de tu proyecto Odoo 17.

2. **Reiniciar el servidor de Odoo:**
   - Después de pegar la carpeta, reinicia el servidor de Odoo para cargar el nuevo módulo.

3. **Actualizar la lista de aplicaciones:**
   - Accede a la interfaz de Odoo.
   - Ve al menú de aplicaciones y actualiza la lista de aplicaciones disponibles.

4. **Activar el módulo:**
   - Busca el módulo `Task Manager` en la lista de aplicaciones.
   - Actívalo.

5. **Acceder y probar:**
   - Una vez activado, podrás ver el módulo `Task Manager` en el menú de aplicaciones.
   - Prueba la gestión de tareas: creación, edición y cambio de estado.

### Opción 2: Instalación Usando Docker

1. **Clonar el repositorio:**
   - Clona este repositorio en tu máquina local ejecutando el siguiente comando:

   ```bash
   git clone <url-del-repositorio>
   ```

2. **Navegar a la carpeta del proyecto:**
   - Dirígete a la carpeta del proyecto recién clonada:

   ```bash
   cd task_manager
   ```

3. **Levantar los contenedores Docker:**
   - Ejecuta el siguiente comando para iniciar los contenedores:

   ```bash
   docker-compose up
   ```

4. **Crear un usuario administrador:**
   - Una vez levantados los contenedores, crea un usuario administrador con la siguiente contraseña:

   ```text
   Usuario: admin
   Contraseña: Edwin2417
   ```

5. **Acceder a Odoo:**
   - Accede a la interfaz de Odoo con el usuario administrador recién creado.

6. **Repetir el proceso de instalación del módulo:**
   - Sigue los mismos pasos de la Opción 1 para activar el módulo en el entorno Docker.