#!/usr/bin/env python
import pygame
import rospy
import sys
import sound_player.srv
import threading
import rospkg
import os

sound_paths = {}

def play_sound_service(req):
    global sound_paths

    if req.name == "":
        rospy.loginfo("Stopping sound")
        pygame.mixer.music.stop()
    else:
        key = req.name
        if not key[0] == "/":
            key = "/" + key

        if key in sound_paths.keys():
            rospy.loginfo("Playing {}".format(key))
            pygame.mixer.music.load(sound_paths[key])
            pygame.mixer.music.play()
        else:
            rospy.logerr("Unknown sound {}".format(key))
    return speech_dispatcher.srv.PlayFileResponse()

def main():
    global sound_paths
    rospy.init_node("sound_player", sys.argv)

    #Get path of this package
    rospack = rospkg.RosPack()
    sounds_path = os.path.join(rospack.get_path("sound_player"), "sounds")

    #Generate keys for sounds from directory structure
    for root, dirs, files in os.walk(sounds_path):
        for f in files:
            key = root[len(sounds_path):] + "/" + os.path.splitext(f)[0]
            path = os.path.join(root, f)
            if key in sound_paths.keys():
                rospy.logerr("Found two sounds with same name but different extension. You will not be able to play one of them.\n{}, \n{} ".format(sound_paths[key], path))
            sound_paths[key] = path
            print key, sound_paths[key]
            

    s = rospy.Service("play_sound", speech_dispatcher.srv.PlayFile, play_sound_service)
    pygame.init()
    rospy.spin()

if __name__ == "__main__":
    main()
