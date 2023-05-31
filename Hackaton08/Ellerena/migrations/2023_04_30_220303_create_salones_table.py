from orator.migrations import Migration


class CreateSalonesTable(Migration):

    def up(self):

        with self.schema.create('salons') as table:
            table.increments('id')
            table.string('nombre').unique()
            table.string('anio_escolar').unique()
            table.timestamps()

    def down(self):

        self.schema.drop('salons')
