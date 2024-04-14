import unittest

class TestHTMLContent(unittest.TestCase):
    def setUp(self):
        # Ruta al archivo HTML (ajusta según sea necesario)
        self.file_path = 'index.html'

    def test_html_content(self):
        # Abre el archivo HTML y léelo
        with open(self.file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Verifica que el contenido del archivo contenga "Hola Mundo" en el título
        self.assertIn('<title>Hola Mundo</title>', html_content)
        
        # Verifica que el contenido del archivo contenga "Hola Mundo" en el cuerpo
        self.assertIn('<h1>Hola Mundo</h1>', html_content)

# Ejecuta las pruebas
if __name__ == '__main__':
    unittest.main()
