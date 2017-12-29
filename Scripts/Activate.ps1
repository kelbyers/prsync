# If cygwin is in path, remove it
if ($env:Path -like '*cygwin*') {
  $env:Path = (($env:Path -split ';') -notlike '*cygwin*') -join ';'
}
if (Test-Path "venv\Scripts\Activate.ps1") { venv\Scripts\Activate.ps1 }
