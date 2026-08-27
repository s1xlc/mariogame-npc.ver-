[app]
# (existing settings...)
title = Mario Game
package.name = mariogame
package.domain = org.mariogame
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,mp3,mp4
source.include_dir = assets
version = 0.1
requirements = kivy,certifi,chardet,filetype,idna,requests,six,urllib3
orientation = portrait
fullscreen = 1
android.permissions = INTERNET

# Explicit versions to avoid license/build-tools errors
android.api = 33
android.min_api = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True