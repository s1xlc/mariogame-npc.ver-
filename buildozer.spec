[app]
title = Mario Game
package.name = mariogame
package.domain = org.mariogame
version = 0.1
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
requirements = python3,kivy,pyjnius
orientation = portrait
android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.ndk = 25b
android.androidx = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
bin_dir = bin
android.accept_sdk_license = True
android.skip_update = False
