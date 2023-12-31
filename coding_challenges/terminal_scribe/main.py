
import math
from terminal_scribe import Canvas, TerminalScribe, RoboticTerminalScribe, RandomizedTerminalScribe, PlotTerminalScribe

def sine(x):
    return 5 * (math.sin(x/4)) + 10

def cosine(x):
    return 5 * (math.cos(x/4)) + 10

canvas = Canvas(30, 30)
# scribe = TerminalScribe(canvas=canvas)
# scribe.plotX(sine)
# scribe.plotX(cosine)


# scribe.setPos((4, 6))
# scribe.setDegrees(150)
# scribe.forward(1000)

# data structure to hold information to create and operate multiple scribes at once. 
# definition includes, name, position and instructions
# instructions are later flattened and executed for all the scribes 
scribes = [
    {
        "name": "scribeZ",
        "type": "robotic",
        "position": (7, 0),
        "instructions": [
            {
                "function": "left",
                "duration": 5
            },
            {
                "function": "down",
                "duration": 4
            },
            {
                "function": "right",
                "duration": 5
            },
            {
                "function": "up",
                "duration": 4
            }
        ]
    },
    {
        "name": "scribeA",
        "type": "terminal",
        "position": (5, 5),
        "instructions": [
            {
                "function": "forward",
                "duration": 30
            }
        ]
    },
    {
        "name": "scribeY",
        "type": "plot",
        "position": (5, 5),
        "instructions": [
            {
                "function": "forward",
                "duration": 30
            }
        ]
    },
    {
        "name": "scribeB",
        "position": (3, 10),
        "type": "random",
        "degrees": 135,
        "instructions": [
            {
                "function": "forward",
                "duration": 500
            }
        ]
    }
]

def createScribe(scribeDefinition, canvas):
    type = scribeDefinition['type']
    if type == 'terminal':
        return TerminalScribe(canvas)
    elif type == 'robotic':
        return RoboticTerminalScribe(canvas)
    elif type == 'plot':
        return PlotTerminalScribe(canvas)
    elif type == 'random':
        return RandomizedTerminalScribe(canvas, scribeDefinition['degrees'] if scribeDefinition['degrees'] else 45)
    else:
        raise ValueError(f'The type {type} is not supported to create a scribe')

for scribeDefinition in scribes:

    scribeDefinition['scribe'] = createScribe(scribeDefinition, canvas)
    scribeDefinition['scribe'].setPos(scribeDefinition['position'])

    scribeDefinition['instructions_flat'] = []
    for instruction in scribeDefinition['instructions']:
        scribeDefinition['instructions_flat'] = scribeDefinition['instructions_flat'] + [instruction['function']] * instruction['duration']

# find the longest instructions arr length
maxInstructionLen = max([len(scribeDefinition['instructions_flat']) for scribeDefinition in scribes])

# for counter execute all the scribes' instructions
for i in range(0, maxInstructionLen):
    for scribeDefinition in scribes:
        if i < len(scribeDefinition['instructions_flat']):
            fun_name = scribeDefinition['instructions_flat'][i]
            if fun_name == 'forward':
                scribeDefinition['scribe'].forward()
            elif fun_name == 'up':
                scribeDefinition['scribe'].drawUp()
            elif fun_name == 'down':
                scribeDefinition['scribe'].drawDown()
            elif fun_name == 'left':
                scribeDefinition['scribe'].drawLeft()
            elif fun_name == 'right':
                scribeDefinition['scribe'].drawRight()
