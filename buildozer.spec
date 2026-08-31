[app]

# Application name
title = Mario Game

# Package information
package.name = mariogame
package.domain = org.mariogame

# Version
version = 0.1

# Location of your main.py
source.dir = .

# Files that will be included in the APK
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf,otf,json,mp3,wav,ogg,mp4

# Python/Kivy dependencies
requirements = python3,kivy,pyjnius

# Phone orientation
orientation = portrait

# Android permissions
android.permissions = INTERNET

# Android configuration
android.api = 33
android.minapi = 21
android.ndk = 25b
android.androidx = True

# Supported CPU architectures
android.archs = arm64-v8a,armeabi-v7a


[buildozer]

# Buildozer logging
log_level = 2

# APK output directory
bin_dir = bin

# Automatically accept Android SDK licenses
android.accept_sdk_license = True

# Allow Buildozer to update Android dependencies
android.skip_update = False
