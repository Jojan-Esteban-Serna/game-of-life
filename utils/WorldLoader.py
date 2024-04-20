from model.WorldBoard import WorldBoard


class CRLF:
    def __repr__(self):
        return "CRLF"


class EOF:
    def __repr__(self):
        return "EOF"


class WorldLoader:
    def load(self, world_board: WorldBoard, pattern: str, initrow, initcol):
        parsed_items = []
        tokens = self.tokenize(pattern)
        parsed = self.parse(tokens)

        for row in range(initrow, initrow + len(parsed)):
            for col in range(initcol, initcol + len(parsed[row - initrow])):
                world_board.world[row][col] = parsed[row - initrow][col - initcol]

    @staticmethod
    def tokenize(stream):
        tokens = []
        current_token = ''
        for char in stream:
            if char.isdigit():
                current_token += char
                continue
            tokens += [current_token, char] if current_token != '' else [char]
            current_token = ''
        return tokens

    @staticmethod
    def parse(tokens):
        preparsed = []
        for i in range(len(tokens)):
            if tokens[i].isdigit():
                tokens[i] = int(tokens[i])
                preparsed.append(tokens[i])

            if tokens[i] == 'o':
                if (i > 0 and isinstance(tokens[i - 1], str)) or i == 0:
                    preparsed.append(1)
                preparsed.append(True)

            if tokens[i] == 'b':
                if (i > 0 and isinstance(tokens[i - 1], str)) or i == 0:
                    preparsed.append(1)
                preparsed.append(False)

            if tokens[i] == '$':
                if isinstance(tokens[i-1],int):
                    preparsed.append(CRLF())
                preparsed.append(CRLF())

            if tokens[i] == '!':
                preparsed.append(EOF())
                break

        matrix = []
        row = []
        for i in range(len(preparsed)):
            if isinstance(preparsed[i], int) and isinstance(preparsed[i + 1], bool):
                row += preparsed[i] * [preparsed[i + 1]]
            if isinstance(preparsed[i], CRLF) or isinstance(preparsed[i], EOF):
                matrix.append(row)
                row = []

        return matrix
