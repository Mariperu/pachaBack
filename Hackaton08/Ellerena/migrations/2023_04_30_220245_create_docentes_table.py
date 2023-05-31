from orator.migrations import Migration


class CreateDocentesTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('docentes') as table:
            table.increments('id')
            table.string('nombre')
            table.string('dni').unique()
            table.integer('edad')
            table.string('email').unique()
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('docentes')
