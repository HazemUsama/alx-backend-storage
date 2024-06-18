-- creates a function SafeDiv that divides (and returns) the first by the second
-- number or returns 0 if the second number is equal to 0

DELIMITER !!

CREATE FUNCTION SafeDiv (
  first INT,
  second INT
) RETURNS INT
BEGIN
  IF second = 0 THEN
    RETURN 0;
  ELSE
    RETURN first / second;
  END IF;
END!!

DELIMITER ;
