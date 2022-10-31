# mahjong-game
First attempted in OxfordHack 2022\
\
Goal:
Singaporean/Malaysian Mahjong that follows rules according to: http://www.singaporemahjong.com/rules/ \
(currently slightly more similar to SzeChuan mahjong since unable to chi)\
\
The game is built using pygame and is semi-functional:
- we can pick up tiles and discard tiles
- we can do peng
- we can win when we have 4 sets of 3 (three of a kind or sequence) and a pair

[//]: # (Hello)
Known BUGS:
- player should not be able to peng on a tile that they discarded themselves
- players are forced to peng if possible - don't have a choice

[//]: # (Hello)
TODO:
- chi/gong functionality
- introduce flowers and animals
- evaluate type of winning hand
- calculate and track points of players over multiple rounds
