## Basic movements

In a turn, the Agent can move to an orthogonally adjacent tile (Up/Down/Left/Right)

#### Demo

The demo shows the Agent performing a move up action.

![Start](../assets/start.png)
![Up](../assets/up.png)

## Collectibles

If an Agent is on the same tile as a Collectible entity, the Agent can use a turn to collect it.

#### Demo

The Agent starts beside a Collectible Gem.

![Collect_Start](../assets/collectible_start.png)

The Agent performs a move to the right to stand on the same tile as the Gem.

![Collect_Sametile](../assets/collectible_same_tile.png)

Now, the Agent can perform a collect action to pick up the gem. It is added to inventory.

![Collected](../assets/collected.png)

## Key and Door

To unlock a door, the Agent must first collect a Key, then move to and unlock the door.

#### Demo

The Agent starts on the same tile as the Collectible Key. Agent can collect it.
![Key_Tile](../assets/key_tile.png)
![Collect_Key](../assets/collect_key.png)

To unlock the door, the Agent first needs to move adjacent to the door. Agent moves 2 steps to the right and 1 step down.

![Beside_Door](../assets/beside_door.png)

Then, the Agent uses the Key to unlock the door.

![Unlock_Door](../assets/unlocked%20door.png)

The door is no longer blocking and Agent is able to move onto the tile with the Door.

![Door_Tile](../assets/door_tile.png)


## Pushable Box

To push a box, Agent needs to stand adjacent to the Box and attempt to move in the direction to push the Box.

#### Demo

The Agent starts to the left of the box as shown in the grid.

![Box_Start](../assets/box_start.png)

Now, if the Agent attempts to move to the right, the Box will be pushed and Agent will move to the right.

![Box_Pushed](../assets/box_pushed.png)

