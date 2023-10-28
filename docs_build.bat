@echo off
@echo .doctrees > docs/.gitignore

if "%*"=="-t" (
	rmdir /Q /S _temp
)

if "%*"=="-d" (
	rmdir /Q /S docs
)

sphinx-build -a source docs 

if "%*"=="-o" (
	cd docs
	rmdir ".git" /S /Q
	git init
	@echo .doctrees > .gitignore
	git add .
	git commit -m "- auto-generated with sphinx -"
	git remote add origin https://github.com/phenopype/static-phenopype-gallery
	git push --force origin main
	cd ..
)