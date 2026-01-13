[app]

title = Excel Learning App
package.name = excellearning
package.domain = org.learn

source.dir = .
source.include_exts = py

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 21

android.permissions = INTERNET

android.allow_backup = True

android.archs = arm64-v8a,armeabi-v7a

[buildozer]

log_level = 2
warn_on_root = 1
