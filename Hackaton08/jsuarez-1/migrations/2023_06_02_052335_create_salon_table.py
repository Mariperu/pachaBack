from orator.migrations import Migration


class CreateSalonTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('salon') as table:
            table.increments('id')
            table.string('identificador')
            table.string('nombre')
            table.string('anioescolar')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('salon')
