from odoo import models, fields

class Task(models.Model):
    _name = 'task.task'
    _description = 'Tareas'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    assigned_to = fields.Many2one('res.users', string="Usuario Asignado")
    deadline = fields.Date(string="Fecha Límite")
    state = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada')
    ], string="Estado", default='pendiente')

    def mark_as_completed(self):
        for task in self:
            task.state = 'completada'
