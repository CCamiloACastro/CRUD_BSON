import pymongo
from bson.raw_bson import RawBSONDocument

# Clase CRUD para manejo de archivos BSON
class BasicBsonCRUD:
    def __init__(self, name_database: str, name_collection: str):
        """
        Constructor de la clase
        Args:
            name_database: Nombre de la base de datos que se creara en Mongodb
            name_collection: Nombre de la colección de datos que se creara en Mongodb
        """
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017/", document_class=RawBSONDocument)
            db = client[name_database]
            self.collection = db[name_collection]
        except Exception as e:
            print(e)

    def crear_uno(self, single_bson):
        """
        Inserta solamente un documento
        Args:
            single_bson: Colección de UN solo documento

        Returns:

        """
        print('create_one')
        try:
            self.collection.insert_one(RawBSONDocument(single_bson))
        except Exception as e:
            print(e)

    def crear_muchos(self, multiple_bson):
        """
        Inserta multiples documentos ESTA FUNCIÓN NO INSERTA MULTIPLES DOCUMENTOS BSON
        Args:
            multiple_bson: Colección con multiples documentos

        Returns:
            los id de los documentos insertados
        """
        print('create_many')
        try:
            resultado = self.collection.insert_many(RawBSONDocument(multiple_bson))
            return print(resultado.inserted_ids)
        except Exception as e:
            print(e)

    def leer_uno(self, criterio: dict):
        """
        Leer un documento que cumpla los criterios especificados
        Args:
            criterio (dict): filtro del documento que se busca leer

        Returns:
            Imprime el documento en formato bson.raw_bson.RawBSONDocument
            Imprime el documento en formato dict_items

        """
        print('read_one')
        document = self.collection.find_one(criterio)
        # Verificar si existen registros
        if document is None:
            print("No hay registros con ese criterio")
        else:
            # imprimir el documento encontrado
            print('Datos en formato BSON')
            print(document)
            print('Datos en formato JSON')
            print(document.items())

    def leer_muchos(self, criterio: dict):
        """
        Busca todos los documentos que cumplan los criterios especificados
        Args:
            criterio (dict): filtro de los documentos que se busca leer

        Returns:
            Imprime el documento en formato bson.raw_bson.RawBSONDocument
            Imprime el documento en formato dict_items
        """
        print('read_many')
        documents = list(self.collection.find(criterio))
        # obtener el número de documentos encontrados
        num_documentos = len(documents)
        print(f'Cantidad de documentos encontrados: {num_documentos}')
        # si no se encontraron documentos, imprimir mensaje
        if num_documentos == 0:
            print("No hay registros con ese criterio")
        else:
            # recorrer el cursor e imprimir los documentos
            for document in documents:
                print('Datos en formato BSON')
                print(document)
                print('Datos en formato JSON')
                print(document.items())

    def actualizar_uno(self, criterio: dict, replace_by: dict):
        """
        Actualiza el primer documento que cumpla el criterio especificado
        Args:
            criterio (dict): filtro del documento que se busca reemplazar
            replace_by (dict): clave, valor que se reemplazará
        Returns:

        """
        print('update_one_doc')
        self.collection.update_one(criterio, replace_by)

    def actualizar_muchos(self, criterio: dict, replace_by: dict):
        """
        Actualiza todos los documento que cumpla el criterio especificado
        Args:
            criterio (dict): filtro del documento que se busca reemplazar
            replace_by (dict): clave, valor que se reemplazará

        Returns:

        """
        print('update_many_doc')
        self.collection.update_many(criterio, replace_by)

    def borrar_uno(self, criterio):
        """
        Borra el primer documento que cumpla con el criterio especificado
        Args:
            criterio (dict): filtro del documento que se busca borrar

        Returns:

        """
        print('delete_one_doc')
        self.collection.delete_one(criterio)

    def borrar_muchos(self, criterio: dict):
        """
        Borra todos los documentos que cumpla el criterio especificado
        Args:
            criterio (dict): filtro del documento que se busca borrar

        Returns:
            La cantidad de registros eliminados
        """
        print('delete_many_doc')
        result = self.collection.delete_many(criterio)
        # imprimir el número de documentos borrados
        print(f"{str(result.deleted_count)} registro(s) eliminados")
