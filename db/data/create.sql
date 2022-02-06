create table packdeps (id SERIAL PRIMARY KEY, pkg VARCHAR(50) NOT NULL, pkgver INTEGER NOT NULL, dep VARCHAR(50) NOT NULL, depver INTEGER NOT NULL)
 
INSERT INTO packdeps (pkg, pkgver, dep, depver) VALUES ('python', 390, 'libpython', 390), ('python', 370, 'libpython', 370), ('python', 390, 'libc', '320'), ('curl', 768, 'openssl', 111)