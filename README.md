# Sound Player
This is a ROS package that offers a service to play sound files using pygame

## Adding sounds
Put the sounds in the sounds directory under the package root, e.g.:
- sound_player
	- sounds
		- test.wav
		- bla
			- noise.wav

## Playing a sound
```
rosservice call /play_sound "name: '/test'"
rosservice call /play_sound "name: '/bla/noise'"
```
