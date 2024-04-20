from model.WorldBoard import WorldBoard
from utils.IO import write_file


class WorldSaver:

    def save(self, world, filename):
        string = self.encode(world)
        write_file(string)

    @staticmethod
    def encode(world: WorldBoard):
        world = world.world

        preencoding = []
        for row in range(len(world)):
            for col in range(len(world[row])):
                preencoding.append(world[row][col])
            if row < len(world) - 1:
                preencoding.append('$')
        preencoding.append('!')

        start = 0
        count = 0
        encoded = ''

        for index in range(len(preencoding)):
            # Si el elemento es igual al anterior, incrementar el contador
            if preencoding[index] == preencoding[start]:
                count += 1
            # Si el elemento es diferente al anterior, codificar el anterior
            else:
                # Si el anterior elemento es un separador, codificar el anterior y añadir el separador
                if isinstance(preencoding[start], str):
                    encoded += preencoding[start]
                # Si el anterior elemento es un True codificarlo como 'o' si es False codificarlo como 'b'
                elif preencoding[start]:
                    encoded += f'{count}o' if count > 1 else 'o'
                elif not preencoding[start]:
                    encoded += f'{count}b' if count > 1 else 'b'
                # El nuevo inicio sera el elemento actual que es diferente al anterior
                start = index
                # Reiniciar el contador
                count = 1
        encoded += preencoding[-1]

        return encoded






