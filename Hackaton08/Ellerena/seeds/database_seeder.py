from orator.seeds import Seeder
from .salons_table_seeder import SalonsTableSeeder
from .alumnos_table_seeder import AlumnosTableSeeder
from .docentes_table_seeder import DocentesTableSeeder
from .cursos_table_seeder import CursosTableSeeder

class DatabaseSeeder(Seeder):

    def run(self):
        """
        Run the database seeds.
        """
        self.call(SalonsTableSeeder)
        self.call(AlumnosTableSeeder)
        self.call(DocentesTableSeeder)
        self.call(CursosTableSeeder)

