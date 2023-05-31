from orator.migrations import Migration


class CreateProductTables(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('product_tables') as table:
            table.increments('id')
            table.string('nombre')
            table.integer('precio')
            table.integer('stock')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('product_tables') as table:
            pass
