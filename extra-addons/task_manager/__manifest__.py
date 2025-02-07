{
    'name': 'Task Manager',
    'version': '1.0',
    'summary': 'Gestor de Tareas',
    'author': 'Edwin Díaz',
    'category': 'Productivity',
    'depends': ['base'],
    'data': [
        'security/task_manager_security.xml',
        'security/ir.model.access.csv',
        'views/task_views.xml',
        'views/task_manager_menu.xml',
        'data/task_data.xml',
    ],
    'installable': True,
    'application': True,
}
