-- Creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score to all Users

DELIMITER !!

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN

  UPDATE users AS u,
    (SELECT SUM(score * weight) / SUM(weight)
      FROM corrections
      JOIN projects ON corrections.project_id = projects.id
      WHERE corrections.user_id = u.id;
  ) AS weighted_score
  SET u.average_score = weighted_score;

END!!

DELIMITER ;

