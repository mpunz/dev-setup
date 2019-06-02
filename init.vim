execute pathogen#infect()

filetype plugin indent on
syntax on

let g:python3_host_prog = '/home/michael/venv/neovim/neovim3/bin/python'

" autocomplete
let g:deoplete#enable_at_startup = 1
let g:deoplete#disable_auto_complete = 1
inoremap <expr> <C-k> deoplete#mappings#manual_complete()
inoremap <expr> <tab> pumvisible() ? "\<c-n>" : "\<tab>"

" type checking
let g:neomake_python_enabled_makers = ['mypy']
let g:neomake_python_mypy_exe = '/home/michael/venv/neovim/neovim3/bin/python'
let g:neomake_python_mypy_args = ['-m', 'mypy']
call neomake#configure#automake('nw', 750)
