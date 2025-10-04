@echo off
for /L %%i in (1,1,5) do (
    start "" python cod%%i.py
)
echo Todos os scripts foram iniciados.
pause

