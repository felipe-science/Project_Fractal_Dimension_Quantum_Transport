@echo off
for /L %%i in (1,1,15) do (
    start "" python zcode%%i.py
)
echo Todos os scripts foram iniciados.
pause

