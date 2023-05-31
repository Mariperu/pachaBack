from orator.migrations import Migration


class CreateUserTables(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('user_tables') as table:
            table.increments('id')
            table.string('name')
            table.string('username')
            table.string('password')
            table.string('roles')
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('user_tables') as table:
            pass
