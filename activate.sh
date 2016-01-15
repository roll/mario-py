# Mario alias
alias mario='python -m mario.cli'

# Git commit hook
if [ ! -f .git/hooks/pre-commit ]; then
    echo -e "#!/bin/sh\n\n\npython -m mario.cli check" > .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
fi

# Python env
virtualenv venv
source venv/bin/activate
pip install -Urrequirements.dev.txt
