[app]

# (str) Title of your application
title = Mario Game

# (str) Package name
package.name = mariogame

# (str) Package domain (needed for android packaging)
package.domain = org.mariogame

# (str) Source files where the include files are located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,ttf,json

# (list) Application requirements
requirements = python3,kivy,pyjnius

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (bool) Enable AndroidX support
android.androidx = True

# (list) The architectures to build for
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (str) Path to build artifact storage
bin_dir = bin

# (bool) Accept SDK license automatically
android.accept_sdk_license = True
