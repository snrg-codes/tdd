# git_push.ps1
$Message = $args[0]

if (-not $Message) {
    $Message = "Auto commit"
}

git add .
git commit -m "$Message"
git push
