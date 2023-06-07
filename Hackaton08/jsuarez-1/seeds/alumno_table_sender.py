from orator.seeds import Seeder

class AlumnoTableSender(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.db.table('alumno').insert({
            'identificador': 'A0001',
            'nombre':'Yuli Suarez',
            'edad': 24,
            'correo': 'Yuliana@gmail.com'
        })

