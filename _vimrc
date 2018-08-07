" 设置Vim字符集『enc』
set encoding=utf-8
" 不要备份文件，使用backup备份文件（原文件加～后缀）
"set nobackup
" 不生成.swap文件
"set noswapfile

" 搜索结果高亮『hls』
set hlsearch
" 启用类似Emacs的增量（incremental）搜索，搜索与输入同时进行『is』
set incsearch
" 搜索内容不区分大小写『ic』
set ignorecase
" 智能匹配，即小写全匹配，大小写混合则严格匹配『scs』
set smartcase

" mouse=a 启动所有模式，会屏蔽鼠标的右键功能；
" mouse=v 让Vim在可视化模式下也可以使用右键粘贴
set mouse=v
" 显示行号『nu』
set number
" 显示光标所在列号『ru』
set ruler
" 高亮当前行『cul』
set cursorline
" 显示匹配的括号『sm』
set showmatch
" 不显示响铃『noeb』
set noerrorbells
" 可视化铃声『vb』
set visualbell
" 光标移动到buffer的顶部和底部时保持3行距离
set scrolloff=3
" 高亮当前列『cuc』
"set cursorcolumn
" 启用List模式，用CTRL-I显示制表符，用$显示行结束符
"set list
" 显示当前的模式，FreeBSD下默认不显示『sc』
set showcmd
" 设置在状态行显示的信息
set laststatus=2
set statusline=\ %<%F[%1*%M%*%n%R%H]%=\ %y\ %0(%{&fileformat}\ %{&encoding}\ %l/%L\,%c%V\ %P%)\

" 启用自动缩进，和上一行的缩进保持一致『ai』
set autoindent
set smartindent
" 使用C语言的缩进风格『cin』
set cindent
" 探测文件类型
filetype on
" 为特定文件类型载入相关缩进文件
filetype indent on
" 设置F6为切换Paste模式的快捷键，便于从其他窗口向Vim中粘贴代码，GUI下的Vim可能无效『pt』
set pastetoggle=<F6>

" 是否符使用空格代替缩进和（软）制表『et』
"set expandtab
set noexpandtab
" 设置制表符为4 个空格『ts』
set tabstop=4
" 设置软制表符为4 个空格『sts』
set softtabstop=4
" 设置缩进为4 个空格『sw』
set shiftwidth=4

" 启用语法高亮『syn』
set background=dark
syntax on
