-- Creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score to all Users

DELIMITER !!

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN

  UPDATE users AS u 
  JOIN (
    SELECT user_id, SUM(score * weight) / SUM(weight) AS weighted_score
    FROM corrections
    JOIN projects ON corrections.project_id = projects.user_id
    GROUP BY user_id
  ) AS c ON u.id = c.user_id
  SET u.average_score = c.weighted_score;

END!!

DELIMITER ;

