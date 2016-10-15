# pycharm-dvorak-keymap
IntelliJ keyboard shortcuts are QWERTY though keyboard is Dvorak.

For all you geeks using a Dvorak keyboard layout and a jetbrains IDE (eg. pycharm, phpstorm etc) you may have noticed an annoying issue where the keymap goes back to qwerty when you use a modifier.  This messes up all the keyboard shortcuts.  

[There's a very old bug on jetbrains' tracker](https://youtrack.jetbrains.com/issue/IDEA-63779), but they are saying it should be fixed upstream by JDK, which of course will never happen.  So here is a keymap for getting your familiar old shortcuts back.

I use this on Linux/GNOME.  If you're working on a Mac, using [karabiner](https://pqrs.org/osx/karabiner/) is a better solution.

### Installation
In your IDE, choose `File -> Import settings...` and select `dvorak_settings.jar`

### What if I don't use the GNOME keymap?
Maybe one day I'll generate bugfixed maps for OSX and the other defaults.  Until that day, you could try the script `to_dvorak.py` to generate your own bugfixed keymap.

You'll need:
 - Python (either 2 or 3, doesn't matter)
 - Couple of requirements - `pip install beautifulsoup4 lxml`
 - An input file to remap

For the default keymaps, look in `<pycharm>/lib/resources.jar/idea/Keymap_*.xml`.  In case you didn't know, a .jar file is just a zip!

### Will the script work for PhpStorm, CLion, RubyMine etc?
I don't know, probably.  Try it and let me know.  
