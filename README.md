# Replication Package of TRADE

## Automated Identification and Refactoring of Code Clones in Test Scripts for Eliminating Duplication

## Abstract
Code clones in test scripts can significantly reduce maintainability. They can lead to duplication especially in ecosystems and product families where applications have commonalities in their test scenarios. We propose and evaluate an automated approach to address this problem. We compare the effectiveness of clone detection tools for detecting code clones in Python test scripts. We use the output of these tools to identify commonalities and code duplication in test scripts. Additionally, we apply static analysis to detect code dependencies and variations in the scripts for steering automated refactoring to remove redundancies. We conduct case studies that involve one industrial and three open-source projects. We observe that up to 5\% reduction in the size of test scripts is possible with automated refactoring.

## File Structure
- `Clone Detection Tools`: contains the installation stages of clone detection tools 
- `DataSet`: the original code of the open source projects used before and after the refactor and the unit test/functional test versions. 
- `Test Refactoring Tool`: contains the automatic refactor tool.
- `Test_Clone_Results`: contains the output before and after automatic refactor.

## Replicate

In the following sections, we describe how to replicate the results for our study.


### Download Open Source Projects

Download open source projects from below.

[Home Assistant](https://github.com/home-assistant/core).
Extract the 'tests' folder from downloaded file `core-dev.zip`.

[Toga](https://github.com/beeware/toga/tree/main).
This project has a test folder in 2 different locations. You need to get both of them.
Extract the '/testbed' folder from downloaded file `toga-main.zip`.
Extract the '/core/tests' folder from downloaded file `toga-main.zip`.

[Kivy](https://github.com/kivy/kivy/tree/master).
Extract the 'kivy/tests' folder from downloaded file `kivy-master.zip`.

## ⚠️ Caution!
**Please use the versions of the open source projects used in this work at the time of writing. You can find out which versions were used in the study and the latest commits below.**  
[here](https://github.com/iOTMecit/TRADE/tree/main/Open%20Source%20Projects).

Alternatively, the original codes in 'Dataset' can be used. [here](https://github.com/iOTMecit/TRADE/tree/main/Dataset).


### Clone Detection Tools

You can find information about the clone detection tools used in this study and how to run them  [here](https://github.com/iOTMecit/TRADE/tree/main/Clone%20Detection%20Tools).


### Installation of Test Refactoring Tool

You can find installation process of the test refactoring tools used in this study [here](https://github.com/iOTMecit/TRADE/tree/main/Test%20Refactoring%20Tool).


