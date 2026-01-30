# Agent Class

The Agent class serves as the API for interacting with Grid Adventure V1. It comprises two mandatory functions and two optional functions for debugging purposes.

| Function | Description |
| --- | --- |
| `__init__(self) -> None` | Initialization function |
| `step(self, state: GridState \| ImageObservation) -> Action` | Step function |
| `parse(self, obs: ImageObservation) -> Action` | Function responsible for generating an Action based on a game representation. |
| `def parse(self, obs: ImageObservation) -> GridState` | Optional function utilized in GridPlay to aid in visualizing what your agent perceives. |
| `def info(self) -> dict[str, Any]` | Optional function utilized in GridPlay to provide any information about your agent. |

## Initialization Function

> `__init__(self) -> None`

This initialization function is executed once when instantiating the agent class.

**Tips:** Utilize this function to declare any internal variables utilized by your agent.

## Step Function
 
> `step(self, state: GridState | ImageObservation) -> Action`

This step function is invoked within the main agent-environment loop. Your implementation of this function serves as the “brain” of your agent, enabling it to make decisions regarding the next action based on the current observation.

## Parse Function 

> `parse(self, obs: ImageObservation) -> GridState` (Optional)

If implemented, it will be invoked by the Grid Play at every step to render what your agent currently sees, i.e., the parsed `GridState` representation from `ImageObservation`. This allows you to identify and correct errors in predicting the `GridState` from the `ImageObservation`.

You may find your agent's vision in the bottom right corner of the screen.

![Parse Window](../assets/parse.png)

In the provided example, we observe the actual grid in the blue square and the agent’s vision in the red square. From here, we can see that the agent mistakenly believes there’s a box in the grid.

## Info Function

> `info(self) -> dict[str, Any]` (Optional)

If implemented, Grid Play will display the information in the dictionary format shown below during each turn.

![Info Window](../assets/info.png)

This allows you to view the internal variables of your agent at every step.