# agents_2d_map
Smart agents which travels the 2d map with training on multiple algorithms.

The aim of this project is to find different solutions to 2d maps travelling problem given different kind of tiles.

For example - tiles coud be normal - nothing, fire - low health, ice - takes more time, mountain - bloackage, and goal.

This project will help mimic multiple human behaviours by applying different kind of algorithms combined with sidderent set of training provided by Trainer class.

# Caution
For now, only the structure of the project is ready. More to be coming soon!

# Sample result
I created 4x4 tile map.

I trained my agent on this map by making a run from random position to the goal.

While running I update state value of each tile.

This is what I got.

1 value represents the goal.

[[0.8909895583809517, 0.9085140719680994, 0.933611406218002, 1], [0.8830120417926579, 0.895065892171084, 0.9068973014002409, 0.937679225714078], [0.881161811459758, 0.8890642081770717, 0.9003466631617233, 0.9167829777019285], [0.8779801435985701, 0.8862612565604371, 0.8951299318547647, 0.9016632183586331]]

From the results it is clear that it manages to find the shortest possible path but not the smartest as it dosn't consider much difference between fire and land/normal tile.
