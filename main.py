from faker import Faker

fake = Faker()

usuarios = []

for num in range(15):
    usuario = {}
    usuario["id"] = num + 1
    usuario["nome"] = fake.name()
    usuario["direccion"] = fake.address()
    usuario["correo electronico"] = fake.email()
    usuario["telefono"] = fake.phone_number()

    usuarios.append(usuario)
    del usuario

print(usuarios)