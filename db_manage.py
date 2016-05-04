# -*- coding: utf-8 -*-

from cu_kg.app import create_app
from flask_migrate import Manager, MigrateCommand

manager = Manager(create_app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
