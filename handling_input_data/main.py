class MolMassInputException(Exception):
    ...


class VolumeMassInputException(Exception):
    ...


class GasInput:
    def __init__(self, mol_mass_input, volume_mass_input, volume_checkbox, volume_percent_checkbox, volume_ml_checkbox,
                 mass_checkbox, mass_percent_checkbox, mass_g_checkbox):
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
            volume = volume_mass_value
            if self.volume_ml_checkbox:
                volume_ml_si = volume / (10 ** 6)  # переводим в СИ из мл в м3
                return GasVolumeMl(mol_mass_si, volume_ml_si)
            elif self.volume_percent_checkbox:
                volume_percent = volume
                return GasVolumePercent(mol_mass_si, volume_percent)
        elif self.mass_checkbox:
            mass = volume_mass_value
            if self.mass_g_checkbox:
                mass_gr_si = mass / (10 ** 3)  # переводим в СИ из г в кг
                return GasMassGr(mol_mass_si, mass_gr_si)
            elif self.mass_percent_checkbox:
                mass_percent = mass
                return GasMassPercent(mol_mass_si, mass_percent)


class GasInterface:
    ...


class GasMassGr(GasInterface):
    def __init__(self, mol_mass_si, mass_gr_si):
        self.mol_mass_si = mol_mass_si
        self.mass_gr_si = mass_gr_si
        self.amount_of_substance = self.mass_gr_si / self.mol_mass_si


class GasMassPercent(GasInterface):
    def __init__(self, mol_mass_si, mass_percent):
        self.mol_mass_si = mol_mass_si
        self.mass_percent = mass_percent
        self.amount_of_substance = self.mass_percent / (self.mol_mass_si * 100)


class GasVolume:
    p = 101300  # давление по умолчанию
    R = 8.314  # универсальная газовая постоянная
    T = 273  # температура по умолчанию


class GasVolumeMl(GasInterface, GasVolume):
    def __init__(self, mol_mass_si, volume_ml_si):
        self.mol_mass_si = mol_mass_si
        self.volume_ml_si = volume_ml_si
        self.amount_of_substance = (self.p * self.volume_ml_si) / (self.R * self.T)


class GasVolumePercent(GasInterface, GasVolume):
    def __init__(self, mol_mass_si, volume_percent):
        self.mol_mass_si = mol_mass_si
        self.volume_percent = volume_percent
        self.amount_of_substance = (self.p * self.volume_percent) / (100 * self.R * self.T)

if __name__ == "__main__":
    gas = GasInput('fe: 3.1', '1.5', True, True, False, False, False, False)
    print(gas.process_input_data())









