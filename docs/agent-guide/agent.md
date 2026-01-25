#Agent Class

## Agent Class Template
The agent class needs to implement 2 functions (init and step).

| Function | Description |
| -- | -- |
|`__init__(self) -> None`| Initialising Function |
|`step(self, state: GridState | Observation) -> Action`| Function used to generate Action given a game representation. This should be the "Brains" of your agent. |

There is a 3rd function in Agent class (parse) that you can choose to implement. The parse function shows how your agent "sees" the grid. This can be useful for debugging image parsing of your agent. In grid-play, this function is called and you can see how your agent parses a given grid to detect any differences.

| Function | Description |
| -- | -- |
|`parse(self, ImageObservation) -> GridState`| Optional function to implement to visualise agent vision in grid-play |
