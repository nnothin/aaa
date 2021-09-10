SELECT * FROM t_employees WHERE deptno = 30;
SELECT  ename, empno, deptno FROM t_employees WHERE job = '经理';
SELECT * FROM t_employees WHERE comm > sal ;
SELECT * FROM t_employees WHERE comm > sal * 0.6;
SELECT * FROM t_employees WHERE (deptno = 10 AND job = '经理' ) OR (deptno = 20 AND job = '分析员');
SELECT *FROM t_employees WHERE (deptno = 10 AND job = "经理")  OR  (deptno = 20 AND job = "分析员") OR (job NOT IN ("经理","武装上将") AND sal  >= 3000);
SELECT * FROM t_employees WHERE comm < 1000 OR comm IS NULL ;
SELECT * FROM t_employees WHERE ename LIKE "___";
SELECT * FROM t_employees WHERE hiredate BETWEEN '2000-1-1' AND '2021-1-1';
SELECT * FROM t_employees ORDER BY empno ASC;
SELECT * FROM t_employees ORDER BY sal DESC,hiredate ASC;
SELECT deptno , AVG(sal) FROM t_employees GROUP BY deptno;
SELECT deptno , COUNT(empno) FROM t_employees GROUP BY deptno;
SELECT job, MAX(sal),MIN(sal),COUNT(*) FROM t_employees GROUP BY job;