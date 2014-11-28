
Debian
====================
This directory contains files used to package barnacoind/barnacoin-qt
for Debian-based Linux systems. If you compile barnacoind/barnacoin-qt yourself, there are some useful files here.

## barnacoin: URI support ##


barnacoin-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install barnacoin-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your barnacoin-qt binary to `/usr/bin`
and the `../../share/pixmaps/barnacoin128.png` to `/usr/share/pixmaps`

barnacoin-qt.protocol (KDE)

