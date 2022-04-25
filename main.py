from bot import Bot
from ResponseList import getResponseList

# Itla Bot
botItla = Bot()
botItla.responsesList.extend(getResponseList())

if __name__ == '__main__':

    print(f"\nSaludos, mi nombre es {botItla.name}  y estoy para asistirte con información sobre el ITLA. ¿Cómo puedo ayudarte?")

    while True:
        print(f"\n{botItla.name}:{botItla.get_response(input('You: '))}")