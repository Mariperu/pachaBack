from orator.migrations import Migration


class CreateProfesorTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('profesor') as table:
            table.increments('id')
            table.string('identificador').unique()
            table.string('nombre').unique()
            table.string('edad')
            table.string('correo').unique()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('profesor')
