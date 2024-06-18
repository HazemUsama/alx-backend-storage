-- Creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score

DELIMITER !!

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
  DECLARE weighted_score FLOAT;

  SELECT weighted_score = SUM(score * weight) / SUM(weight)
  FROM corrections
  JOIN projects ON corrections.project_id = projects.id
  WHERE corrections.user_id = user_id;

  UPDATE users
  SET average_score = weighted_score
  WHERE id = user_id;
END!!

DELIMITER ;
