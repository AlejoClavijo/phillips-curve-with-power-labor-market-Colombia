#Lenguage necessary

python version 3.7.9
pip version 20.1.1
git version 2.36.1.windows.1


#The first is necessary create a digital enviorement 

#code for windows:

    .\TRABAJOGRADO
    git init
    python -m venv env 
    doskey STAR = .\env\Scripts\activate
    doskey CLOSE = .\env\Srcipts\deactivate 
    STAR

#After we install 

    pip install pandas 


#If you wash send the local repository to remote repository you can:

    git remote add modelpaper https://github.com/AlejoClavijo/phillips-curve-with-power-labor-market-Colombia.git

    (Only if you don´t change of name of the branch)
        git branch -m main 

    git push -u modelpaper main 

