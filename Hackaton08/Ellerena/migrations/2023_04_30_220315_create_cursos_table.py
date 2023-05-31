from orator.migrations import Migration


class CreateCursosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('cursos') as table:
            table.increments('id')
            table.string('nombre').unique()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('cursos')
