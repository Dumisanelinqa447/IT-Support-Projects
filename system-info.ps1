Write-Host "==== SYSTEM INFORMATION ===="

$computer = $env:COMPUTERNAME
Write-Host "Computer Name: $computer"

$user = $env:USERNAME
Write-Host "Logged-in User: $user"

$os = Get-WmiObject Win32_OperatingSystem
Write-Host "OS Version: " $os.Caption

Write-Host "`nLocal Users:"
Get-LocalUser | Select Name, Enabled
