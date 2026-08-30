[app]

title = Mario Game
package.name = mariogame
package.domain = org.mariogame
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,json
requirements = python3,kivy,pyjnius
orientation = portrait
android.permissions = INTERNET

# Target and minimum SDK versions
android.api = 33
android.minapi = 21

# Stable NDK version for GitHub Actions container builds
android.ndk = 25b

android.androidx = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
bin_dir = bin
android.accept_sdk_license = True
```[How to Convert your Kivy Apps to APK Using GitHub Actions](https://www.youtube.com/watch?v=wbJxJ2Zjy_o)

This video provides a helpful visual walkthrough of setting up a clean GitHub Actions pipeline for compiling Kivy applications into Android APKs.
