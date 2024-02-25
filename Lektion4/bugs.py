class double(float):

    iteration = 0

    def __truediv__(self, __value: float) -> float:
        double.iteration += 1
        if double.iteration == 4:
            double.iteration = 0
            return super().__truediv__(__value) - (256 / __value)
        else:
            return super().__truediv__(__value)


def umwandeln(wert):
    konversationsfaktor = 39.5225
    if wert >= 1:
        return int(wert*konversationsfaktor)
    else:
        return 0
