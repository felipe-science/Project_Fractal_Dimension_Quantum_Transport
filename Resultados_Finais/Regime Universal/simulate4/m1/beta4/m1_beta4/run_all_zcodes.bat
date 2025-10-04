@echo off
for /L %%i in (1,1,10) do (
    start "" python runG%%i.py
)
echo Todos os scripts foram iniciados.
pause

