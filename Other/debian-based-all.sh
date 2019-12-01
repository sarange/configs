# Modified script from https://essex09.github.io/2018-11-22-i3-gaps-kali/
# Go to tmp for a cleaner build
cd /tmp

sudo apt install -y libxcb-shape0-dev libxcb-composite0-dev libxcb-randr0-dev libxcb-xtest0-dev libxcb-xinerama0-dev libxcb-shape0-dev libxcb-xkb-dev xcb-proto python-xcbgen doxygen libxcb-ewmh-dev psmisc libxkbfile-dev python-requests fonts-font-awesome

# Install i3 and it's dependencies
echo -e "Installing i3"
sudo apt install i3 -y

# i3-gaps Dependencies
echo -e "Installing i3-gaps dependencies"
sudo apt install -y libxcb-keysyms1-dev libpango1.0-dev libxcb-util0-dev xcb libxcb1-dev libxcb-icccm4-dev libyajl-dev libev-dev libxcb-xkb-dev libxcb-cursor-dev libxkbcommon-dev libxcb-xinerama0-dev libxkbcommon-x11-dev libstartup-notification0-dev libxcb-randr0-dev libxcb-xrm0 libxcb-xrm-dev

# i3-gaps Installation
echo -e "Installing i3-gaps"
mkdir gui && cd gui
git clone https://www.github.com/Airblader/i3 i3-gaps && cd i3-gaps

## Source: https://github.com/Airblader/i3/wiki/Compiling-&-Installing
# Compile & Install
autoreconf --force --install
rm -rf build/
mkdir -p build && cd build/
../configure --prefix=/usr --sysconfdir=/etc --disable-sanitizers
make
sudo make install

# Polybar
git clone https://github.com/polybar/polybar.git --recursive
mkdir build
cd build
cmake ..
make -j$(nproc)
sudo make install

# Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
pip3 install virtualenv --user
git clone "https://github.com/MichaelAquilina/zsh-autoswitch-virtualenv.git" "$ZSH_CUSTOM/plugins/autoswitch_virtualenv"
ln -s ~/.config/i3/zshrc ~/.zshrc
ln -s ~/.config/i3/sarange.zsh-theme ~/.oh-my-zsh/themes/sarange.zsh-theme
xrdb -load ~/.config/i3/Xresources
