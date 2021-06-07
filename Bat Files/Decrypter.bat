@ECHO OFF

:Dec
set /p cho= Are you sure you want to Decrypt File? (y/n)
if %cho%==Y goto Y2
if %cho%==y goto Y2
if %cho%==n goto END
if %cho%==N goto END 
goto END
:Y2
echo Enter password to Decrypt Files
set/p "pass=＞"
if NOT %pass%== 456 goto FAIL
"C:\Users\Dhana\PycharmProjects\pythonProject\venv\Scripts\python.exe" "C:\Users\Dhana\PycharmProjects\dsgsec2\Dec.py"
@pause

echo Files Decrypted
goto END

:FAIL
"C:\Users\Dhana\PycharmProjects\pythonProject\venv\Scripts\python.exe" "C:\Users\Dhana\PycharmProjects\dsgsec2\AM2.py"
@pause
echo Invalid password
goto END

:END
pause


