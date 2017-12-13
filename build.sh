apktool d /apk/app-release.apk build
# jarsigner -sigalg MD5withRSA -digestalg SHA1 -keystore /Applications/Android Studio.app/Contents/bin/mykeystore -storepass 123456 signedjar app-release-unsigned