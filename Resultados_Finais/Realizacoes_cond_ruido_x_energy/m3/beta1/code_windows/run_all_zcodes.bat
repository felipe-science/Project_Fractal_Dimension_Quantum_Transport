@echo off
for /L %%i in (1,1,15) do (
    start "" python cond_ruido_beta1_m3_%%i.py
)
echo Fim da execução.
pause

