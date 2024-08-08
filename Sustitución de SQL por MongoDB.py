from pymongo import MongoClient
from bson.objectid import ObjectId

# Configurar la conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['recetas_db']
recetas_collection = db['recetas']

def agregar_receta():
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes (separados por comas): ")
    pasos = input("Ingrese los pasos: ")
    receta = {
        'nombre': nombre,
        'ingredientes': ingredientes,
        'pasos': pasos
    }
    recetas_collection.insert_one(receta)
    print("Receta agregada exitosamente.")

def actualizar_receta():
    id_str = input("Ingrese el ID de la receta que desea actualizar: ")
    try:
        id = ObjectId(id_str)
        receta = recetas_collection.find_one({'_id': id})
        if receta:
            nombre = input("Ingrese el nuevo nombre de la receta: ")
            ingredientes = input("Ingrese los nuevos ingredientes (separados por comas): ")
            pasos = input("Ingrese los nuevos pasos: ")
            recetas_collection.update_one(
                {'_id': id},
                {'$set': {'nombre': nombre, 'ingredientes': ingredientes, 'pasos': pasos}}
            )
            print("Receta actualizada exitosamente.")
        else:
            print("Receta no encontrada.")
    except Exception as e:
        print(f"Error: {e}")

def eliminar_receta():
    id_str = input("Ingrese el ID de la receta que desea eliminar: ")
    try:
        id = ObjectId(id_str)
        result = recetas_collection.delete_one({'_id': id})
        if result.deleted_count > 0:
            print("Receta eliminada exitosamente.")
        else:
            print("Receta no encontrada.")
    except Exception as e:
        print(f"Error: {e}")

def ver_recetas():
    recetas = recetas_collection.find({}, {'_id': 1, 'nombre': 1})
    if recetas:
        for receta in recetas:
            print(f"ID: {receta['_id']}, Nombre: {receta['nombre']}")
    else:
        print("No hay recetas disponibles.")

def buscar_receta():
    id_str = input("Ingrese el ID de la receta que desea buscar: ")
    try:
        id = ObjectId(id_str)
        receta = recetas_collection.find_one({'_id': id})
        if receta:
            print(f"Nombre: {receta['nombre']}")
            print(f"Ingredientes: {receta['ingredientes']}")
            print(f"Pasos: {receta['pasos']}")
        else:
            print("Receta no encontrada.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\nOpciones:")
        print("1) Agregar nueva receta")
        print("2) Actualizar receta existente")
        print("3) Eliminar receta existente")
        print("4) Ver listado de recetas")
        print("5) Buscar ingredientes y pasos de receta")
        print("6) Salir")
        
        opcion = input("Seleccione una opción: ").lower()

        if opcion == '1':
            agregar_receta()
        elif opcion == '2':
            actualizar_receta()
        elif opcion == '3':
            eliminar_receta()
        elif opcion == '4':
            ver_recetas()
        elif opcion == '5':
            buscar_receta()
        elif opcion == '6':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()
    client.close()
