# PMD - CPD

For linux:

	cd $HOME
	wget https://github.com/pmd/pmd/releases/download/pmd_releases%2F7.0.0/pmd-dist-7.0.0-bin.zip
	unzip pmd-dist-7.0.0-bin.zip
	alias pmd="$HOME/pmd-bin-7.0.0/bin/pmd"
	pmd check -d /usr/src -R rulesets/java/quickstart.xml -f text

After installation go to directory of code to be analyze by terminal
After:

	pmd cpd --minimum-tokens 35 --dir pmd-bin-7.0.0/HomeAssistant/ --language python --format text > cpd_results.xml

## ⚠️ Caution!
**Use --skip-lexical-errors for Toga project.** 

# Nicad
Install Nicad from:
	https://www.txl.ca/txl-nicaddownload.html

After installation go to directory of code to be analyze by terminal 
	
	cd NiCad-6.2

Create a directory to hold the source systems and results of the NiCad clone analysis. If you're running NiCad in place, the ./systems directory in the NiCad distribution directory is appropriate.
	
	mkdir ./systems
	
Copy the entire source directory of the system you want to analyze to the analysis directory

	cp -r ./examples/JHotDraw ./systems/
 
Editing config file:
	
 	1) Enter the 'config' folder and create the 'myconfig.cfg' and 'myconfig-report.cfg' file.
 	2) Copy default.cfg to myconfig.cfg and default-report.cfg to myconfig-report.cfg
  	3) Change 'minsize' from 10 to 5 for both files
   	4) For similarity rate bigger than 80% change 'threshold' to 0.2 for both files
    	5) Save and quit

Run the NiCad command, specifying the analysis granularity and language of the system you want to analyze. 

	./nicad6 functions py systems/HomeAssistant/ myconfig-report.cfg

# Simian
Install Simian from:
	https://simian.quandarypeak.com/docs/
 
After installation go to directory of code to be analyze by terminal 
	
	cd simian
	
Copy the code to be analyze inside of simian directory

Run simian command

	java -jar simian.jar -formatter=xml:output.xml "**/*.py"
 For Threshold:

 	java -jar simian.jar -formatter=xml:output.xml -threshold=5 "**/*.py"


