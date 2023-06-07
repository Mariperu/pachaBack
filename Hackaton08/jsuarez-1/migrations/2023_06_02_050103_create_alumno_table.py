from orator.migrations import Migration


class CreateAlumnoTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('alumno') as table:
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
        self.schema.drop('alumno')
