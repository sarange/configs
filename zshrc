#!/usr/bin/env bash
#####
# File: /home/sarange/.config/i3/zshrc
# Project: /home/sarange/.config/i3
# Created Date: Sunday, June 16th 2019, 2:51:06 pm
# Author: sarange
# -----
# Last Modified: Mon Jul 22 2019
# Modified By: sarange
# -----
# Copyright (c) 2019 sarange
# 
# Talk is cheap. Show me the code.
#####

# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:/usr/local/bin:$PATH:$HOME/.gem/ruby/2.6.0/bin:/usr/local/bin/pip:$HOME/.local/bin

# Path to your oh-my-zsh installation.
export ZSH=$HOME/.oh-my-zsh

# Fix terminal
TERM=xterm-256color

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
ZSH_THEME="bira"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
  git
  virtualenv
  archlinux
  nmap
  colorize
  colored-man-pages
  command-not-found
  extract
  web-search
  autoswitch_virtualenv $plugins
)

source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

# Old zshrc
# export USE_CCACHE=1
export EDITOR=vim
export HISTCONTROL=ignorespace

# New
autoload -U up-line-or-beginning-search
autoload -U down-line-or-beginning-search

zle -N up-line-or-beginning-search
zle -N down-line-or-beginning-search

bindkey "^[[A" up-line-or-beginning-search # Up
bindkey "^[[B" down-line-or-beginning-search # Down
bindkey "^d" backward-kill-line # Ctrl+D
bindkey "^H" backward-delete-word # Ctrl+Bksp

alias backup='~/Documents/backup.sh'
alias luks_C='sudo cryptsetup luksClose'
alias luks_O='sudo cryptsetup luksOpen'
alias luks_T1='sudo cryptsetup luksOpen /dev/LvmCryptStorage/T1 T1 && sudo mount /dev/mapper/T1 ~/Media/Luks/T1'
alias luks_T2='sudo cryptsetup luksOpen /dev/LvmCryptStorage/T2 T2 && sudo mount /dev/mapper/T2 ~/Media/Luks/T2'
alias luks_T3='sudo cryptsetup luksOpen /dev/LvmCryptStorage/T3 T3 && sudo mount /dev/mapper/T3 ~/Media/Luks/T3'
alias luks_CA='sudo umount ~/Media/Luks/T*; sudo cryptsetup luksClose'
alias baya='backup && yasu'
alias htb_con='sudo openvpn ~/Documents/PenTest/hackthebox/Other/sarange.ovpn'
alias htb='cd ~/Documents/PenTest/hackthebox/'
alias wallppotd='~/.config/i3/scripts/potd.py'
alias setwall='~/.config/i3/scripts/setWal.py'
alias qrcode='~/.config/i3/scripts/qrcode.sh'
alias incog='fc -p'
