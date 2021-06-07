@ECHO OFF

:Enc
set /p cho= Are you sure you want to verify Digital Signatures? (y/n)
if %cho%==Y goto Yes
if %cho%==y goto Yes
if %cho%==n goto END
if %cho%==N goto END 
goto END
:Yes
"C:\Users\Dhana\PycharmProjects\pythonProject\venv\Scripts\python.exe" "C:\Users\Dhana\PycharmProjects\dsgsec2\Receiver.py"
@pause

echo Digital Signatures checked. Check verification folder
goto END

:END
pause

