from enum import Enum

from pydantic import BaseModel


class ArmorTypeEnum(str, Enum):
    light = "Light Armor"
    medium = "Medium Armor"
    heavy = "Heavy Armor"
    shields = "Shield"


class WeaponTypeEnum(str, Enum):
    simple = "Simple Weapon"
    martial = "Martial Weapon"
    single_weapon = "Weapon"


class ArmorProficiency(BaseModel):
    type: ArmorTypeEnum

    def __str__(self):
        return f"{self.type} Proficiency"


class WeaponProficiency(BaseModel):
    type: WeaponTypeEnum
    name: str | None = None

    def __str__(self):
        if self.type == WeaponTypeEnum.single_weapon:
            return f"{self.name}s"
        return f"{self.type} Proficiency"


class OtherProficiency(BaseModel):
    name: str


class CharacterClass(BaseModel):
    name: str


class CharacterLevel(BaseModel):
    character_class: CharacterClass
    level: int


class Feature(BaseModel):
    name: str
    description: str = ""


class Race(BaseModel):
    name: str
    description: str = ""
    feature: Feature | None = None


class Background(BaseModel):
    name: str
    description: str = ""
    personality_traits: list[str] = []
    ideal: str | None = None
    bond: str | None = None
    flaw: str | None = None
    feature: Feature | None = None


class SkillProficiencies(BaseModel):
    acrobatics: bool = False
    animal_handling: bool = False
    arcana: bool = False
    athletics: bool = False
    deception: bool = False
    history: bool = False
    insight: bool = False
    intimidation: bool = False
    investigation: bool = False
    medicine: bool = False
    nature: bool = False
    perception: bool = False
    performance: bool = False
    persuasion: bool = False
    religion: bool = False
    sleight_of_hand: bool = False
    stealth: bool = False
    survival: bool = False


class SavingThrows(BaseModel):
    strength: bool = False
    dexterity: bool = False
    constitution: bool = False
    intelligence: bool = False
    wisdom: bool = False
    charisma: bool = False


class Character(BaseModel):
    name: str
    race: Race | None = None
    background: Background | None = None
    base_class: CharacterClass | None = None
    character_levels: list[CharacterClass] = []
    strength: int = 10
    dexterity: int = 10
    constitution: int = 10
    intelligence: int = 10
    wisdom: int = 10
    charisma: int = 10
    saving_throws: SavingThrows = SavingThrows()
    skill_proficiencies: SkillProficiencies = SkillProficiencies()
    features: list[Feature] = []
    weapon_proficiencies: list[WeaponProficiency] = []
    armor_proficiencies: list[ArmorProficiency] = []
    other_proficiencies: list[OtherProficiency] = []
    languages: list[str] = ["Common"]
