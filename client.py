from __future__ import annotations
import asyncio
import json
import os
import multiprocessing
import subprocess
from typing import Any, Dict
import zipfile
from asyncio import StreamReader, StreamWriter
import ModuleUpdate
import Utils
from settings import get_settings

ModuleUpdate.update()
import requests

# CommonClient import first to trigger ModuleUpdater
from CommonClient import CommonContext, server_loop, gui_enabled, \
    ClientCommandProcessor, logger, get_base_parser

class FoMCommandProcessor(ClientCommandProcessor):
    def __init__(self,ctx):
            super.__init__(ctx)

class FoMContext(CommonContext):
    game = "Fields of Mistria"
    items_handling = 0b111

    slot_data: Dict[str, Utils.Any] = {}
    deathlink = False
    goal = 0
    museum_completion_percentage = 100
    story_checks = False
    renown_level = False
    renown_rank = False
    elevatorsanity = False
    seed_name = 0
    item_dict = {}

    def __init__(self, server_address, password):
        super(FoMContext, self).__init__(server_address, password)
        self.game = "Fields of Mistria"
        self.slot_data: Dict[str, Any] = {}

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(FoMContext, self).server_auth(password_requested)
        await self.get_username()
        self.tags = set()
        await self.send_connect()

    async def connect(self, address: typing.Optional[str] = None):
        #resetFilesStates()
        await super().connect(address)
    
    async def disconnect(self, allow_autoreconnect: bool = False):
        #self.resetFilesStates()
        await super().disconnect(allow_autoreconnect)

    async def connection_closed(self):
        self.resetFilesStates()
        await super().connection_closed()

    async def shutdown(self):
        self.resetFilesStates()
        await super().shutdown()


    def on_deathlink(self, data: Utils.Dict[str, Utils.Any]) -> None:
        super().on_deathlink(data)

    def run_gui(self):
        from kvui import GameManager

        class FoMManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Fields of Mistria Client"

        self.ui = FoMManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def on_package(self, cmd: str, args: Dict[str, Any]) -> None:
        mod_data_path = get_settings().fom_settings.mod_data_path        
        
        if not os.path.exists(mod_data_path):
            mod_data_path = Utils.user_path(mod_data_path)
        
        mod_path = mod_data_path + "/ap_rando"

        if cmd == "RoomInfo":

            self.seed_name = args["seed_name"]
            
            with open(mod_path+"/seeds/status.json", 'w') as f:
                connection_data = {
                    "connected": True,
                    "seed_name": self.seed_name
                }
                connect_json_str = json.dumps(connection_data, indent=4)
                f.write(connect_json_str)

            if not os.path.exists(mod_path+"/seeds"):
                os.makedirs(mod_path+ "/seeds")

            if not os.path.exists(mod_path + "/seeds/" +self.seed_name):
                os.mkdir(mod_path + "/seeds/" + self.seed_name)

            try:
                open(mod_path + "/seeds/" + self.seed_name + "/items.json", 'x')
            except:
                print("items.json already exists")

            try:
                with open(mod_path + "/seeds/" + self.seed_name + "/locations.json", 'x') as f:
                    f.write("{\"locations\": []}")
            except:
                print("locations.json already exists")
        
        if cmd == "Connected":
            self.deathlink = args["slot_data"]["death_link"] == 1

            print(args["slot_data"]["goal"])

            self.goal = args["slot_data"]["goal"]
            match self.goal:
                case _:
                    self.museum_completion_percentage = args["slot_data"]["museum_completion_percentage"]
            self.story_checks = args["slot_data"]["story_checks"] == 1
            self.renown_level = args["slot_data"]["renown_level"] == 1
            self.renown_rank = args["slot_data"]["renown_rank"] == 1
            self.elevatorsanity = args["slot_data"]["elevatorsanity"] == 1

            json_data = {
                "deathlink": self.deathlink,
                "goal": self.goal,
                "museum_completion_percentage": self.museum_completion_percentage,
                "story_checks": self.story_checks,
                "renown_level": self.renown_level,
                "renown_rank": self.renown_rank,
                "elevatorsanity": self.elevatorsanity
            }
            
            if self.deathlink == 1:
                try:
                    open(mod_path + "/seeds/" + self.seed_name + "/deathlink.json", 'x')
                except:
                    print("deathlink.json already exists")
                
            json_str = json.dumps(json_data, indent = 4)

            with open(mod_path + "/seeds/"+ self.seed_name+"/settings.json", 'w') as f:
                f.write(json_str)
            

        if cmd == "ReceivedItems":

            for Item in args["items"]:
                if Item.item in self.item_dict:
                    self.item_dict[Item.item] += 1
                else:
                    self.item_dict.update({Item.item: 1})

            item_json = json.dumps(self.item_dict)

            try:
                with open(mod_path + "/seeds/" + self.seed_name + "/items.json", 'w') as f:
                    f.write(item_json)
            except:
                with open(mod_path + "/seeds/" + self.seed_name + "/items.json", 'w') as f:
                    f.write(item_json)
            
            
            

    def resetFilesStates(self) -> None:
        if self.seed_name is None:
            return
        mod_path = get_settings().fom_settings.mod_data_path + "/ap_rando"
        
        try:
            os.remove(mod_path + "/seeds/" + self.seed_name + "/settings.json")
        except:
            print("couldn't remove settings.json")
        try:
            os.remove(mod_path + "/seeds/" + self.seed_name + "/items.json")
        except:
            print("couldn't remove items.json")
        try:
            os.remove(mod_path + "/seeds/" + self.seed_name + "/deathlink.json")
        except:
            print("couldn't remove deathlink.json")
        
        with open(mod_path+"/seeds/status.json", 'w') as f:
            connection_data = {
                "connected": False
            }
            connect_json_str = json.dumps(connection_data, indent=4)
            f.write(connect_json_str)

            

def launch(*args):
    async def main(args):
        ctx = FoMContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        await ctx.exit_event.wait()
        ctx.server_address = None

        await ctx.exit_event.wait()
        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="FoM Client")

    args, rest = parser.parse_known_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()
