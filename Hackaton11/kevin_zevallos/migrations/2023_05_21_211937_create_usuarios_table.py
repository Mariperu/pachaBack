from orator.migrations import Migration


class CreateUsuariosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('usuarios') as table:
            table.increments('id')
            table.string('nombre')
            table.string('password')
            table.string('rol')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('usuarios')
