#!/bin/bash

#Copyright (C) 2015 Barajas D. Paul <Paul.Barajas@linux.com>

USR_DIR="/home/pi/"
VIM_DIR="${USR_DIR}.vim"

if [ "${USER}" != "root" ]; then

    echo "Please run as root"
    exit
fi

apt-get install vim
apt-get install terminator
apt-get install exuberant-ctags

if [ ! -d "${VIM_DIR}" ]; then
    mkdir -p "${VIM_DIR}"
fi

mkdir -p autoload  bitmaps  bundle  colors  plugin

echo "installing vim-resource..."

cp -rv vim_package/vim-pathogen/autoload "${VIM_DIR}"
cp -rv vim_package/vim-sensible/plugin/ "${VIM_DIR}"
cp -rv vim_package/vim-colors-solarized "${VIM_DIR}"
cp -rv vim_package/taglist.vim "${VIM_DIR}/plugin"
cp -rv vim_package/vimrc "${USR_DIR}.vimrc"

echo "...finish"
