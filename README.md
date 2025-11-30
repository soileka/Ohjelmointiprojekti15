# Coding a simple password manager

## Learning goals

Through this assignment,  you will learn to write and test a tiny software program collaboratively as a group.

## Background 

Develop a Python-based password manager that allows users to store and retrieve website login credentials. If you can, implement also a password strength checker to encourage users to create strong passwords. If you have time and motivation for more, add a password generator feature that allows users to generate strong and random passwords when adding new entries to the password manager.  You are provided with a coding template with ready-made functions for Ceaser cipher encryption and decryption.  Please note that the Caesar cipher encryption is only for educational purposes. Real-world password managers use robust encryption algorithms and secure storage methods.

## Preparatory actions

1. Create a new repository for your team based on this template called "emptypwmanager". See instructions at [GitHub Docs: Creating a repository from a template] (https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
2. Protect the main branch of your repository. Notice a blue warning message about an unprotected branch and follow a link to the branch protection settings. Under "Branch rules", select "Require a pull request before merging". Optionally, to require approval (by another group member) before a pull request can be merged, you can also select "Require approvals". See more instructions at [GitHub Docs: Managing a branch protection rule] https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule
3. Optionally, use GitHub issues to manage your work as a team and assign tasks to each group member.  For instructions, see [GitHub Docs: Quickstart for GitHub Issues]  https://docs.github.com/en/issues/tracking-your-work-with-issues/quickstart

## Workflow actions

1.  Implement a simple password manager on top of the ready template (at main.py). Do NOT change names of functions, nor the provided user interface.
2.  Implement the following functions: adding password, retrieving password, loading passwords from file and saving passwords to file. Optionally, add a password strength checker and random password generator.7
3.  Follow instructions in the coding template on how to implement the functions. If you need to divert from the instructions, explain clearly in commends why you have done so.
4.	Please use the provided functions to encrypt and decrypt the password instead of writing them to file with plain text (while noting this encryption methos is only good for educational purposes).
5.  Test your password manager either manually or by using a ready-made code for automated unit tests (at test.py).  If you want to improve unit tests, please add your own file (e.g. mytest.py) for the purpose.
6.  Make sure that all relevant code changes are merged into the main repository before submitting the assignment for review. See Canvas for instructions on how to submit.
