from django.test import TestCase
from django.core.files.images import get_image_dimensions
from matricula.models import Curso, Alumno

class CursoTestCase(TestCase):

    def setUp(self):
        Curso.objects.create(abrev="1db", denom=" ", imagen="/img.png")

    def test_curso_without_denom(self):
        curso = Curso.objects.get(abrev="1db")
        self.assertTrue(curso.__str__()== " ")


class AlumnoImagenSize(TestCase):

	def setUp(self):
		Alumno.objects.create(dni="77777777", nombre="prueba", apellidos="test", imagen="/static/fotos/descarga.png")

	def test_alumno_imagen_size(self):
		alumno = Alumno.objects.get(dni="77777777")
		self.assertEqual(alumno.imgWeight(),500)

		

