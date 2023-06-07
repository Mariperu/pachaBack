from orator.migrations import Migration


class CreateCursoTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('curso') as table:
            table.increments('id')
            table.string('identificador').unique()
            table.string('nombre').unique()
            table.timestamps()


    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('curso')
