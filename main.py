Calc_Options = """

"""

From = """Options

1.) atm
2.) psi
3.) kpa
4.) torr

"""


class convert:
    def __init__(self) -> None:
        print(From)
        self.atm = float(1.0)
        self.psi = float(14.7)
        self.kpa = float(101.3)
        self.torr = float(760.0)
        all_options = [1, 2, 3, 4]
        self.option = int(
            input("Please pick your unit that you have. (1 = atm, 2 = psi, etc) ")
        )
        if self.option not in all_options:
            print("That is not an option!")
            convert()
        self.number = float(input("How much of the item do you have? "))
        self.converter = int(
            input(
                "Please pick your unit that you are converting to. (1 = atm, 2 = psi, etc) "
            )
        )
        print(self.main())

    def main(self) -> int:
        # I lost all basic knowledge of python dont judge
        if self.option == 1 and self.converter == 2:
            return self.number * self.psi
        if self.option == 1 and self.converter == 3:
            return self.number * self.kpa
        if self.option == 1 and self.converter == 4:
            return self.number * self.torr
        if self.option == 2 and self.converter == 1:
            return self.number / self.psi
        if self.option == 2 and self.converter == 3:
            return self.number * self.kpa / self.psi
        if self.option == 2 and self.converter == 4:
            return self.number * self.torr / self.psi
        if self.option == 3 and self.converter == 1:
            return self.number / self.kpa
        if self.option == 3 and self.converter == 2:
            return self.number * self.psi / self.kpa
        if self.option == 3 and self.converter == 4:
            return self.number * self.torr / self.kpa
        if self.option == 4 and self.converter == 1:
            return self.number / self.torr
        if self.option == 4 and self.converter == 2:
            return self.number * self.psi / self.torr
        if self.option == 4 and self.converter == 3:
            return self.number * self.kpa / self.torr


# can't use if name == main on Ti-84 plus ce calculator because that messes it up
convert()
