from typing import NamedTuple
from BaseClasses import Item, ItemClassification

from .Names import ItemName

class FoMItem(Item):
    game: str = "Fields of Mistria"

class FoMItemData(NamedTuple):
    id: int
    item_class: ItemClassification = ItemClassification.progression

offset: int = 0
season_list = {
	ItemName.Season.Spring: FoMItemData(4000, ItemClassification.progression),
    ItemName.Season.Summer: FoMItemData(4001, ItemClassification.progression),
    ItemName.Season.Fall: FoMItemData(4002, ItemClassification.progression),
    ItemName.Season.Winter: FoMItemData(4003, ItemClassification.progression)
}

quest_list = {
    ItemName.Quest.UpperMines: FoMItemData(4500, ItemClassification.progression)
}

spell_list = {
    ItemName.Spell.Fire: FoMItemData(5000, ItemClassification.progression),
    ItemName.Spell.Heal: FoMItemData(5001, ItemClassification.progression),
    ItemName.Spell.Growth: FoMItemData(5002, ItemClassification.progression),
    ItemName.Spell.Rain: FoMItemData(5003, ItemClassification.progression)
}

tool_list = {
	ItemName.Tool.Axe: FoMItemData(2500, ItemClassification.progression),
    ItemName.Tool.Hoe: FoMItemData(2501, ItemClassification.progression),
    ItemName.Tool.Net: FoMItemData(2502, ItemClassification.progression),
    ItemName.Tool.WateringCan: FoMItemData(2503, ItemClassification.progression),
    ItemName.Tool.Pickaxe: FoMItemData(2504, ItemClassification.progression),
    ItemName.Tool.Sword: FoMItemData(2505, ItemClassification.progression),
    ItemName.Tool.FishingRod: FoMItemData(2506, ItemClassification.progression),
    ItemName.Tool.Shovel: FoMItemData(2507, ItemClassification.progression),
    ItemName.Tool.Pouch: FoMItemData(2508, ItemClassification.progression)
}

armor_list = {
    ItemName.Armor.Helmet: FoMItemData(2550, ItemClassification.progression),
    ItemName.Armor.Chest: FoMItemData(2551, ItemClassification.progression),
    ItemName.Armor.Pants: FoMItemData(2552, ItemClassification.progression),
    ItemName.Armor.Shoes: FoMItemData(2553, ItemClassification.progression),
    ItemName.Armor.Wristband: FoMItemData(2554, ItemClassification.progression),
    ItemName.Armor.HeroRing: FoMItemData(2555, ItemClassification.progression)
}

building_list = {
	ItemName.Building.Barn: FoMItemData(2600, ItemClassification.useful),
    ItemName.Building.Coop: FoMItemData(2601, ItemClassification.progression),
    ItemName.Building.Greenhouse: FoMItemData(2602, ItemClassification.useful),
    ItemName.Building.Kitchen: FoMItemData(2603, ItemClassification.useful),
    ItemName.Building.Crafting: FoMItemData(2604, ItemClassification.filler),
    ItemName.Building.Horse: FoMItemData(2605, ItemClassification.progression)
}

farm_item_list = {
	ItemName.FarmItem.BigBell: FoMItemData(2700, ItemClassification.filler),
    ItemName.FarmItem.AnimalSprite: FoMItemData(2701, ItemClassification.filler),
    ItemName.FarmItem.WaterSprite: FoMItemData(2702, ItemClassification.filler)
}

prog_perk_list = {
	ItemName.ProgressionPerk.AquaticAntiquities: FoMItemData(3000, ItemClassification.progression),
    ItemName.ProgressionPerk.WellPlaced: FoMItemData(3001, ItemClassification.progression),
    ItemName.ProgressionPerk.SunkenSecrets: FoMItemData(3002, ItemClassification.progression),
    ItemName.ProgressionPerk.MistSight: FoMItemData(3003, ItemClassification.progression),
    ItemName.ProgressionPerk.LostToHistory: FoMItemData(3004, ItemClassification.progression),
    ItemName.ProgressionPerk.Legendary: FoMItemData(3005, ItemClassification.progression),
    ItemName.ProgressionPerk.FormerFarmers: FoMItemData(3006, ItemClassification.progression)
}

perk_list = {
	ItemName.Perk.PreparedPicker: FoMItemData(3007, ItemClassification.useful),
    ItemName.Perk.ADayWellSpent: FoMItemData(3008, ItemClassification.useful),
    ItemName.Perk.GreenThumb: FoMItemData(3009, ItemClassification.useful),
    ItemName.Perk.Refreshing: FoMItemData(3010, ItemClassification.useful),
    ItemName.Perk.Bountiful: FoMItemData(3011, ItemClassification.useful),
    ItemName.Perk.HeavyDuty: FoMItemData(3012, ItemClassification.useful),
    ItemName.Perk.WellWatered: FoMItemData(3013, ItemClassification.useful),
    ItemName.Perk.NiceSwing: FoMItemData(3014, ItemClassification.useful),
    ItemName.Perk.LivingOffTheLand: FoMItemData(3015, ItemClassification.useful),
    ItemName.Perk.SuperbSower: FoMItemData(3016, ItemClassification.useful),
    ItemName.Perk.HarvestTime: FoMItemData(3017, ItemClassification.useful),
    ItemName.Perk.PrizeWinning: FoMItemData(3018, ItemClassification.useful),
    ItemName.Perk.SickleSword: FoMItemData(3019, ItemClassification.useful),
    ItemName.Perk.Ornamental: FoMItemData(3020, ItemClassification.useful),
    ItemName.Perk.PerfectPollinators: FoMItemData(3021, ItemClassification.useful),
    ItemName.Perk.MagicDesign: FoMItemData(3022, ItemClassification.useful),
    ItemName.Perk.EarthlyEssence: FoMItemData(3023, ItemClassification.useful),
    ItemName.Perk.WeedlineWatcher: FoMItemData(3024, ItemClassification.useful),
    ItemName.Perk.CurrencyOfCareThree: FoMItemData(3025, ItemClassification.useful),
    ItemName.Perk.AppealingReeling: FoMItemData(3026, ItemClassification.useful),
    ItemName.Perk.CatchoftheDay: FoMItemData(3027, ItemClassification.useful),
    ItemName.Perk.LuckyHaul: FoMItemData(3028, ItemClassification.useful),
    ItemName.Perk.PerfectCatch: FoMItemData(3029, ItemClassification.useful),
    ItemName.Perk.SchoolCrasher: FoMItemData(3030, ItemClassification.useful),
    ItemName.Perk.UnexpectedHaul: FoMItemData(3031, ItemClassification.useful),
    ItemName.Perk.FullClass: FoMItemData(3032, ItemClassification.useful),
    ItemName.Perk.TreasureTrove: FoMItemData(3033, ItemClassification.useful),
    ItemName.Perk.WeedlineWatcherTwo: FoMItemData(3034, ItemClassification.useful),
    ItemName.Perk.AppealingReelingTwo: FoMItemData(3035, ItemClassification.useful),
    ItemName.Perk.Frenzy: FoMItemData(3036, ItemClassification.useful),
    ItemName.Perk.WhataCatch: FoMItemData(3037, ItemClassification.useful),
    ItemName.Perk.LuckyHaulTwo: FoMItemData(3038, ItemClassification.useful),
    ItemName.Perk.AbyssalAscendence: FoMItemData(3039, ItemClassification.useful),
    ItemName.Perk.MuseumQuality: FoMItemData(3040, ItemClassification.useful),
    ItemName.Perk.Unpeatable: FoMItemData(3041, ItemClassification.useful),
    ItemName.Perk.WesternRuinsScholar: FoMItemData(3042, ItemClassification.useful),
    ItemName.Perk.SunkenTreasure: FoMItemData(3043, ItemClassification.useful),
    ItemName.Perk.Stoneturner: FoMItemData(3044, ItemClassification.useful),
    ItemName.Perk.EasternRoadScholar: FoMItemData(3045, ItemClassification.useful),
    ItemName.Perk.Pursuit: FoMItemData(3046, ItemClassification.useful),
    ItemName.Perk.BackinVogue: FoMItemData(3047, ItemClassification.useful),
    ItemName.Perk.NaturalBeauty: FoMItemData(3048, ItemClassification.useful),
    ItemName.Perk.MuseumQualityTwo: FoMItemData(3049, ItemClassification.useful),
    ItemName.Perk.MuseumQualityThree: FoMItemData(3050, ItemClassification.useful),
    ItemName.Perk.BackInVogueTwo: FoMItemData(3051, ItemClassification.useful),
    ItemName.Perk.NaturalBeautyTwo: FoMItemData(3052, ItemClassification.useful),
    ItemName.Perk.WasteNotWantNot: FoMItemData(3053, ItemClassification.useful),
    ItemName.Perk.TimeToEat: FoMItemData(3054, ItemClassification.useful),
    ItemName.Perk.RestorativeCooking: FoMItemData(3055, ItemClassification.useful),
    ItemName.Perk.TasteMaker: FoMItemData(3056, ItemClassification.useful),
    ItemName.Perk.AwardWinning: FoMItemData(3057, ItemClassification.useful),
    ItemName.Perk.LikableCooking: FoMItemData(3058, ItemClassification.useful),
    ItemName.Perk.Seasoned: FoMItemData(3059, ItemClassification.useful),
    ItemName.Perk.TimetoEatTwo: FoMItemData(3060, ItemClassification.useful),
    ItemName.Perk.AWaytotheHeart: FoMItemData(3061, ItemClassification.useful),
    ItemName.Perk.DinnerForTwo: FoMItemData(3062, ItemClassification.useful),
    ItemName.Perk.SpeedyCooking: FoMItemData(3063, ItemClassification.useful),
    ItemName.Perk.TimetoEatThree: FoMItemData(3064, ItemClassification.useful),
    ItemName.Perk.LovableCooking: FoMItemData(3065, ItemClassification.useful),
    ItemName.Perk.Snacktime: FoMItemData(3066, ItemClassification.useful),
    ItemName.Perk.CaffeineCrimes: FoMItemData(3067, ItemClassification.useful),
    ItemName.Perk.MagicalMeals: FoMItemData(3068, ItemClassification.useful),
    ItemName.Perk.FairyCooking: FoMItemData(3069, ItemClassification.useful),
    ItemName.Perk.FeedingFrenzy: FoMItemData(3070, ItemClassification.useful),
    ItemName.Perk.CloseBond: FoMItemData(3071, ItemClassification.useful),
    ItemName.Perk.BarnyardBounty: FoMItemData(3072, ItemClassification.useful),
    ItemName.Perk.CurrencyofCare: FoMItemData(3073, ItemClassification.useful),
    ItemName.Perk.WelcomeHome: FoMItemData(3074, ItemClassification.useful),
    ItemName.Perk.FeedPrepper: FoMItemData(3075, ItemClassification.useful),
    ItemName.Perk.CurrencyOfCareTwo: FoMItemData(3076, ItemClassification.useful),
    ItemName.Perk.DiscountTreats: FoMItemData(3077, ItemClassification.useful),
    ItemName.Perk.WelcomeHomeTwo: FoMItemData(3078, ItemClassification.useful),
    ItemName.Perk.BarnyardBountyTwo: FoMItemData(3079, ItemClassification.useful),
    ItemName.Perk.WindDown: FoMItemData(3080, ItemClassification.useful),
    ItemName.Perk.TheBellTolls: FoMItemData(3081, ItemClassification.useful),
    ItemName.Perk.MaximumMilling: FoMItemData(3082, ItemClassification.useful),
    ItemName.Perk.BarnyardBountyThree: FoMItemData(3083, ItemClassification.useful),
    ItemName.Perk.HammerTiming: FoMItemData(3084, ItemClassification.useful),
    ItemName.Perk.Lumberjack: FoMItemData(3085, ItemClassification.useful),
    ItemName.Perk.Masonry: FoMItemData(3086, ItemClassification.useful),
    ItemName.Perk.Forager: FoMItemData(3087, ItemClassification.useful),
    ItemName.Perk.HammerTimingTwo: FoMItemData(3088, ItemClassification.useful),
    ItemName.Perk.Natural: FoMItemData(3089, ItemClassification.useful),
    ItemName.Perk.QualityCrafting: FoMItemData(3090, ItemClassification.useful),
    ItemName.Perk.WorkingwiththeGrain: FoMItemData(3091, ItemClassification.useful),
    ItemName.Perk.MaterialWorld: FoMItemData(3092, ItemClassification.useful),
    ItemName.Perk.SteadySupplies: FoMItemData(3093, ItemClassification.useful),
    ItemName.Perk.SetPieces: FoMItemData(3094, ItemClassification.useful),
    ItemName.Perk.HammerTimingThree: FoMItemData(3095, ItemClassification.useful),
    ItemName.Perk.LumberjackTwo: FoMItemData(3096, ItemClassification.useful),
    ItemName.Perk.UndergroundInspiration: FoMItemData(3097, ItemClassification.useful),
    ItemName.Perk.DeliberateDebris: FoMItemData(3098, ItemClassification.useful),
    ItemName.Perk.WorkingWithTheGrainTwo: FoMItemData(3099, ItemClassification.useful),
    ItemName.Perk.CopperExpert: FoMItemData(3100, ItemClassification.useful),
    ItemName.Perk.TimeSensitive: FoMItemData(3101, ItemClassification.useful),
    ItemName.Perk.SharpBlacksmithing: FoMItemData(3102, ItemClassification.useful),
    ItemName.Perk.FortifiedBlacksmithing: FoMItemData(3103, ItemClassification.useful),
    ItemName.Perk.IronExpert: FoMItemData(3104, ItemClassification.useful),
    ItemName.Perk.TimeSensitiveTwo: FoMItemData(3105, ItemClassification.useful),
    ItemName.Perk.LeechBlacksmithing: FoMItemData(3106, ItemClassification.useful),
    ItemName.Perk.LightweightBlacksmithing: FoMItemData(3107, ItemClassification.useful),
    ItemName.Perk.Empowered: FoMItemData(3108, ItemClassification.useful),
    ItemName.Perk.HastyBlacksmithing: FoMItemData(3109, ItemClassification.useful),
    ItemName.Perk.SilverExpert: FoMItemData(3110, ItemClassification.useful),
    ItemName.Perk.TimeSensitiveThree: FoMItemData(3111, ItemClassification.useful),
    ItemName.Perk.EmpoweredTwo: FoMItemData(3112, ItemClassification.useful),
    ItemName.Perk.GoldExpert: FoMItemData(3113, ItemClassification.useful),
    ItemName.Perk.TirelessBlacksmithing: FoMItemData(3114, ItemClassification.useful),
    ItemName.Perk.TimeSensitiveFour: FoMItemData(3115, ItemClassification.useful),
    ItemName.Perk.EarthBreaker: FoMItemData(3116, ItemClassification.useful),
    ItemName.Perk.Oreriginal: FoMItemData(3117, ItemClassification.useful),
    ItemName.Perk.Reclaimer: FoMItemData(3118, ItemClassification.useful),
    ItemName.Perk.TreasureHunter: FoMItemData(3119, ItemClassification.useful),
    ItemName.Perk.IronHound: FoMItemData(3120, ItemClassification.useful),
    ItemName.Perk.TrueBlue: FoMItemData(3121, ItemClassification.useful),
    ItemName.Perk.Treasured: FoMItemData(3122, ItemClassification.useful),
    ItemName.Perk.MineTime: FoMItemData(3123, ItemClassification.useful),
    ItemName.Perk.Resonance: FoMItemData(3124, ItemClassification.useful),
    ItemName.Perk.EarthBreakerTwo: FoMItemData(3125, ItemClassification.useful),
    ItemName.Perk.SilverSeeker: FoMItemData(3126, ItemClassification.useful),
    ItemName.Perk.FantasticFinds: FoMItemData(3127, ItemClassification.useful),
    ItemName.Perk.GoodAsGold: FoMItemData(3128, ItemClassification.useful),
    ItemName.Perk.RefinedRockery: FoMItemData(3129, ItemClassification.useful),
    ItemName.Perk.BreakOneGetTwo: FoMItemData(3130, ItemClassification.useful),
    ItemName.Perk.GuardiansShield: FoMItemData(3131, ItemClassification.useful),
    ItemName.Perk.TrueStrike: FoMItemData(3132, ItemClassification.useful),
    ItemName.Perk.JumpAttack: FoMItemData(3133, ItemClassification.useful),
    ItemName.Perk.WellArmed: FoMItemData(3134, ItemClassification.useful),
    ItemName.Perk.QuickFooted: FoMItemData(3135, ItemClassification.useful),
    ItemName.Perk.WhatAnOffer: FoMItemData(3136, ItemClassification.useful),
    ItemName.Perk.GenerousInDefeat: FoMItemData(3137, ItemClassification.useful),
    ItemName.Perk.DungeonDelicacies: FoMItemData(3138, ItemClassification.useful),
    ItemName.Perk.PerfectPrefix: FoMItemData(3139, ItemClassification.useful),
    ItemName.Perk.Rocking: FoMItemData(3140, ItemClassification.useful),
    ItemName.Perk.InMotion: FoMItemData(3141, ItemClassification.useful),
    ItemName.Perk.OutOfJuice: FoMItemData(3142, ItemClassification.useful),
    ItemName.Perk.SonicBoom: FoMItemData(3143, ItemClassification.useful),
    ItemName.Perk.GiftExchange: FoMItemData(3144, ItemClassification.useful),
    ItemName.Perk.GuardiansShieldTwo: FoMItemData(3145, ItemClassification.useful),
    ItemName.Perk.TrueStrikeTwo: FoMItemData(3146, ItemClassification.useful),
    ItemName.Perk.Horsepower: FoMItemData(3147, ItemClassification.useful),
    ItemName.Perk.HarvestHorse: FoMItemData(3148, ItemClassification.useful),
    ItemName.Perk.NiceRide: FoMItemData(3149, ItemClassification.useful)
}

consumable_list = {
	ItemName.Consumable.ManaPotion: FoMItemData(2000, ItemClassification.filler),
    ItemName.Consumable.Tesserae: FoMItemData(2002, ItemClassification.filler),
    ItemName.Consumable.FairySyrup: FoMItemData(2003, ItemClassification.filler),
    ItemName.Consumable.HealingSyrup: FoMItemData(2004, ItemClassification.filler),
    ItemName.Consumable.RestorativeSyrup: FoMItemData(2005, ItemClassification.filler),
    ItemName.Consumable.SpeedySyrup: FoMItemData(2006, ItemClassification.filler),
    ItemName.Consumable.StaminaSyrup: FoMItemData(2007, ItemClassification.filler),
    ItemName.Consumable.StaminaUp: FoMItemData(2008, ItemClassification.useful),
    ItemName.Consumable.HeartCrystal: FoMItemData(2009, ItemClassification.useful),
    ItemName.Consumable.GiantEssence: FoMItemData(2010, ItemClassification.progression),
    ItemName.Consumable.LargeEssence: FoMItemData(2011, ItemClassification.useful),
    ItemName.Consumable.MediumEssence: FoMItemData(2012, ItemClassification.useful),
    ItemName.Consumable.SmallEssence: FoMItemData(2013, ItemClassification.useful),
    ItemName.Consumable.TinyEssence: FoMItemData(2014, ItemClassification.useful),
    ItemName.Consumable.FastFood: FoMItemData(2015, ItemClassification.filler),
    ItemName.Consumable.Poison: FoMItemData(2016, ItemClassification.filler),
    ItemName.Consumable.Fire: FoMItemData(2017, ItemClassification.filler),
    ItemName.Consumable.Ice: FoMItemData(2018, ItemClassification.filler),
    ItemName.Consumable.Coffee: FoMItemData(2019, ItemClassification.filler),
    
    ItemName.OtherFiller.ResourceWood: FoMItemData(2020, ItemClassification.filler),
    ItemName.OtherFiller.ResourceStone: FoMItemData(2021, ItemClassification.filler),
    ItemName.OtherFiller.ResourceWoodSmall: FoMItemData(2022, ItemClassification.filler),
    ItemName.OtherFiller.ResourceStoneSmall: FoMItemData(2023, ItemClassification.filler),
    ItemName.OtherFiller.Renown: FoMItemData(2024, ItemClassification.filler)
}

seed_list = {
	ItemName.Seed.Basil: FoMItemData(1629, ItemClassification.filler),
    ItemName.Seed.Beet: FoMItemData(1630, ItemClassification.filler),
    ItemName.Seed.Broccoli: FoMItemData(1631, ItemClassification.filler),
    ItemName.Seed.BurdockRoot: FoMItemData(1632, ItemClassification.filler),
    ItemName.Seed.Cabbage: FoMItemData(1633, ItemClassification.filler),
    ItemName.Seed.Carrot: FoMItemData(1634, ItemClassification.filler),
    ItemName.Seed.Catmint: FoMItemData(1635, ItemClassification.filler),
    ItemName.Seed.Cauliflower: FoMItemData(1636, ItemClassification.filler),
    ItemName.Seed.Celosia: FoMItemData(1637, ItemClassification.filler),
    ItemName.Seed.Chickpea: FoMItemData(1638, ItemClassification.filler),
    ItemName.Seed.ChiliPepper: FoMItemData(1639, ItemClassification.filler),
    ItemName.Seed.Chrysanthemum: FoMItemData(1640, ItemClassification.filler),
    ItemName.Seed.Corn: FoMItemData(1641, ItemClassification.filler),
    ItemName.Seed.Cosmos: FoMItemData(1642, ItemClassification.filler),
    ItemName.Seed.Cranberry: FoMItemData(1643, ItemClassification.filler),
    ItemName.Seed.Cucumber: FoMItemData(1644, ItemClassification.filler),
    ItemName.Seed.Daffodil: FoMItemData(1645, ItemClassification.filler),
    ItemName.Seed.DaikonRadish: FoMItemData(1646, ItemClassification.filler),
    ItemName.Seed.Daisy: FoMItemData(1647, ItemClassification.filler),
    ItemName.Seed.Dill: FoMItemData(1648, ItemClassification.filler),
    ItemName.Seed.FrostLily: FoMItemData(1649, ItemClassification.filler),
    ItemName.Seed.Garlic: FoMItemData(1650, ItemClassification.filler),
    ItemName.Seed.Heather: FoMItemData(1651, ItemClassification.filler),
    ItemName.Seed.Iris: FoMItemData(1652, ItemClassification.filler),
    ItemName.Seed.Jasmine: FoMItemData(1653, ItemClassification.filler),
    ItemName.Seed.Lilac: FoMItemData(1654, ItemClassification.filler),
    ItemName.Seed.Marigold: FoMItemData(1655, ItemClassification.filler),
    ItemName.Seed.MoonFruit: FoMItemData(1656, ItemClassification.filler),
    ItemName.Seed.Magic: FoMItemData(1657, ItemClassification.filler),
    ItemName.Seed.NightQueen: FoMItemData(1658, ItemClassification.filler),
    ItemName.Seed.Onion: FoMItemData(1659, ItemClassification.filler),
    ItemName.Seed.Oregano: FoMItemData(1660, ItemClassification.filler),
    ItemName.Seed.Pea: FoMItemData(1661, ItemClassification.filler),
    ItemName.Seed.Poinsettia: FoMItemData(1662, ItemClassification.filler),
    ItemName.Seed.Potato: FoMItemData(1663, ItemClassification.filler),
    ItemName.Seed.Pumpkin: FoMItemData(1664, ItemClassification.filler),
    ItemName.Seed.Rice: FoMItemData(1665, ItemClassification.filler),
    ItemName.Seed.Rosemary: FoMItemData(1666, ItemClassification.filler),
    ItemName.Seed.Sage: FoMItemData(1667, ItemClassification.filler),
    ItemName.Seed.Snapdragon: FoMItemData(1668, ItemClassification.filler),
    ItemName.Seed.SnowPeas: FoMItemData(1669, ItemClassification.filler),
    ItemName.Seed.SnowdropAnemone: FoMItemData(1670, ItemClassification.filler),
    ItemName.Seed.Strawberry: FoMItemData(1671, ItemClassification.filler),
    ItemName.Seed.SugarCane: FoMItemData(1672, ItemClassification.filler),
    ItemName.Seed.Sunflower: FoMItemData(1673, ItemClassification.filler),
    ItemName.Seed.SweetPotato: FoMItemData(1674, ItemClassification.filler),
    ItemName.Seed.Tea: FoMItemData(1675, ItemClassification.filler),
    ItemName.Seed.TempleFlower: FoMItemData(1676, ItemClassification.filler),
    ItemName.Seed.Thyme: FoMItemData(1677, ItemClassification.filler),
    ItemName.Seed.Tomato: FoMItemData(1678, ItemClassification.filler),
    ItemName.Seed.Tulip: FoMItemData(1679, ItemClassification.filler),
    ItemName.Seed.Turnip: FoMItemData(1680, ItemClassification.filler),
    ItemName.Seed.Viola: FoMItemData(1681, ItemClassification.filler),
    ItemName.Seed.Watermelon: FoMItemData(1682, ItemClassification.filler),
    ItemName.Seed.Wheat: FoMItemData(1683, ItemClassification.filler)
}

item_list = season_list | quest_list | tool_list | building_list | farm_item_list | prog_perk_list | perk_list | consumable_list | seed_list | spell_list | armor_list

season_amt = {
    ItemName.Season.Summer: 1,
    ItemName.Season.Fall: 1,
    ItemName.Season.Winter: 1
}

quest_amt = {}
for quest in quest_list:
	quest_amt[quest] = 1

spell_amt = {}
for spell in spell_list:
	spell_amt[spell] = 1

tool_amt = {
	ItemName.Tool.Axe: 6,
    ItemName.Tool.Hoe: 5,
    ItemName.Tool.Net: 5,
    ItemName.Tool.WateringCan: 5,
    ItemName.Tool.Pickaxe: 5,
    ItemName.Tool.Sword: 5,
    ItemName.Tool.FishingRod: 5,
    
    ItemName.Tool.Shovel: 6,
    ItemName.Tool.Pouch: 2
}

armor_amt = {
    # Assuming mistril (or additional) armor releases, increase the progressive armor sets by 1 on update
    ItemName.Armor.Helmet: 4,
    ItemName.Armor.Chest: 4,
    ItemName.Armor.Pants: 4,
    ItemName.Armor.Shoes: 4,
    ItemName.Armor.Wristband: 4,
    ItemName.Armor.HeroRing: 1
}

building_amt = {
	ItemName.Building.Barn: 3,
    ItemName.Building.Coop: 3,
    ItemName.Building.Greenhouse: 2,
    
    # Change to 4 when Champion's Kitchen comes out?
    ItemName.Building.Kitchen: 3,
    ItemName.Building.Crafting: 1,
    ItemName.Building.Horse: 1
}


farm_item_amt = {
	ItemName.FarmItem.BigBell: 1,
    ItemName.FarmItem.AnimalSprite: 3
}


prog_perk_amt = {}
for perk in prog_perk_list:
	prog_perk_amt[perk]= 1

perk_amt = {}
for perk in perk_list:
	perk_amt[perk] = 1


consumable_amt = {
	ItemName.Consumable.StaminaUp: 5,
    ItemName.Consumable.HeartCrystal: 5,
    ItemName.Consumable.Poison: 3,
    ItemName.Consumable.Fire: 3,
    ItemName.Consumable.Ice: 3,
    
	ItemName.Consumable.GiantEssence: 34
}

fixed_amount = season_amt | quest_amt | tool_amt | armor_amt | building_amt | farm_item_amt | prog_perk_amt | perk_amt | consumable_amt | spell_amt

seed_fillers = {}
for seed in seed_list:
	seed_fillers[seed] = 1

fillers = {
	ItemName.Consumable.ManaPotion: 2,
	ItemName.Consumable.Tesserae: 2,
	ItemName.Consumable.FairySyrup: 2,
	ItemName.Consumable.HealingSyrup: 2,
	ItemName.Consumable.RestorativeSyrup: 2,
	ItemName.Consumable.SpeedySyrup: 2,
	ItemName.Consumable.StaminaSyrup: 2,
	ItemName.Consumable.FastFood: 2,
	ItemName.Consumable.Coffee: 2,

	ItemName.Consumable.LargeEssence: 7,
	ItemName.Consumable.MediumEssence: 5,
	ItemName.Consumable.SmallEssence: 3,
	ItemName.Consumable.TinyEssence: 1,
    
    ItemName.OtherFiller.ResourceStone: 5,
    ItemName.OtherFiller.ResourceWood: 5,
    ItemName.OtherFiller.ResourceStoneSmall: 5,
    ItemName.OtherFiller.ResourceWoodSmall: 5,
    ItemName.OtherFiller.Renown: 5
}

fillers = seed_fillers | fillers

#traps = {}