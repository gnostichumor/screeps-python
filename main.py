import harvester
import builder
import upgrader
# defs is a package which claims to export all constants and some JavaScript objects, but in reality does
#  nothing. This is useful mainly when using an editor like PyCharm, so that it 'knows' that things like Object, Creep,
#  Game, etc. do exist.
from defs import *

# These are currently required for Transcrypt in order to use the following names in JavaScript.
# Without the 'noalias' pragma, each of the following would be translated into something like 'py_Infinity' or
#  'py_keys' in the output file.
__pragma__('noalias', 'name')
__pragma__('noalias', 'undefined')
__pragma__('noalias', 'Infinity')
__pragma__('noalias', 'keys')
__pragma__('noalias', 'get')
__pragma__('noalias', 'set')
__pragma__('noalias', 'type')
__pragma__('noalias', 'update')

max_creeps = 10

# get number of harvesters
# define builder
# define upgrader
# define repairer
# 



def creepName():
    return f'harvester{Game.time}''

def main():
    """
    Main game logic loop.
    """
    for name in Object.keys(Memory.creeps):
        if not Game.creeps[name]:
            del Memory.creeps[name]
            console.log("Clearing old creep from memory:", name)

    for name in Object.keys(Game.creeps):
        creep = Game.creeps[name]
        harvester.run(creep)

    #Run each spawn
    for name in Object.keys(Game.spawns):
        spawn = Game.spawns[name]
        if not spawn.spawning:
            # Get the number of our creeps in the room.
            num_creeps = _.sum(Game.creeps, lambda c: c.pos.roomName == spawn.pos.roomName)
            console.log(num_creeps)
            # If there are no creeps, spawn a creep once energy is at 250 or more
            if num_creeps < max_creeps and spawn.room.energyAvailable >= 250:
                spawn.spawnCreep([WORK, CARRY, MOVE, MOVE], creepName(), {'memory': {'role': 'harvester'}})
            # If there are less than 15 creeps but at least one, wait until all spawns and extensions are full before
            # spawning.
            elif num_creeps < max_creeps and spawn.room.energyAvailable >= spawn.room.energyCapacityAvailable:
                # If we have more energy, spawn a bigger creep.
                if spawn.room.energyCapacityAvailable >= 350:
                    spawn.spawnCreep([WORK, CARRY, CARRY, MOVE, MOVE, MOVE])
                else:
                    spawn.spawnCreep([WORK, CARRY, MOVE, MOVE])  
    
module.exports.loop = main
