"f http://stackoverflow.com/questions/4976776/how-to-get-path-to-the-current-vimscript-being-executed
" Absolute path of script file with symbolic links resolved:
let s:current_file = resolve(expand('<sfile>:p'))
call OrchestraAddPath(s:current_file)

call Ostinato('CursorMoved', 'plop.wav')
call Ostinato('CursorMovedI', 'bub.wav')
call Ostinato('WinEnter', 'techno.wav')
call Ostinato('InsertEnter', 'bubble.wav')
call Ostinato('InsertLeave', 'mouth_pop.wav')
