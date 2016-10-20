CREATE TABLE employees (emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(10),
                        mgr_emp_id INTEGER REFERENCES employees
);

INSERT INTO employees (name, mgr_emp_id) VALUES
  ('Jane', NULL),
  ('Jessica', 1),
  ('Al', 2),
  ('Bob', 2),
  ('Jen', 2),
  ('Janet', 1),
  ('Nick', 6),
  ('Nora', 6),
  ('Henri', 8);

-- List all employees and their manager's name

SELECT e.emp_id,
       e.name,
       m.name AS manager_name
FROM employees AS e
  LEFT JOIN employees AS m ON (e.mgr_emp_id = m.emp_id);


-- List names of managers and their # of direct reports,
-- for those managers having >1 direct report

SELECT m.name,
       COUNT(*) AS reports
FROM employees AS m
  LEFT JOIN employees AS e ON (m.emp_id = e.mgr_emp_id)
GROUP BY m.emp_id
HAVING COUNT(*) > 1;


-- List people who do not manage anyone

-- (or as a join)

SELECT m.name AS nonmgr
FROM employees AS m
  LEFT JOIN employees AS e ON (e.mgr_emp_id = m.emp_id)
WHERE e.emp_id IS NULL;

-- (as a subquery)

SELECT name AS nongmr
FROM employees
WHERE emp_id NOT IN (
  SELECT mgr_emp_id
  FROM employees
  WHERE mgr_emp_id IS NOT NULL
);

-- (as another kind of subquery using EXISTS)

SELECT name AS nonmgr
FROM employees AS nm
WHERE NOT EXISTS (
  SELECT *
  FROM employees AS e
  WHERE e.mgr_emp_id = nm.emp_id
);
