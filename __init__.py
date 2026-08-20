import settings
from typing import Dict, Any, ClassVar
from BaseClasses import MultiWorld, Region, Item, LocationProgressType
from worlds.AutoWorld import World
from Utils import visualize_regions
from worlds.generic.Rules import set_rule, add_rule, forbid_item, add_item_rule
from worlds.LauncherComponents import Component, components, icon_paths, Type, launch
from .items import (FoMItem, FoMItemData, item_list, fixed_amount, fillers)
from .locations import(baseRegion, springRegion, summerRegion, fallRegion, winterRegion, upperminesRegion, tidecavernRegion, deepearthRegion, lavacavesRegion, deepwoodsRegion, aquaticPerkRegion, oopartPerkRegion, sunkenPerkRegion, mistPerkRegion, ritualPerkRegion, legendaryPerkRegion, vintagePerkRegion, perk1Region, perk2Region, perk3Region, perk4Region, perk5Region, elevatorUpperRegion, elevatorTideRegion, elevatorEarthRegion, elevatorLavaRegion, storyquestRegion, renownlevelRegion, renownrankRegion, horsestatueRegion, victoryRegion, minesPQRegion)
from .locations import (FoMAdvancement, all_items)
from .options import FieldsOfMistriaOptions

def launch_client(*args):
    from .client import launch as client_main
    launch(client_main, name="FoMClient", args = args)

components.append(
    Component(
        "Fields Of Mistria Client",
        component_type=Type.CLIENT,
        func=launch_client,
        icon="Fields of Mistria"
        ))

icon_paths["Fields of Mistria"] = f"ap:{__name__}/assets/icon.png"

class FoMSettings(settings.Group):
    class ModDataPath(settings.UserFolderPath):
        """Folder path to Fields of Mistria mod_data folder"""
        copy_to = None
        description = "Fields of Mistria mod_data folder"
    
    mod_data_path: ModDataPath = ModDataPath(ModDataPath.copy_to)

class FieldsOfMistriaWorld(World):
    """
    Fields of Mistria is a farming simulator developed by NPC Studios.
    """
    game = "Fields of Mistria"
    topology_present = False

    settings: ClassVar[FoMSettings]
    settings_key = "fom_settings"
    item_name_to_id = {name: data.id for name, data in item_list.items()}
    location_name_to_id = {name: data.id for name, data in all_items.items()}
    options_dataclass = FieldsOfMistriaOptions
    options: FieldsOfMistriaOptions

    def generate_early(self) -> None:
        self.multiworld.push_precollected(self.create_item("Spring"))

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)

        base_region = Region("Base", self.player, self.multiworld)
        base_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, base_region)for loc_name, loc_data in baseRegion.items()]
        
        # Season Regions
        spring_region = Region("Spring", self.player, self.multiworld)
        spring_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, spring_region)for loc_name, loc_data in springRegion.items()]
        summer_region = Region("Summer", self.player, self.multiworld)
        summer_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, summer_region)for loc_name, loc_data in summerRegion.items()]
        fall_region = Region("Fall", self.player, self.multiworld)
        fall_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, fall_region)for loc_name, loc_data in fallRegion.items()]
        winter_region = Region("Winter", self.player, self.multiworld)
        winter_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, winter_region)for loc_name, loc_data in winterRegion.items()]
        
        # Mine Regions
        uppermines_region = Region("Upper Mines", self.player, self.multiworld)
        uppermines_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, uppermines_region)for loc_name, loc_data in upperminesRegion.items()]
        tidecavern_region = Region("Tide Caverns", self.player, self.multiworld)
        tidecavern_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, tidecavern_region)for loc_name, loc_data in tidecavernRegion.items()]
        deepearth_region = Region("Deep Earth", self.player, self.multiworld)
        deepearth_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, deepearth_region)for loc_name, loc_data in deepearthRegion.items()]
        lavacaves_region = Region("Lava Caves", self.player, self.multiworld)
        lavacaves_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, lavacaves_region)for loc_name, loc_data in lavacavesRegion.items()]
        deepwoods_region = Region("Deep Woods", self.player, self.multiworld)
        deepwoods_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, deepwoods_region)for loc_name, loc_data in deepwoodsRegion.items()]
        
        # Perk Based Regions
        mines_pq_region = Region("Mines Perks & Questline", self.player, self.multiworld)
        mines_pq_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, mines_pq_region)for loc_name, loc_data in minesPQRegion.items()]
        aquaticPerk_region = Region("Aquatic Antiquities Perk", self.player, self.multiworld)
        aquaticPerk_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, aquaticPerk_region)for loc_name, loc_data in aquaticPerkRegion.items()]
        oopartPerk_region = Region("Well Placed Perk", self.player, self.multiworld)
        oopartPerk_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, oopartPerk_region)for loc_name, loc_data in oopartPerkRegion.items()]
        sunkenPerk_region = Region("Sunken Secrets Perk", self.player, self.multiworld)
        sunkenPerk_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, sunkenPerk_region)for loc_name, loc_data in sunkenPerkRegion.items()]
        mistPerk_region = Region("Mist Sight Perk", self.player, self.multiworld)
        mistPerk_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, mistPerk_region)for loc_name, loc_data in mistPerkRegion.items()]
        ritualPerk_region = Region("Lost to History Perk", self.player, self.multiworld)
        ritualPerk_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, ritualPerk_region)for loc_name, loc_data in ritualPerkRegion.items()]
        legendaryPerk_region = Region("Legendary Perk", self.player, self.multiworld)
        legendaryPerk_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, legendaryPerk_region)for loc_name, loc_data in legendaryPerkRegion.items()]
        vintagePerk_region = Region("Former Farmers Perk", self.player, self.multiworld)
        vintagePerk_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, vintagePerk_region)for loc_name, loc_data in vintagePerkRegion.items()]

        # Perk Acquire Regions
        tier1Perk_region = Region("Tier 1 Perks", self.player, self.multiworld)
        tier1Perk_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, tier1Perk_region)for loc_name, loc_data in perk1Region.items()]
        tier2Perk_region = Region("Tier 2 Perks", self.player, self.multiworld)
        tier2Perk_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, tier2Perk_region)for loc_name, loc_data in perk2Region.items()]
        tier3Perk_region = Region("Tier 3 Perks", self.player, self.multiworld)
        tier3Perk_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, tier3Perk_region)for loc_name, loc_data in perk3Region.items()]
        tier4Perk_region = Region("Tier 4 Perks", self.player, self.multiworld)
        tier4Perk_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, tier4Perk_region)for loc_name, loc_data in perk4Region.items()]
        tier5Perk_region = Region("Tier 5 Perks", self.player, self.multiworld)
        tier5Perk_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, tier5Perk_region)for loc_name, loc_data in perk5Region.items()]

        #Other Regions
        horsestatue_region = Region("Horse Statue Perks", self.player, self.multiworld)
        horsestatue_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, horsestatue_region)for loc_name, loc_data in horsestatueRegion.items()]
        
        if (self.options.elevatorsanity.value == 1):
            uppermines_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, uppermines_region)for loc_name, loc_data in elevatorUpperRegion.items()]
            tidecavern_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, tidecavern_region)for loc_name, loc_data in elevatorTideRegion.items()]
            deepearth_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, deepearth_region)for loc_name, loc_data in elevatorEarthRegion.items()]
            lavacaves_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, lavacaves_region)for loc_name, loc_data in elevatorLavaRegion.items()]
        if(self.options.story_checks.value == 1):
            storyQuest_region = Region("Story Quests", self.player, self.multiworld)
            storyQuest_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, storyQuest_region) for loc_name, loc_data in storyquestRegion.items()]
        if(self.options.renown_level.value == 1):
            renownLevel_region = Region("Renown Levels", self.player, self.multiworld)
            renownLevel_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, renownLevel_region) for loc_name, loc_data in renownlevelRegion.items()]
        if(self.options.renown_rank.value == 1):
            renownRank_region = Region("Renown Ranks", self.player, self.multiworld)
            renownRank_region.locations += [FoMAdvancement(self.player, loc_name, loc_data.id, renownRank_region) for loc_name, loc_data in renownrankRegion.items()]
        
        self.multiworld.regions += [menu_region, base_region]
        self.multiworld.regions += [spring_region, summer_region, fall_region, winter_region]
        self.multiworld.regions += [uppermines_region, tidecavern_region, deepearth_region, lavacaves_region]
        self.multiworld.regions += [deepwoods_region]
        self.multiworld.regions += [mines_pq_region, aquaticPerk_region, oopartPerk_region, sunkenPerk_region, mistPerk_region, ritualPerk_region, legendaryPerk_region, vintagePerk_region]
        self.multiworld.regions += [tier1Perk_region, tier2Perk_region, tier3Perk_region, tier4Perk_region, tier5Perk_region]
        self.multiworld.regions += [horsestatue_region]
        
        if (self.options.story_checks.value == 1):
            self.multiworld.regions += [storyQuest_region]
        if (self.options.renown_level.value == 1):
            self.multiworld.regions += [renownLevel_region]
        if (self.options.renown_rank.value == 1):
            self.multiworld.regions += [renownRank_region]

        menu_region.connect(base_region)
        base_region.connect(spring_region)
        
        if(self.options.story_checks.value == 1):
            base_region.connect(storyQuest_region)
        if(self.options.renown_level.value == 1):
            base_region.connect(renownLevel_region)
        if(self.options.renown_rank.value == 1):
            base_region.connect(renownRank_region)
        
        
        base_region.add_exits({"Upper Mines": "Mines Entrance", "Aquatic Antiquities Perk": "Obtain Aquatic Antiquities", "Well Placed Perk": "Obtain Well Placed", "Sunken Secrets Perk": "Obtain Sunken Secrets", "Mist Sight Perk": "Obtain Mist Sight", "Legendary Perk": "Obtain Legendary", "Former Farmers Perk": "Obtain Former Farmers", "Tier 1 Perks": "Tier 1 Essence", "Deep Woods": "Obtain Dragon's Breath", "Horse Statue Perks": "Unlock Horse Statue"})
        
        uppermines_region.connect(mines_pq_region)
        uppermines_region.add_exits({"Tide Caverns": "Enter Tide Caverns"})
        tidecavern_region.add_exits({"Deep Earth": "Enter Deep Earth"})
        deepearth_region.add_exits({"Lava Caves": "Enter Lava Caves"})
        
        tier1Perk_region.add_exits({"Tier 2 Perks": "Tier 2 Essence"})
        tier2Perk_region.add_exits({"Tier 3 Perks": "Tier 3 Essence"})
        tier3Perk_region.add_exits({"Tier 4 Perks": "Tier 4 Essence"})
        tier4Perk_region.add_exits({"Tier 5 Perks": "Tier 5 Essence"})
        
        tidecavern_region.add_exits({"Lost to History Perk": "Obtain Lost to History"})
        
        spring_region.add_exits({"Summer": "Summer Starts"})
        summer_region.add_exits({"Fall": "Fall Starts"})
        fall_region.add_exits({"Winter": "Winter Starts"})
        
        if (self.options.goal.value == 1):
            self.multiworld.completion_condition[self.player] = lambda state: state.can_reach_location("Mines Floor 80", self.player)

    def set_rules(self) -> None:
        set_rule(self.multiworld.get_entrance("Summer Starts", self.player), lambda state: state.has("Summer", self.player, 1))
        set_rule(self.multiworld.get_entrance("Fall Starts", self.player), lambda state: state.has("Fall", self.player, 1))
        set_rule(self.multiworld.get_entrance("Winter Starts", self.player), lambda state: state.has("Winter", self.player, 1))
        
        set_rule(self.multiworld.get_entrance("Mines Entrance", self.player), lambda state: state.has("Mines Unlock", self.player, 1))
        set_rule(self.multiworld.get_entrance("Enter Tide Caverns", self.player), lambda state: state.has("Progressive Pickaxe", self.player, 2))
        set_rule(self.multiworld.get_entrance("Enter Deep Earth", self.player), lambda state: state.has("Progressive Pickaxe", self.player, 3))
        set_rule(self.multiworld.get_entrance("Enter Lava Caves", self.player), lambda state: state.has("Progressive Pickaxe", self.player, 4))

        set_rule(self.multiworld.get_entrance("Obtain Aquatic Antiquities", self.player), lambda state: state.has("Aquatic Antiquities Perk", self.player, 1))
        set_rule(self.multiworld.get_entrance("Obtain Well Placed", self.player), lambda state: state.has("Well Placed Perk", self.player, 1))
        set_rule(self.multiworld.get_entrance("Obtain Sunken Secrets", self.player), lambda state: state.has("Sunken Secrets Perk", self.player, 1))
        set_rule(self.multiworld.get_entrance("Obtain Mist Sight", self.player), lambda state: state.has("Mist Sight Perk", self.player, 1))
        set_rule(self.multiworld.get_entrance("Obtain Lost to History", self.player), lambda state: state.has("Lost to History Perk", self.player, 1))
        set_rule(self.multiworld.get_entrance("Obtain Legendary", self.player), lambda state: state.has("Legendary Perk", self.player, 1))
        set_rule(self.multiworld.get_entrance("Obtain Former Farmers", self.player), lambda state: state.has("Former Farmers Perk", self.player, 1))
        set_rule(self.multiworld.get_entrance("Obtain Dragon's Breath", self.player), lambda state: state.has("Dragon's Breath", self.player, 1))
        
        set_rule(self.multiworld.get_entrance("Unlock Horse Statue", self.player), lambda state: state.has("Horse Statue", self.player, 1))
        
        set_rule(self.multiworld.get_entrance("Tier 1 Essence", self.player), lambda state: state.has("Giant Essence Stone", self.player, 3))
        set_rule(self.multiworld.get_entrance("Tier 2 Essence", self.player), lambda state: state.has("Giant Essence Stone", self.player, 7))
        set_rule(self.multiworld.get_entrance("Tier 3 Essence", self.player), lambda state: state.has("Giant Essence Stone", self.player, 14))
        set_rule(self.multiworld.get_entrance("Tier 4 Essence", self.player), lambda state: state.has("Giant Essence Stone", self.player, 27))
        set_rule(self.multiworld.get_entrance("Tier 5 Essence", self.player), lambda state: state.has("Giant Essence Stone", self.player, 29))

    def create_items(self) -> None:
        for name, quantity in fixed_amount.items():
            for i in range(quantity):
                item = self.create_item(name)
                self.multiworld.itempool.append(item)
        
        filler = len(all_items) - sum(fixed_amount.values())
        for _ in range(filler):
            name = self.random.choices(list(fillers.keys()), weights = list(fillers.values()))[0]
            item = self.create_item(name)
            self.multiworld.itempool.append(item)

    def create_item(self, name: str) -> Item:
        item_data = item_list[name]
        item = FoMItem(name, item_data.item_class, item_data.id, self.player)
        return item
    
    def fill_slot_data(self) -> Dict[str, Any]:
        slot_data = self.options.as_dict("goal", "museum_completion_percentage", "story_checks", "renown_level", "renown_rank", "elevatorsanity", "death_link")
        return slot_data