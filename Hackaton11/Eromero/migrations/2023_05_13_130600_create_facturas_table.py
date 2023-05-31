# Migración para la tabla de facturas
from orator.migrations import Migration

class CreateFacturasTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('facturas') as table:
            table.increments('id')
            table.integer('usuario_id').unsigned()
            table.foreign('usuario_id').references('id').on('usuarios')
            table.integer('producto_id').unsigned()
            table.foreign('producto_id').references('id').on('productos')
            table.integer('cantidad')
            table.decimal('total', 8, 2)
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('facturas')
