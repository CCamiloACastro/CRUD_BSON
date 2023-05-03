Librerías que hay que instalar:

`pip install pymongo`

`pip install bson`

`pip install python-bsonjs`


### CRUD Mongo con usando python, json y bson


**CRUD** (Crear, Leer, Actualizar, Eliminar) es un acrónimo de las cuatro operaciones 
básicas para almacenamiento persistente 

## Crear un documento

En MongoDB, existen tres métodos principales para insertar documentos en 
una colección: _insert(), insert_one() e insert_many()_.

    La principal diferencia entre ellos radica en la cantidad de documentos que se pueden insertar de una sola vez:

    insert() permite la inserción de uno o varios documentos en una colección.
    insert_one() permite la inserción de un solo documento en una colección.
    insert_many() permite la inserción de varios documentos en una colección.
    
Además, también hay diferencias en la forma en que manejan las excepciones 
y la forma en que devuelven el resultado de la operación de inserción.

**insert()** 
: Devuelve un objeto InsertOneResult, que contiene información 
sobre la operación de inserción, incluyendo el número de documentos insertados
y los identificadores generados automáticamente para los documentos insertados.

**insert_one()**
: Devuelve un objeto InsertOneResult similar a insert(), 
pero solo para un solo documento.

**insert_many()** 
: Devuelve un objeto InsertManyResult, que contiene información 
sobre la operación de inserción, incluyendo el número de documentos insertados
y los identificadores generados automáticamente para los documentos insertados.

Es importante destacar que, en general, es más eficiente insertar varios 
documentos a la vez utilizando insert_many() en lugar de insertarlos uno 
por uno con insert_one() o insert(). Esto se debe a que insert_many() 
reduce la cantidad de operaciones de red necesarias para insertar varios 
documentos, lo que puede mejorar significativamente el rendimiento en
entornos de alta carga.

    El método insert() ya no existe en las últimas versiones de 
    PyMongo (a partir de la versión 4.0). En su lugar, se recomienda
    utilizar los     métodos insert_one o insert_many dependiendo 
    de si quieres insertar un solo documento o varios documentos, 
    respectivamente.

## Leer un Documento

**find()**
: Devuelve un cursor que contiene todos los documentos que coinciden con los 
criterios de búsqueda

**find_one()**
: Devuelve solamente el primer documento que cumple con los criterios de 
búsqueda especificados.

## Actualizar un documento

En MongoDB, update(), update_one() y update_many() son métodos que se utilizan
para actualizar documentos en una colección que cumplan con los **criterios 
de búsqueda especificados**.

La principal diferencia entre estos métodos es la cantidad de documentos que 
se actualizan:

**update()**
: Actualiza todos los documentos que coinciden con los criterios de búsqueda 
especificados.

**update_one()** 
: Actualiza solamente el primer documento que cumple con los criterios de 
búsqueda especificados.

**update_many()** 
: Actualiza todos los documentos que coinciden con los criterios de búsqueda 
especificados.

    El método update() ya no está disponible en la versión más reciente de 
    pymongo. En su lugar, se debe utilizar el método update_one() o update_many() 
    dependiendo del caso.

## Eliminar un Documento

**delete_one()**
: Borra solamente el primer documento que cumple con los criterios de 
búsqueda especificados

    Si en la colección hay varios documentos que cumplen con los criterios de 
    búsqueda especificados, delete_one() solo borrará el primer documento 
    que encuentre y no afectará a los demás documentos.

**delete_many()** 
: Borra todos los documentos que cumplan con dichos criterios.


Operadores

* `$eq` - equal - igual
* `$lt` - lower than - menor que
* `$lte` - low than equal - menor o igual que
* `$gt` - greater than - mayor que
* `$gte` - greater than equal - mayor o igual que
* `$ne` - not equal - distinto
* `$in` - in - dentro de
* `$nin` - not in - no dentro de
