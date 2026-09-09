# Instala a tarefa do Windows que roda o coletor da leitura do dia, todo dia as 06:00.
# O coletor so LE feeds publicos e grava em diario/raw/ (pasta ignorada pelo git).
# Nada e publicado por esta tarefa.
#
# Rodar UMA VEZ:
#   powershell -ExecutionPolicy Bypass -File "<caminho deste arquivo>"
#
# Para desligar depois:
#   Unregister-ScheduledTask -TaskName "InteressePublico_Coletor" -Confirm:$false
#
# NOTA DE ENCODING: este arquivo NAO pode conter caractere acentuado (o Windows
# PowerShell 5.1 le .ps1 sem BOM como ANSI e corrompe o caminho). Por isso os
# caminhos sao derivados de $PSScriptRoot, nunca escritos a mao.

$ErrorActionPreference = "Stop"

$wd     = $PSScriptRoot
$script = Join-Path $wd "coletor.py"

if (-not (Test-Path $script)) {
    Write-Error "Nao encontrei o coletor em: $script"
    exit 1
}

$py = (Get-Command python -ErrorAction SilentlyContinue).Source
if (-not $py) { $py = "C:\Users\eu_br\AppData\Local\Programs\Python\Python312\python.exe" }
if (-not (Test-Path $py)) {
    Write-Error "Nao encontrei o python. Ajuste a variavel `$py neste script."
    exit 1
}

Write-Output "python  : $py"
Write-Output "coletor : $script"
Write-Output ""

$action    = New-ScheduledTaskAction -Execute $py -Argument "`"$script`"" -WorkingDirectory $wd
$t1        = New-ScheduledTaskTrigger -Daily -At ([datetime]"06:00")
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited
# Nomes certos dos parametros: -AllowStartIfOnBatteries e -DontStopIfGoingOnBatteries.
$settings  = New-ScheduledTaskSettingsSet -StartWhenAvailable `
                -AllowStartIfOnBatteries `
                -DontStopIfGoingOnBatteries `
                -ExecutionTimeLimit (New-TimeSpan -Minutes 20)

Register-ScheduledTask -TaskName "InteressePublico_Coletor" `
  -Action $action -Trigger $t1 -Principal $principal -Settings $settings `
  -Description "Coleta os feeds publicos (mainstream, independente, checagem, oficial, popular, mundo) para a leitura do dia do repositorio interesse-publico. So le; nao publica. Se o PC estava desligado as 06:00, roda ao ligar." `
  -Force | Out-Null

$t = Get-ScheduledTask -TaskName "InteressePublico_Coletor"
Write-Output "OK: tarefa InteressePublico_Coletor registrada (estado: $($t.State))"
$t.Triggers | ForEach-Object { Write-Output ("  gatilho: " + $_.StartBoundary) }
Write-Output ""
Write-Output "Conferir o que ja foi coletado:"
Write-Output "  python `"$script`" --status"
