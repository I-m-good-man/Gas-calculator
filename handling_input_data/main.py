class MolMassInputException(Exception):
    ...


class VolumeMassInputException(Exception):
    ...


class VolumeMassCheckboxError(Exception):
    ...


class GasInput:
    def __init__(self, mol_mass_input, volume_mass_input, volume_checkbox, volume_percent_checkbox, volume_ml_checkbox,
                 mass_checkbox, mass_percent_checkbox, mass_g_checkbox, p, T, amount_of_substance_checkbox,
                 mole_checkbox):
        self.mol_mass_input = mol_mass_input
        self.volume_checkbox = volume_checkbox
        self.volume_percent_checkbox = volume_percent_checkbox
        self.volume_ml_checkbox = volume_ml_checkbox
        self.mass_checkbox = mass_checkbox
        self.mass_percent_checkbox = mass_percent_checkbox
        self.mass_g_checkbox = mass_g_checkbox
        self.volume_mass_input = volume_mass_input
        self.p = p
        self.T = T
        self.amount_of_substance_checkbox = amount_of_substance_checkbox
        self.mole_checkbox = mole_checkbox

    def process_input_data(self):
        """
        Обрабатывает введенные данные и возвращает объект газа.
        :return:
        """
        mol_mass_value = self.mol_mass_input.split(':')[-1].strip().replace(',', '.')
        try:
            mol_mass_value = float(mol_mass_value)
        except ValueError:
            raise MolMassInputException('Ошибка при вводе молярной массы.')
        # переводим в СИ
        mol_mass_si = mol_mass_value / 1000

        try:
            volume_mass_value = float(self.volume_mass_input.strip().replace(',', '.'))
        except ValueError:
            raise VolumeMassInputException('Ошибка при вводе массы/объема.')

        if self.volume_checkbox:
            volume = volume_mass_value
            if self.volume_ml_checkbox:
                volume_ml_si = volume / (10 ** 6)  # переводим в СИ из мл в м3
                return GasVolumeMl(mol_mass_si, volume_ml_si, self.p, self.T)
            elif self.volume_percent_checkbox:
                volume_percent = volume
                return GasVolumePercent(mol_mass_si, volume_percent, self.p, self.T)
            else:
                raise VolumeMassCheckboxError('Не выбран единица измерения ввода объема.')
        elif self.mass_checkbox:
            mass = volume_mass_value
            if self.mass_g_checkbox:
                mass_gr_si = mass / (10 ** 3)  # переводим в СИ из г в кг
                return GasMassGr(mol_mass_si, mass_gr_si)
            elif self.mass_percent_checkbox:
                mass_percent = mass
                return GasMassPercent(mol_mass_si, mass_percent)
            else:
                raise VolumeMassCheckboxError('Не выбран единица измерения ввода массы.')
        elif self.amount_of_substance_checkbox:
            amount = volume_mass_value
            if self.mole_checkbox:
                amount_si = amount
                return GasAmountMole(mol_mass_si, amount_si)
            else:
                raise VolumeMassCheckboxError('Не выбран единица измерения ввода кол-ва вещества')


class GasInterface:
    amount_of_substance = None
    mol_mass_si = None


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
    R = 8.314472  # универсальная газовая постоянная


class GasVolumeMl(GasInterface, GasVolume):
    def __init__(self, mol_mass_si, volume_ml_si, p, T):
        self.mol_mass_si = mol_mass_si
        self.volume_ml_si = volume_ml_si
        self.p = p
        self.T = T
        self.amount_of_substance = (self.p * self.volume_ml_si) / (self.R * self.T)


class GasVolumePercent(GasInterface, GasVolume):
    def __init__(self, mol_mass_si, volume_percent, p, T):
        self.mol_mass_si = mol_mass_si
        self.volume_percent = volume_percent
        self.p = p
        self.T = T
        self.amount_of_substance = (self.p * self.volume_percent) / (100 * self.R * self.T)


class GasAmountMole(GasInterface):
    def __init__(self, mol_mass_si, amount_si):
        self.mol_mass_si = mol_mass_si
        self.amount_si = amount_si
        self.amount_of_substance = amount_si


class PercentSumError(Exception):
    ...


class GasTypeError(Exception):
    ...


class GasCalculations:
    def __init__(self, gas_list):
        self.gas_list = gas_list
        self.R_universe = 8.314
        self._M = None  # в г/моль
        self._R = None

    def check_gases(self):
        random_gas = self.gas_list[0]
        percent_sum = 0
        for gas in self.gas_list:
            if type(gas) != type(random_gas):
                raise GasTypeError('Выбор массы/объема должен быть одинаковым для всех газов.')
            else:
                if isinstance(gas, GasVolumePercent):
                    percent_sum += gas.volume_percent
                elif isinstance(gas, GasMassPercent):
                    percent_sum += gas.mass_percent
        if (isinstance(random_gas, GasVolumePercent) or isinstance(random_gas, GasMassPercent)) and percent_sum != 100:
            raise PercentSumError(f'Суммарное число процентов переданных значений {percent_sum}, а должно быть 100.')

    @property
    def M(self):
        self._M = round(sum(map(lambda x: x.mol_mass_si * x.amount_of_substance, self.gas_list)) /
                sum(map(lambda x: x.amount_of_substance, self.gas_list)) * 1000, 6)
        return self._M

    @property
    def R(self):
        self._R = round(self.R_universe / (self.M / 1000), 6)
        return self._R


if __name__ == "__main__":
    gas = GasInput('fe: 3.1', '1.5', True, True, False, False, False, False, 273, 10000).process_input_data()
    gc = GasCalculations([gas]*10)
    print(gc.M, gc.R)










