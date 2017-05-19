CREATE VIEW top_articles as
  SELECT title, count(log.path) as views
  FROM articles, log
  WHERE log.path = CONCAT('/article/', articles.slug)
  AND log.method = 'GET'
  GROUP BY title
  ORDER BY views DESC;

CREATE VIEW top_authors as
  SELECT name, count(log.path) as views
  FROM authors, articles, log
  WHERE authors.id = articles.author AND log.path = CONCAT('/article/', articles.slug)
  AND log.method = 'GET'
  GROUP BY name
  ORDER BY views DESC;

CREATE VIEW errors_per_day AS
  SELECT  date_log, ROUND((100.0 * (errors::decimal / total::decimal)), 2) AS errors_perc
  FROM (
    SELECT COUNT(*) AS total,
      SUM(CASE WHEN status != '200 OK' THEN 1 ELSE 0 END) AS errors,
      date_trunc('day',log.time)::date AS date_log
    FROM log
    GROUP BY date_log
  ) summary_day
  ORDER BY errors_perc DESC;