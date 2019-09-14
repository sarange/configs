#!/usr/bin/zsh
#####
# File: /home/sarange/.config/i3/link.sh
# Project: /home/sarange/.config/i3
# Created Date: Sunday, June 16th 2019, 8:49:49 pm
# Author: sarange
# -----
# Last Modified: Thu Sep 12 2019
# Modified By: sarange
# -----
# Copyright (c) 2019 sarange
# 
# Talk is cheap. Show me the code.
#####

sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-autosuggestions ~/.zsh/zsh-autosuggestions
pip3 install virtualenv --user
git clone "https://github.com/MichaelAquilina/zsh-autoswitch-virtualenv.git" "$ZSH_CUSTOM/plugins/autoswitch_virtualenv"
ln -s ~/.config/i3/zshrc ~/.zshrc
ln -s ~/.config/i3/sarange.zsh-theme ~/.oh-my-zsh/themes/sarange.zsh-theme
xrdb -load ~/.config/i3/Xresources
mkdir ~/.config/youtube-dl && ln -s ~/.config/i3/youtube-dl/config ~/.config/youtube-dl/config
ln -s ~/.config/i3/newsboat/ ~/.config/