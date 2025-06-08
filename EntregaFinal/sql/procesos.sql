-- Añade el precio final con IVA al producto. Es función porque devuelve un valor (el precio con IVA)
DELIMITER //
CREATE FUNCTION calcular_iva(precio DECIMAL(10,2)) RETURNS DECIMAL(10,2)
BEGIN
  RETURN ROUND(precio * 0.21, 2);
END//

-- Actualiza la tabla de productos con el stock. Es procedure porque no devuelve un valor, si no que hace un UPDATE
CREATE PROCEDURE aumentar_stock(IN pid INT, IN incremento INT)
BEGIN
  UPDATE products SET VitalityDays = VitalityDays + incremento WHERE ProductID = pid;
END//
DELIMITER ;
