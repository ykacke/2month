class Computer:
    def __init__(self, cpu: int, memory: int):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @property
    def memory(self):
        return self.__memory

    @cpu.setter
    def cpu(self, value: int):
        self.__cpu = value

    @memory.setter
    def memory(self, value: int):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f"Computer:\n - CPU: {self.__cpu}\n - Memory: {self.__memory}GB"

    # Методы сравнения по памяти (memory)
    def __eq__(self, other):
        return isinstance(other, Computer) and self.memory == other.memory

    def __ne__(self, other):
        return isinstance(other, Computer) and self.memory != other.memory

    def __lt__(self, other):
        return isinstance(other, Computer) and self.memory < other.memory

    def __le__(self, other):
        return isinstance(other, Computer) and self.memory <= other.memory

    def __gt__(self, other):
        return isinstance(other, Computer) and self.memory > other.memory

    def __ge__(self, other):
        return isinstance(other, Computer) and self.memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value: list):
        self.__sim_cards_list = value

    def call(self, sim_card_number: int, call_to_number: str):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print("Некорректный номер сим-карты.")

    def __str__(self):
        sim_cards_info = "\n".join(
            [f"   SIM-{i + 1}: {sim}" for i, sim in enumerate(self.__sim_cards_list)]
        )
        return f"Phone:\n - SIM Cards:\n{sim_cards_info}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu: int, memory: int, sim_cards_list: list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location: str):
        print(f"Построение маршрута до {location}...")

    def __str__(self):
        return f"SmartPhone:\n{Computer.__str__(self)}\n{Phone.__str__(self)}"


# Тестирование
if __name__ == "__main__":

    pc1 = Computer(cpu=4, memory=16)
    pc2 = Computer(cpu=3, memory=23)
    pc3 = Computer(cpu=7, memory=16)

    print("Сравнение объектов Computer:")
    print("PC1 == PC2:", pc1 == pc2)
    print("PC1 < PC2:", pc1 < pc2)
    print("PC1 > PC2:", pc1 > pc2)
    print("Результат вычислений PC1:", pc1.make_computations())
    print()


    phone = Phone(sim_cards_list=["Beeline", "MegaCom", "O!"])
    print("Информация о телефоне:")
    print(phone)
    phone.call(1, "+996 777 99 88 11")
    print()


    smartphone = SmartPhone(cpu=8, memory=64, sim_cards_list=["Beeline", "O!"])
    print("Информация о смартфоне:")
    print(smartphone)
    smartphone.use_gps("Бишкек, площадь Ала-Тоо")
