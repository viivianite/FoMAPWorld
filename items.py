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
    ItemName.Spell.Rain: FoMItemData(5003, ItemClassification.progression),
    ItemName.Spell.Light: FoMItemData(5004, ItemClassification.progression)
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
	ItemName.Building.Barn: FoMItemData(2600, ItemClassification.progression),
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
	ItemName.ProgressionPerk.SunkenSecrets: FoMItemData(3012, ItemClassification.progression),
    ItemName.ProgressionPerk.AquaticAntiquities: FoMItemData(3048, ItemClassification.progression),
    ItemName.ProgressionPerk.WellPlaced: FoMItemData(3088, ItemClassification.progression),
    ItemName.ProgressionPerk.Legendary: FoMItemData(3103, ItemClassification.progression),
    ItemName.ProgressionPerk.LostToHistory: FoMItemData(3127, ItemClassification.progression),
    ItemName.ProgressionPerk.FormerFarmers: FoMItemData(3128, ItemClassification.progression),
    ItemName.ProgressionPerk.MistSight: FoMItemData(3135, ItemClassification.progression),
    ItemName.ProgressionPerk.PerfectPick: FoMItemData(3156, ItemClassification.progression),
    ItemName.ProgressionPerk.LostToHistoryII: FoMItemData(3159, ItemClassification.progression)
}

perk_list = {
    ItemName.Perk.ADayWellSpent: FoMItemData(3000, ItemClassification.useful),
    ItemName.Perk.FeedingFrenzy: FoMItemData(3001, ItemClassification.useful),
    ItemName.Perk.BarnyardBounty: FoMItemData(3002, ItemClassification.useful),
    ItemName.Perk.AppealingReeling: FoMItemData(3003, ItemClassification.useful),
    ItemName.Perk.CatchOfTheDay: FoMItemData(3004, ItemClassification.useful),
    ItemName.Perk.CloseBond: FoMItemData(3005, ItemClassification.useful),
    ItemName.Perk.WelcomeHome: FoMItemData(3006, ItemClassification.useful),
    ItemName.Perk.WelcomeHomeII: FoMItemData(3007, ItemClassification.useful),
    ItemName.Perk.GreenThumb: FoMItemData(3008, ItemClassification.useful),
    ItemName.Perk.NiceSwing: FoMItemData(3009, ItemClassification.useful),
    ItemName.Perk.Refreshing: FoMItemData(3010, ItemClassification.useful),
    ItemName.Perk.SunkenTreasure: FoMItemData(3011, ItemClassification.useful),
    ItemName.Perk.Unpeatable: FoMItemData(3013, ItemClassification.useful),
    ItemName.Perk.WesternRuinsScholar: FoMItemData(3014, ItemClassification.useful),
    ItemName.Perk.GuardiansShield: FoMItemData(3015, ItemClassification.useful),
    ItemName.Perk.JumpAttack: FoMItemData(3016, ItemClassification.useful),
    ItemName.Perk.TrueStrike: FoMItemData(3017, ItemClassification.useful),
    ItemName.Perk.OreRiginal: FoMItemData(3018, ItemClassification.useful),
    ItemName.Perk.EarthBreaker: FoMItemData(3019, ItemClassification.useful),
    ItemName.Perk.WellArmed: FoMItemData(3020, ItemClassification.useful),
    ItemName.Perk.Reclaimer: FoMItemData(3021, ItemClassification.useful),
    ItemName.Perk.TreasureHunter: FoMItemData(3022, ItemClassification.useful),
    ItemName.Perk.Bountiful: FoMItemData(3023, ItemClassification.useful),
    ItemName.Perk.HeavyDuty: FoMItemData(3024, ItemClassification.useful),
    ItemName.Perk.WellWatered: FoMItemData(3025, ItemClassification.useful),
    ItemName.Perk.SchoolCrasher: FoMItemData(3026, ItemClassification.useful),
    ItemName.Perk.LuckyHaul: FoMItemData(3027, ItemClassification.useful),
    ItemName.Perk.RestorativeCooking: FoMItemData(3028, ItemClassification.useful),
    ItemName.Perk.Seasoned: FoMItemData(3029, ItemClassification.useful),
    ItemName.Perk.TimeToEat: FoMItemData(3030, ItemClassification.useful),
    ItemName.Perk.TimeToEatII: FoMItemData(3031, ItemClassification.useful),
    ItemName.Perk.AwardWinning: FoMItemData(3032, ItemClassification.useful),
    ItemName.Perk.LikableCooking: FoMItemData(3033, ItemClassification.useful),
    ItemName.Perk.HammerTiming: FoMItemData(3034, ItemClassification.useful),
    ItemName.Perk.HammerTimingII: FoMItemData(3035, ItemClassification.useful),
    ItemName.Perk.Lumberjack: FoMItemData(3036, ItemClassification.useful),
    ItemName.Perk.Masonry: FoMItemData(3037, ItemClassification.useful),
    ItemName.Perk.Forager: FoMItemData(3038, ItemClassification.useful),
    ItemName.Perk.WasteNotWantNot: FoMItemData(3039, ItemClassification.useful),
    ItemName.Perk.TasteMaker: FoMItemData(3040, ItemClassification.useful),
    ItemName.Perk.CopperExpert: FoMItemData(3041, ItemClassification.useful),
    ItemName.Perk.IronExpert: FoMItemData(3042, ItemClassification.useful),
    ItemName.Perk.TimeSensitive: FoMItemData(3043, ItemClassification.useful),
    ItemName.Perk.TimeSensitiveII: FoMItemData(3044, ItemClassification.useful),
    ItemName.Perk.SharpBlacksmithing: FoMItemData(3045, ItemClassification.useful),
    ItemName.Perk.FortifiedBlacksmithing: FoMItemData(3046, ItemClassification.useful),
    ItemName.Perk.PreparedPicker: FoMItemData(3047, ItemClassification.useful),
    ItemName.Perk.WorkingWithTheGrain: FoMItemData(3049, ItemClassification.useful),
    ItemName.Perk.QualityCrafting: FoMItemData(3050, ItemClassification.useful),
    ItemName.Perk.Natural: FoMItemData(3051, ItemClassification.useful),
    ItemName.Perk.LeechBlacksmithing: FoMItemData(3052, ItemClassification.useful),
    ItemName.Perk.LightweightBlacksmithing: FoMItemData(3053, ItemClassification.useful),
    ItemName.Perk.Stoneturner: FoMItemData(3054, ItemClassification.useful),
    ItemName.Perk.EasternRoadScholar: FoMItemData(3055, ItemClassification.useful),
    ItemName.Perk.IronHound: FoMItemData(3056, ItemClassification.useful),
    ItemName.Perk.TrueBlue: FoMItemData(3057, ItemClassification.useful),
    ItemName.Perk.Treasured: FoMItemData(3058, ItemClassification.useful),
    ItemName.Perk.MineTime: FoMItemData(3059, ItemClassification.useful),
    ItemName.Perk.QuickFooted: FoMItemData(3060, ItemClassification.useful),
    ItemName.Perk.GenerousInDefeat: FoMItemData(3061, ItemClassification.useful),
    ItemName.Perk.WhatAnOffer: FoMItemData(3062, ItemClassification.useful),
    ItemName.Perk.DungeonDelicacies: FoMItemData(3063, ItemClassification.useful),
    ItemName.Perk.FeedPrepper: FoMItemData(3064, ItemClassification.useful),
    ItemName.Perk.CurrencyOfCare: FoMItemData(3065, ItemClassification.useful),
    ItemName.Perk.GeminiSeason: FoMItemData(3066, ItemClassification.useful),
    ItemName.Perk.MuseumQualityI: FoMItemData(3067, ItemClassification.useful),
    ItemName.Perk.Pursuit: FoMItemData(3068, ItemClassification.useful),
    ItemName.Perk.PerfectCatch: FoMItemData(3069, ItemClassification.useful),
    ItemName.Perk.WeedlineWatcher: FoMItemData(3070, ItemClassification.useful),
    ItemName.Perk.UnexpectedHaul: FoMItemData(3071, ItemClassification.useful),
    ItemName.Perk.SpeedyCooking: FoMItemData(3072, ItemClassification.useful),
    ItemName.Perk.LovableCooking: FoMItemData(3073, ItemClassification.useful),
    ItemName.Perk.FairyCooking: FoMItemData(3074, ItemClassification.useful),
    ItemName.Perk.HastyBlacksmithing: FoMItemData(3075, ItemClassification.useful),
    ItemName.Perk.TirelessBlacksmithing: FoMItemData(3076, ItemClassification.useful),
    ItemName.Perk.SilverExpert: FoMItemData(3077, ItemClassification.useful),
    ItemName.Perk.BackInVogue: FoMItemData(3078, ItemClassification.useful),
    ItemName.Perk.TimeSensitiveIII: FoMItemData(3079, ItemClassification.useful),
    ItemName.Perk.Empowered: FoMItemData(3080, ItemClassification.useful),
    ItemName.Perk.EmpoweredII: FoMItemData(3081, ItemClassification.useful),
    ItemName.Perk.DinnerForTwo: FoMItemData(3082, ItemClassification.useful),
    ItemName.Perk.AWayToTheHeart: FoMItemData(3083, ItemClassification.useful),
    ItemName.Perk.FullClassI: FoMItemData(3084, ItemClassification.useful),
    ItemName.Perk.TimeToEatIII: FoMItemData(3085, ItemClassification.useful),
    ItemName.Perk.Resonance: FoMItemData(3086, ItemClassification.useful),
    ItemName.Perk.NaturalBeauty: FoMItemData(3087, ItemClassification.useful),
    ItemName.Perk.MuseumQualityII: FoMItemData(3089, ItemClassification.useful),
    ItemName.Perk.PerfectPrefix: FoMItemData(3090, ItemClassification.useful),
    ItemName.Perk.Rocking: FoMItemData(3091, ItemClassification.useful),
    ItemName.Perk.InMotion: FoMItemData(3092, ItemClassification.useful),
    ItemName.Perk.OutOfJuice: FoMItemData(3093, ItemClassification.useful),
    ItemName.Perk.MaterialWorld: FoMItemData(3094, ItemClassification.useful),
    ItemName.Perk.SteadySupplies: FoMItemData(3095, ItemClassification.useful),
    ItemName.Perk.SetPieces: FoMItemData(3096, ItemClassification.useful),
    ItemName.Perk.HammerTimingIII: FoMItemData(3097, ItemClassification.useful),
    ItemName.Perk.LivingOffTheLand: FoMItemData(3098, ItemClassification.useful),
    ItemName.Perk.SuperbSower: FoMItemData(3099, ItemClassification.useful),
    ItemName.Perk.HarvestTime: FoMItemData(3100, ItemClassification.useful),
    ItemName.Perk.PrizeWinning: FoMItemData(3101, ItemClassification.useful),
    ItemName.Perk.TreasureTrove: FoMItemData(3102, ItemClassification.useful),
    ItemName.Perk.WeedlineWatcherII: FoMItemData(3104, ItemClassification.useful),
    ItemName.Perk.EarthBreakerII: FoMItemData(3105, ItemClassification.useful),
    ItemName.Perk.SilverSeeker: FoMItemData(3106, ItemClassification.useful),
    ItemName.Perk.FantasticFinds: FoMItemData(3107, ItemClassification.useful),
    ItemName.Perk.CurrencyOfCareII: FoMItemData(3108, ItemClassification.useful),
    ItemName.Perk.CurrencyOfCareIII: FoMItemData(3109, ItemClassification.useful),
    ItemName.Perk.DiscountTreats: FoMItemData(3110, ItemClassification.useful),
    ItemName.Perk.BarnyardBountyII: FoMItemData(3111, ItemClassification.useful),
    ItemName.Perk.AncientInspiration: FoMItemData(3112, ItemClassification.useful),
    ItemName.Perk.UndergroundInspiration: FoMItemData(3113, ItemClassification.useful),
    ItemName.Perk.DeliberateDebris: FoMItemData(3114, ItemClassification.useful),
    ItemName.Perk.Snacktime: FoMItemData(3115, ItemClassification.useful),
    ItemName.Perk.CaffeineCrimes: FoMItemData(3116, ItemClassification.useful),
    ItemName.Perk.AppealingReelingII: FoMItemData(3117, ItemClassification.useful),
    ItemName.Perk.Frenzy: FoMItemData(3118, ItemClassification.useful),
    ItemName.Perk.WhatACatch: FoMItemData(3119, ItemClassification.useful),
    ItemName.Perk.TheBellTolls: FoMItemData(3120, ItemClassification.useful),
    ItemName.Perk.MaximumMilling: FoMItemData(3121, ItemClassification.useful),
    ItemName.Perk.BarnyardBountyIII: FoMItemData(3122, ItemClassification.useful),
    ItemName.Perk.WindDown: FoMItemData(3123, ItemClassification.useful),
    ItemName.Perk.SickleSword: FoMItemData(3124, ItemClassification.useful),
    ItemName.Perk.Ornamental: FoMItemData(3125, ItemClassification.useful),
    ItemName.Perk.PerfectPollinators: FoMItemData(3126, ItemClassification.useful),
    ItemName.Perk.Horsepower: FoMItemData(3129, ItemClassification.useful),
    ItemName.Perk.HarvestHorse: FoMItemData(3130, ItemClassification.useful),
    ItemName.Perk.NiceRide: FoMItemData(3131, ItemClassification.useful),
    ItemName.Perk.MuseumQualityIII: FoMItemData(3132, ItemClassification.useful),
    ItemName.Perk.SonicBoom: FoMItemData(3133, ItemClassification.useful),
    ItemName.Perk.GiftExchange: FoMItemData(3134, ItemClassification.useful),
    ItemName.Perk.EarthlyEssence: FoMItemData(3136, ItemClassification.useful),
    ItemName.Perk.AbyssalAscendence: FoMItemData(3137, ItemClassification.useful),
    ItemName.Perk.GoldExpert: FoMItemData(3138, ItemClassification.useful),
    ItemName.Perk.TimeSensitiveIV: FoMItemData(3139, ItemClassification.useful),
    ItemName.Perk.BackInVogueII: FoMItemData(3140, ItemClassification.useful),
    ItemName.Perk.MagicalMeals: FoMItemData(3141, ItemClassification.useful),
    ItemName.Perk.GoodAsGold: FoMItemData(3142, ItemClassification.useful),
    ItemName.Perk.RefinedRockery: FoMItemData(3143, ItemClassification.useful),
    ItemName.Perk.BreakOneGetTwo: FoMItemData(3144, ItemClassification.useful),
    ItemName.Perk.LuckyHaulII: FoMItemData(3145, ItemClassification.useful),
    ItemName.Perk.LumberjackII: FoMItemData(3146, ItemClassification.useful),
    ItemName.Perk.MagicDesign: FoMItemData(3147, ItemClassification.useful),
    ItemName.Perk.NaturalBeautyII: FoMItemData(3148, ItemClassification.useful),
    ItemName.Perk.GuardianShieldII: FoMItemData(3149, ItemClassification.useful),
    ItemName.Perk.TrueStrikeII: FoMItemData(3150, ItemClassification.useful),
    ItemName.Perk.WorkingWithTheGrainII: FoMItemData(3151, ItemClassification.useful),
    ItemName.Perk.SureStrike: FoMItemData(3152, ItemClassification.useful),
    ItemName.Perk.GenerousInDefeatII: FoMItemData(3153, ItemClassification.useful),
    ItemName.Perk.FriendShaped: FoMItemData(3154, ItemClassification.useful),
    ItemName.Perk.MistrilMastery: FoMItemData(3155, ItemClassification.useful),
    ItemName.Perk.VoidValue: FoMItemData(3157, ItemClassification.useful),
    ItemName.Perk.MistrilExpert: FoMItemData(3158, ItemClassification.useful),
    ItemName.Perk.VoidCrafting: FoMItemData(3160, ItemClassification.useful),
    ItemName.Perk.BigWaterSprites: FoMItemData(3161, ItemClassification.useful),
    ItemName.Perk.EspressoYourself: FoMItemData(3162, ItemClassification.useful),
    ItemName.Perk.Playtime: FoMItemData(3163, ItemClassification.useful),
    ItemName.Perk.Eggstra: FoMItemData(3164, ItemClassification.useful),
    ItemName.Perk.CloseBondII: FoMItemData(3165, ItemClassification.useful),
    ItemName.Perk.TrueTrust: FoMItemData(3166, ItemClassification.useful),
    ItemName.Perk.HammerTimingIV: FoMItemData(3167, ItemClassification.useful),
    ItemName.Perk.DeliberateDebrisII: FoMItemData(3168, ItemClassification.useful),
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
	ItemName.Seed.Sunflower: FoMItemData(1000, ItemClassification.filler),
    ItemName.Seed.Basil: FoMItemData(1001, ItemClassification.filler),
    ItemName.Seed.Broccoli: FoMItemData(1002, ItemClassification.filler),
    ItemName.Seed.Cabbage: FoMItemData(1003, ItemClassification.filler),
    ItemName.Seed.Carrot: FoMItemData(1004, ItemClassification.filler),
    ItemName.Seed.Cauliflower: FoMItemData(1005, ItemClassification.filler),
    ItemName.Seed.Catmint: FoMItemData(1006, ItemClassification.filler),
    ItemName.Seed.Celosia: FoMItemData(1007, ItemClassification.filler),
    ItemName.Seed.Chickpea: FoMItemData(1008, ItemClassification.filler),
    ItemName.Seed.ChiliPepper: FoMItemData(1009, ItemClassification.filler),
    ItemName.Seed.Chrysanthemum: FoMItemData(1010, ItemClassification.filler),
    ItemName.Seed.Corn: FoMItemData(1011, ItemClassification.filler),
    ItemName.Seed.Cranberry: FoMItemData(1012, ItemClassification.filler),
    ItemName.Seed.Cucumber: FoMItemData(1013, ItemClassification.filler),
    ItemName.Seed.Daffodil: FoMItemData(1014, ItemClassification.filler),
    ItemName.Seed.Daisy: FoMItemData(1015, ItemClassification.filler),
    ItemName.Seed.Dill: FoMItemData(1016, ItemClassification.filler),
    ItemName.Seed.Cosmos: FoMItemData(1017, ItemClassification.filler),
    ItemName.Seed.Iris: FoMItemData(1018, ItemClassification.filler),
    ItemName.Seed.Lilac: FoMItemData(1019, ItemClassification.filler),
    ItemName.Seed.Marigold: FoMItemData(1020, ItemClassification.filler),
    ItemName.Seed.NightQueen: FoMItemData(1021, ItemClassification.filler),
    ItemName.Seed.Oregano: FoMItemData(1022, ItemClassification.filler),
    ItemName.Seed.Pea: FoMItemData(1023, ItemClassification.filler),
    ItemName.Seed.Potato: FoMItemData(1024, ItemClassification.filler),
    ItemName.Seed.Pumpkin: FoMItemData(1025, ItemClassification.filler),
    ItemName.Seed.Sage: FoMItemData(1026, ItemClassification.filler),
    ItemName.Seed.SnowdropAnemone: FoMItemData(1027, ItemClassification.filler),
    ItemName.Seed.Strawberry: FoMItemData(1028, ItemClassification.filler),
    ItemName.Seed.SweetPotato: FoMItemData(1029, ItemClassification.filler),
    ItemName.Seed.Thyme: FoMItemData(1030, ItemClassification.filler),
    ItemName.Seed.Tomato: FoMItemData(1031, ItemClassification.filler),
    ItemName.Seed.Tulip: FoMItemData(1032, ItemClassification.filler),
    ItemName.Seed.Turnip: FoMItemData(1033, ItemClassification.filler),
    ItemName.Seed.Watermelon: FoMItemData(1034, ItemClassification.filler),
    ItemName.Seed.SugarCane: FoMItemData(1035, ItemClassification.filler),
    ItemName.Seed.Tea: FoMItemData(1036, ItemClassification.filler),
    ItemName.Seed.Garlic: FoMItemData(1037, ItemClassification.filler),
    ItemName.Seed.Heather: FoMItemData(1038, ItemClassification.filler),
    ItemName.Seed.MoonFruit: FoMItemData(1039, ItemClassification.filler),
    ItemName.Seed.Onion: FoMItemData(1040, ItemClassification.filler),
    ItemName.Seed.Rice: FoMItemData(1041, ItemClassification.filler),
    ItemName.Seed.Rosemary: FoMItemData(1042, ItemClassification.filler),
    ItemName.Seed.Viola: FoMItemData(1043, ItemClassification.filler),
    ItemName.Seed.Wheat: FoMItemData(1044, ItemClassification.filler),
    ItemName.Seed.Beet: FoMItemData(1045, ItemClassification.filler),
    ItemName.Seed.BurdockRoot: FoMItemData(1046, ItemClassification.filler),
    ItemName.Seed.DaikonRadish: FoMItemData(1047, ItemClassification.filler),
    ItemName.Seed.FrostLily: FoMItemData(1048, ItemClassification.filler),
    ItemName.Seed.Jasmine: FoMItemData(1049, ItemClassification.filler),
    ItemName.Seed.Poinsettia: FoMItemData(1050, ItemClassification.filler),
    ItemName.Seed.Snapdragon: FoMItemData(1051, ItemClassification.filler),
    ItemName.Seed.SnowPeas: FoMItemData(1052, ItemClassification.filler),
    ItemName.Seed.TempleFlower: FoMItemData(1053, ItemClassification.filler),
    ItemName.Seed.Magic: FoMItemData(1054, ItemClassification.filler)
}

item_list = season_list | quest_list | tool_list | building_list | farm_item_list | prog_perk_list | perk_list | consumable_list | seed_list | spell_list | armor_list

season_amt = {
    #ItemName.Season.Spring: 1,
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