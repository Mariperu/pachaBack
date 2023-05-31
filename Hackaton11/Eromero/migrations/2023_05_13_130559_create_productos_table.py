# Migración para la tabla de productos
from orator.migrations import Migration

class CreateProductosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('productos') as table:
            table.increments('id')
            table.string('nombre')
            table.string('categoria')
            table.integer('stock')
            table.decimal('precio', 8, 2)  # 8 digitos en total, 2 despues del punto decimal
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('productos')
