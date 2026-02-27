from faker import Faker
import random

fake = Faker("es_ES")

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

usuario_premiado = usuarios[random.randint(0, 14)]

print(f"O usuario chamado {usuario_premiado["nome"]} foi o afortunado!")
