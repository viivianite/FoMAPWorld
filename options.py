from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Range, Choice, PerGameCommonOptions, ExcludeLocations  # , OptionGroup


class Goal(Choice):
    """
    Museum Completion: Complete a certain percentage of the museum.
    Bottom of the Mines: Reach the bottom of the mines. (As of v1.14.1, level 80)
    """
    display_name = "Goal"
    option_museum_completion = 0
    option_bottom_of_the_mines = 1
    default = option_museum_completion

class MuseumCompletionPercentage(Range):
    """
    NOTE: Currently hardcoded to 50% - ignore this option.
    
    If your goal is 'Museum Completion', specify the percentage of the museum you need to complete.
    If your goal isn't 'Museum Completion', you can ignore this setting.
    """
    display_name = "Museum Completion Percentage"
    range_start = 50
    range_end = 100
    default = 50


class StoryChecks(Choice):
    """
    Enabling this option will add Story Quests (both by mail and on the bulletin board) as checks.
    """
    display_name = "Story Quest Checks"
    option_true = 1
    option_false = 0
    default = option_true
    
class RenownLevelChecks(Choice):
    """
    Enabling this option will add Renown Levels as checks.
    """
    display_name = "Renown Level Checks"
    option_true = 1
    option_false = 0
    default = option_false

class RenownRankChecks(Choice):
    """
    Enabling this option will add Town Ranks as checks.
    """
    display_name = "Town Rank Checks"
    option_true = 1
    option_false = 0
    default = option_false

class ElevatorSanity(Choice):
    """
    Enabling this option will add mines elevators as checks.
    """
    display_name = "Elevator Checks"
    option_true = 1
    option_false = 0
    default = option_true

class FoMExcludeLocations(ExcludeLocations):
    testset = set()
    for i in range(94):
        testset.add(f"Renown Level {i+1}")
    testset.add("Town Rank Stone")
    testset.add("Town Rank Copper")
    testset.add("Town Rank Ruby")
    testset.add("Town Rank Iron")
    testset.add("Town Rank Sapphire")
    testset.add("Town Rank Silver")
    testset.add("Town Rank Emerald") 
    testset.add("Town Rank Gold")
    testset.add("Town Rank Diamond")
    default = frozenset(testset)


@dataclass
class FieldsOfMistriaOptions(PerGameCommonOptions):
    goal: Goal
    museum_completion_percentage: MuseumCompletionPercentage
    story_checks: StoryChecks
    renown_level: RenownLevelChecks
    renown_rank: RenownRankChecks
    elevatorsanity: ElevatorSanity
    death_link: DeathLink
    exclude_locations: FoMExcludeLocations
