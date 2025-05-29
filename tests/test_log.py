import unittest
from datetime import datetime
from logs import Log  
import tempfile
import csv
import os


class TestLog(unittest.TestCase):

    def setUp(self):
        # Crea un archivo CSV temporal
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv', mode='w', newline='', encoding='utf-8')
        self.campos = ["timestamp", "estado", "sala", "temperatura", "humedad", "co2"]
        self.writer = csv.DictWriter(self.temp_file, fieldnames=self.campos)
        self.writer.writeheader()
        self.valid_row = {
            "timestamp": datetime.now().isoformat(),
            "estado": "Normal",
            "sala": "A1",
            "temperatura": "23",
            "humedad": "45",
            "co2": "400"
        }
        self.writer.writerow(self.valid_row)
        self.invalid_row = {
            "timestamp": "",  # Falta timestamp
            "estado": "Alerta",
            "sala": "B1",
            "temperatura": "30",
            "humedad": "50",
            "co2": "800"
        }
        self.writer.writerow(self.invalid_row)
        self.temp_file.close()

        self.log = Log(self.temp_file.name)

    def tearDown(self):
        # Elimina el archivo temporal
        os.remove(self.temp_file.name)
        if os.path.exists("errores_logs.csv"):
            os.remove("errores_logs.csv")

    def test_validar_fila_valida(self):
        valido, motivo = self.log.validar_fila(self.valid_row)
        self.assertTrue(valido)
        self.assertEqual(motivo, "")

    def test_validar_fila_invalida(self):
        valido, motivo = self.log.validar_fila(self.invalid_row)
        self.assertFalse(valido)
        self.assertIn("Falta campo", motivo)

    def test_leer_logs_separa_validos_e_invalidos(self):
        self.log.leer_logs()
        self.assertEqual(len(self.log.logs_validos), 1)
        self.assertEqual(len(self.log.logs_invalidos), 1)


if __name__ == "__main__":
    unittest.main()
