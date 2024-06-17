-- computes and store the average score for a student
DELIMITER !!

CREATE PROCEDURE ComputeAverageScoreForUser
  @student_id INT
AS
BEGIN
  DECLARE @average_score float;

  SELECT @average_score = AVG(score) FROM corrections
  WHERE student_id = @student_id;

  UPDATE users
  SET average_score = @average_score
  WHERE id = @student_id;

END!!

DELIMITER ;
