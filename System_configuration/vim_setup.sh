#!/bin/bash

#Copyright (C) 2015 Barajas D. Paul <Paul.Barajas@linux.com>
SOURCE_PATH=`pwd`
USR_DIR=${HOME}
VIM_DIR="${USR_DIR}/.vim"


sudo -k bash <<EOF

apt-get install -y vim
apt-get install -y terminator
apt-get install -y exuberant-ctags

EOF

if [ ! -d "${VIM_DIR}" ]; then
    mkdir -p "${VIM_DIR}"
fi

#mkdir -p autoload  bitmaps  bundle  colors  plugin

cd vim_package/
git clone git@github.com:tpope/vim-pathogen.git
git clone git@github.com:tpope/vim-sensible.git
git clone git@github.com:altercation/vim-colors-solarized.git
git clone git@github.com:vim-scripts/taglist.vim.git
cd ..
echo "installing vim-resource..."

cp -rv vim_package/vim-pathogen/autoload "${VIM_DIR}"
cp -rv vim_package/vim-sensible/plugin/ "${VIM_DIR}"
cp -rv vim_package/vim-colors-solarized "${VIM_DIR}"
cp -rv vim_package/taglist.vim "${VIM_DIR}/plugin"
cp -rv vim_package/vimrc "${USR_DIR}/.vimrc"

echo "...finish"
