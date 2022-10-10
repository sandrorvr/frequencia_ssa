BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "escala_escala" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"date"	date NOT NULL,
	"road"	varchar(20) NOT NULL,
	"begin"	time NOT NULL,
	"end"	time NOT NULL,
	"foothold"	varchar(250) NOT NULL,
	"worker"	varchar(120) NOT NULL,
	"zone"	varchar(20) NOT NULL,
	"equipment"	varchar(3) NOT NULL,
	"group"	varchar(3) NOT NULL
);
INSERT INTO "escala_escala" ("id","date","road","begin","end","foothold","worker","zone","equipment","group") VALUES (1,'2022-10-01','-1','21:33:00','21:35:00','casa','sandro','1','vtr','i');
COMMIT;
