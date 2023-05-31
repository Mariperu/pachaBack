from orator.seeds import Seeder


class AlumnosTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('alumnos').insert([{
            'nombre': 'Carlos Guevara',
            'dni': '12398723',
            'edad': '14',
            'email': 'cguevara@email.com'
        },
        {
            'nombre': 'Alvaro Paredes',
            'dni': '928312374',
            'edad': '15',
            'email': 'aparedes@gmail.com' 
        },
        {
            'nombre': 'Juan Pinto',
            'dni': '9934823723',
            'edad': '12',
            'email': 'jpinto@gmail.com'  
        },
        {
            'nombre': 'José Beltran',
            'dni': '384734234',
            'edad': '15',
            'email': 'jbeltran@gmail.com'  
        },
        {
            'nombre': 'Alicia Peralta',
            'dni': '00239231',
            'edad': '14',
            'email': 'aperalta@gmail.com'
        }    
        ])

