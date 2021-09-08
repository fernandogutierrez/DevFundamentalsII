class IceCream:
    def __init__(self, levels):
        self._status = "Unknown"
        self._levels = levels

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, new_state):
        self._status = new_state

    @property
    def treatment_levels(self):
        return self._levels


class TreatmentListLevel:
    def __init__(self, treatment_level_list):
        self._treatment_level_list = treatment_level_list

    def get_list(self):
        return self._treatment_level_list

    def contains(self, other_treatment_list):
        for other_tr_lvl in other_treatment_list.get_list():
            for tr_lvl in self._treatment_level_list:
                if tr_lvl == other_tr_lvl:
                    break
            else:
                return False
        return True


class TreatmentLevel:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def __eq__(self, other_level):
        return self._name == other_level.name and self._value == other_level.value


class IceCreamStandards:
    def __init__(self, treatment_level_list):
        self._standard_levels = treatment_level_list

    def validate(self, ice_cream):
        if ice_cream.treatment_levels.contains(self._standard_levels):
            return "VALID"
        else:
            return "DISCARD"


class IceCreamCompany:
    def __init__(self, ice_cream_standards, ingredients):
        self._flavor = ""
        self._ingredients = ingredients
        self._ice_cream_standards = ice_cream_standards
        self._valid_products = []

    def deliver_products(self, ice_cream_list):
        for ice_cream in ice_cream_list:
            if self._ice_cream_standards.validate(ice_cream) == "VALID":
                self._valid_products.append(ice_cream)
        return self._valid_products


if __name__ == "__main__":
    tr_lvl_lst_1 = TreatmentListLevel([TreatmentLevel("Pasteurization", 20),
                                       TreatmentLevel("Homogenization", 10),
                                       TreatmentLevel("Creaming", 6)])

    tr_lvl_lst_2 = TreatmentListLevel([TreatmentLevel("Pasteurization", 20),
                                       TreatmentLevel("Homogenization", 2),
                                       TreatmentLevel("Creaming", 6)])

    tr_lvl_lst_3 = TreatmentListLevel([TreatmentLevel("Pasteurization", 20),
                                       TreatmentLevel("Homogenization", 7),
                                       TreatmentLevel("Creaming", 65)])

    tr_lvl_lst_4 = TreatmentListLevel([TreatmentLevel("Pasteurization", 20),
                                       TreatmentLevel("Homogenization", 10),
                                       TreatmentLevel("Creaming", 6)])

    ice_cr_1 = IceCream(tr_lvl_lst_1)
    ice_cr_2 = IceCream(tr_lvl_lst_2)
    ice_cr_3 = IceCream(tr_lvl_lst_3)
    ice_cr_4 = IceCream(tr_lvl_lst_4)
    ice_cr_5 = IceCream(tr_lvl_lst_1)

    ice_cr_stds = IceCreamStandards(tr_lvl_lst_1)

    ice_cr_cmp = IceCreamCompany(ice_cr_stds, ["1/2 Cup of milk", "1 tablespoon vanilla extract", "1/8 teaspoon salt"])

    valid_ice_creams = ice_cr_cmp.deliver_products([ice_cr_1, ice_cr_2, ice_cr_3, ice_cr_4, ice_cr_5])
    print(valid_ice_creams)

