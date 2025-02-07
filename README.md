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
   git clone https://github.com/Edwin2417/Task-Manager---Edwin-Diaz
   ```

2. **Levantar los contenedores Docker:**
   - Ubícate en la raíz del proyecto (por ejemplo, `C:\Users\eddm2\Desktop\DANGER\Personal\TaskManager>`) y ejecuta:

   ```bash
   docker-compose up -d
   ```

3. **Esperar a que los servicios se inicialicen:**
   - Verifica que los contenedores estén corriendo con:
   
   ```bash
   docker ps
   ```
   
   - Asegúrate de que los servicios de Odoo y PostgreSQL estén activos.

4. **Acceder a Odoo:**
   - Abre tu navegador y accede a Odoo en:

   ```
   http://localhost:8069
   ```

5. **Crear un usuario administrador:**
   - Cuando Odoo cargue por primera vez, te pedirá crear un usuario. Usa la siguiente contraseña para el usuario administrador:

   ```text
   Admin Password: Edwin2417
   ```
   
   - Luego, ingresa un correo y una contraseña a tu gusto.

6. **Activar el módulo en Odoo:**
   - Sigue los mismos pasos de la Opción 1 para activar el módulo en el entorno Docker.