# Half Life 2 Patcher for ARM (Apple Silicon) Macs
This was written by me (because the manual process is sometimes complicated)

# How to use
Requirements: Python

As no other modules are being used, you only need the `release-osx` file

Download it via the release tab.

Change permission by using
```sh
chmod +x release-osx
```

Run it via
```sh
./release-osx
```

Then, follow the instructions on the terminal.

The program will patch, after you gave it the Half Life 2 path, the game automatically.

You can then play Half Life 2 over steam now on your ARM Mac.

# Non interaction mode without patching
To only build the patch, run
```sh
./release-osx --debug
```

You can find the build at `source-engine/hl2`

# Use in other projects
You can use the modules in different projects, like patching different games.
