from orator.seeds import Seeder


class CursoTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table("curso").insert(
            {
                'identificador': 'C0001',
                'nombre':'C1',
            }
        )

