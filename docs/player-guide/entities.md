## Floor

![Floor](../assets/floor.png)

**Description:**
Floor is the basic tile of the grid. Other entities can be present on Floor tiles.


## Agent

![Agent](../assets/human.png)

**Description:**  
The Agent is the character that you will control and play as. You will move around the grid and aim to complete the objective. Agent starts with predetermined Health points. Reducing Agent HP results in a game loss.

In 1 turn, an Agent can either move to an orthogonally adjacent tile (Up/Down/Left/Right), pickup a Collectible item or use a Key to unlock a Door.
Every move that an Agent takes in the game is associated with a uniform Cost. This includes wasted moves such as attempting to move into a Wall. The player should aim to meet the objective with lowest Cost incurred.

## Wall

![Wall](../assets/wall.png)

**Description:**

Walls can be present on the grid and restrict movement of the Agent.
A Wall is a Blocking entity and Agent will not be able to move onto a tile containing a Wall.

## Exit

![Exit](../assets/exit.png)

**Description:**  
This is the final escape tile that Agent needs to land on to complete the objective.

## Coin

![Coin](../assets/coin.png)

**Description:**  
Coin is a Collectible and Rewardable entity. Agent may collect the coin to reduce total Cost by 5. Note that picking up still incurs cost of 3, so total Cost is reduced by 2.


## Gem

![Gem](../assets/gem.png)

**Description:**  
Gem is a Collectible and Required entity. Agent needs to collect all gems present in the grid before moving to Exit to complete the objective.

## Key

![Key](../assets/key.png)

**Description:** 
Key is a Collectible entity. Agent can collect the Key which is needed to unlock a Door. To unlock the Door, the Agent needs to be orthogonally adjacent to a locked door and use the Key to unlock it.

## Door

![Locked_Door](../assets/locked_door.png)

**Description:**
A locked Door is a Blocking entity. Agent will not be able to pass through it. If a Key is used to unlock it, it becomes a unlocked door ![Unlocked_Door](../assets/opened_door.png) and is no longer Blocking.


## Box

![Box](../assets/box.png)

**Description:**
Box is a Blocking and Pushable entity. You are not able to pass through a Box but you can push it onto a free tile. A Box can be pushed onto a tile if there is no Blocking entity present in that tile. To push a box, the Agent needs to be orthogonally adjacent to the Box and attempt to move in the desired direction to push the Box. Note that both the Agent and the Box will move during this action.

## Lava

![Lava](../assets/lava.png)

**Description:**
Lava tiles have Damage associated with them. When the Agent lands on a Lava tile, 1 damage is dealt to it. The Agent loses if HP drops to 0.

## Powerups
Powerups are Collectible entities that are present in the grid. Each powerup is associated with a usage limit.

## Speed

![Speed](../assets/boots_powerup.png)

**Description:**
The Speed powerup allows the Agent to move 2 tiles in 1 turn. It lasts for 5 turns. 
Agent can still be blocked by any Blocking entities in the way. If the Agent passes through or lands on Lava tiles, Damage is still taken accordingly.

## Shield

![Shield](../assets/shield_powerup.png)

**Description:**
Shield gives the Agent Immunity. It has a usage limit of 5. When the Agent passes through or lands on a Lava tile, the Agent does not take Damage but loses 1 use of the powerup instead.

## Ghost

![Ghost](../assets/ghost_powerup.png)

**Description:**
Ghost gives the Agent Phasing. It lasts for 5 turns. While active, the Agent cannot be blocked by any Blocking entities. The Agent does not take Damage from tiles as well.
