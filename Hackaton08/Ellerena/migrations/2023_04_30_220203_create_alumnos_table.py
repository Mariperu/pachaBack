from orator.migrations import Migration


class CreateAlumnosTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('alumnos') as table:
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
        self.schema.drop('alumnos')
