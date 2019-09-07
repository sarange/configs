# Script from https://essex09.github.io/2018-11-22-i3-gaps-kali/
# Go to tmp for a cleaner build
cd /tmp

apt install libxcb-shape0-dev libxcb-composite0-dev libxcb-randr0-dev libxcb-xtest0-dev libxcb-xinerama0-dev libxcb-shape0-dev libxcb-xkb-dev xcb-proto python-xcbgen doxygen libxcb-ewmh-dev psmisc libxkbfile-dev python-requests fonts-font-awesome -y

# Install i3 and it's dependencies
echo -e "Installing i3"
apt-get install i3 -y

# i3-gaps Dependencies
echo -e "Installing i3-gaps dependencies"
apt-get install -y libxcb-keysyms1-dev libpango1.0-dev libxcb-util0-dev xcb libxcb1-dev libxcb-icccm4-dev libyajl-dev libev-dev libxcb-xkb-dev libxcb-cursor-dev libxkbcommon-dev libxcb-xinerama0-dev libxkbcommon-x11-dev libstartup-notification0-dev libxcb-randr0-dev libxcb-xrm0 libxcb-xrm-dev

# i3-gaps Installation
echo -e "Installing i3-gaps"
mkdir gui && cd gui
git clone https://www.github.com/Airblader/i3 i3-gaps && cd i3-gaps

## Source: https://github.com/Airblader/i3/wiki/Compiling-&-Installing
# Compile & Install
autoreconf --force --install
rm -rf build/
mkdir -p build && cd build/
