from config import supabase

# Crear tablas en Supabase
def crear_tablas():
    supabase.table("usuarios").create({
        "id": "uuid",
        "nombre": "text",
        "password": "text",
        "is_admin": "boolean"
    }, if_not_exists=True)

    supabase.table("posesionarios").create({
        "id": "uuid",
        "nombre": "text",
        "apellido_paterno": "text",
        "apellido_materno": "text",
        "telefono": "text",
        "domicilio": "text",
        "parcela_id": "uuid"
    }, if_not_exists=True)

    supabase.table("parcelas").create({
        "id": "uuid",
        "medida": "text",
        "colindancia_norte": "text",
        "colindancia_sur": "text",
        "colindancia_este": "text",
        "colindancia_oeste": "text",
        "posesionario_id": "uuid"
    }, if_not_exists=True)

crear_tablas()
