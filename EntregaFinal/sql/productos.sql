-- Ranking de precio del más caro al más barato
WITH TopProducts AS (
  SELECT ProductID, AVG(TotalPrice) AS avg_price
  FROM sales
  GROUP BY ProductID
)
SELECT tp.*,
       RANK() OVER (ORDER BY tp.avg_price DESC) AS price_rank
FROM TopProducts tp
