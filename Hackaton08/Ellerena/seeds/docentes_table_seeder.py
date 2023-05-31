from orator.seeds import Seeder


class DocentesTableSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('docentes').insert([{
            'nombre': 'Patricio Gimenez',
            'dni': '665454345',
            'edad': '45',
            'email': 'pgimenez@email.com'
        },
        {
            'nombre': 'Alexander Arriola',
            'dni': '88457436',
            'edad': '34',
            'email': 'aarriola@gmail.com' 
        },
        {
            'nombre': 'Maynar keenan',
            'dni': '845743534',
            'edad': '32',
            'email': 'mkeenan@gmail.com'  
        },
        {
            'nombre': 'Jason Becker',
            'dni': '834732434',
            'edad': '45',
            'email': 'jbecker@gmail.com'  
        },
        {
            'nombre': 'Berta Suarez',
            'dni': '342342353',
            'edad': '84',
            'email': 'bsuarez@gmail.com'
        }    
        ])

