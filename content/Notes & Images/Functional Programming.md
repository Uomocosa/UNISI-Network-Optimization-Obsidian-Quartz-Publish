### Functional Programming is all about programming without mutable state.
Always prefer Immutability:
	- **Predictability**: output only depends on inputs.
	- **Composability**: side effects are hard to compose.
	- **Testability**: easer to test.
	
That is to say in a NON-Functional programming language, such as python, javascript, ... you **can** use mutable objects, just **AVOID, NON-LOCAL MUTATIONS**, this is to say that mutations should all be incapsulated, such as inside a function.	

----

### Functional Core, Imperative Shell
Strive for an Impure code only at the last lines, such as code that print or display somenthing on the screen, or modifies a file.
At the **Core** of your code you should always have only pure functions.
**DELAY SIDE-EFFECTS TO PUSH THEM AT THE END OF THE CODE**

----

- [[Wikipedia Definition]]
										<br>
- [[Immutable Objects or Variables]]
										<br>
- [[Side Effects]]
										<br>
- [[Pure Functions]]
	- [[First Order Functions]]
	- [[Higher Class Functions - Function Constructors]]
- [[Monads]]