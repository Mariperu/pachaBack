from orator.migrations import Migration


class CreateSalonCursoTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('salon_curso') as table:
            table.integer('curso_id')
            table.integer('salon_id')
            table.foreign('curso_id').references('id').on('curso')
            table.foreign('salon_id').references('id').on('salon')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('salon_curso')
