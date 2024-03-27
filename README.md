# Automatización proceso de creación ambiente de desarrollo

El ambiente se compone de:

- Contenedor Postgres (v12) con Postgis (v3) : En el cual se generará el modelo de interlist.
- Contenedor Java : En el cual se ejecutaran los comandos posteriores de interlist (importación, validación y exportación).

## Organización del repo

``` bash
  .
  ├── command_builder.py        : Clase que permite la construcción del comando de interrlist
  ├── delete.xtf                : Archivo a generar 
  ├── docker-compose.yml 
  ├── IGAC.xtf                  : XTF a revisar
  ├── jars                      : Librerías de interlist necesarias
  │   ├── ili2pg-4.4.4
  │   └── RIC
  ├── LICENSE                   : free software? hasta no tener permisos :v
  ├── main.py                   : Archivo inicial para correr el script
  ├── output                    : Carpeta para guardar las salidas
  ├── postgis_data              : Carpeta que almacena la BD de postgis
  ├── README.md                 : El readme ;)
  └── scripts                   : Scripts necesarios
      └── wait-for-postgres.sh  : Script para esperar que posgis se active y generar el modelo
```

## Como ejecutar el ambiente de desarrollo

Para correr el ambiente ejecutar

```bash
  docker-compose up 
```

También se puede correr como demonio

```bash
  docker-compose up -d
```

El servidor postgis tiene el puerto 5432 abierto a la realización de peticiones.

### Ayuda

#### Comandos importantes

```bash
java -jar $PWD/jars/ili2pg-4.4.4/ili2pg-4.4.4.jar --schemaimport --dbhost localhost --dbport 5432 --dbusr postgres --dbpwd admin --dbdatabase db --dbschema postgres --setupPgExt --coalesceCatalogueRef --createEnumTabs --createNumChecks --coalesceMultiSurface --coalesceMultiLine --coalesceMultiPoint --coalesceArray --beautifyEnumDispName --createUnique --createGeomIdx --createFk --createFkIdx --createMetaInfo --expandMultilingual --createTypeConstraint --createEnumTabsWithId --createTidCol --smart2Inheritance --strokeArcs --defaultSrsCode 9377 --preScript $PWD/jars/RIC/5_RIC_dev/insert_ctm12_pg.sql --modeldir $PWD/jars/RIC/ --models Modelo_Aplicacion_LADMCOL_RIC_V0_1
```

```bash
java -jar $PWD/jars/ili2pg-4.4.4/ili2pg-4.4.4.jar --import --importTid --dbhost localhost --dbport 5432 --dbusr postgres --dbpwd admin --dbdatabase db --dbschema delete --coalesceCatalogueRef --createEnumTabs --createNumChecks --coalesceMultiSurface --coalesceMultiLine --coalesceMultiPoint --coalesceArray --beautifyEnumDispName --createUnique --createGeomIdx --createFk --createFkIdx --createMetaInfo --expandMultilingual --createTypeConstraint --createEnumTabsWithId --createTidCol --smart2Inheritance --strokeArcs --defaultSrsCode 9377 --modeldir $PWD/jars/RIC/ --models Modelo_Aplicacion_LADMCOL_RIC_V0_1 $PWD/output/IGAC_25372.xtf
```

#### Vídeo tutorial

[El video tutorial](https://www.youtube.com/watch?v=JTBW-2pCFrg)
