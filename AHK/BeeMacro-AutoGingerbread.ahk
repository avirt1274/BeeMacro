n::  ; Клавиша активация скрипта
Loop
{	
    Click down
    Sleep 50
    Click up
    Sleep 50
    SendInput, {E Down}
    Sleep 100
    SendInput, {E Up}
}
return

m:: ; Клавиша закрытия скрипта
ExitApp