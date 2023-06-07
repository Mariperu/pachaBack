from orator.seeds import Seeder
from .alumno_table_sender import AlumnoTableSender #El nombre deberia ser AlumnoTableSeeder
from .profesor_table_seed import ProfesorTableSeed
from .curso_table_seeder import CursoTableSeeder
from .salon_table_seeder import SalonTableSeeder

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(AlumnoTableSender)
        self.call(ProfesorTableSeed)
        self.call(CursoTableSeeder)
        self.call(SalonTableSeeder)

