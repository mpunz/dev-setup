.PHONY: neovim

all: editor dot

neovim:
	sudo apt-get install -y ninja-build gettext libtool libtool-bin autoconf automake cmake g++ pkg-config unzip
	rm -rf neovim
	git clone https://github.com/neovim/neovim.git
	rm -rf ${HOME}/bin/neovim
	mkdir -p ${HOME}/bin/neovim
	cd neovim && make CMAKE_EXTRA_FLAGS="-DCMAKE_INSTALL_PREFIX=${HOME}/bin/neovim" && make install
	rm -rf neovim
	rm -rf ~/.config/nvim/*
	
pathogen:
	mkdir -p ~/.config/nvim/autoload
	mkdir -p ~/.config/nvim/bundle
	curl -LSso ~/.config/nvim/autoload/pathogen.vim https://tpo.pe/pathogen.vim

dot:
	@cp bashrc.skeleton ${HOME}/.bashrc.skeleton
	@cp bashrc ${HOME}/.bashrc
	@cp aliases ${HOME}/.aliases
	@cp init.vim ${HOME}/.config/nvim/init.vim

editor: neovim pathogen
