# Game Representation

Grid Adventure V1 operates as a turn based game. Players are supplied a snapshot of a turn of the Game. Players then return an action, which is then used to generate the snapshot.

## Types of representation
There are 3 ways for a Game Snapshot to be represented.

| Representation Type | Description |
| --- | --- |
| [GridState](gridstate.md) | A grid based representation using 2D Array. This is the most intuitive Representation. |
| [ImageObservation](image_observation.md) | An RGBA Image representation using a 3D Array, with additional info stored in an information dictionary |
| [State](state.md) | An Immutable world state. This is the most comprehensive, but low level representation |

**Note**: The Capstone Project can be solved without using the **State Representation**.
