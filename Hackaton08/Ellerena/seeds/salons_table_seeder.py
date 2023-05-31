from orator.seeds import Seeder


class SalonsTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('salons').insert([{
            'nombre': 'Primer Grado C',
            'anio_escolar': '1'
        },
        {
            'nombre': 'Segundo Grado A',
            'anio_escolar': '2'  
        },
        {
            'nombre': 'Tercer Grado A',
            'anio_escolar': '3'  
        },
        {
            'nombre': 'Cuarto Grado B',
            'anio_escolar': '4'  
        },
        {
            'nombre': 'Quinto Grado B',
            'anio_escolar': '5'  
        }    
        ])

