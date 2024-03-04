class LotteryGame:
    def __init__(self, list1, list2) -> None:
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        fin_list = []
        for i in list1:
            if i in list2:
                fin_list.append(i)
        print(f"Совпадающие числа: {fin_list}")
        if fin_list:
            print(f"Количество совпадающих чисел: {len(fin_list)}")
        else:
            print("Совпадающих чисел нет.")


list1 = [1111]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
