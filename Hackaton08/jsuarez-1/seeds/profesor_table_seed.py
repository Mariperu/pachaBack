from orator.seeds import Seeder


class ProfesorTableSeed(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('profesor').insert({
            'identificador': 'P0001',
            'nombre':'Jose Ruiz',
            'edad': 30,
            'correo': 'Jose@gmail.com'
        })

