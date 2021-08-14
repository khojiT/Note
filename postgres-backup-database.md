C:\Program Files\PostgreSQL\13

ALTER DATABASE your_db OWNER TO your_django_db_user

ALTER TABLE django_site OWNER TO your_django_db_user

sudo -u postgres psql 
drop database faramiran2
create database faramiran2
sudo -u postgres psql -f /home/hesam/projects/faramiran/data000312.out faramiran2

\c faramiran2
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO fara;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO root;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO fara;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO fara;
REASSIGN OWNED BY root to fara ;



psql.exe -U USERNAME -d DATABASENAME -f  BACKUP_FILE_NAME.sql
