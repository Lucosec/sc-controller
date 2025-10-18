"""SC-Controller - Paths.

Methods in this module are used to determine stuff like where user data is stored,
where sccdaemon can be executed from and similar.

This is gui-only thing, as sccdaemon doesn't really need to load anything what
python can't handle.
All this is needed since I want to have entire thing installable, runnable
from source tarball *and* debugable in working folder.
"""
import os
from pathlib import Path
import sys

def get_config_path() -> str:
	"""Return configuration directory.

	~/.config/scc under normal conditions.Path("$HOME/.config")
	"""
	confdir = Path(os.getenv("HOME")).joinpath(".config")
	if "XDG_CONFIG_HOME" in os.environ:
		confdir = Path(os.environ['XDG_CONFIG_HOME'])
	return Path(confdir, "scc").as_posix()


def get_profiles_path() -> str:
	"""Return directory where profiles are stored.

	~/.config/scc/profiles under normal conditions.
	"""
	return Path(get_config_path(), "profiles").as_posix()


def get_default_profiles_path() -> str:
	"""Return directory where default profiles are stored.

	Probably something like /usr/share/scc/default_profiles,
	or $SCC_SHARED/default_profiles if program is being started from
	script extracted from source tarball
	"""
	return Path(get_share_path(), "default_profiles").as_posix()


def get_menuicons_path() -> str:
	"""Return directory where menu icons are stored.

	~/.config/scc/menu-icons under normal conditions.
	"""
	return Path(get_config_path(), "menu-icons").as_posix()


def get_default_menuicons_path() -> str:
	"""Return directory where default menu icons are stored.

	Probably something like /usr/share/scc/images/menu-icons,
	or $SCC_SHARED/images/menu-icons if program is being started from
	script extracted from source tarball
	"""
	return Path(get_share_path(), "images/menu-icons").as_posix()


def get_button_images_path() -> str:
	"""Return directory where button images are stored.

	/usr/share/scc/images/button-images by default.
	"""
	return Path(get_share_path(), "images/button-images").as_posix()


def get_menus_path() -> str:
	"""Return directory where profiles are stored.

	~/.config/scc/profiles under normal conditions.
	"""
	return Path(get_config_path(), "menus").as_posix()


def get_default_menus_path() -> str:
	"""Return directory where default profiles are stored.

	Probably something like /usr/share/scc/default_profiles,
	or ./default_profiles if program is being started from
	extracted source tarball
	"""
	return Path(get_share_path(), "default_menus").as_posix()


def get_controller_icons_path() -> str:
	"""Return directory where controller icons are stored.

	~/.config/scc/controller-icons under normal conditions.

	This directory may not exist.
	"""
	return Path(get_config_path(), "controller-icons").as_posix()


def get_default_controller_icons_path() -> str:
	"""Return directory where controller icons are stored.

	Probably something like /usr/share/scc/images/controller-icons,
	or ./images/controller-icons if program is being started from
	extracted source tarball.

	This directory should always exist.
	"""
	return Path(get_share_path(), "images", "controller-icons").as_posix()


def get_share_path() -> str:
	"""Return directory where shared files are kept.

	Usually "/usr/share/scc" or $SCC_SHARED if program is being started from
	script extracted from source tarball
	"""
	if "SCC_SHARED" in os.environ:
		return Path(os.environ["SCC_SHARED"]).as_posix()
	paths = (
		"/usr/local/share/scc/",
		"/app/usr/share/scc/",
		os.path.expanduser("~/.local/share/scc"),
		Path(sys.prefix, "share/scc").as_posix()
	)
	for path in paths:
		p = Path(path)
		if p.exists():
			return p.as_posix()
	# No path found, assume default and hope for best
	return "/usr/share/scc"


def get_pid_file() -> str:
	"""Return path to PID file.

	~/.config/scc/daemon.pid under normal conditions.
	"""
	return Path(get_config_path(), "daemon.pid").as_posix()


def get_daemon_socket() -> str:
	"""Return path to socket that can be used to control sccdaemon.

	~/.config/scc/daemon.socket under normal conditions.
	"""
	return Path(get_config_path(), "daemon.socket").as_posix()
