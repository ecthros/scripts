execute pathogen#infect()


" Spaces instead of tabs
let tabsize = 4
execute "set tabstop=".tabsize
execute "set shiftwidth=".tabsize
execute "set softtabstop=".tabsize

" Line Numbers
set number

" Color Scheme

colorscheme peachpuff
syntax enable
set background=light

" Other

set nocompatible
set backspace=indent,eol,start
set expandtab
set showmatch
set mouse=a
if has("mouse_sgr")
    set ttymouse=sgr
else
    set ttymouse=xterm2
end


set ruler
set showcmd

" Search Options
set smartcase
set ignorecase
set hlsearch

set statusline+=%f
set ls=2
set linebreak

" Indent
set autoindent
filetype indent plugin on

" Keyboard Mappings "
"-------------------"

" Press either Shift + Up or Shift + Down to move lines up or down
nnoremap <S-down> :m .+1<CR>==
nnoremap <S-up> :m .-2<CR>==
inoremap <S-down> <Esc>:m .+1<CR>==gi
inoremap <S-up> <Esc>:m .-2<CR>==gi
vnoremap <S-down> :m '>+1<CR>gv=gv
vnoremap <S-up> :m '<-2<CR>gv=gv

" Press Shift + Ctrl + d to duplicate a line
nnoremap <C-S-d> :t.<CR>==
inoremap <C-S-d> <Esc>:t.<CR>==gi

" Clear search highlights by pressing return in command mode
nnoremap <CR> :noh<CR><CR>


autocmd InsertEnter * :set number
autocmd InsertLeave * :set relativenumber

set mouse=
