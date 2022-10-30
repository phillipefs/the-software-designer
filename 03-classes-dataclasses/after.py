import random
import string
from dataclasses import dataclass, field
from enum import Enum, auto


def generate_vehicle_license() -> str:
    """Helper method for generating a vehicle license number."""

    digit_part = "".join(random.choices(string.digits, k=2))
    letter_part_1 = "".join(random.choices(string.ascii_uppercase, k=2))
    letter_part_2 = "".join(random.choices(string.ascii_uppercase, k=2))
    return f"{letter_part_1}-{digit_part}-{letter_part_2}"


class Accessory(Enum):
    AIRCO = auto()
    CRUISECONTROL = auto()
    NAVIGATION = auto()
    OPENROOF = auto()
    BATHTUB = auto()
    MINIBAR = auto()


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()

def default_accessories():
    return [Accessory.AIRCO]


@dataclass(frozen=True)
class Vehicle:
    brand: str
    model: str
    color: str
    license_plate: str = field(default_factory=generate_vehicle_license) #Init=False bloqueia a inicialização da licensa no momento de instância. 
    fuel_type: FuelType = FuelType.ELECTRIC
    accessories: list[Accessory] = field(default_factory=lambda: [Accessory.AIRCO])
    #accessories: list[Accessory] = field(default_factory=default_accessories) 2ª Opção

    """
    Código abaixo comentado pois foi passado o parametro frozen=True. 
    Isso significa que o objeto não pode sofrer alteração após instânciar 
    """
    # def __post_init__(self):
    #     """
    #     Este método é chamado após a instanciar um veículo.
    #     Utilizado para criar uma regra na hora de instânciar, caso o veiculo seja Tesla, será instânciado de uma forma diferente
    #     adicionando um -t no final da criação
    #     """
    #     self.license_plate = generate_vehicle_license()
    #     if self.brand == 'Tesla':
    #         self.license_plate += "-t"



def main() -> None:
    """
    Create some vehicles and print their details.
    """

    tesla = Vehicle(
        brand="Tesla",
        model="Model 3",
        color="black",
        #license_plate=generate_vehicle_license(), Passou a ser gerado automaticamente na linha 39
        accessories=[
            Accessory.AIRCO,
            Accessory.MINIBAR,
            Accessory.NAVIGATION,
            Accessory.CRUISECONTROL,
        ],
    )
    volkswagen = Vehicle(
        brand="Volkswagen",
        model="ID3",
        color="white",
        accessories=[Accessory.AIRCO, Accessory.NAVIGATION], 
    )
    bmw = Vehicle(
        brand="BMW",
        model="520e",
        color="blue",
        fuel_type=FuelType.PETROL,
        accessories=[Accessory.NAVIGATION, Accessory.CRUISECONTROL],
    )

    print(tesla)
    print(volkswagen)
    print(bmw)


if __name__ == "__main__":
    main()
