- [ ] launch current version

tech:
- enable database 
	- install database
- enable user data
- save user commands to database
- enable scheduler
	- install scheduler

- 1) show list of commands in a /help command
- 2) a special, 'personalized-only' mode where a single user is supported and list of command is dynamically updated

bugfixes
- [ ] 1) strip stuff
- [ ] 2) command description cannot be empty
- [ ] 3) format command to lower_case

basic features:
- remove command
- edit command


features:
- schedule
- gpt -> help create a command
	- start working on my utils collection
		- idea 1: "is this a good name for ..."
		- idea 2: parse func inputs (+ unused data)
		- idea 3: fill & ask for missing data
- gpt -> help schedule a command


tech demo - new ideas:
- new 'ai command' decorator
	- automatically extract structured kwargs from message text / content - with ai
	- ask user for missing data in a sub-chat dialogue
	- add to ai toolkit -> process in chat handler


