BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Glicemia" (
	"Glicemia"	INTEGER,
	"Data"	INTEGER
);
CREATE TABLE IF NOT EXISTS "Alimentos" (
	"Codigo"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"Categoria"	TEXT,
	"Nome"	TEXT,
	"Porcao"	REAL,
	"Calorias"	REAL,
	"Carboidratos"	REAL,
	"Acucares"	REAL,
	"Proteinas"	REAL,
	"GordurasTotais"	REAL,
	"GordurasSaturadas"	REAL,
	"GordurasTrans"	REAL,
	"FibraAlimentar"	REAL,
	"Sodio"	REAL
);
INSERT INTO "Alimentos" VALUES (0,'Pães','Pão Francês',50.0,115.0,24.0,0.0,3.8,0.0,0.0,0.0,2.2,247.0);
INSERT INTO "Alimentos" VALUES (1,'Frutas','Maçã',20.0,67.0,16.0,0.0,0.4,0.0,0.0,0.0,2.5,25.0);
INSERT INTO "Alimentos" VALUES (2,'Doces','Chocolate Barra Meio Amargo Nestlé',25.0,127.0,14.0,14.0,1.6,7.0,3.8,0.0,1.6,0.0);
COMMIT;
