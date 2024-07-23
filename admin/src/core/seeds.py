from src.core.models import user

def run():
    """
        La idea de este metodo es crear datos prefijados en la base de datos de modo que no haya que 
        crearlos de cero a mano ;)
    """

    print("Creando datos...")
    print("Creando usuarios...")
    
    super_admin = user.create_user(
        name="Super",
        surname="Administrador",
        email="superadmin@gmail.com",
        password="1234",
        active=True,
        is_super_admin=True
    )

    test_user = user.create_user(
        name="Giovanni",
        surname="Giorgio",
        email="giovanni.giorgio@gmail.com",
        password="1234",
        active=True
    )

    print("Usuarios creados!")
    print("Datos cargados, izi")