# copy and paste your SQL queries into each of the below variables (omit %sql)
# note: do NOT rename variables

Q1a = '''
SELECT *
FROM R r1, R r2
WHERE r1.X = r2.X 
AND r1.Y = r2.Y 
AND (r1.W <> r2.W OR r1.Z <> r2.Z);
'''

Q1b = '''
SELECT *
FROM R r1, R r2
WHERE r1.W = r2.W AND (r1.X <> r2.X OR r1.Y <> r2.Y OR r1.Z <> r2.Z)
OR r1.X = r2.X AND (r1.W <> r2.W OR r1.Y <> r2.Y OR r1.Z <> r2.Z)
OR r1.Y = r2.Y AND (r1.X <> r2.X OR r1.W <> r2.W OR r1.Z <> r2.Z)
OR r1.Z = r2.Z AND (r1.X <> r2.X OR r1.Y <> r2.Y OR r1.W <> r2.W);
'''

Q1c = '''
SELECT *
FROM S s1, S s2
WHERE s1.B = s2.B AND NOT EXISTS (
    SELECT * 
    FROM S s3
    WHERE s3.B = s1.B
        AND s3.D = s1.D
        AND s3.E = s1.E
        AND s3.A = s2.A
        AND s3.C = s2.C);
'''

Q2a_F1 = [(set(['V','W']), set(['X','Y','Z'])),
     (set(['V','X']), set(['W','Y','Z'])),
     (set(['V','Y']), set(['W','X','Z'])),
     (set(['V','Z']), set(['W','X','Y'])),
     (set(['W','X']), set(['V','Y','Z'])),
     (set(['W','Y']), set(['V','X','Z'])),
     (set(['W','Z']), set(['V','X','Y'])),
     (set(['X','Y']), set(['V','W','Z'])),
     (set(['X','Z']), set(['V','W','Y'])),
     (set(['Y','Z']), set(['V','W','X']))]

Q2a_F2 = [(set(['X','Y','Z']), set(['V','W'])),
     (set(['W','Y','Z']), set(['V','X'])),
     (set(['W','X','Z']), set(['V','Y'])),
     (set(['W','X','Y']), set(['V','Z'])),
     (set(['V','Y','Z']), set(['W','X'])),
     (set(['V','X','Z']), set(['W','Y'])),
     (set(['V','X','Y']), set(['W','Z'])),
     (set(['V','W','Z']), set(['X','Y'])),
     (set(['V','W','Y']), set(['X','Z'])),
     (set(['V','W','X']), set(['Y','Z']))]

Q2b_ = '''
DROP TABLE IF EXISTS T; 
CREATE TABLE T (A INT, B INT, C INT, D INT);
INSERT INTO T VALUES (0,0,0,0);
INSERT INTO T VALUES (0,1,1,1);
INSERT INTO T VALUES (2,1,2,2);
INSERT INTO T VALUES (3,3,2,3);
INSERT INTO T VALUES (2,2,2,0);
INSERT INTO T VALUES (0,2,0,0);
INSERT INTO T VALUES (0,3,0,2);
INSERT INTO T VALUES (4,3,0,2);
INSERT INTO T VALUES (3,0,0,2);
INSERT INTO T VALUES (3,1,4,2);
INSERT INTO T VALUES (4,1,3,2);
'''

Q3a = '''
DROP TABLE IF EXISTS A;
CREATE TABLE A (X INT, Y INT, Z INT);
INSERT INTO A VALUES (1,2,3);
INSERT INTO A VALUES (2,3,4);
INSERT INTO A VALUES (3,4,5);
DROP TABLE IF EXISTS B;
CREATE TABLE B (X INT, Y INT, Z INT);
DROP TABLE IF EXISTS C; 
CREATE TABLE C (X INT, Y INT, Z INT);
INSERT INTO C VALUES (1,2,3);
INSERT INTO C VALUES (2,3,4);
INSERT INTO C VALUES (3,4,5);
INSERT INTO C VALUES (1,3,5);
'''

Q3b = '''
DROP TABLE IF EXISTS A;
CREATE TABLE A (X INT, Y INT, Z INT);
INSERT INTO A VALUES (0,0,0);
INSERT INTO A VALUES (0,1,1);
INSERT INTO A VALUES (2,0,2);
INSERT INTO A VALUES (1,1,1);
INSERT INTO A VALUES (1,1,3);
INSERT INTO A VALUES (0,1,3);
INSERT INTO A VALUES (2,3,3);

DROP TABLE IF EXISTS B;
CREATE TABLE B (X INT, Y INT, Z INT);
INSERT INTO B VALUES (0,0,0);
INSERT INTO B VALUES (0,1,1);
INSERT INTO B VALUES (2,0,2);
INSERT INTO B VALUES (1,1,1);
INSERT INTO B VALUES (1,1,3);
INSERT INTO B VALUES (0,1,3);

DROP TABLE IF EXISTS C;
CREATE TABLE C (X INT, Y INT, Z INT);
INSERT INTO C VALUES (0,0,0);
INSERT INTO C VALUES (0,1,1);
INSERT INTO C VALUES (2,0,2);
INSERT INTO C VALUES (1,1,1);
INSERT INTO C VALUES (1,1,3);
INSERT INTO C VALUES (0,1,3);
INSERT INTO C VALUES (2,3,3);
INSERT INTO C VALUES (2,4,3);
'''

Q3c = '''
DROP TABLE IF EXISTS A;
CREATE TABLE A (X INT, Y INT, Z INT);
INSERT INTO A VALUES (4,2,1);
INSERT INTO A VALUES (5,2,1);
INSERT INTO A VALUES (4,3,1);
INSERT INTO A VALUES (5,3,1);

DROP TABLE IF EXISTS B;
CREATE TABLE B (X INT, Y INT, Z INT);
INSERT INTO B VALUES (4,2,1);
INSERT INTO B VALUES (5,2,1);
INSERT INTO B VALUES (4,3,1);

DROP TABLE IF EXISTS C;
CREATE TABLE C (X INT, Y INT, Z INT);
INSERT INTO C VALUES (4,2,1);
INSERT INTO C VALUES (5,2,1);
INSERT INTO C VALUES (4,3,1);
INSERT INTO C VALUES (5,3,1);
INSERT INTO C VALUES (4,7,1);
'''

#################################
# do NOT modify below this line #
#################################