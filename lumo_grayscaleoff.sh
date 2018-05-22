#!/bin/zsh
# A simple script for making it colour!

defaults write com.apple.universalaccess grayscale -bool no
defaults write com.apple.CoreGraphics DisplayUseForcedGray -bool no

launchctl unload /System/Library/LaunchAgents/com.apple.universalaccessd.plist
launchctl load /System/Library/LaunchAgents/com.apple.universalaccessd.plist
