[Original Video](https://www.youtube.com/watch?v=KNjiKbSSlCM)

----


- Suppose you write a good program. What **thoughts** led you there?
- No one knows how to teach programs, so how do we solve it?
	- **FEEDBACK**.
	- Try somenthing, does it work? can it be improved?
	- Feedback can be used with, programs, feeling and even thought process.
- What do we do with teams that struggle to talk about feelings.
	- Handle them a personality test, like the Myers-Brigss Type Indicator (the worst type system), it divides people in 16 types
	- Or even better and funnier - [Searls-Briggs Type Test](https://docs.google.com/forms/d/e/1FAIpQLSfHlw_qQLPcZTE4_oSlSxdivJQEJQ30jL7E8FFusUdqqHUbEw/viewform)
- Practice **top-down programming**.
	- Or even better, create flow charts, dont make single units of code do redundant work, know before hand how the program will be structured then begin to work.
	- **Start with psudo-code**.
- Practice **Reductionism**: brake big scary problems into smaller more manageble ones.
	- **Whats the code that i wished i had**.
- Programming is just communication to the next developer hows gonna pick up your code.
	- Note that that programmer is probabily gonna be you from the future.
- Make your code more **Discoverable**
	- Programs are **DIGRAPHS** (Directed Graphs), like tree graphs where each branch is like a function call.
	- What if every feature was a tree? Much better.

	![[Pasted image 20220103114551.png]]
- Make it **Minimalistic**: A programm should be tidy, symmetrical, terse.
- **Decide upon a style of programming**, dont change everything every time.
	- If u want to improve the code, do it once you are finished.
- **Prepare for Complexity**
	- Too small units do not exist, you will make the bigger later.
- Single Responsability principle: one object should do one thing.
	- **Delegators**: break up the work and give it to the workers:

	![[Pasted image 20220103115826.png]]
	
	- **Workers** or **Logic Nodes**: pure functions that handle only one aspect of the code.

	![[Pasted image 20220103120004.png]]
	
	- **Value**: wrap a bit of data, the types passed around the functions, in functional programming we can see them as the **State**

	![[Pasted image 20220103134209.png]]
	
	- Distrut everyone, even yourself
	- How to do your future self a favour?
		- Use **Disposable Architecture**: No piece of code is there to remain, all can (and maybe will) be changed in the future.

		![[Pasted image 20220103134639.png]]
		
		Dispose of all things you want to change, then the next thing before them (in the previous example i wanted to change the Sorecrast Shake and MakeNewShake)
- **Code reuse isn't free**, try to reuse as little code as possible, writing small units of code is the way to go
	- Increment the renewal code
	- You dont have to trust your past self
- **Wrap 3rd party code** transform them in type you own before using them in your code

---
# Always improve how you code using FEEDBACK from yourself and your team
---

- First thing to do on a team is agree all together to a **NORMALIZATION** on the style, and structure of a project.