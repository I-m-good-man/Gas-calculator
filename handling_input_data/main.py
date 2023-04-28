class MolMassInputException(Exception):
    ...


class VolumeMassInputException(Exception):
    ...


class Gas:
    def __init__(self, mol_mass_input, volume_mass_input, volume_checkbox, volume_percent_checkbox, volume_ml_checkbox, mass_checkbox,
                 mass_percent_checkbox, mass_g_checkbox):
        self.mol_mass_input = mol_mass_input
        self.volume_checkbox = volume_checkbox
        self.volume_percent_checkbox = volume_percent_checkbox
        self.volume_ml_checkbox = volume_ml_checkbox
        self.mass_checkbox = mass_checkbox
        self.mass_percent_checkbox = mass_percent_checkbox
        self.mass_g_checkbox = mass_g_checkbox
        self.volume_mass_input = volume_mass_input

    def process_input_data(self):
        """
        Обрабатывает введенные данные и возвращает объект газа.
        :return:
        """
        mol_mass_value = self.mol_mass_input.split(':')[-1].strip().replace(',', '.')
        try:
            mol_mass_value = float(mol_mass_value)

        except ValueError:
            raise MolMassInputException()
        # переводим в СИ
        mol_mass_si = mol_mass_value / 1000

        try:
            volume_mass_value = float(self.volume_mass_input.strip())
        except ValueError:
            raise VolumeMassInputException()

        if self.volume_checkbox:
            if self.volume_ml_checkbox:
                ...
            elif self.volume_percent_checkbox:
                ...
        elif self.mass_checkbox:
            if self.mass_g_checkbox:
                ...
            elif self.mass_percent_checkbox:
                ...




if __name__ == "__main__":
    gas = Gas('fe: 3.1', '1.5', True, True, False, False, False, False)
    print(gas.process_input_data())









