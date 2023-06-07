from orator.migrations import Migration


class CreateCursoAlumnoTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('curso_alumno') as table:
            table.integer('curso_id').unsigned()
            table.foreign('curso_id').references('id').on('curso')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('curso_alumno')
