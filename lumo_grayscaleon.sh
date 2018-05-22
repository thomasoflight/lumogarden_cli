#!/bin/zsh
# A simple script for making it gray!

defaults write com.apple.universalaccess grayscale -bool yes
defaults write com.apple.CoreGraphics DisplayUseForcedGray -bool yes

launchctl unload /System/Library/LaunchAgents/com.apple.universalaccessd.plist
launchctl load /System/Library/LaunchAgents/com.apple.universalaccessd.plist
