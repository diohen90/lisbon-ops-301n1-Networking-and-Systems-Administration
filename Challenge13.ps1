# Set the variables for the new user
$firstName = "Franz"
$lastName = "Ferdinand"
$displayName = "$firstName $lastName"
$office = "Springfield"
$state = "OR"
$department = "TPS Department"
$jobTitle = "TPS Reporting Lead"
$email = "ferdi@GlobeXpower.com"
$username = "ferdinand"

# Generate a secure password for the user
$securePassword = ConvertTo-SecureString -String "P@ssw0rd123" -AsPlainText -Force

# Create the new user account
New-ADUser -Name $displayName `
           -GivenName $firstName `
           -Surname $lastName `
           -DisplayName $displayName `
           -Office $office `
           -State $state `
           -Department $department `
           -Title $jobTitle `
           -AccountPassword $securePassword `
           -Enabled $true `
           -UserPrincipalName "$username@GlobeXpower.com" `
           -EmailAddress $email `
           -Path "CN=Users, DC=net2grid, DC=globexpower, DC=com"