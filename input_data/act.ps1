$License = Get-CimInstance SoftwareLicensingProduct -Filter "Name like 'Windows%'" |
where { $_.PartialProductKey } | select Description, LicenseStatus
 
Write-Output $License