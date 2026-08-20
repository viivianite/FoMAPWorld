# FoM Archipelago Randomizer

An Archipelago implementation for farming simulator [Fields of Mistria](https://store.steampowered.com/app/2142790/Fields_of_Mistria/).

## Gameplay

Your goal is to **complete 50% of the museum** by donating items that are part of the collections. Due to the nature of randomizers, there are some noticeable differences from a vanilla playthrough, including:

- Starting with different tools from the beginning
- Being able to talk to Caldarus and collect essence from the beginning
- Certain story progression is now shuffled into randomization (e.g. access to the mines, unlocking the Horse Statue
- The cost of perks have been rebalanced
- Items have been removed from certain vendors (see **Notes**)
- You can optionally enable `deathlink`, allowing you to send other players who have deathlink enabled a death upon reaching 0 HP and vice versa. Receiving a death will immediately send you to Valen's clinic as if you hit 0 HP and fast forward to the next day. 

### Items
The following items are considered progression as necessary to get you through the main storyline and locations:
- Ability to skip to different seasons, with the `PGUP` button (please see **Notes** for several caveats)
- Access to the mines
- Spells
- Progressive tools
- Progressive inventory upgrades
- Progressive armor
- The Hero's Ring (from Adeline's 8 heart event)
- Buildings
- Horse statue
- Essence stones

Remaining filler items include:
- Farm sprites
- Big Bell
- Perks
- Potions and syrups
- Tesserae
- Maximum stats gain items (i.e. Heart Crystal and Stamina Up)
- Wheedle's consumables
- Coffee
- Resource bundles
- Town renown
- All seeds

### Locations
Locations that contain items by default include:
- Donating individual items to the museum's collection
- Completing the mines questline
- Unlocking skill perks through the dragon statues or horse statue

Optional locations include:
- **Story Quests**: Completing quests from the mailbox or request board marked as story quests.
- **Elevatorsanity**: Progressing through each elevator lift in the mines.
- **Renownsanity**: Reaching each town renown level (and rank). (See **Notes**)


## Setup Guide

### Requirements
- [Mods of Mistria Installer (MOMI)](https://github.com/Garethp/Mods-of-Mistria-Installer) by Garethp
- [Archipelago Launcher](https://github.com/ArchipelagoMW/Archipelago)
(**version 0.6.7 or later**)
- The latest version of the [Fields of Mistria APWorld](https://github.com/viivianite/FoMAPWorld/releases)
- The latest version of the [Fields of Mistria Archipelago Mod](https://github.com/viivianite/FoMAPMod/releases)

### Installation
1. Follow MOMI installation instructions.
2. Extract the files from the FoM Archipelago mod into the "mods" folder in your Fields of Mistria directory.
3. Run MOMI and install the mod.
4. Follow the Archipelago installation instructions.
5. Double click the downloaded .apworld file to install it into Archipelago's directory OR drag the .apworld into the Archipelago's custom_worlds directory.
6. When first connecting to the Fields of Mistria client, you will be prompted to open to the mod_data path. This is typically located in `%localappdata%/FieldsOfMistria/`.

### Connecting to Archipelago

## Notes
**Due to the nature of this mod, it is likely to be incompatible with mods that add items or alter gameplay in any fashion.**

This mod is still in development (and the game is receiving active updates that can break the mod), so you will almost certainly encounter unexpected situations. Known issues will be updated here as they arise.
