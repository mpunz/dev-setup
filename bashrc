source $HOME/.bashrc.skeleton

if [[ ":$PATH:" != *":$HOME/bin/neovim/bin:"* ]]; then
  export PATH=$HOME/bin/neovim/bin:$PATH
fi

if [[ ":$PATH:" != *":$HOME/bin/utils:"* ]]; then
  export PATH=$HOME/bin/utils:$PATH
fi

source $HOME/.aliases

#export PATH=$PATH:/usr/local/go/bin
