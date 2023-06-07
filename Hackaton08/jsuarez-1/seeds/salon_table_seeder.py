from orator.seeds import Seeder


class SalonTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table("salon").insert(
            {
                'identificador': 'S0001',
                'nombre':'S1',
                'anioescolar':'2023',
            }
        )

