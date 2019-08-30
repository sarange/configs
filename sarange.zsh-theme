#####
# File: /home/sarange/.oh-my-zsh/themes/sarange.zsh-theme
# Project: /home/sarange/.oh-my-zsh/themes
# Created Date: Monday, August 26th 2019, 12:05:28 am
# Author: sarange
# -----
# Last Modified: Fri Aug 30 2019
# Modified By: sarange
# -----
# Copyright (c) 2019 sarange
# 
# Talk is cheap. Show me the code.
#####

# Custom colors
color1=244 # background
color2=128 # git
color3=200 # venv
color4=154 # git branch
color5=150 # priv_sign_without
color6=196 # exit_code

# Git info
local git_info='$(git_prompt_info)'
ZSH_THEME_GIT_PROMPT_PREFIX="%{$FG[$color2]%} git:%{$FG[$color4]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_DIRTY=" %{$FG[124]%}✗"
ZSH_THEME_GIT_PROMPT_CLEAN=" %{$FG[046]%}✓"


# Virtual Enviroment
local venv_prompt='$(virtualenv_prompt_info)'
ZSH_THEME_VIRTUAL_ENV_PROMPT_PREFIX="%{$FG[$color3]%}<"
ZSH_THEME_VIRTUAL_ENV_PROMPT_SUFFIX=">%{$FG[$color1]%} @ %{$reset_color%}"
ZSH_THEME_VIRTUALENV_PREFIX=$ZSH_THEME_VIRTUAL_ENV_PROMPT_PREFIX
ZSH_THEME_VIRTUALENV_SUFFIX=$ZSH_THEME_VIRTUAL_ENV_PROMPT_SUFFIX

# User Privilage
if [[ $UID -eq 0 ]]; then
    local user_host='%{$terminfo[bold]$fg[red]%}%n@%m %{$reset_color%}'
    local user_priv='#'
else
    local user_host='%{$terminfo[bold]$fg[green]%}%n@%m %{$reset_color%}'
    local user_priv='$'
fi

# Prompt format:
#
# ∂<venv> @ username ∈ hostname ⊇ directory git:branch status ∑:exit_code
# ${priv_sign} COMMAND
#
# For example:
#
# ∂<pyfacebook> @ sarange ∈ archlinux ⊇ ~/Documents/pyfacebook git:master ✓ 
# $ 

local priv_sign='%{$terminfo[bold]$fg[red]%}⟼ ${user_priv}%{$reset_color%}'
local priv_sign_without='%{$terminfo[bold]$FG[$color5]%}∂%{$reset_color%}'
local username='%(#,%{$bg[yellow]%}%{$fg[black]%}%n%{$reset_color%},%{$fg[blue]%}%n)%{$FG[$color1]%}'
local hostname='%{$fg[blue]%}%m%{$FG[$color1]%}'
local current_dir='%{$terminfo[bold]$fg[yellow]%}%~%{$reset_color%}'
local exit_code='%(?,,%{$FG[$color6]%}∑:%?%{$reset_color%})'

PROMPT="${priv_sign_without} ${venv_prompt}${username} ∈ ${hostname} ⊇ ${current_dir}${git_info}
${priv_sign} "

RPROMPT="$exit_code"
