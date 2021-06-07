@ECHO OFF

:Enc
set /p cho= Are you sure you want to Encrypt Files? (y/n)
if %cho%==Y goto Yes
if %cho%==y goto Yes
if %cho%==n goto END
if %cho%==N goto END 
goto END
:Yes
"C:\Users\Dhana\PycharmProjects\pythonProject\venv\Scripts\python.exe" "C:\Users\Dhana\PycharmProjects\dsgsec2\Enc.py"
@pause

echo Files Encrypted
goto END

:END
pause

