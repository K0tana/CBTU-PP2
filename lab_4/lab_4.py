from loguru import logger
import json
logger.add("debug.log", format="{time}, {level}, {message}", level="DEBUG", rotation="10 KB", compression="zip")

with open('data.json') as f:
    data = json.load(f)


head = """Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------"""



@logger.catch
def find():
    print(head)
    for i in data["imdata"]:
        in_1 = i["l1PhysIf"]["attributes"]["dn"]
        in_2 = i["l1PhysIf"]["attributes"]["speed"]
        in_3 = i["l1PhysIf"]["attributes"]["mtu"]
    # logger.debug(print(f"{in_1:71} {in_2}  {in_3:^7}"))
        print(f"{in_1:71} {in_2}  {in_3:^7}")

a = 1
find()